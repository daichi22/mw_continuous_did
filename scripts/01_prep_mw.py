"""
01_prep_mw.py
最低賃金データ（wide形式）を月次パネルに変換する。

処理内容:
  1. wide → long（都道府県 × 発効年月日 × 時間額）
  2. 各都道府県 × 年月に「発効月から新賃金を割り当て」（発効日の属する月を新賃金の開始月とする）
  3. 出力: data/mw_monthly.csv（prefecture, year, month, min_wage）
"""

from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

SCRIPT_DIR = Path(__file__).parent
DATA_DIR   = SCRIPT_DIR.parent / "data"
OUT_PATH   = DATA_DIR / "mw_monthly.csv"

EXCEL_EPOCH = datetime(1899, 12, 30)

def parse_excel_date(val):
    """Excelシリアル値またはdatetimeをpd.Timestampに変換する。"""
    if pd.isna(val):
        return pd.NaT
    if isinstance(val, (int, float)) and 10000 < val < 60000:
        return pd.Timestamp(EXCEL_EPOCH + timedelta(days=int(val)))
    return pd.to_datetime(val, errors="coerce")

# ── 1. 読み込み ───────────────────────────────────────────────────────
raw = pd.read_excel(DATA_DIR / "001571219.xlsx", header=[0, 1])
print(f"shape: {raw.shape}")

pref_series = raw.iloc[:, 0]

# 結合セルのforward-fill
col_l0 = raw.columns.get_level_values(0).tolist()
filled_l0 = []
prev = ""
for v in col_l0:
    if not str(v).startswith("Unnamed"):
        prev = v
    filled_l0.append(prev)

print("年度一覧:", sorted(set(filled_l0[1:])))

# ── 2. wide → long ────────────────────────────────────────────────────
records = []
i = 1
while i + 1 < len(raw.columns):
    yr = filled_l0[i]
    wage_col = raw.iloc[:, i]
    date_col = raw.iloc[:, i + 1]

    for pref, wage, eff in zip(pref_series, wage_col, date_col):
        if pd.isna(pref) or pd.isna(wage) or pd.isna(eff):
            continue  # i は内側ループで動かさない
        try:
            records.append({
                "prefecture": str(pref).strip(),
                "fiscal_year_label": yr,
                "min_wage": int(wage),
                "effective_date": parse_excel_date(eff),
            })
        except (ValueError, TypeError):
            pass
    i += 2

SUFFIXES = {"北海道": "道", "東京都": "都", "大阪府": "府", "京都府": "府"}
SPECIAL  = {"神奈川": "神奈川県", "和歌山": "和歌山県", "鹿児島": "鹿児島県"}

def normalize_pref(name: str) -> str:
    """'三　重' → '三重県'、'東　京' → '東京都' のように変換する。"""
    stripped = name.replace("　", "").replace(" ", "").strip()
    if stripped in SPECIAL:
        return SPECIAL[stripped]
    for full in SUFFIXES:
        if full.startswith(stripped):
            return full
    return stripped + "県"

mw_long = (
    pd.DataFrame(records)
    .dropna(subset=["prefecture", "min_wage", "effective_date"])
    .sort_values(["prefecture", "effective_date"])
    .reset_index(drop=True)
)

# 全国加重平均額を明示除外
mw_long = mw_long[~mw_long["prefecture"].str.contains("全国", na=False)]

# 都道府県名を正規化（'三　重' → '三重県'）
mw_long["prefecture"] = mw_long["prefecture"].map(normalize_pref)

print(f"\nlong形式 shape: {mw_long.shape}")
print("都道府県数:", mw_long["prefecture"].nunique())
assert mw_long["prefecture"].nunique() == 47, \
    f"都道府県数が47ではありません: {mw_long['prefecture'].nunique()}"

# ── 3. 発効月ベースで月次グリッドに割り当て ──────────────────────────
# 発効日の属する月（月初）を新賃金の開始月とする
# 例: 発効日 2022-10-12 → 2022-10-01 から新賃金
mw_long["effective_month"] = mw_long["effective_date"].dt.to_period("M").dt.to_timestamp()

# 同一都道府県・同一発効月で額が食い違うケースがないことを確認
conflict = mw_long.groupby(["prefecture", "effective_month"])["min_wage"].nunique()
assert (conflict <= 1).all(), "同一都道府県・同一発効月に異なる最低賃金があります"

# 重複行を除去（同一月・同一額の重複は問題ないが明示的に落とす）
mw_long = mw_long.drop_duplicates(subset=["prefecture", "effective_month", "min_wage"])

min_date = mw_long["effective_month"].min()
max_date = pd.Timestamp("2026-03-01")
months = pd.date_range(min_date, max_date, freq="MS")
prefs  = sorted(mw_long["prefecture"].unique())

results = []
for pref in prefs:
    pref_mw = (
        mw_long[mw_long["prefecture"] == pref]
        [["effective_month", "min_wage"]]
        .sort_values("effective_month")
        .rename(columns={"effective_month": "date"})
    )
    pref_grid = pd.DataFrame({"date": months, "prefecture": pref})
    merged = pd.merge_asof(
        pref_grid.sort_values("date"),
        pref_mw,
        on="date",
        direction="backward",
    )
    results.append(merged)

mw_monthly = pd.concat(results, ignore_index=True)
mw_monthly["year"]  = mw_monthly["date"].dt.year
mw_monthly["month"] = mw_monthly["date"].dt.month
mw_monthly = (
    mw_monthly[["prefecture", "year", "month", "min_wage"]]
    .sort_values(["prefecture", "year", "month"])
    .reset_index(drop=True)
)

# 重複チェック
dups = mw_monthly.duplicated(subset=["prefecture", "year", "month"]).sum()
assert dups == 0, f"重複行あり: {dups}件"

print(f"\n月次パネル shape: {mw_monthly.shape}")
print(mw_monthly.head(15))

# 欠損確認は分析期間（2013年以降）に限定
mw_analysis = mw_monthly[mw_monthly["year"] >= 2013]
print("\n欠損確認（2013年以降）:\n", mw_analysis.isnull().sum())
assert mw_analysis["min_wage"].isna().sum() == 0, "分析期間に min_wage 欠損あり"

print(f"\n年範囲: {mw_monthly['year'].min()} 〜 {mw_monthly['year'].max()}")

# ── 4. 東京 2022年10月の確認 ─────────────────────────────────────────
tokyo = mw_monthly[
    (mw_monthly["prefecture"].str.contains("東京")) &
    (mw_monthly["year"] == 2022) &
    (mw_monthly["month"].isin([9, 10, 11]))
]
print("\n【確認】東京 2022年9〜11月の最低賃金:")
print(tokyo.to_string(index=False))

# ── 5. 保存 ───────────────────────────────────────────────────────────
mw_monthly.to_csv(OUT_PATH, index=False, encoding="utf-8-sig")
print(f"\n保存完了: {OUT_PATH}")
