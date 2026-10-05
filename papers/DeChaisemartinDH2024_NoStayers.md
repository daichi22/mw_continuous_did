arXiv:2402.05432v1[econ.EM]8Feb2024

# Difference-in-Differences Estimators with Continuous Treatments and no Stayers

### Clément de Chaisemartin, Xavier D’Haultfœuille and Gonzalo Vazquez-Bare∗

Many treatments or policy interventions are continuous in nature. Examples include prices, taxes or temperatures. Empirical researchers have usually relied on two-way fixed effect regressions to estimate treatment effects in such cases, see e.g. Deschênes and Greenstone (2012). However, such estimators are not robust to heterogeneous treatment effects in general (De Chaisemartin and D’Haultfœuille, 2020); they also rely on the linearity of treatment effects. We propose estimators for continuous treatments that do not impose those restrictions, and that can be used when there are no stayers: the treatment of all units changes from one period to the next. This is for instance the case when the treatment is precipitations or temperatures: for instance, temperatures of all US counties change, if ever so slightly, between two consecutive years. We start by extending the nonparametric results of de Chaisemartin et al. (2023) to cases without stayers. We also present a parametric estimator, and use it to revisit Deschênes and Greenstone (2012).

## 1 Set-up, assumptions and parameter of interest

A representative unit is drawn from an infinite super population, and observed at two time periods. All expectations below are taken with respect to the distribution of variables in the super population. We are interested in the effect of a continuous and scalar treatment variable on that unit’s outcome. Let Dt denote the unit’s treatment at period t ∈ {1,2} and let Dt denote its support; let also D denote the support of (D1,D2). For any (d1,d2) ∈ D, let Yt(d1,d2) denote the unit’s potential outcome at t with treatment d, and let Yt denote

![image 1](<2402.05432v1_images/imageFile1.png>)

∗Chaisemartin: Sciences Po Paris, clement.dechaisemartin@sciencespo.fr. D’Haultfœuille: CRESTENSAE, xavier.dhaultfoeuille@ensae.fr. Vazquez-Bare: University of California, Santa Barbara, gvazquez@econ.ucsb.edu.

their observed outcomes: Yt = Yt(D1,D2). Finally, for any random variables (Xt)t=1,2, let ∆X = X2 − X1. We impose the following assumptions:

- Assumption 1 (Static model) For all t ∈ {1,2} and (d1,d2) ∈ D, Yt(d1,d2) only depends on dt; we denote it by Yt(dt).
- Assumption 2 (Parallel trends) ∀d ∈ D1, E(∆Y (d)|D1 = d,D2) = E(∆Y (d)|D1 = d).
- Assumption 3 (Bounded treatment, bounded-lipschitz potential outcomes)

- 1. D1 and D2 are bounded subsets of R.
- 2. ∃Y ≥ 0: sup(d


![image 2](<2402.05432v1_images/imageFile2.png>)

1,d2)∈D E[Y |D1 = d1,D2 = d2] < ∞, and ∀(t,d,d′) ∈ {1,2} × Dt2, |Yt(d) − Yt(d′)| ≤ Y |d − d′|.

![image 3](<2402.05432v1_images/imageFile3.png>)

![image 4](<2402.05432v1_images/imageFile4.png>)

Assumptions 2-3 are also imposed by de Chaisemartin et al. (2023), and are discussed therein.

- Assumption 4 (No stayers but quasi-stayers) P(∆D = 0) = 0, P(|∆D| ≤ η) > 0 ∀η > 0.


First, Assumption 4 states that there are no “stayers”, namely units for which D1 = D2. This is in contrast with de Chaisemartin et al. (2023), who assume throughout that there are stayers. Second, Assumption 4 states that there are “quasi-stayers”, namely units whose treatment change may be infinitesimally small. This assumption is realistic when the treatment is, say, temperatures: some counties may have very similar temperatures from one year to the next, though no county has exactly the same temperatures.

Hereafter, we focus on the following effect:

Y2(D2) − Y2(D1) D2 − D1

