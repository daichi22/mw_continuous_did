---
marp: true
theme: default
paginate: true
size: 16:9
math: mathjax
header: ''
footer: ''
style: |
  section {
    font-family: 'Hiragino Sans', 'Yu Gothic', 'Noto Sans CJK JP', sans-serif;
    padding: 46px 64px;
    background: #fafafa;
    color: #1a1a2e;
  }
  h1 {
    font-size: 42px;
    letter-spacing: -0.03em;
    margin-bottom: 24px;
    color: #1f4e67;
  }
  h2 {
    font-size: 31px;
    margin-bottom: 18px;
  }
  h3 {
    font-size: 25px;
    margin: 0 0 12px 0;
  }
  p, li {
    font-size: 23px;
    line-height: 1.5;
  }
  table {
    font-size: 21px;
    width: 100%;
  }
  th {
    background: #1f4e67;
    color: white;
    padding: 10px 14px;
  }
  td {
    padding: 10px 14px;
    border: 1px solid #e5e7eb;
  }
  tr:nth-child(even) { background: #f0f4f8; }
  strong { color: #0f766e; }
  .note {
    font-size: 21px;
    background: #f3f4f6;
    padding: 14px 18px;
    border-radius: 12px;
    margin-top: 20px;
    max-width: 880px;
    display: inline-block;
  }
  .note-full {
    font-size: 21px;
    background: #f3f4f6;
    padding: 14px 18px;
    border-radius: 12px;
    margin-top: 20px;
  }
  .two-col {
    display: grid;
    grid-template-columns: 0.9fr 1.1fr;
    gap: 34px;
    align-items: start;
  }
  .two-col-even {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 34px;
    align-items: start;
  }
  .three-col {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 24px;
    align-items: start;
  }
  .box {
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 18px 22px;
  }
  .box-accent {
    background: #f0f9f8;
    border: 1px solid #0f766e;
    border-radius: 14px;
    padding: 18px 22px;
  }
  .box-warn {
    background: #fff7ed;
    border: 1px solid #c2410c;
    border-radius: 14px;
    padding: 18px 22px;
  }
  .box-new {
    background: #eff6ff;
    border: 2px solid #1d4ed8;
    border-radius: 14px;
    padding: 18px 22px;
  }
  .lead h1 { font-size: 50px; }
  .lead .note { max-width: 920px; }
  .bad { color: #b91c1c; font-weight: 700; }
  .good { color: #047857; font-weight: 700; }
  .warn { color: #c2410c; font-weight: 700; }
  .new { color: #1d4ed8; font-weight: 700; }
  .small { font-size: 18px; color: #555; }
  section.dense { padding: 32px 52px; }
  section.dense p, section.dense li { font-size: 19px; line-height: 1.35; }
  section.dense h1 { font-size: 36px; margin-bottom: 14px; }
  section.dense h2 { font-size: 27px; margin-bottom: 12px; }
  section.dense h3 { font-size: 22px; margin: 0 0 8px 0; }
  section.dense .small { font-size: 15px; }
  section.dense .note-full { font-size: 17px; padding: 10px 14px; }
  section.dense .note { font-size: 15px; padding: 8px 12px; }
  section.dense table { font-size: 18px; }
  section.dense .box, section.dense .box-accent, section.dense .box-warn, section.dense .box-new { padding: 12px 16px; }
  .fig-center {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
  }
  section::after {
    content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    font-size: 16px;
    color: #888;
  }
---

<!-- _class: lead -->

# 連続処置DiDにおける<br>TWFE推定量の問題

## 最低賃金パネルデータによる実証と<br>Monte Carloシミュレーション

---

# 背景：何をやろうとしていたか

<div class="two-col-even" style="margin-top: 16px">

<div class="box">

### データ

- **毎月勤労統計（地方調査）** × **都道府県別最低賃金**
- 47都道府県 × 月次パネル（2013-01〜2026-03）
- 7,097行（2019-05〜12欠測）

</div>

<div class="box">

### 当初の推定式

$$Y_{it} = \beta \cdot \log(MW_{it}) + \alpha_i + \gamma_t + \varepsilon_{it}$$

- $Y$: 賃金・労働時間（毎勤）
- $D$: $\log(MW)$（連続処置変数）
- TWFE（都道府県FE + 年月FE）

</div>

</div>

<div class="note-full" style="margin-top: 20px">

最低賃金が賃金・労働時間に与える効果をTWFEで推定しようとした。<br>
**処置変数は連続量**（log最低賃金の水準）であり、binary DiDの枠組みとは異なる。

</div>

---

<!-- _class: dense -->

# 実証結果：TWFEでおかしなことが起きた

### サンプル期間を分割すると**係数の符号が反転**する

それぞれの期間で**独立にTWFEを推定**した結果:

| アウトカム | 全期間 | 2013-2018 | 2020-2025 |
|-----------|--------|-----------|-----------|
| log(所定内給与) | −0.020 | **−0.730** | **+0.091** |
| log(総実労働時間) | −0.160* | **+0.221** | **−0.193**\*\* |
| 所定外労働時間 | −1.998 | **+17.6** | **−7.06**\* |

<div class="small" style="margin-top: 4px">
係数の解釈: log-log仕様では弾力性。例: $\hat{\beta} = -0.193$ → MW が1%上昇すると総実労働時間が約0.19%減少。<br>所定外労働時間は水準(時間)なので、$\hat{\beta} = -7.06$ → $\log(MW)$が1単位増（MW約2.7倍）で7時間減。
</div>

<div class="box-warn" style="margin-top: 10px">

**3つのアウトカム全てで符号が反転。** サンプル期間次第で「最低賃金は労働時間を増やす」にも「減らす」にもなる。真の効果が逆転したのか？推定量の問題か？

</div>

---

# 問い：なぜTWFEは不安定なのか？

<div class="two-col-even" style="margin-top: 20px">

<div class="box-warn">

### 仮説1: 真の効果が変わった

コロナ前後で最低賃金の効果が本当に逆転した？

→ あり得るが、3アウトカム全てで同時に反転するのは不自然

</div>

<div class="box-accent">

### 仮説2: TWFE推定量の問題

連続処置のもとでTWFEは何を推定しているのか？

→ **Callaway, Goodman-Bacon, Sant'Anna (2024)** が指摘する問題

</div>

</div>

<div class="box-new" style="margin-top: 24px">

**本研究の方向転換：** 最低賃金の効果の大きさを論じる前に、そもそもTWFE推定量が連続処置のもとで何を推定しているのかを検証する必要がある。<br>→ 推定手法そのものの検討に焦点を移した。

</div>

---

<!-- _class: dense -->

# Goodman-Bacon (2021) 分解：TWFEの正体

### TWFEの $\hat{\beta}$ は、すべての「2×2 DiD」の加重平均に分解できる

$$\hat{\beta}^{TWFE} = \underbrace{\sum_k s_{kU} \hat{\beta}_{kU}}_{\textbf{① 処置 vs 未処置 ✓}} + \underbrace{\sum_{k \text{ early}} s_{kl} \hat{\beta}_{kl}}_{\textbf{② 早期 vs 後期 ✓}} + \underbrace{\sum_{k \text{ late}} s_{kl} \hat{\beta}_{kl}}_{\textbf{③ 後期 vs 早期 ✗}}$$

<div class="three-col" style="margin-top: 16px">

<div class="box-accent">

### ① 処置群 vs 未処置群

理想的な比較

→ 正の重み ✓

</div>

<div class="box">

### ② 早期処置 vs 後期処置

後期処置群は処置前なので適切なコントロール

→ 正の重み ✓

</div>

<div class="box-warn">

### ③ 後期処置 vs 早期処置

早期処置群は**すでに処置済み**
→ コントロールとして不適切
→ **負の重みが発生しうる**

</div>

</div>

<div class="note-full" style="margin-top: 14px">

③の比較で、処置効果が時間とともに変化（dynamic treatment effects）すると、「すでに処置を受けた群」の変化がコントロールに混入し、biasを生む。重み$s_{kl}$はサンプルサイズと処置タイミングの分散に依存。

</div>

---

<!-- _class: dense -->

# 連続処置への拡張：Callaway et al. (2024)

### 連続処置では、そもそも**何を推定したいか**が2つある

<div class="two-col-even" style="margin-top: 12px">

<div class="box">

### Level効果

処置を受けること自体の効果:
$$ATT(d) = E[Y(d) - Y(0) \mid D = d]$$

「最低賃金が$d$の県は、仮にMWがなかったら？」

</div>

<div class="box-accent">

### Dose-response効果

処置の**強度**による効果の変化:
$$\tau(d) = \frac{\partial}{\partial d} E[Y(d) \mid D = d]$$

「MWが1%上がると、アウトカムはどう変わる？」

</div>

</div>

### TWFEの $\hat{\beta}$ は、これらのどちらも正しく推定できない場合がある:

<div class="two-col-even" style="margin-top: 8px">

<div class="box-warn">

### ① Estimand Problem（非線形dose-response）

$\tau(d) = \beta_1 d + \beta_2 d^2$ のとき、$\hat{\beta}$は $\beta_1$ でも $\beta_2$ でもない → $N \to \infty$ でも解決しない

</div>

<div class="box-warn">

### ② 負の重み問題（処置効果の異質性）

$\beta_i \sim N(\beta, \sigma^2_{het})$ のとき、全個体で $\beta_i > 0$ でも $\hat{\beta} < 0$ が起こりうる → sign flipの原因

</div>

</div>

---

<!-- _class: dense -->

# Monte Carlo シミュレーションの設計

### 実データの最低賃金パスを固定し、アウトカムのみを人工的に生成する

<div class="two-col-even" style="margin-top: 8px">

<div>

**固定するもの:**
- 47都道府県の実際の$\log(MW_{it})$の時系列
- パネル構造（県×月）

**生成するもの（DGP）:**
$$Y_{it} = \alpha_i + \gamma_t + \tau_i(D_{it}) + \varepsilon_{it}$$

- $\alpha_i \sim N(0, 0.1)$: 県固定効果
- $\gamma_t \sim N(0, 0.05)$: 時点固定効果
- $\varepsilon_{it} \sim N(0, 0.018)$: 誤差項
  - 0.018は実データのTWFE残差の標準偏差から設定

</div>

<div>

### 4つのDGP（$\beta_{true} = 0.3$）

| DGP | dose-response | 異質性 |
|-----|:---:|:---:|
| A: 線形・均質 | $\beta d$ | なし |
| B: 非線形 | $\beta d + \kappa d^2$ | なし |
| C: 異質 | $\beta_i d$ | $\beta_i \sim N(\beta, 0.5)$ |
| D: 非線形+異質 | $\beta_i d + \kappa d^2$ | あり |

**反復:** 1,000回
**評価:** 前半(2013-18)と後半(2020-25)で別々にTWFE推定し、sign flip率・Bias・Coverage（95%CIが$\beta_{true}$を含む率）を計測

</div>

</div>

---

# MC結果：異質性がsign flipを引き起こす

<div class="two-col-even" style="margin-top: 16px">

<div>

| DGP | Bias | Sign Flip率 | Coverage |
|-----|------|:-----------:|:--------:|
| A: 線形・均質 | −0.001 | <span class="good">2.7%</span> | 93.2% |
| B: 非線形 | **+0.619** | <span class="good">0.0%</span> | <span class="bad">0.0%</span> |
| C: 異質 | −0.004 | <span class="bad">42.3%</span> | 92.7% |
| D: 両方 | **+0.593** | <span class="bad">24.0%</span> | <span class="bad">85.1%</span> |

</div>

<div>

### 読み方

- **DGP-A:** 問題なし（ベンチマーク）
- **DGP-B:** 安定しているが0.3とは全く違う値に収束
  → TWFEは**別のものを推定**している
- **DGP-C:** ノイズを消しても（ε=0）44.7%がflip
  → 偶然ではなく**TWFEの推定対象自体が不安定**
- **DGP-D:** 両方の問題が複合

</div>

</div>

<div class="note-full" style="margin-top: 14px">

**核心:** DGP-Bでは、TWFEは安定しているが**研究者が知りたいパラメータとは別のものを推定**している。DGP-Cでは、県ごとの効果の違いとTWFEの重みづけの組み合わせで、**TWFEが狙っている対象自体が期間によって正にも負にもなる**。偶然の誤差（sampling variation）ではない。

</div>

---

# MC結果：$\hat{\beta}$ の分布

<div class="fig-center" style="margin-top: 12px">
<img src="../output/figures/04_mc_beta_distribution.png" width="880">
</div>

<div class="small" style="text-align: center; margin-top: 8px">
DGP別のTWFE推定量 $\hat{\beta}$ の分布（前半 vs 後半、各1,000回）。<br>
**DGP-A**（線形・均質）: 分布が狭く安定。**DGP-C**（異質）: 分布が広がり、前半と後半で符号をまたぐ → sign flip。<br>
**DGP-B**（非線形）: 分布は狭いが真の値（0.3）から大きくずれている → estimand problem。
</div>

---

# まとめと今後

<div class="two-col-even" style="margin-top: 16px">

<div class="box-accent">

### わかったこと

1. TWFEは連続処置下で**サンプル期間によって符号が反転**する（実証的事実）
2. MCで**推定値の不安定性を3つのレイヤーに分解**:
   - 真の効果 ≠ TWFEの推定対象（非線形）
   - TWFEの推定対象自体が不安定（異質性）
   - 偶然の誤差（β≈0なら自然にflip）
3. 異質性によるflipは偶然ではなく**構造的**（ε=0でも44.7%がflip）

</div>

<div class="box">

### 今後

- **Callaway et al. (2024) の理論的整理**
  TWFE decompositionの数式を正式に理解・記述
- **代替推定量の検討**
  De Chaisemartin & D'Haultfœuille (2024) の
  no-stayer推定量（dcDH）の理解と実装
- **MCにdcDHを組み込んだ比較**
  TWFEの問題をdcDHが解消するか検証

</div>

</div>

<div class="note-full" style="margin-top: 20px">

**現時点での貢献:** 日本の最低賃金データを用いて、連続処置DiDにおけるTWFE推定量の問題を実証的に示し、Monte Carloシミュレーションでメカニズムを特定した。

</div>

---

<!-- _class: dense -->

# 参考文献

- Callaway, B., Goodman-Bacon, A., & Sant'Anna, P. (2024). Difference-in-differences with a continuous treatment. *NBER Working Paper* 32117.
- De Chaisemartin, C., D'Haultfœuille, X., & Vazquez-Bare, G. (2024). Difference-in-differences estimators for treatments continuously distributed at every period. *arXiv:2402.05432*.
- Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. *Journal of Econometrics*, 225(2), 254–277.

**データ**
- 厚生労働省「毎月勤労統計調査（地方調査）」
- 厚生労働省「地域別最低賃金の全国一覧」
