# CLAUDE.md - 最低賃金×連続処置DID

## プロジェクト概要

卒業論文プロジェクト。日本の地域別最低賃金の効果を実証すると同時に、最低賃金を連続処置として捉えた場合のDiD推定上の問題を検討する。estimand/estimatorそのものを研究対象の一部にする。

構成: **計量理論の整理 → Monte Carlo Simulation → Empirical Application**

詳細は `docs/research_plan.md` 参照。

## 識別戦略

**処置変数**: $D_{it} = \log(MW_{it})$

**メイン推定量**: Callaway, Goodman-Bacon, Sant'Anna (2024) の continuous-treatment DiD
- Rの`contdid`パッケージで実装
- estimandはdose-response curve

**対比**: TWFEとの比較が卒論の方法論的中心
- treatment effect heterogeneityやnonlinear dose-responseがあるとTWFEは何を推定するのか
- estimation error vs estimand problem の区別

**内生性**: MW水準自体の内生性を完全に解決することは中心にしない。識別上の限界を明記する。

## データ

| データ | パス | 内容 |
|---|---|---|
| 分析パネル | `data/analysis_panel.csv` | maikin + log(MW) 結合済み（7,097行×16列）|
| 毎月勤労統計 | `data/maikin_panel.csv` | 都道府県×月次（2013-01〜2026-03、2019-05〜12欠測）|
| 最低賃金月次 | `data/mw_monthly.csv` | 発効月ベースの都道府県別最低賃金 |

### analysis_panel.csv カラム

pref_code, pref_name, year, month, workers, hours_total, hours_scheduled, hours_overtime, days_worked, wage_total, wage_regular, wage_scheduled, wage_special, wage_overtime, min_wage, log_mw

- wage_overtime = wage_regular - wage_scheduled（計算値）
- 2019-05〜2019-12は厚労省サイトに地方調査ファイルが存在しないためギャップ

## スクリプト構成

| スクリプト | 役割 |
|---|---|
| `01_prep_mw.py` | 最低賃金データのwideからlong、月次変換 |
| `20_download_maikin.py` | 毎月勤労統計（地方調査）の取得・パース（厚労省Excel） |
| `21_merge_panel.py` | maikin + log(MW) 結合 → analysis_panel.csv |

### 今後（Jupyter Notebook）

- 記述統計・可視化
- TWFE推定
- continuous DID推定（R contdid）
- Monte Carlo Simulation

## 実装上の注意

- 元データは編集しない
- 出力は `output/` に保存
- データ準備（20, 21番台）は `.py` スクリプト
- 分析コード（記述統計、推定、Simulation）は **Jupyter Notebook** (`.ipynb`)

## 先行研究

- Callaway, Goodman-Bacon, Sant'Anna (2024) "Difference-in-Differences with a Continuous Treatment" — 理論的支柱
- Nguyen (2025) "The Impact of Minimum Wages on Employment" — 労働時間アウトカムの先行事例
- 有賀健「新規高卒者の労働市場」— 都道府県パネル×log(MW)の国内先例
- 論文ノートは `docs/literature/` にある

## 未確定事項

- [ ] Simulationの射程: DGP設計の詳細（線形/非線形dose-response, heterogeneity構造）