θ0 =E |∆D| E(|∆D|

×

(1)

![image 5](<2402.05432v1_images/imageFile5.png>)

![image 6](<2402.05432v1_images/imageFile6.png>)

E (sgn(∆D)(Y2(D2) − Y2(D1))) E(|∆D|)

=

.

![image 7](<2402.05432v1_images/imageFile7.png>)

θ0 is a weighted average of the slopes of units’ potential-outcome functions, from their periodone to their period-two treatment, the so-called WAOSS in de Chaisemartin et al. (2023). It follows from the mean-value theorem that it may be seen as a weighted average marginal effect.

## 2 Nonparametric identification and estimation

Theorem 1 If Assumptions 1-4 hold,

θ0 = [E (S∆Y ) − ζ0]/E[|∆D|], with S := sgn(∆D) and

E(∆Y |D1,|D2 − D1| ≤ η) .

ζ0 := E S lim

η↓0

Theorem 1 shows that without stayers, θ0 is identified by the limit (as η ↓ 0) of a differencein-difference comparing the ∆Y of all units and of quasi-stayers.

We now discuss estimation of θ0. Only the estimation of ζ0 raises difficulties. We show in the proof of Theorem 1 that under our assumptions, g(d1,δ) := E[∆Y |D1 = d1,∆D = δ] is welldefined and continuous at (d1,0), for any d1 ∈ D1. Hence, ζ0 satisfies ζ0 = E [Sg(D1,0)]. This formulation links our problem to the estimation of nonparametric additive models. To see this, suppose that the variables (W,X) ∈ R×Rk satisfy h(x) := E[W|X = x] = kj=1 hj(xj) for some unknown functions (hj)j=1,...,k. Then, under the normalization E[hj(Xj)] = 0 for j < k, we can identify and estimate hk by remarking that

hk(xk) = E[h(X1,...,Xk−1,xk)]. (2)

We can then estimate hk(xk) by first estimating h with any usual nonparametric estimator, and second plugging it in the sample counterpart of the expectation in (2). As Linton and Nielsen (1995) and Kong, Linton and Xia (2010) show, the corresponding estimator is, under regularity conditions, asymptotically normal and converges at the standard univariate nonparametric rate (namely, n2/5, with n the sample size). This rate is also the optimal convergence rate for this problem (Stone, 1985). Up to minor changes (in ζ0, g plays the role of h in (2) and ζ0 also includes S), our parameter ζ0 can be obtained in the same way as hk(xk), so we can also obtain an asymptotically normal estimator converging at the n2/5 rate.

This contrasts with the standard (n1/2) rate obtained for the estimators of the WAOSS in the presence of stayers, as shown by de Chaisemartin et al. (2023). To understand the difference, note that with stayers, the proportion of units used as controls to reconstruct switchers’ counterfactual outcome evolution remains positive as n → ∞. On the other hand, it tends to zero here, since we need to consider quasi-stayers, with η → 0 as n → ∞ to avoid any bias. This results in a lower rate of convergence.

Finally, in applications with no stayers, it is more difficult to propose placebo estimators of the parallel trends assumption. When a third period of data, period zero, is available, a placebo mimics the actual estimator, replacing ∆Y by units’ period-zero-to-one outcome evolution. However, as units’ treatments may have changed from period zero to one, one would need to restrict the sample to period-zero-to-one quasi-stayers, to avoid that the placebo differs from zero due to the treatment’s effect. Thus, the placebo would compare the period-zero-to-one outcome evolution of period-one-to-two switchers and quasi-stayers, restricting the sample to period-zero-to-one quasi-stayers. Then, we conjecture that the number of units used as controls by the placebo may tend to zero faster than the number of units used as controls by the actual estimator, for instance if being a period-zero-to-one and a period-one-to-two quasi-stayer are independent events. Then, the placebo may converge at an even slower rate than the actual estimator.

## 3 A parametric approach

We now consider a parametric root-n consistent estimator, that avoids issues related to nonparametric estimation and inference, while still allowing for heterogeneous and nonlinear effects. Specifically, we impose that g(d1,δ) = gλ

(d1,δ), where the family (gλ)λ∈Rp is known (but λ0 is not). By definition of g and Assumption 2,

0

g(d1,δ) = E[Y2(d1) − Y1(d1)|D1 = d1] + δE

Y2(d1 + δ) − Y2(d1) δ

D1 = d1,∆D = δ .

![image 8](<2402.05432v1_images/imageFile8.png>)

Thus, the parametric assumption amounts to imposing restrictions on both d1  → E[Y2(d1)− Y1(d1)|D1 = d1] and the average slope (d1,δ)  → E[(Y2(d1+δ)−Y2(d1))/ δ|D1 = d1,∆D = δ]. For instance, if gλ(d1,δ) is linear, we assume that the former function is linear, and the latter is constant. Similarly, g is a polynomial if both functions are polynomial. Note that we can test that E[∆Y |D1 = d1,∆D = δ] = gλ

(d1,δ) for some λ0 by a parametric specification test, see e.g. Bierens (1982) or Hong and White (1995).

0

We consider a simple two-step estimator based on this parametric restriction and an i.i.d. sample (D1i,∆Di,∆Yi)i=1,...,n. In the first step, we estimate λ0 by (linear or nonlinear) least squares or, more generally, a GMM estimator λ. In the second step, we estimate θ0 by

n

i=1 Si(∆Yi − g λ(D1i,0))

θ =

.

![image 9](<2402.05432v1_images/imageFile9.png>)

n

i=1 |∆Di|

Since θ may be seen as a two-step GMM estimator, we obtain, under Assumptions 1-4 and

standard regularity conditions on λ  → gλ(d1,δ),

√n θ − θ0 −→ d N (0,V (ψ)), where the influence function ψ satisfies

![image 10](<2402.05432v1_images/imageFile10.png>)

1 E[|∆D|]

ψ =

![image 11](<2402.05432v1_images/imageFile11.png>)

(D1,0)) − E S

