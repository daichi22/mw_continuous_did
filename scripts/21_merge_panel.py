"""
21_merge_panel.py
毎月勤労統計パネル（maikin_panel.csv）と最低賃金データ（mw_monthly.csv）を結合し、
log(MW)を処置変数として追加した分析用パネルを作成する。

出力: data/analysis_panel.csv
"""

import numpy as np
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"

mk = pd.read_csv(DATA_DIR / "maikin_panel.csv")
mw = pd.read_csv(DATA_DIR / "mw_monthly.csv")

SUFFIX_MAP = {"県": "", "府": "", "都": "", "道": ""}


def strip_suffix(name: str) -> str:
    if name == "北海道":
        return name
    for suffix in SUFFIX_MAP:
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


mw["pref_name"] = mw["prefecture"].apply(strip_suffix)

panel = mk.merge(
    mw[["pref_name", "year", "month", "min_wage"]],
    on=["pref_name", "year", "month"],
    how="left",
)

panel["log_mw"] = np.log(panel["min_wage"])

n_total = len(panel)
n_matched = panel["min_wage"].notna().sum()
n_missing = panel["min_wage"].isna().sum()

print(f"Total rows: {n_total}")
print(f"MW matched: {n_matched}")
print(f"MW missing: {n_missing}")

if n_missing > 0:
    missing = panel[panel["min_wage"].isna()]
    print(f"\nMissing MW rows:")
    print(missing[["pref_name", "year", "month"]].drop_duplicates().head(20).to_string())

panel.sort_values(["pref_code", "year", "month"], inplace=True)
panel.reset_index(drop=True, inplace=True)

out_path = DATA_DIR / "analysis_panel.csv"
panel.to_csv(out_path, index=False, encoding="utf-8-sig")

print(f"\nSaved: {out_path}")
print(f"Shape: {panel.shape}")
print(f"Columns: {list(panel.columns)}")
print(f"\nlog_mw range: [{panel['log_mw'].min():.4f}, {panel['log_mw'].max():.4f}]")
print(f"min_wage range: [{panel['min_wage'].min():.0f}, {panel['min_wage'].max():.0f}]")
print(f"\nSample:\n{panel[['pref_name','year','month','min_wage','log_mw','hours_total','wage_total']].head(5).to_string()}")
