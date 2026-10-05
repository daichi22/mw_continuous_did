# 研究計画

## 卒論の方向性

中心テーマ:

> **日本の地域別最低賃金の効果を実証すると同時に、最低賃金を連続処置として捉えた場合のDiD推定上の問題を検討する。**

単なる「最低賃金を上げると雇用・賃金がどうなるか」という実証研究にはせず、**estimand / estimatorそのものを研究対象の一部にする**。

## 構成

### 1. 実証

毎月勤労統計を用いて、都道府県別パネルで最低賃金の影響を推定する。

処置は

$$
D_{it}=\log(MW_{it})
$$

アウトカムについて最低賃金の効果を推定するが、「効果が出た／出なかった → 経済理論で解釈」というだけの卒論にはしない。

### 2. 計量的な問題意識

最低賃金はbinary treatmentではなく、地域・時点によって強度が異なる**continuous treatment**。

通常のTWFEで推定した係数を最低賃金の因果効果として解釈してよいのかを検討する。

特にCallaway, Goodman-Bacon, Sant'Anna (2024) のcontinuous-treatment DiDを軸に、

* 何がestimandなのか
* どのparallel trends仮定が必要なのか
* treatment effect heterogeneityやnonlinear dose-responseがあるとTWFEは何を推定するのか
* continuous-treatment DiDでは何が識別・推定できるのか

を整理する。ここが卒論の方法論的な中心。

### 3. Monte Carlo simulation

理論整理だけで終わらず、**推定量の有限標本特性をsimulationで調べる**。

特に毎勤×最低賃金の実証環境を意識して、47都道府県という比較的小さい $N$、現実に近い最低賃金の処置分布などをDGPに反映させる。

例えば真のdose-responseを

$$
\tau(d)=\beta d
$$

から

$$
\tau(d)=\beta_1 d+\beta_2 d^2
$$

のような非線形なものに変えたり、heterogeneity、noise、処置分布、sample sizeなどを操作する。

TWFEとcontinuous-treatment DiD系推定量について、Bias, Variance, RMSE, Coverage などを比較する。

重要なのは**「どの推定量が勝つか」を決めることではない**。むしろ、

$$
\text{DGPの性質} \rightarrow \text{推定量の理論的性質} \rightarrow \text{有限標本での挙動}
$$

を説明する。特に、

$$
\underbrace{\hat\theta-\theta}_{\text{Estimation error}}
\qquad\text{と}\qquad
\underbrace{\theta-\tau}_{\text{Estimand problem}}
$$

を区別できると面白い。サンプルサイズを増やせば前者は小さくなっても、そもそもTWFEが関心のある因果効果とは違うものを推定しているなら後者は残る、ということをsimulationで可視化できる。

### 4. 最後に実データへ戻る

simulationで確認した性質を踏まえて、TWFE vs Continuous-treatment DiD を実際の毎勤×最低賃金データに適用する。

> **推定方法・estimandの違いによって、日本の最低賃金について得られる実証的結論がどの程度変わるのか**

を見る。

これで、

$$
\text{計量理論} \rightarrow \text{Simulation} \rightarrow \text{Empirical Application}
$$

という一本の構成になる。

## 内生性について

最低賃金水準自体の内生性を完全に解決することは、今回の中心にはしない。

IVなど適切な外生変動を見つけられれば別だが、無理に弱いIVを持ってくるくらいなら、識別上の限界を明記する。

> **「最低賃金の因果効果を完全に識別した」と主張すること**

ではなく、

> **一定の識別仮定の下で、連続処置としての最低賃金をどう推定するべきなのかを吟味すること**

に力を使う。

## 設計上のポイント

最低賃金は研究対象であると同時に、continuous-treatment DiDという計量問題を考えるためのempirical applicationでもある。

実証結果が「最低賃金は雇用を○%減らした」みたいに派手でなくても問題ない。卒論の価値を**有意な結果の発見だけに依存させない**構造。

学部卒論として、新推定量や新しい漸近理論まで手を出さず、**既存理論を理解 → simulationで有限標本特性を検証 → 実データへ適用**までを丁寧にやる。