S (∆Y − gλ

0

∂g ∂λ

0 × ξ − θ0|∆D| ,

(D1,0)|λ=λ

![image 12](<2402.05432v1_images/imageFile12.png>)

with ξ the influence function of λ. We can thus simply estimate V (ψ) by a plug-in estimator, using an initial estimator of ξ.

## 4 Application

We use the data from Deschênes and Greenstone (2012) to compute our parametric estimator. The authors use a balanced panel of 2,342 US counties in years 1987, 1992, 1997, and 2002, and consider TWFE regressions, weighted by counties’ farmland acres, of annual agricultural profits in county c and year t on four treatment variables: growing season degree days, growing season degree days squared, precipitations, and precipitations squared. To fit in the two-periods-one-treatment case we consider, we restrict the data to years 1997 and 2002, and we focus on the growing season degree days treatment. The coefficient of that treatment in a TWFE regression estimated on years 1997 and 2002 and weighted by counties’ farmland acres is equal to -0.024 (s.e. clustered at the county level: 0.007), which is close to the corresponding TWFE coefficient keeping the four years and all treatments (-0.015, s.e. clustered at the county level: 0.005). Assuming that

E[Y2(d1) − Y1(d1)|D1 = d1] = λ0,1 + λ0,2d1 and

E

Y2(d1 + δ) − Y2(d1) δ

D1 = d1,∆D = δ = λ0,3 + λ0,4d1 + λ0,5δ,

![image 13](<2402.05432v1_images/imageFile13.png>)

we find that θ, weighted by counties’ farmland acres as well, is equal to −0.018 (s.e.: 0.011) Thus, the conclusion from the TWFE regression seems robust to allowing for some effect heterogeneity, even though the estimated effect is less significant. While arguably restrictive, our model for the conditional expectation function of slopes allows for some non-linearity and heterogeneity in the effects of temperatures on agricultural output.

## Appendix: proof of theorem 1

It suffices to show that a.s., lim

E (∆Y |D1,|∆D| ≤ η) = E (Y2(D1) − Y1(D1)|D1,D2) . (3)

η↓0

Fix η > 0. By Assumption 4, P(|∆D| ≤ η|D1) > 0. Thus, E (∆Y |D1,|∆D| ≤ η) is welldefined. Moreover,

E (∆Y |D1,|∆D| ≤ η) =E (Y2(D2) − Y2(D1)|D1,|∆D| ≤ η)

+ E (Y2(D1) − Y1(D1)|D1,|∆D| ≤ η). (4) Now, by Jensen’s inequality and Point 2 of Assumption 3,

E [Y2(D2) − Y2(D1)|D1,|∆D| ≤ η] ≤E (|Y2(D2) − Y2(D1)| |D1,|∆D| ≤ η) ≤E Y |D2 − D1| |D1,|∆D| ≤ η ≤ηE sup

![image 14](<2402.05432v1_images/imageFile14.png>)

![image 15](<2402.05432v1_images/imageFile15.png>)

E Y |D1 = d1,D2 = d2 |D1,|∆D| ≤ η

(d1,d2)∈D

![image 16](<2402.05432v1_images/imageFile16.png>)

≤Kη (5) for some K < ∞. Next, by Assumption 2,

![image 17](<2402.05432v1_images/imageFile17.png>)

E (Y2(D1) − Y1(D1)|D1,|∆D| ≤ η) =E (Y2(D1) − Y1(D1)|D1)

=E (Y2(D1) − Y1(D1)|D1,D2) . Combined with (4)-(5), this yields (3)

## References

Bierens, Herman J. 1982. “Consistent model specification tests.” Journal of Econometrics,

20(1): 105–134.

De Chaisemartin, Clément, and Xavier D’Haultfœuille. 2020. “Two-way fixed effects estimators with heterogeneous treatment effects.” American Economic Review, 110(9): 2964–2996.

de Chaisemartin, Clément, Xavier D’Haultfœuille, Félix Pasquier, and Gonzalo Vazquez-Bare. 2023. “Difference-in-differences estimators for treatments continuously distributed at every period.” arXiv preprint arXiv:2201.06898.

Deschênes, Olivier, and Michael Greenstone. 2012. “The economic impacts of climate change: evidence from agricultural output and random fluctuations in weather: reply.” American Economic Review, 102(7): 3761–3773.

Hong, Yongmiao, and Halbert White. 1995. “Consistent specification testing via nonparametric series regression.” Econometrica: Journal of the Econometric Society, 63: 1133– 1159.

Kong, Efang, Oliver Linton, and Yingcun Xia. 2010. “Uniform Bahadur representation for local polynomial estimates of M-regression and its application to the additive model.” Econometric Theory, 26(5): 1529–1564.

#### Linton, Oliver, and Jens Perch Nielsen. 1995. “A kernel method of estimating struc-

tured nonparametric regression based on marginal integration.” Biometrika, 82(1): 93–100. Stone, Charles J. 1985. “Additive regression and other nonparametric models.” The Annals

of Statistics, 13(2): 689–705.

