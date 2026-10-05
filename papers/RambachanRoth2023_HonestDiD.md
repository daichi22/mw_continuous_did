# A More Credible Approach to Parallel Trends∗

##### Ashesh Rambachan† Jonathan Roth‡ April 1, 2022

###### Abstract

This paper proposes tools for robust inference in difference-in-differences and eventstudy designs where the parallel trends assumption may be violated. Instead of requiring that parallel trends holds exactly, we impose restrictions on how different the post-treatment violations of parallel trends can be from the pre-treatment differences in trends (“pre-trends”). The causal parameter of interest is partially identified under these restrictions. We introduce two approaches that guarantee uniformly valid inference under the imposed restrictions, and we derive novel results showing that they have desirable power properties in our context. We illustrate how economic knowledge can inform the restrictions on the possible violations of parallel trends in two economic applications. We also highlight how our approach can be used to conduct sensitivity analyses showing what causal conclusions can be drawn under various restrictions on the possible violations of the parallel trends assumption.

Keywords: Difference-in-differences, event-study, parallel trends, robust inference, sensitivity analysis, partial identification.

∗This paper was previously titled, “An Honest Approach to Parallel Trends.” We are grateful to Isaiah Andrews, Elie Tamer, and Larry Katz for their invaluable advice and encouragement. We also thank Clément de Chaisemartin, Gary Chamberlain, Raj Chetty, Peter Ganong, Ed Glaeser, Nathan Hendren, Ryan Hill, Ariella Kahn-Lang, Jens Ludwig, Sendhil Mullainathan, Claudia Noack, Frank Pinter, Adrienne Sabety, Pedro Sant’Anna, Jesse Shapiro, Neil Shephard, Jann Spiess, Jim Stock, and seminar participants at Brown, Chicago Booth, Dartmouth, Harvard, Michigan, Microsoft, Princeton, Rochester, UCL, Yale, SEA 2021, and ASSA 2022 for helpful comments, and Dorian Carloni for kindly sharing data. We gratefully acknowledge financial support from the NSF Graduate Research Fellowship under Grant DGE1745303 (Rambachan) and Grant DGE1144152 (Roth).

†Harvard University. Email: asheshr@g.harvard.edu ‡Brown University. Email: jonathanroth@brown.edu

## 1 Introduction

Researchers using difference-in-differences (DiD) and related methods are often unsure about the validity of the parallel trends assumption needed for point identification of the causal parameter of interest. It has therefore become common practice to assess the plausibility of the parallel trends assumption by testing for pre-treatment differences in trends (“pretrends”). Although pre-trends tests are intuitive, recent research has shown that they may suffer from low power (Freyaldenhoven, Hansen and Shapiro, 2019; Kahn-Lang and Lang, 2020; Bilinski and Hatfield, 2020; Roth, Forthcoming), and that conditioning the analysis on passing pre-trends tests introduces statistical issues related to pre-testing (Roth, Forthcoming). How then should researchers proceed when they are unsure about the validity of the parallel trends assumption?

This paper proposes methods for robust inference and sensitivity analysis in empirical settings where the parallel trends assumption may not hold. Building on work by Manski and Pepper (2018), we show that the causal parameter of interest can be (partially) identified under a large class of restrictions that impose that the post-treatment violations of parallel trends cannot be “too different” from the pre-trends. We then introduce methods that yield uniformly valid inference for the treatment effect under the imposed restrictions. Intuitively, our inference methods account for both statistical uncertainty (we can only noisily estimate the true pre-trend) as well as “identification uncertainty” (even if the true pre-trend were known, we may not know exactly how to extrapolate it). Our approach thus formalizes the intuition motivating pre-trends testing while avoiding the statistical issues described above.

More concretely, we consider a setting in which the researcher estimates a vector of “event-

study” coefficients βˆ “ pβˆpre1 ,βˆpost1 q1 P R¯T`T¯, where βˆpre and βˆpost respectively correspond with estimates for

T pre-treatment periods and T¯ post-treatment periods. We assume that βˆ is consistent for the reduced-form parameter β, which can be decomposed as

¯

˜ 0

¸

˜ δpre δpost

¸

, (1)

β “

`

τpost

loooomoooon“: τ

loooomoooon

“: δ

where τ is a causal parameter of interest that is assumed to be 0 in the pre-treatment period and δ is a bias from a difference in trends. For instance, in the canonical (nonstaggered) difference-in-differences framework, βˆ may be the coefficients from an “eventstudy regression” specification, τ the vector of period-specific average treatment effects on the treated (ATT) for some policy of interest, and δ the difference in trends of untreated potential outcomes between the treated and comparison groups. As we discuss in Section

- 2, this framework also applies to more complicated empirical settings, such as those with staggered treatment timing (e.g. Callaway and Sant’Anna, 2020; Sun and Abraham, 2020).


The usual parallel trends assumption used to point identify τpost is that δpost “ 0, and researchers frequently assess the plausibility of this assumption by testing the null hypothesis δpre “ 0 (a “pre-trends” test).

Instead of imposing that the parallel trends assumption holds exactly, we place restrictions on the possible post-treatment difference in trends δpost given the point identified pretrend δpre. Such restrictions formalize the intuition motivating pre-trends tests, namely that pre-trends are informative about counterfactual post-treatment differences in trends. Formally, we assume that δ P ∆ for some researcher-specified set ∆, and show that the causal parameter τpost is partially identified under such restrictions.

Restrictions of this form can be used to formalize a wide variety of intuitions about possible violations of the parallel trends assumption that are commonly expressed in applied work. For example, as discussed in Manski and Pepper (2018), researchers may be willing to assume that the confounding factors that create post-treatment violations of parallel trends are similar in magnitude to those in the pre-treatment period. This intuition can be formalized by specifying a ∆ that bounds the maximal post-treatment violation of parallel trends by a parameter M¯ times the maximal pre-treatment violation of parallel trends. In other contexts, researchers are concerned about violations of parallel trends from secular trends that are assumed to evolve smoothly over time. This intuition can be formalized by bounding the extent to which the slope of the violation of parallel trends can change over time. We adopt a flexible framework that allows researchers to capture these intuitions, as well as many other restrictions that are implied by context-specific knowledge about possible confounding factors.

We then introduce methods to conduct uniformly valid inference on a scalar parameter of the form θ “ l1τpost under the restriction δ P ∆. As emphasized in the recent literature on pre-trends testing, the pre-treatment coefficients βˆpre are often imprecise estimates of δpre. It is therefore important to introduce inference methods that account for the statistical uncertainty in the estimation of the event-study coefficients. We introduce two main inference approaches, with different desirable properties depending on the shape of ∆.

We first introduce a general inference approach that can accommodate a wide variety of restrictions of ∆. This approach is based on the observation that conducting inference on θ can be cast as the problem of testing a system of moment inequalities, allowing us to leverage a large econometrics literature on moment inequality testing (Canay and Shaikh (2017) provide a recent review). The moments have a potentially large number of nuisance parameters that enter linearly, and we therefore consider an implementation of this approach

based on the conditional and hybrid approaches of Andrews, Roth and Pakes (2021, henceforth ARP), who considered moment inequalities with this structure. Uniform size control for these tests follows nearly immediately from results in ARP.

We then prove that the tests proposed by ARP have some desirable power properties in our context. First, the conditional and hybrid tests are consistent, in the sense that they have power approaching 1 against fixed alternatives outside of the identified set. Second, we prove that the conditional test has optimal local asymptotic power under a linear independence constraint qualification (LICQ) assumption. As described in Kaido, Molinari and Stoye (2021), LICQ and related constraint qualifications have been used widely in the partial identification literature, and are often imposed to ensure size control. By contrast, we show that ARP conditional test is asymptotically valid even when LICQ fails, but has optimal local asymptotic power envelope when LICQ is satisfied. Intuitively, this result implies that the conditional test will perform well when the binding and non-binding moments are “far apart” relative to the sampling variation in the data. We provide several intuitive examples to illustrate when this result will and will not be applicable. Our result also implies that the ARP hybrid test will have near-optimal local asymptotic power under LICQ. These power results are new, and exploit additional structure in our context not contained in ARP.

Our second approach to inference is based on fixed length confidence intervals (FLCIs) (Donoho, 1994). FLCIs have desirable finite-sample guarantees for particular ∆s of interest. In particular, results from Armstrong and Kolesár (2018, 2020b) imply that when ∆ is convex and centrosymmetric, FLCIs have near-optimal expected length in the finite-sample normal model. These results are applicable for one of our leading examples, ∆SD, which restricts the smoothness of the difference in trends. In Monte Carlo simulations, we find that the use of such FLCIs can lead to substantial power gains over the conditional/hybrid approaches for ∆SD when the length of the identified set is short relative to the sampling variation in the data. This is intuitive since the asymptotic power guarantees for the conditional/hybrid approaches are in the asymptotic regime where sampling uncertainty is small relative to the length of the identified set, in contrast to the finite-sample guarantees for FLCIs. On the other hand, FLCIs are applicable for a much smaller range of ∆s: indeed, we show that for many other choices of ∆, they will be inconsistent in the strong sense that power against fixed points outside the identified set need not converge to one asymptotically.

Based on our theoretical results and Monte Carlo simulations, we recommend the ARP hybrid approach for general forms of ∆, but prefer the FLCI approach in special cases (such

- as for ∆SD) where the conditions for consistency and finite-sample near-optimality are met. We recommend that applied researchers use our methods to construct robust confidence


sets under economically-motivated restrictions on how the pre-trends relate to the post-

treatment violations of parallel trends. Our tools can also be used to to conduct sensitivity analyses in which the researcher reports confidence sets under varying restrictions on the possible differences in trends. For example, if the researcher suspects that the confounding factors in the post-treatment periods are similar in magnitude to those in the pre-treatment period, then it may be reasonable to impose that the post-treatment violations of parallel trends are no larger than the maximum pre-treatment violation of parallel trends. As a sensitivity analysis, the researcher might also report confidence sets that allow the post-treatment maximum violations of parallel trends to be up to M¯ times larger than the maximum pretreatment violation for different values of M¯ . Performing such sensitivity analyses makes clear what must be assumed about the possible differences in trends in order to draw specific causal conclusions. We provide an R package, HonestDiD, that implements our recommended methods.1 We illustrate our recommended approach with applications to two recently published papers, in which we show how the choice of the restrictions ∆ can be tailored to the economic context.

Related literature: The approach in this paper builds on the foundational partial identification analysis for DiD in Manski and Pepper (2018). Manski and Pepper consider identification under researcher-specified bounds on the magnitude of δpost (what they call “bounded DiD variation”), and calibrate these bounds using the maximal pre-treatment violation of parallel trends in their empirical application on the effects of right-to-carry gun laws.2 One of our leading classes of restrictions, ∆RM, formalizes this calibration approach by bounding the magnitude of post-treatment violations of parallel trends by M¯ times the maximal pre-treatment violation. Our framework also allows for many other intuitive restrictions such as bounds on how far δ can deviate from linearity — and it can be applied to a variety of difference-in-differences estimators, including recent proposals for settings with staggered treatment timing. Most importantly, while Manski and Pepper (2018) provide a framework for identification, we provide inference methods to construct uniformly valid confidence sets for the treatment effect of interest. This allows applied researchers to account for statistical uncertainty in their analyses, which can be important since event-study coefficients are often imprecisely estimated in practice.

Several other recent papers consider various relaxations of the parallel trends assumption. Keele, Small, Hsu and Fogarty (2019) develop techniques for testing the sensitivity

- 1The latest version of the R package can be downloaded by visiting http://github.com/ asheshrambachan/HonestDiD.
- 2Manski and Pepper (2018) also consider “bounded time” and “bounded state” restrictions that bound how much the mean of Y p0q can differ either across treatment groups or within-groups over time. Such restrictions could also be incorporated into our framework by augmenting the vector βˆ to include group-specific sample averages.


of DiD designs to violations of the parallel trends assumption, but they do not incorporate information from the observed pre-trends in their sensitivity analysis. Empirical researchers commonly adjust for the extrapolation of a linear trend from the pre-treatment periods when there are concerns about violations of the parallel trends assumption, which is valid if the difference in trends is exactly linear (e.g., Dobkin, Finkelstein, Kluender and Notowidigdo, 2018; Goodman-Bacon, 2018, 2021; Bhuller, Havnes, Leuven and Mogstad, 2013). Our methods nest this approach as a special case, but allow for valid inference under less restrictive assumptions about the class of possible differences in trends (such as when δ is only approximately linear). Freyaldenhoven et al. (2019) propose a method that allows for violations of the parallel trends assumption but requires an additional covariate that is affected by the same confounding factors as the outcome but not by the treatment of interest. Ye, Keele, Hasegawa and Small (2020) consider partial identification of treatment effects when there exist two control groups whose outcomes have a bracketing relationship with the outcome of the treated group. Leavitt (2020) proposes an empirical Bayes approach calibrated to pre-treatment differences in trends, and Bilinski and Hatfield (2020) and Dette and Schumann (2020) propose approaches based on pre-tests for the magnitude of the pre-treatment violations of parallel trends.

Our methods address several concerns related to current empirical practice in differencein-differences and event-study designs. First, pre-trends tests may be underpowered against meaningful violations of parallel trends, potentially leading to severe undercoverage of conventional confidential intervals (Freyaldenhoven et al., 2019; Bilinski and Hatfield, 2020; Kahn-Lang and Lang, 2020; Roth, Forthcoming). Second, statistical distortions from pretrends tests may further undermine the performance of conventional inference procedures (Roth, Forthcoming). Third, parametric approaches to controlling for pre-existing trends may be sensitive to functional form assumptions (Wolfers, 2006; Lee and Solon, 2011). We address these issues by providing tools for inference that do not rely on an exact parallel trends assumption, incorporate statistical uncertainty about the estimated event-study coefficients, and make clear the mapping between the researcher’s assumptions about the potential differences in trends and the strength of their causal conclusions.

Our work complements a growing literature on the causal interpretation of event-study coefficients in two-way fixed effects models in the presence of staggered treatment timing and heterogeneous treatment effects (Borusyak and Jaravel, 2016; Athey and Imbens, 2021; Goodman-Bacon, 2021; Callaway and Sant’Anna, 2020; de Chaisemartin and D’Haultfœuille, 2020; Sun and Abraham, 2020). A key finding is that regression coefficients from conventional approaches may not produce convex weighted averages of treatment effects even if parallel trends holds. Several alternative estimators have been proposed that consistently estimate

interpretable causal estimands under a suitable parallel trends assumption. Our methodology can be used in conjunction with these alternative estimators to assess their sensitivity to violations of the corresponding parallel trends assumption; see Section 2.1 for additional details.

More broadly, our work contributes to a larger econometric literature that uses partial identification to provide empirical researchers with tractable tools to conduct inference under assumptions that may be more credible in empirical practice; see, for example, Manski (2003, 2007, 2013), Tamer (2010), Ho and Rosen (2017), and Molinari (2020) for reviews.

## 2 Model set-up

#### 2.1 Event-study Coefficients

We suppose that the researcher has estimated a vector of “event-study coefficients” βˆn P R¯T`T¯, which can be partitioned into vectors of coefficients corresponding with the pretreatment and post-treatment periods, βˆn “ pβˆn,pre1 ,βˆn,post1 q, where βˆn,pre P R¯T and βˆn,post P RT¯. Event-study estimates of this form arise from non-staggered DiD as well as a variety of related estimators, as we illustrate with several examples

- Example 1 (Non-staggered DiD). Consider the canonical DiD setting in which we have a


T,...,T¯, and units with Di “ 1 receive a treatment beginning in period t “ 1, while units with Di “ 0 never receive the treatment. It is common to report difference-in-differences estimates of the form

balanced panel of units from period t “ ´¯

βˆs “ pY¯s1 ´ Y¯s0q ´ pY¯01 ´ Y¯00q,

where Y¯sd is the sample mean of the outcome for units with Di “ d in period t “ s. Intuitively, βˆs compares the change in the mean outcome between period 0 and period s for the treated and comparison units. In this setting, the estimates βˆs are numerically equivalent to the OLS coefficients from the regression

Yit “ λi ` φt ` ÿ

βs ˆ rt “ ss ˆ Di ` it. (2)

s‰0

In this case, βˆpost collects the estimated coefficients corresponding with treated periods, pβˆ1,...,βˆT¯q, while βˆpre collects the estimated coefficients corresponding with periods before treatment pβˆ´

T,...βˆ´1q.

¯

- Example 2 (Staggered DiD). Event-study coefficients can also be obtained from more complicated DiD procedures. For example, in settings with staggered treatment timing, Callaway and Sant’Anna (2020) propose event-study estimates of the form

βˆr “ ÿ

g

wgATTzpg,g ` rq,

where ATTzpg,tq is a difference-in-differences estimate that compares the evolution of the outcome for units first treated at period g to units first-treated after period t between time periods g ´ 1 and t, and the wg are weights that sum to one (e.g. proportional to sample size). In this case, βˆpost collects the values of βˆr for r ě 0 (i.e. estimates where one of the groups is treated), and βˆpre collects the values of βˆr for values of r ă 0. Several other related procedures have been proposed for constructing event-study coefficients in contexts with staggered treatment timing; see de Chaisemartin and D’Haultfœuille (2021) and Roth, Sant’Anna, Bilinski and Poe (2022) for reviews.

- Example 3 (Other related estimators). Other examples of estimators that can be used to produce event-studies coefficients of the form considered here include the GMM procedure proposed by Freyaldenhoven et al. (2019), instrumental variables event-studies (Hudson, Hull and Liebersohn, 2017), as well estimators that flexibly control for differences in covariates between treated and comparison groups (e.g., Heckman, Ichimura, Smith and Todd, 1998; Abadie, 2005; Sant’Anna and Zhao, 2020).


#### 2.2 Causal Decomposition

Under mild regularity conditions, all of the estimators described above will be asymptotically normally distributed, satisfying ?npβˆn ´ βq Ñ N p0, Σ˚q for some parameter vector β. We assume the parameter vector β satisfies the following causal decomposition.

- Assumption 1. The parameter vector β can be decomposed as


˜ τpre τpost

¸

˜ δpre δpost

¸

with τpre “ 0. (3)

β “

`

loooomoooon“: τ

loooomoooon

“: δ

The first term, τ, represents the treatment effects of interest. We assume the treatment has no causal effect prior to its implementation, so τpre “ 0. The second term, δ, represents the difference in trends between the treated and comparison groups that would have occurred

absent treatment. The parallel trends assumption imposes that δpost “ 0, and therefore βpost “ τpost under parallel trends.

Example: Non-staggered DiD (continued) Suppose the observed outcome satisfies Yit “ DiYitp1q`p1´DiqYitp0q, where Yitp1q and Yitp0q are respectively the potential outcomes when unit i is ultimately treated / not treated. Assume further that there is no anticipation of treatment, so that Yitp1q “ Yitp0q for all t ă 1. Then, for any s, under mild regularity conditions βˆs will be consistent for

βs “ τATT,s ` EloooooooooooooooooooooooooooooooooooomoooooooooooooooooooooooooooooooooooonrYisp0q ´ Yi0p0q|DDifferentiali “ 1s ´trendErY“is: δps0q ´ Yi0p0q|Di “ 0s

,

where τATT,s “ ErYisp1q ´ Yisp0q|Di “ 1s is the average treatment effect on the treated in period s, and δs is the difference in trends in potential outcomes between period 0 and period s.3 Since the no-anticipation assumption implies that τATT,s “ 0 for s ă 0, this yields the decomposition (3).

Example: Staggered DiD (continued) Likewise, in the staggered DiD context, define Yitpgq to be the potential outcome for unit i in period t if they are first treated at period g and Yitp8q to be the never-treated potential outcome. Then βˆr will be consistent for the parameter βr “ τr ` δr, where τr “ ř

g wgATTpg,g ` rq and ATTpg,g ` rq “ ErYi,g`rpgq ´ Yi,g`rp8q|Gi “ gs is the ATT in period g ` r for units first treated

- at period g. Likewise δr “ ř


wgδg,g`r, where δg,g`r “ ErYi,g`rp8q ´ Yi,g´1p8q|Gi “ gs ´ ErYi,g`rp8q ´ Yi,g´1p8q|Gi ą g ` rs is the difference in trends in never-treated potential outcomes between units first treated at period g and units first treated after period g`r. Under a no-anticipation assumption, τr “ 0 for r ă 0, which again yields the decomposition (3).

Example: Other related estimators (continued) We can decompose β as in (3) for other estimators as well. For example, for event-study IVs (with non-staggered timing), τpost is a vector containing the local average treatment effect for each period, and δ represents the violation of the exclusion restriction at each period. For methods that flexibly control for covariate differences between treated and comparison groups, τpost is again a vector of ATTs, and δpost represents a weighted average (across covariates) of the violation of the conditional parallel trends assumption.

3We focus on the ATT as the target parameter, as in most of the DiD literature. If one is interested in the population-wide average treatment effect (ATE), one could obtain bounds on the ATE under restrictions on treatment effect heterogeneity, or other assumptions that allow one to bound the treatment effects for untreated units; see Manski and Pepper (2013) for an insightful discussion.

#### 2.3 Target parameter and identification

We suppose the target parameter is a linear combination of the post-treatment causal effects, θ :“ l1τpost for some known T¯-vector l. For example, θ equals the t-th period causal effect τt when the vector l equals the t-th standard basis vector. Similarly, θ equals the average causal effect across all post-treatment periods when l “ ` 1

˘1

.

T¯,..., T1¯

We obtain partial identification of θ by assuming that δ lies in a researcher-specified set of possible differences in trends ∆ Ď R¯T`T¯. This nests the usual parallel trends assumption as the special case with ∆ “ tδ : δpost “ 0u. Since δpre “ βpre is identified, the assumption that δ “ pδpre1 ,δpost1 q1 P ∆ restricts the possible values of δpost given the identified value of the pre-treatment difference in trends δpre.

It is natural to place restrictions on the relationship between δpre and δpost, since applied researchers frequently test the null hypothesis δpre “ 0 in order to assess the plausibility of the assumption that δpost “ 0. Our identification framework, which generalizes the partial identification framework in Manski and Pepper (2018), thus helps formalize the intuition motivating pre-trends testing.

Under the assumption that δ P ∆ ‰ tδ : δpost “ 0u, the parameter θ will typically be set-identified. The identified set is the set of values for θ that are consistent with a given value of β under the restriction δ P ∆,

˜ 0

¸+. (4)

#θ : Dδ P ∆,τpost P RT¯ s.t. l1τpost “ θ,β “ δ `

Spβ,∆q :“

τpost

When ∆ is a closed and convex set, the identified set has a simple characterization.

- Lemma 2.1. If ∆ is closed and convex, then Spβ,∆q is an interval in R, Spβ,∆q “ rθlbpβ,∆q,θubpβ,∆qs, where


θlbpβ,∆q :“ l1βpost ´ ´max

l1δpost, s.t. δ P ∆,δpre “ βpre¯ looooooooooooooooooooooomooooooooooooooooooooooon

, (5)

δ

“:bmaxpβpre,∆q

θubpβ,∆q :“ l1βpost ´ ´min

l1δpost, s.t. δ P ∆,δpre “ βpre¯ loooooooooooooooooooooomoooooooooooooooooooooon

. (6)

δ

“:bminpβpre,∆q

Proof. Re-arranging terms in (4), the identified set can be equivalently written as Spβ,∆q “ tθ : Dδ P ∆ s.t. δpre “ βpre,θ “ l1βpost ´ l1δpostu. The result is then immediate.

| |
|---|


T “ T¯ “ 1), the ATT in period 1 is point identified if we assume that the counterfactual post-treatment

###### Example: Non-staggered DiD (continued) In the three-period DiD model (

¯

difference in trends δ1 is exactly zero (parallel trends). Instead, we assume δ “ pδ´1,δ1q1 P ∆ for some set ∆. When ∆ is closed and convex, the identified set for the ATT in period 1 is rβ1 ´ bmax,β1 ´ bmins, where bmax “ maxδ δ1 s.t pδ´1,δ1q1 P ∆ is the maximum possible bias of βˆ1 given δ´1 “ β´1 and bmin is defined analogously.

Additionally, it is immediate from the definition of the identified set in (4) that if ∆ is the finite union of sets, ∆ “ ŤK

k“1 ∆k, then its identified set is the union of the identified sets for its subcomponents,

ďK

Spβ,∆kq. (7)

Spβ,∆q “

k“1

This fact will be useful, since several empirically relevant choices of ∆ can be written as the finite union of convex sets as we will see below.

#### 2.4 Possible choices of ∆

The class of possible differences in trends ∆ must be specified by the researcher, and the choice of ∆ will depend on the economic context. We highlight several possible choices of ∆ that may be reasonable in empirical applications and formalize intuitive arguments that are commonly made by applied researchers regarding possible violations of parallel trends. Throughout our discussion, we write δpre “ pδ´

T,...δ´1q1 and δpost “ pδ1,...δT¯q1, with δ0 normalized to zero. This aligns the notation with Example 1, where δ corresponds to the difference in trends between treated and comparison groups, and δ0 is normalized to zero.

¯

###### 2.4.1 Bounding Relative Magnitudes

In empirical applications, researchers may be willing to assume that the confounding factors which produce non-parallel trends in the post-treatment periods are not too much larger in magnitude than the confounding factors in the pre-treatment periods. In their empirical application to right-to-carry gun laws, Manski and Pepper (2018) operationalize this intuition by calibrating bounds on |δ1| to the largest violations of parallel trends in the pre-treatment period (see their Table 3).4 Such a restriction can be formalized in our framework by imposing that δ P ∆RMpM¯ q for M¯ ě 0, where

∆RMpM¯ q “ tδ : @t ě 0, |δt`1 ´ δt| ď M¯ ¨ max

|δs`1 ´ δs|u.

să0

4In their application, Manski and Pepper (2018) observe the outcome for the entire population of interest, and thus their observed pre-treatment data corresponds with δpre rather than βˆpre.

∆RMpM¯ q bounds the maximum post-treatment violation of parallel trends between consecutive periods by M¯ times the maximum pre-treatment violation of parallel trends. We use the abbreviation RM for “relative magnitudes”. The choice ∆RMpM¯ q may be reasonable if the researcher suspects that possible violations of parallel trends are driven by confounding economic shocks that are of a similar magnitude to confounding economics shocks in the pre-period. When the number of pre-treatment and post-treatment periods is similar, a natural benchmark may be M¯ “ 1, which bounds the worst-case post-treatment difference in trends by the equivalent maximum in the pre-treatment period.

T “ T¯ “ 1), assuming δ P ∆RMpM¯ q “ tpδ´1,δ1q1 : |δ1| ď M¯ |δ´1|u bounds the magnitude of δ1 based on the magnitude of δ´1. The larger the magnitude of the pre-treatment violation in parallel trends, |δ´1|, the wider the range of possible post-treatment violations of parallel trends.

###### Example: Non-staggered DiD (continued) In the three-period DiD model (

¯

###### 2.4.2 Smoothness restrictions

In other empirical settings, researchers may be worried about confounding from secular trends (e.g. long-run changes in labor supply) that they suspect evolve smoothly over time. In such settings, it is common for empirical researchers to control for a linear group-specific time trend.5 This approach is valid if the difference in trends is linear, i.e. ∆ “ tδ: δt “ γ ¨ t,γ P Ru. There are often concerns, however, that the linear specification is not exactly correct (Wolfers, 2006; Lee and Solon, 2011). A natural relaxation is therefore to impose only that the differential trends evolve smoothly over time by bounding the extent to which its slope may change across consecutive periods. Such a restriction can be formalized in our framework by imposing that δ P ∆SDpMq for M ě 0, where

∆SDpMq :“ tδ : |pδt`1 ´ δtq ´ pδt ´ δt´1q| ď M, @tu. (8)

The parameter M ě 0 governs the amount by which the slope of δ can change between consecutive periods, and thus bounds the discrete analog of the second derivative. We use the abbreviation SD for “second differences” or “second derivative.”6 In the special case where M “ 0, ∆SDp0q requires that the difference in trends be exactly linear, which corresponds

- 5Specifically, researchers often augment specification (2) with group-specific linear trends, an approach Dobkin et al. (2018) refer to as a “parametric event-study.” An analogous approach is to estimate a linear trend using only observations prior to treatment, and then subtract out the estimated linear trend from the observations after treatment (Bhuller et al., 2013; Goodman-Bacon, 2018, 2021).
- 6Restrictions on the second derivative of the conditional expectation function or density have been used in regression discontinuity settings (Kolesár and Rothe, 2018; Frandsen, 2016; Noack and Rothe, 2020). Smoothness restrictions are also used to obtain partial identification in Kim, Kwon, Kwon and Lee (2018).


with the assumption underlying the parametric linear specification common in applied work.

Example: Non-staggered DiD (continued). In the three-period DiD model, assuming the differential trend is exactly linear is equivalent to assuming ∆ “ tδ : δ1 “ ´δ´1u. Assuming δ P ∆SDpMq requires only that the linear extrapolation be approximately correct, δ1 P r´δ´1 ´ M,´δ´1 ` Ms.

###### 2.4.3 Combining smoothness and relative magnitudes bounds

In some contexts, researchers may be willing to assume that the difference in trends evolves relatively smoothly over time but may be unsure about the smoothness bound M ě 0 introduced above. In such cases, it may be reasonable to assume that the possible non-linearities in the post-treatment difference in trends are bounded by the observed non-linearities in the pre-treatment difference in trends. This can be formalized with the restriction

∆SDRMpM¯ q “ tδ : @t ě 0, |pδt`1 ´ δtq ´ pδt ´ δt´1q| ď M¯ ¨ max

|pδs`1 ´ δsq ´ pδs ´ δs´1q|u,

să0

which bounds the maximum deviation from a linear trend in the post-treatment period by

- M¯ ě 0 times the equivalent maximum in the pre-treatment period. The set ∆SDRMpM¯ q is thus similar to ∆SDpMq introduced above, except it allows the magnitude of the possible non-linearity to explicitly depend on the observed pre-trends.


###### 2.4.4 Sign and monotonicity restrictions

Context-specific knowledge may sometimes also suggest sign or monotonicity restrictions on the differential trend. For instance, if the policy of interest occurs at the same time as a confounding policy change that we expect to have a positive effect on the outcome, we might restrict the post-treatment bias to be positive, δ P ∆PB :“ tδ : δt ě 0 @t ě 0u. Likewise, there may be secular pre-existing trends that we expect would have continued following the treatment date.7 We may then wish to impose that the differential trend be increasing, δ P ∆I :“ tδ : δt ě δt´1 @tu, or monotone with unknown sign, δ P ∆Mon :“ ∆I Yp´∆Iq. Sign and monotonicity restrictions may be combined with the previously discussed restrictions, such as ∆SDPBpMq :“ ∆SDpMq X ∆PB, ∆SDIpMq :“ ∆SDpMq X ∆I, and ∆RMIpM¯ q :“ ∆RMpM¯ q X ∆I.

7Monotone violations of parallel trends are often discussed in applied work. For example, Lovenheim and Willen (2019) argue that violations of parallel trends cannot explain their results because “pre-[treatment] trends are either zero or in the wrong direction (i.e., opposite to the direction of the treatment effect).” Greenstone and Hanna (2014) estimate upward-sloping pre-existing trends and argue that “if the pre-trends had continued” their estimates would be upward biased.

###### 2.4.5 Polyhedral restrictions

Although the restrictions described above will be sensible in many empirical contexts, researchers will often have context-specific knowledge that motivates alternative restrictions than what we introduced above. To accommodate such cases, we consider the broad class of ∆s that can be written as polyhedra (sets defined by linear inequalities), or the finite union of polyhedra.

- Definition 1 (Polyhedral restriction). The class ∆ is polyhedral if it takes the form ∆ “ tδ : Aδ ď du for some known matrix A and vector d.


All of the examples described above can be written either as polyhedral restrictions or finite unions of such restrictions. For instance, ∆SDpMq and ∆SDPBpMq can be written directly as polyhedra.8 Likewise, ∆RMpM¯ q or ∆SDRMpM¯ q can be written as the finite union of polyhedra, where each polyhedron corresponds with a different location for the maximum pre-treatment violation.9

The class of (finite unions of) polyhedra is quite broad, and allows for a variety of other restrictions that may be relevant in empirical work. For example researchers studying labor market training and related programs may be concerned about Ashenfelter’s dip (Ashenfelter, 1978), in which earnings for the treated group trend downwards (relative to control) before treatment and upwards afterwards. In this type of setting, researchers might naturally use a polyhedral ∆ to impose i) restrictions on the signs of the pre-treatment and post-treatment biases, as well as ii) restrictions on the magnitude of the rebound effect relative to the pre-treatment shock.

#### 2.5 Inferential Goal

As discussed above, the event study coefficients βˆn will satisfy ?npβˆn ´ βq Ñd N p0, Σ˚q for a wide variety of commonly-used estimators. This suggests the finite-sample normal approximation

βˆn «d N pβ, Σnq, (9)

where «d denotes approximate equality in distribution and Σn “ Σ˚{n. We will construct confidence sets that are uniformly valid for all parameter values θ in the identified set when

ˆ ´8In1 our1 ongoing three-period difference-in-differences example, ∆SDpMq “ tδ : ASDδ ď dSDu for ASD “

˙ and dSD “ pM,Mq1. This generalizes naturally when there are multiple pre-periods and multiple post-periods.

1 ´1

9For example, define the polyhedra ∆RMs,` pM¯ q “ tδ : @t ě 0,|δt`1 ´δt| ď M¯ pδs`1 ´δsqu and ∆RMs,´ “ tδ : @t ě 0,|δt`1 ´ δt| ď ´M¯ pδs`1 ´ δsqu. Then ∆RMpM¯ q “ Ť

`

∆RMs,` pM¯ q Y ∆RMs,´ pM¯ q˘

.

să0

the approximation in (9) holds exactly with Σn known. That is, we construct confidence sets Cnpβˆn,Σnq satisfying

´θ P Cnpβˆn,Σnq¯ ě 1 ´ α. (10)

Pβˆ

inf

inf

n„Npδ`τ, Σnq

δP∆,τ

θPSpδ`τ,∆q

In Section 3.3, we will show that finite-sample size control in the normal model in the sense of (10) translates to uniform asymptotic size control over a large class of data-generating processes when Σn is replaced by a consistent estimate Σˆn. That is, we will show that the constructed confidence sets further satisfy

PP ´θ P Cnpβˆn,Σˆnq¯ ě 1 ´ α. (11) for a large class of distributions P such that δP P ∆ for all P P P.

liminf

inf

inf

nÑ8

PPP

θPSpδP `τP ,∆q

We will focus on constructing confidence sets for the case where ∆ is a polyhedron. For the case where ∆ is the finite union of polyhedra, a valid confidence set can be constructed by taking the union of the confidence sets for each of its components.

- Lemma 2.2. Suppose that for each k “ 1,...,K, the confidence set Cn,kpβˆn,Σnq satisfies

(10) with ∆ “ ∆k. Then the confidence set Cnpβˆn,Σnq “ ŤK

k“1 Cn,kpβˆn,Σnq satisfies (10) with ∆ “ ŤK

k“1 ∆k.

In the next two sections, we introduce two approaches to obtain confidence sets satisfying (10), with different desirable properties depending on the form of ∆. The first approach, based on moment inequalities, accommodates a wide range of restrictions ∆ and has some desirable asymptotic power guarantees. The second approach, based on fixed length confidence intervals, can potentially offer finite-sample power improvements for certain special classes of ∆ of interest, such as ∆SDpMq.

- 3 Inference using Moment Inequalities


In this section, we introduce a general approach for inference that has good asymptotic properties over a large class of possible restrictions ∆. We show that inference on the partially identified parameter θ “ l1τpost in this setting is equivalent to testing a system of moment inequalities with a potentially large number of nuisance parameters that enter the moments linearly. We consider an implementation based on the conditional approach developed in ARP, which allows us to obtain computationally tractable confidence sets with desirable power properties for many parameter configurations.

#### 3.1 Representation as a moment inequality problem with linear nuisance parameters

Consider the problem of conducting inference on θ “ l1τpost when ∆ takes the polyhedral form ∆ “ tδ : Aδ ď du. We will develop tests that have exact size under the null hypothesis H0 : θ “ θ,δ¯ P ∆ when the normal approximation (9) holds exactly with known variance matrix Σn. In Section 3.3, we will provide conditions under which size control in the finite sample normal model translates to uniform asymptotic size control over a large class of data-generating processes.

As a first step, we show that testing H0 is equivalent to testing a system of moment inequalities with linear nuisance parameters in the normal model. Observe that if βˆn „ n„Npδ`τ, Σnq

”βˆn ´ τı “ δ. It follows that δ P ∆ “ tδ : Aδ ď du if and only if Eβˆ

- N pβ, Σnq for β satisfying (3), then Eβˆ


”Aβˆn ´ Aτı ď d. Defining Yn “ Aβˆn ´ d and Lpost “ r0,Is1 to be the matrix such that τ “ Lpostτpost, it is immediate that the null hypothesis H0 is equivalent to the composite null

n„Npδ`τ, Σnq

H0 : Dτpost P RT¯ s.t. l1τpost “ θ¯ and Eβˆ

n„Npδ`τ,Σnq rYn ´ ALpostτposts ď 0. (12)

Testing the null hypothesis H0 is therefore equivalent to testing that the moment inequalities Eβˆ

n„Npδ`τ,Σnq rYn ´ ALpostτposts ď 0 hold for some value of τpost satisfying l1τpost “ θ.

For the purposes of developing tests, it will be useful to re-cast this null hypothesis in terms of moments involving an unrestricted nuisance parameter τ˜ of dimension T¯ ´ 1. By applying a change of basis to the matrix ALpost, we can re-write the expression ALpostτpost

- as A˜pθ,τ˜1q1 for τ˜ PT¯´1.10 The null H0 is then equivalent to


H0 : Dτ˜ P RT¯´1 s.t. E”Y˜npθ¯q ´ X˜τ˜ı ď 0, (13)

where Y˜pθ¯q “ Yn ´ A˜p¨,1qθ¯ and X˜ “ A˜p¨,´1q.11 Since Y˜npθ¯q is normally distributed with covariance matrix Σ˜n “ AΣnA1 under the finite-sample normal model, testing H0 : θ “ θ,δ¯ P ∆ is equivalent to testing a system of moment inequalities with linear nuisance parameters.

The testing problem (13) is a special case of the problem studied in ARP, which focuses on

10Let Γ be a square matrix with the vector l1 in the first row and remaining rows chosen so that Γ has

¨ ˝

˛ ‚. If T¯ “ 1, then τ˜ is

θ

full rank. Define A˜ :“ ALpostΓ´1. Then ALpostτpost “ A˜Γτpost “ A˜

looooomooooonΓp´1:,“¨qτ˜τpost

0-dimensional and should be interpreted as 0.

11We use the notation Vp¨,1q to denote the first column of a matrix V , and Vp¨,´1q to denote the matrix containing all but the first column of V .

testing null hypotheses of the form H0 : Dτ s.t. ErY pθq ´ Xτ |Xs ď 0 (a.s.). Our setting is a special case of this framework in which: i) the variable X takes the degenerate distribution X “ X˜, and ii) Y pθq “ Y˜pθq is linear in θ. This additional structure will play an important role in the development of our asymptotic power results below.

#### 3.2 Constructing conditional and hybrid confidence sets

We consider tests for the system of moment inequalities describe above using the conditional and hybrid methods proposed by ARP. This is for both computational and efficiency reasons. From the computational perspective, a practical challenge to testing the hypothesis (13) in our setting is that the dimension of the nuisance parameter τ˜ is T¯ ´ 1, and thus will be large if there are many post-treatment periods. For example, 5 of the 12 recent event-study papers reviewed in Roth (Forthcoming) have T¯ ą 10. This renders many moment inequality methods, especially those which rely on test inversion over a grid for the full parameter vector, computationally infeasible. To tractably deal with the nuisance parameter, we consider tests based on the conditional and hybrid approaches of ARP, which directly exploit the linear structure of the hypothesis (13) to deliver computationally tractable tests even when the number of post-treatment periods T¯ is large.12 From the perspective of power, we will show that the tests proposed by ARP have (near-)optimal local asymptotic power in our setting when an LICQ condition is satisfied.

We briefly sketch the construction of the conditional testing approach in our setting, and refer the reader to ARP for full details. These tests are implemented in the R package, HonestDiD, that accompanies the paper.

Conditional confidence sets. Suppose we wish to test (13) for some fixed θ¯. The conditional testing approach considers tests based on the profiled test statistic

η s.t. Y˜npθ¯q ´ X˜τ˜ ď σ˜n ¨ η, (14)

ηˆ :“ min

η,τ˜

where σ˜n “ bdiagpΣ˜nq. This linear program selects the value of the nuisance parameters τ˜ P RT¯´1 that minimizes the maximum studentized moment. Duality results from linear

12Other moment inequality methods have been proposed for subvector inference, but typically do not exploit the linear structure of our setting — see, e.g, Romano and Shaikh (2008); Chernozhukov, Newey and Santos (2015); Bugni, Canay and Shi (2017); Chen, Christensen and Tamer (2018); Kaido, Molinari and Stoye (2019). Cho and Russell (2019), Gafarov (2019), and Flynn (2019) also provide methods for subvector inference with linear moment inequalities, but in contrast to our approach require a linear independence constraint qualification (LICQ) assumption for size control. More recently, Cox and Shi (2022) introduced new tests for the linear moment inequality setting in ARP; see Section 3.5 below for further discussion.

programming (e.g. Schrijver (1986), Section 7.4) imply that the value ηˆ obtained from the primal program (14) equals the optimal value of the dual program13

γ1Y˜npθ¯q s.t. γ1X˜ “ 0,γ1σ˜n “ 1,γ ě 0. (15)

ηˆ “ max

γ

If a vector γ˚ is optimal in the dual problem above, then it is a vector of Lagrange multipliers for the primal problem. Standard results in linear programming imply that the optimum is always obtained at one of the finite set of vertices, V pΣnq (also known as the set of basic feasible solutions). We denote by Vˆn Ă V pΣnq the set of optimal vertices of the dual program.14

To construct critical values, ARP use the fact that the distribution of ηˆ has a truncated normal distribution conditional on the event that γ˚ is optimal in the dual problem. Specifically,

ηˆ|tγ˚ P Vˆn,Sn “ su „ ξ |ξ P rvlo,vups, where ξ „ N ´γ˚1 µ˜pθ¯q, γ˚1 Σ˜nγ˚¯, µ˜pθ¯q “ E”Y˜npθ¯qı, Sn “ pI ´ Σ˜

γ˚1 Σ˜nγ˚γ˚1 qY˜npθ¯q, and vlo,vup are known functions of Σ˜n,s,γ˚ (see Lemma 2 in ARP).15 Intuitively, the distribution of ηˆ depends on the vector µ˜pθ¯q, and so to eliminate the dependence on the components of µ˜pθ¯q other than γ1µ˜pθ¯q, we condition on Sn, which is a sufficient statistic for the components of µ˜pθ¯q that are orthogonal to γ˚1 µ˜pθ¯q.

nγ˚

ARP show that all quantiles of the conditional distribution of ηˆ in the previous display are increasing in γ˚1 µ˜pθ¯q. Moreover, the null hypothesis (13) implies γ˚1 µ˜pθ¯q ď 0. To see why this is the case, note that the definition of the dual problem (15) implies that γ˚ ě 0 and γ˚1 X˜ “ 0, whereas the null hypothesis implies that there exists τ˜ such that µ˜pθ¯q´X˜τ˜ ď 0. It follows that γ˚1 µ˜pθ¯q “ γ˚1 pµ˜pθ¯q´X˜τ˜q ď 0 under the null. The ARP conditional test therefore uses the critical value maxt0,cC,αu, where cC,α is the 1 ´ α quantile of the truncated normal distribution ξ|ξ P rvlo,vups under the worst-case assumption that γ˚1 µ˜pθ¯q “ 0.16 We denote

- 13Technically, the duality results require that ηˆ be finite. However, one can show that ηˆ is finite with probability 1, unless the span of X˜ contains a vector with all negative entries, in which case the identified set for θ is the real line. We therefore trivially define our test never to reject if ηˆ “ ´8.
- 14In general, there may not be a unique solution to the dual program. ARP show that in the context of the finite sample normal, conditional on any one vertex of the dual program’s feasible set being optimal, every other vertex is optimal with either probability 0 or 1. In the finite sample normal model it thus suffices to condition on the event that a vector γ˚ P Vˆ. Our conditions for asymptotic validity of the conditional test below, however, ensure that the optimal vertex will be unique w.p.a. 1.
- 15The cutoffs vlo and vup are the maximum and minimum of the set tx : x “ maxγPF


###### γ1ps ` Σ˜

nγ˚

γ˚1 Σ˜nγ˚xqu

n

when γ˚1 Σ˜nγ˚ ‰ 0, where Fn is the feasible set of the dual program (15). When γ˚1 Σ˜nγ˚ “ 0, we define vlo “ ´8 and vup “ 8, so the conditional test rejects if and only if ηˆ ą 0.

16As noted in ARP, the truncation at 0 is not necessary for the conditional test to control size in the finite sample normal model, but it simplifies asymptotic arguments. It also prevents the test from rejecting when

by ψαCpβˆn,A,d,θ,¯ Σnq an indicator for whether the conditional test rejects the null that θ “ θ¯ for ∆ “ tδ : Aδ ď du.

We can then form a confidence set for θ by test inversion, Cα,nC pβˆn,Σnq :“ tθ¯ : ψαCpβˆn,A,d,θ,¯ Σnq “

”ψαCpβˆn,A,d,l1τpost,Σnqı ď

- 0u. The construction of the conditional test implies that Eβˆ


n„Npδ`τ, Σnq

α for any δ P ∆. It therefore follows that Cα,nC pβˆn,Σnq satisfies the finite-sample coverage requirement (10). In Section 3.3 below, we show that coverage in the normal model translates to uniform asymptotic coverage over a large class of DGPs.

- Example 4. An instructive example is when T¯ “ 1 (so that there are no nuisance parame-


ters), and Σ˜n “ I. Then ηˆ “ maxj Y˜n,j is the maximum component of Y˜n, vlo “ maxj‰ˆj Y˜n,j is the second-largest element of Y˜n (where ˆj denotes the index of the max), and vup “ 8. Thus, the conditional test rejects when ηˆ exceeds the 1 ´ α quantile of the standard normal distribution truncated to rvlo,8q. Intuitively, this means that the conditional test will tend to reject when the maximum sample moment is far enough away from the second-largest sample moment. Two special cases are worth special consideration. First, consider the case where in population one moment is violated and the remaining moments are very slack, e.g. µ˜1 ą 0 while µ˜j ! 0 for j ‰ 1. Then with high probability ηˆ will equal Y˜n,1 and vlo will be very negative. Thus, the conditional test will behave similarly to a one-sided t-test using Y˜n,1, which can be shown to be the most powerful test in the finite-sample normal model in this example. On the other hand, if µ1 « µ2 ą 0, then the maximum and second-largest sample moments (i.e. ηˆ and vlo) will be close together with high probability, so the conditional test may not reject with substantial probability even if both µ1 and µ2 are large, and thus the conditional test may have poor power. To improve power in these settings where the binding and non-binding moments are close together (relative to sampling variation), ARP introduce a “hybrid” test, which we describe next.

Hybrid confidence sets. ARP propose a “hybrid” test that combines the conditioning approach above with a test based on the “least-favorable” assumption that µ˜pθ¯q “ 0. In particular, ARP show that the distribution of ηˆ under the null is bounded above (in the sense of first-order stochastic dominance) by the distribution of ηˆ when µ˜pθ¯q “ 0 (see Section 3.2 of ARP). One can therefore construct a size-κ least-favorable (LF) test in the finite-sample normal model that rejects whenever ηˆ exceeds the 1 ´ κ quantile of maxγPVpΣq γ1ξ, where ξ „ N ´0, Σ˜n¯. This critical value, which we will denote by cLF,κ can easily be calculated by simulation. For 0 ă κ ă α, the ARP conditional-LF hybrid test is defined to reject if a first-stage, size-κ LF test rejects. If this first-stage test does not reject, then in the second

all moments are satisfied in sample.

`α1´´κκ˘

conditional test that also conditions on the event that the first-stage LF test did not reject. In particular, by similar logic as for the conditional test, we have that

stage the hybrid test conducts a modified version of the size-

ηˆ|tγ˚ P Vˆn,Sn “ s,ηˆ ď cLF,κu „ ξ |ξ P rvlo,vHups,

where vHup “ mintvlo,cLF,κu (see Section 3.4 of ARP). The second-stage of the hybrid test rejects if ηˆ exceeds the critical value for the size-

`α1´´κκ˘

conditional test that uses vHup instead of vup. We will denote by ψκ,αC-LFpβˆn,A,d,θ,¯ Σnq an indicator for whether the hybrid test rejects

- at a particular value θ¯, and denote by Cκ,α,nC-LFpβˆn,Σnq the confidence set that collects the values of θ¯ for which the hybrid test does not reject. As with the conditional test, by construction the hybrid confidence set satisfies that coverage criterion (10) in the finite-sample normal model. In our implementation below, we use κ “ α{10, following ARP.


#### 3.3 Uniform asymptotic size control

We now provide conditions under which size control in the finite sample normal model translates to uniform asymptotic size control over a large class of data-generating processes P under which βˆn is asymptotically normally distributed and Σn is replaced with a consistent estimator Σˆn. In particular, we provide sufficient conditions on βˆn,Σˆn, and ∆ such that the higher-level conditions for size control in ARP are satisfied (Proposition 2 in ARP).

Throughout this section, we fix ∆ “ tAδ ď du for some A with all non-zero rows, and assume that ∆ is non-empty. We consider a class of data-generating processes, indexed by P P P, under which ?npβˆn ´ βPq is asymptotically normal, where βP satisfies the causal decomposition in (3), i.e. βP “ δP ` LpostτP,post for δP P ∆ and τP,post P R¯T. The parameter of interest is θP :“ l1τP,post, for some fixed l ‰ 0. Our first assumption imposes uniform asymptotic normality of βˆn.

- Assumption 2. Let BL1 denote the set of Lipschitz functions which are bounded by 1 in absolute value and have Lipschitz constant bounded by 1. We assume


?npβˆn ´ βPqqı ´ ErfpξPqsˇ “ 0,

ˇEP ”fp

lim

sup

sup

nÑ8

PPP

fPBL1

where ξP „ N p0, ΣPq, and βP “ δP ` LpostτP,post for δP P ∆ and τP,post P RT¯.

Convergence in distribution is equivalent to convergence in bounded Lipschitz metric (see Theorem 1.12.4 in van der Vaart and Wellner (1996)), so Assumption 2 formalizes the notion of uniform convergence in distribution of ?npβˆn ´ βPq to a N p0, ΣPq variable under P.

Our next two assumptions require that the eigenvalues of the asymptotic variance of βˆn be bounded above and away from zero, and that there exists a uniformly consistent estimator for the variance of βˆn.

- Assumption 3. Let S denote the set of matrices with eigenvalues bounded below by ¯

λ ą 0 and above by λ¯ ě ¯

λ. For all P P P, ΣP P S.

- Assumption 4. We have an estimator Σˆn that is uniformly consistent for ΣP,

lim

nÑ8

sup

PPP

PP ´||Σˆn ´ ΣP|| ą ¯ “ 0,

for all ą 0. Finally, we impose some regularity conditions on the matrix A.

- Assumption 5. At least one of the following holds.


- (A) For k1 ` k2 “ dimpδq, the matrix A can be written as TQ, where Q has full row-rank

and T “

¨ ˚ ˝

Ik

1

0 ´Ik

1

0 0 Ik

2

˛ ‹ ‚. (We allow for the case where one of k1 or k2 is 0, in which

case the zero-dimensional blocks can be ignored).

- (B) Let γ¯1,...,γ¯K be the elements of V pIq. Then for all k, either γ¯k1 A “ 0 or infaě0 infj‰k ||pγ¯k´ aγ¯jq1A|| ą 0.


Part (A) of Assumption 5 imposes that the only source of degeneracy in the rows of A is matching inequalities of opposite signs. This is the case for many restrictions of interest, such as ∆SDpMq and the polyhedra that form ∆RMpM¯ q. Part (B) provides an alternative, higher-level condition that ensures that for distinct vertices γ¯k,γ¯j, the random variables γ¯j1Y˜ and γ¯k1 Y˜ are not perfectly positively correlated with each other. Assumption 5 is used to guarantee that degeneracy in the asymptotic distribution of γ1Y˜ arises only from known degeneracies in A. We note, however, that Assumption 5 does not rule out settings where the solutions to the bounds of the identified set given in equation (5) and (6) are non-unique or degenerate (i.e., where the extreme points for θ occur at “flat faces” of the identified set). If A is full-rank, for example, then Assumption 5(A) holds trivially with T “ I, and thus the mean of the moments µ˜pθ¯q is completely unrestricted.17

17Some values of A satisfying Assumption 5 may imply that certain pairs of moments cannot simultaneously be binding. For example, the restriction that |δ1| ď 1 can be represented as δ1 ď 1 and ´δ1 ď 1, which satisfies Assumption 5(A), but clearly both moments cannot simultaneously bind. Nevertheless Assumption 5(A) is compatible with “flat faces” even when A is not full rank. For example, if ∆ corresponds with the restrictions |δ1| ď 1 and |δ2| ď 1, then the extreme points for θ “ τ2 occur at flat faces of the identified set for pτ1,τ2q.

The assumptions stated above are sufficient for the conditions in Proposition 2 in ARP, which establishes uniform size control for the conditional and hybrid tests.

- Proposition 3.1. Suppose Assumptions 2 to 5 hold. Then the conditional and LF-hybrid tests uniformly control size. That is, for any α ă 0.5,


EP „ψαCpβˆn,A,d,θP,

Σˆnq ď α.

1 n

limsup

sup

nÑ8

PPP

EP „ψκ,αC-LFpβˆn,A,d,θP,

Σˆnq ď α.

1 n

limsup

sup

nÑ8

PPP

#### 3.4 Uniform asymptotic consistency

We next provide conditions under which the conditional and hybrid tests are uniformly asymptotically consistent, in the sense that power against fixed alternatives outside the identified set converges uniformly to 1. To establish uniform consistency of the conditional and hybrid tests, we strengthen Assumptions 2 and 3 as follows.

- Assumption 6. Let Wn “ ppβˆn ´ βPq1,pvecpΣˆnq ´ vecpΣPqq1q1, where vecpΣq is the vector of the elements of the matrix Σ. We assume

lim

nÑ8

sup

PPP

sup

fPBL1

ˇˇEP

“

fp

?nWnq‰ ´ E

“

fpξP`q‰

ˇˇ “ 0,

where ξP` „ N p0, VPq, VP “

˜ ΣP VP,βΣ

VP,Σβ VP,Σ

¸.

- Assumption 7. For all P P P, ΣP P S and the matrix VP defined in Assumption 6 lies in a


compact set V. Additionally, pΣP ´VP,βΣVP,:ΣVP,Σβq has eigenvalues bounded below by λ˜ ą 0, where : denotes the Moore-Penrose inverse.

Assumption 6 strengthens Assumption 2 to require that βˆn and Σˆn have a joint normal asymptotic distribution. Although somewhat more restrictive, event-study estimates are often estimated via OLS, and standard covariance estimators for OLS, including cluster-robust variance estimators, produce asymptotically normal estimates as the number of clusters grows large (Hansen, 2007; Stock and Watson, 2008; Hansen and Lee, 2019). We do not impose that the asymptotic distributions of βˆn and Σˆn are independent, as would occur in linear models if the linear model is properly specified. Assumption 7 strengthens Assumption 3 to require that the asymptotic distribution of βˆn is not perfectly asymptotically colinear with Σˆn.

Under the imposed assumptions, we obtain uniform consistency of the conditional and hybrid tests.

- Proposition 3.2. Suppose Assumptions 4 to 7 hold. Then for any x ą 0 and α ă 0.5,

lim

nÑ8

inf

PPP

EP „ψαCpβˆn,A,d,θPub ` x,

1 n

Σˆnq “ 1

lim

nÑ8

inf

PPP

EP „ψκ,αC-LFpβˆn,A,d,θPub ` x,

1 n

Σˆnq “ 1,

where θPub “ supSpβP,∆q is the upper bound of the identified set. The analogous result holds replacing θPub ` x with θPlb ´ x for θPlb “ inf SpβP,∆q.

- 3.5 Optimal local asymptotic power


We next provide conditions under which the conditional test has optimal local asymptotic power. We first state the conditions and our formal results, and then provide several examples highlighting when the assumptions will and will not hold.

###### 3.5.1 Main results

We begin by defining the linear independence constraint qualification (LICQ). Recall that the upper bound of the identified set is given by

l1δpost, s.t. Aδ ď d,δpre “ βpre¯. Since δpost “ βpost ´ τpost, we can re-write the upper bound as a maximization over τpost, θubpβ,∆q “ max

θubpβ,∆q “ l1βpost ´ ´min

δ

l1τpost, s.t. ´ Ap¨,postqτpost ď d ´ Aβ, (16)

τpost

where Ap¨,postq contains the columns of A corresponding with δpost. Let τpost˚ denote a solution to the optimization for θubpβ,∆q in (16), and let B˚ denote the indices of the binding

constraints, so that ´ApB˚,postqτpost˚ “ dB˚´ApB˚,¨qβ and ´Ap´B˚,postqτpost˚ ă d´B˚´Ap´B˚,¨qβ.

- Definition 2 (LICQ). We say that the linear independence constraint qualification (LICQ)


holds in direction l if there exists a solution τpost˚ to (16) such that the gradient of the binding constraints with respect to τpost, ´ApB˚,postq, has full row rank.18 We define LICQ in the direction ´l analogously for the optimization that replaces max with min in (16).

18The definition of LICQ in Kaido et al. (2021) would require that this condition holds for all solutions τpost˚ . For our results, however, it is sufficient for the condition to hold for some solution τpost˚ .

For ą 0, we define P to be the set of distributions P P P such that LICQ holds in the direction l and the non-binding constraints are slack by at least , i.e. ´Ap´B˚,postqτpost˚ ă d ´ AβP ´ .

Our next result states that for P P P , the local power of the conditional test converges to the power envelope for tests that control size in the finite sample normal model. To state this result formally, we define Iαp∆,Σnq to be the collection of confidence sets that control size in the finite sample normal model, i.e. confidence sets satisfying (10).

Proposition 3.3. Suppose Assumptions 2 to 4 hold. Let θPub “ supSpβP,∆q. Then for any

ą 0, x ą 0, and α ă 0.5,

Σˆnq ´ ρ˚αpP,xqˇ “ 0, where

sup PPP ˇEP „ψαCpβˆn,A,d,θPub `

1 n

1 ?n

x,

lim

nÑ8

xq R Cα,n˙

ˆpθPub `

1 ?n

ρ˚αpP,xq “ lim

Pβˆ

sup

n„NpβP ,n1 ΣP q

nÑ8

Cα,nPIαp∆,n1 ΣP q

is the optimal local asymptotic power of a size-α test in the finite sample normal model. An analogous result holds for the lower bound under the class of distributions where LICQ holds in direction ´l.

Since the LF-hybrid test rejects whenever the conditional test with size α1´´κκ rejects, it is immediate that the local asymptotic power of the LF-hybrid test is at least as good as the power of the optimal size-

`α1´´κκ˘

test.

Corollary 3.1. Under the conditions of Proposition 3.3,

liminf

inf

nÑ8

PPP

ˆEP „ψκ,αC-LFpβˆn,A,d,θPub `

1 ?n

Σˆnq ´ ρ˚α´κ

pP,xq˙ ě 0.

1 n

x,

1´κ

We emphasize that Proposition 3.3 and Corollary 3.1 are new, and exploit structure in our context not contained in the more general setting considered in ARP.

###### 3.5.2 Discussion and Examples

As discussed in Kaido et al. (2021), LICQ and related constraint qualifications have been used frequently in the partial identification literature. Intuitively, LICQ ensures that the bounds of the identified set are differentiable with respect to the means of the moments pµ˜pθ¯qq, and thus avoids challenges related to estimation and inference on non-differentiable parameters (Hirano and Porter, 2012). Uniform LICQ conditions have been invoked recently

by Gafarov (2019) and Cho and Russell (2019), and a related Slater constraint qualification is used in Kaido and Santos (2014). One important distinction between our results and previous results using LICQ is that we do not require LICQ for our size control results (Proposition 3.1). Thus, our tests control size even when LICQ fails (and so the bounds may be non-differentiable), but Proposition 3.3 shows that this does not come at the cost of power asymptotically when indeed LICQ holds.19

- Figure 1: Diagram illustrating when LICQ (Assumption 2) will and will not hold in the case where T¯ “ 2.


τ2

τ2

τ2

´Ap1,postqτpost “ d1 ´ Ap1,¨qβ

´Ap1,postqτpost “ d1 ´ Ap1,¨qβ

´Ap1,postqτpost “ d1 ´ Ap1,¨qβ

τpost˚

τpost˚

- ´Ap2,postqτpost “ d2 ´ Ap2,¨qβ
- ´Ap3,postqτpost “ d3 ´ Ap3,¨qβ


- ´Ap2,postqτpost “ d2 ´ Ap2,¨qβ
- ´Ap3,postqτpost “ d3 ´ Ap3,¨qβ


###### l

l

l

´Ap2,postqτpost “ d2 ´ Ap2,¨qβ

τ1

τ1

τ1

(a)

(c)

(b)

Note: In each panel, we assume that the rows associated with binding moments are ordered first in the matrix A for ease of notation. The blue shading denotes the identified set for pτ1,τ2q and the dashed red arrow points in the direction l “ p21, 12q1. In panel (a), LICQ is satisfied since there is a unique τpost˚ (colored in red) at which two linearly independent moments are binding. In panel (b), even though τpost˚ is not unique, LICQ is satisfied as there is either one or two linearly independent binding moments at the values of τpost˚ colored in red. In panel (c), there are three binding moments at τpost˚ (colored in red), and so LICQ is violated.

###### Figure 1 provides geometric intuition for when LICQ will and will not hold in the case where T¯ “ 2 and the target parameter is the average of the post-treatment effects, θ “

- 1

- 2pτ1 ` τ2q. In panel (a), there is a unique τpost˚ (colored in red) at which two linearly independent moments bind, so LICQ is satisfied. LICQ is likewise satisfied in panel (b), where the optimal τpost˚ is not unique (a so-called “flat-face” problem). This is because at the indicated values τpost˚ (colored in red), there is either one or two linearly independent binding moments. A failure of LICQ is shown in panel (c). In this example, there are three binding


###### moments at τpost˚ (colored in red), so the binding constraints cannot be linearly independent in R2. Such a situation may arise when there are both smoothness restrictions and sign or shape restrictions that are simultaneously binding at the boundary of the identified set.

19We view this result as loosely parallel to results in the weak identification literature showing that certain procedures control size under weak identification but are efficient under strong identification (e.g. Moreira, 2003).

In the three period DiD model (where there are no nuisance parameters, since T¯ “ 1), LICQ is satisfied when the bounds of the identified set are each determined by one moment. This holds everywhere for ∆SDpMq when M ą 0. It holds almost everywhere for ∆SDPBpMq when M ą 0, although it fails when both the sign restrictions and smoothness restrictions are simultaneously binding. (For LICQ to hold with non-binding moments slack by at least

, i.e. P P P , δP must not be local to a point at which LICQ fails.) When M “ 0, both the upper and lower bounds for ∆SDpMq and ∆SDPBpMq are binding, so LICQ fails.

More generally, the result in Proposition 3.3 is under the asymptotic regime where the sampling variation grows small relative to the length of the identified set, and thus the binding and non-binding moments are “far” apart relative to sampling variation. Importantly, it can be shown that the LICQ condition rules out settings where θ is point identified. Thus, the asymptotics considered in Proposition 3.3 may not provide a good approximation to the finite-sample performance of the conditional test in settings where θ is point-identified, or when the length of the identified set is “small” relative to sampling variation.

We are not aware of results analogous to Proposition 3.3 for any test that controls size in the finite-sample normal model. Kaido and Santos (2014) provide an efficiency result under a related Slater constraint qualification condition, but their test does not control size when the constraint qualification fails. It is worth highlighting that if LICQ holds for a particular set of moments, then it also holds if one adds moments that are slack at the optimal τpost˚ .

- Proposition 3.3 thus requires that the asymptotic power of the test is not affected by the inclusion of slack moments. The only other tests that we are aware of that control size in the finite-sample normal model and have this form of insensitivity to slack moments are the tests proposed by Cox and Shi (2022). An interesting open question is whether the tests proposed by Cox and Shi (2022) also converge to the power envelope under LICQ.20


###### 3.5.3 Extensions

- Proposition 3.3 is stated for the case when ∆ is a single polyhedron. An immediate corollary,


however, is that when ∆ “ ŤK

k“1 ∆k, the conditional test based on the union of confidence sets has optimal local asymptotic power when the ∆k that determines the identified set bounds is unique and satisfies the conditions of Proposition 3.3. This implies, for example, that when ∆ “ ∆RMpM¯ q, the power of the conditional test converges to the power envelope when there is a unique (non-zero) pre-treatment maximum violation, i.e. when maxsă0 |δs`1 ´ δs| ą 0 and has a unique solution.21 Likewise, the conditional test has opti-

- 20Extending the results to the Cox and Shi tests is non-trivial given that they use a different test statistic and form critical values in a different way.
- 21For this convergence to hold uniformly, the non-binding moments must be slack by , so we would need that maxsă0 |δs`1 ´ δs| is at least greater than the second largest difference.


mal local asymptotic power for ∆SDRMpM¯ q when there is a unique maximum non-linearity in the pre-treatment period. Intuitively, this is because the upper bound of the identified set is determined by a single ∆k˚ satisfying LICQ, so the conditional test for this ∆k˚ has optimal local asymptotic power, whereas our consistency results imply that the tests for the remaining ∆k that do not determine the identified set bound reject with probability approaching 1. See Corollary 4.1 in the working paper version of this paper for a formal derivation (Rambachan and Roth, 2021).

Proposition 3.3 shows that under LICQ the local asymptotic power of the conditional test converges to the power envelope for tests controlling size in the finite-sample normal model. In the working paper version of this paper, we showed that the power envelope from the finite-sample normal model corresponds with the power-envelope among tests that control size asymptotically and have certain invariance properties using results in Müller (2011) (Proposition E.4 in Rambachan and Roth (2021)).

## 4 Inference using Fixed Length Confidence Intervals

We next consider fixed length confidence intervals (FLCIs) based on affine estimators. While the conditional and hybrid confidence sets offer attractive asymptotic power guarantees under asymptotics in which sampling variation grows small relative to the length of the identified set, FLCIs offer finite-sample power guarantees (in the normal model) for certain classes ∆ of interest. In certain special cases, FLCIs may thus outperform the ARP tests when sampling variation is large relative to the length of the identified set. For brevity of exposition, we focus on the properties of FLCIs in the case where the finite-sample normal approximation (9) holds exactly with Σn known; Armstrong and Kolesár (2020b) provide uniform asymptotic results for FLCIs under conditions similar to those in Section 3.3.

- 4.1 Constructing FLCIs Following Donoho (1994) and Armstrong and Kolesár (2018, 2020a), we consider fixed


´lengtha ` v1βconfidenceˆn¯ ˘ χ, whereintervalsa andbasedχ areonscalarsan affineandestimatorv P R¯T`T¯for. Weθ, minimizedenoted bytheCα,nhalf-lengthpa,v,χq :of“ the confidence interval, χ, subject to the constraint that Cα,npa,v,χq satisfies the coverage requirement (10) in the finite-sample normal model.

Observe that if βˆn „ N pβ, Σnq, then a ` v1βˆn „ N pa ` v1β, v1Σnvq, and hence |a ` v1βˆn ´θ| „ |N pb, v1Σnvq|, where b “ a`v1β ´θ is the affine estimator’s bias for θ. Observe further that θ P Cα,npa,v,χq if and only if |a ` v1βˆn ´ θ| ď χ. For fixed values a and v, the

˘| distribution, where ¯b is the affine estimator’s worst-case bias

smallest value of χ that satisfies (10) is therefore the 1 ´ α quantile of the |N `

¯b, v1Σnv

|a ` v1 pδ ` Lpostτpostq ´ l1τpost|. (17)

¯bpa,vq :“ sup

δP∆,τpostPRT¯

Let cvαptq denote the 1 ´ α quantile of the folded normal distribution |N pt, 1q|.22 For fixed a and v, the smallest value of χ satisfying the coverage requirement (10) is thus

χnpa,v;αq “ σv,n ¨ cvαp¯bpa,vq{σv,nq, (18)

?v1Σnv. The optimal (i.e., minimum-length) FLCI is constructed by choosing the values of a and v to minimize (18). When ∆ is convex, this minimization can be solved as a nested optimization problem, where both the inner and outer minimizations are convex (Low, 1995; Armstrong and Kolesár, 2018, 2020a). We denote the 1´α level, optimal FLCI by Cα,nFLCIpβˆn,Σnq :“ ´an ` vn1 βˆn¯ ˘ χn, where χn :“ infa,v χnpa,v;αq and an, vn are the optimal values in the minimization.

where σv,n :“

Example: ∆SDpMq. Suppose θ “ τ1. For ∆SDpMq, the affine estimator used by the optimal FLCI takes the form a`v1βˆn “ βˆn,1´ř0

T`1 ws ´βˆn,s ´ βˆn,s´1¯, where the weights ws sum to one (but may be negative). This estimator adjusts the event-study coefficient for t “ 1 by an estimate of the differential trend between t “ 0 and t “ 1 formed by taking a weighted average of the differential trends in periods prior to treatment. The worst-case bias will be smaller if more weight is placed on pre-treatment periods closer to the treatment date, but it may reduce variance to place more weight on earlier pre-periods. The weights ws are optimally chosen to balance this tradeoff.

s“´¯

#### 4.2 Finite-sample near optimality

In particular cases of interest, such as when ∆ “ ∆SDpMq, the optimal FLCIs introduced above have near-optimal expected length in the finite-sample normal model. The following result, which is an immediate consequence of results in Armstrong and Kolesár (2018, 2020a), bounds the ratio of the expected length of the shortest possible confidence interval that controls size relative to the length of the optimal FLCI.

- Assumption 8. Assume i) ∆ is convex and centrosymmetric (i.e. δ˜ P ∆ implies ´δ˜ P ∆), and ii) δ P ∆ is such that pδ˜´ δq P ∆ for all δ˜ P ∆.


22If t “ 8, we define cvα “ 8.

- Proposition 4.1. Suppose δ and ∆ satisfy Assumption 8. Let Iαp∆,Σnq denote the class of confidence sets that satisfy the coverage criterion (10) at the 1 ´ α level. Then, for any τ with τpre “ 0 and Σn positive definite,


α,nPIαp∆,Σnq Eβˆ

n„Npδ`τ,Σnq rλpCα,nqs 2χn ě

infC

z1´αp1 ´ αq ´ z˜αΦpz˜αq ` φpz1´αq ´ φpz˜αq z1´α{2

,

where λp¨q denotes the length (Lebesgue measure) of a set and z˜α “ z1´α ´ z1´α{2.

Part i) of Assumption 8 is satisfied for ∆SDpMq but not for our other ongoing examples. For example, ∆SDPBpMq is convex but not centrosymmetric, and ∆RMpM¯ q is neither convex nor centrosymmetric. Part ii) of Assumption 8 is satisfied whenever parallel trends holds in both the pre-treatment and post-treatment periods pδ “ 0q and whenever δ is a linear trend for the case of ∆SDpMq.

FLCIs thus offer attractive guarantees for the case of ∆SDpMq. When α “ 0.05, the lower bound in Proposition 4.1 evaluates to 0.72, meaning that the expected length of the shortest possible confidence set that satisfies the coverage requirement (10) is at most 28% shorter than the length of the optimal FLCI when the conditions of the proposition hold.

#### 4.3 (In)Consistency of FLCIs

As discussed above, these finite-sample guarantees do not apply for several types of restrictions ∆ of importance, including those that construct bounds using the maximum pretreatment violation or incorporate sign and shape restrictions. We now show that the FLCIs can perform poorly under such restrictions. We first provide two illustrative examples, and then state a formal inconsistency result.

Example: ∆SDPBpMq and ∆SDIpMq. Suppose θ “ τ1. It can be shown that the worstcase bias of an affine estimator over ∆SDPBpMq or ∆SDIpMq is the same as the worst-case bias for that estimator over ∆SDpMq.23 Since the construction of the optimal FLCI depends only on the worst-case bias and variance of the affine estimator, it follows that the optimal FLCI constructed using ∆SDPBpMq or ∆SDIpMq is the same as the one constructed using ∆SDpMq. Therefore, the optimal FLCI does not adapt to additional sign or monotonicity restrictions.

23Suppose the vector δ¯ maximizes the bias for an affine estimator pa,vq over ∆SDpMq. The vector that adds a constant slope to δ¯, say δ˜c “ δ¯` c ¨ p´¯

T,...,T¯q1, also lies in ∆SDpMq, and for c sufficiently large, δ˜c will lie in ∆SDPBpMq. Moreover, the worse-case bias will be the same for δ and δ˜c, since if pa,vq has finite worst-case bias it must subtract out a weighted average of the pre-treatment slopes.

Example: ∆RMpM¯ q. Suppose θ “ τ1. If ∆ “ ∆RMpM¯ q and M¯ ą 0, then all affine estimators for τ1 have infinite worst-case bias, since δ P ∆RMpM¯ q can have |δ1| arbitrarily large if |δ´1| is also sufficiently large. Thus, the only valid FLCI is the entire real line.

We next provide a formal result on the (in)consistency of the FLCIs. Specifically, we will show that even as the sampling variation Σn converges to 0, the optimal FLCI will include fixed points outside of the identified set with positive probability unless certain special conditions are met.24 Recall from Lemma 2.1 that the identified set Spβ,∆q is an interval when ∆ is convex, with length equal to θubpβ,∆q´θlbpβ,∆q “ bmaxpβpre,∆q´bminpβpre,∆q. Since the length of the identified set only depends on βpre and ∆, denote it by LIDpβpre,∆q. Our next result shows that Cα,nFLCIpβˆn,Σnq is consistent if and only if LIDpβpre,∆q is its maximum possible value, provided that the identified set is not the entire real line (in which case any procedure is trivially consistent).

- Assumption 9 (Identified set maximal length and finite). Suppose δ P ∆ is such that


preP∆pre LIDpδ˜pre,∆q ă 8, where ∆pre “ tδpre P R¯T : Dδpost s.t. pδpre1 ,δpost1 q1 P ∆u is the set of possible values for δpre.

LIDpδpre,∆q “ supδ˜

- Proposition 4.2. Suppose ∆ is convex and α ă 0.5. Fix δ P ∆ and τ with τpre “ 0, and suppose Spδ ` τ,∆q ‰ R. Then pδ,∆q satisfy Assumption 9 if and only if Cα,nFLCIpβˆn,Σnq is consistent, meaning that for Σn “ Σ˚{n,


´θout P Cα,nFLCIpβˆn,Σnq¯ “ 0 for all θout R Spδ ` τ,∆q.

Pβˆ

lim

n„Npδ`τ, Σnq

nÑ8

Thus, if Assumption 9 fails, then Cα,nFLCIpβˆn,Σnq is inconsistent in the strong sense that it includes fixed points outside of the identified set with non-vanishing probability. It follows that there will be some δ P ∆ such that the FLCI is inconsistent under δ unless the identified set is always the same length. Proposition 4.2 is new, and may be relevant for other settings in which FLCIs are used.

The intuition for the possible inconsistency of FLCIs is as follows: to ensure that an FLCI satisfies the coverage requirement (10), its length must be at least supδ˜

preP∆pre LIDpδ˜pre,∆q. However, this implies that if in fact LIDpδpre,∆q ă supδ˜

preP∆pre LIDpδ˜pre,∆q, then the FLCI is strictly longer than the length of the identified set, regardless of the value of Σn, and thus some points outside of the identified set must be covered with non-vanishing probability. This reflects the fact that FLCIs are by construction fixed length, and thus their length does not adapt to information in the data about the length of the identified set. By contrast, the

24For ease of exposition, we present a result using “small-Σ” asymptotics in the normal model, as in e.g., Kadane (1971) and Moreira and Ridder (2019).

length of the conditional/hybrid confidence sets can depend on βˆpre and thus “adapts” to the length of the identified set.

In the three-period difference-in-differences example, Assumption 9 holds everywhere for ∆SDpMq (since the identified set is always the same length, 2M), for values of δ where the sign restrictions do not bind for ∆SDPBpMq, and nowhere for the polyhedra that form ∆RMpM¯ q. The restrictiveness of Assumption 9 thus depends greatly on ∆.

The results in this section establish that when certain conditions on ∆ are satisfied, optimal FLCIs are consistent and have desirable finite-sample guarantees in terms of expected length. FLCIs are thus attractive for our baseline smoothness class ∆SDpMq, since they are guaranteed to be consistent and offer attractive finite-sample guarantees. Our inconsistency result shows, however, that FLCIs may perform poorly for other choices of ∆ that may be of interest in empirical applications, such as those that construct bounds using a pre-treatment maximum or incorporate sign and monotonicity restrictions.

## 5 Simulation study

In this section, we conduct a simulation study to investigate the performance of the discussed confidence sets across a range of relevant data-generating processes. We find good size control for all of the procedures, and therefore focus in the main text on a comparison of power to provide concrete recommendations on the best approach in practice. In the supplementary material, we present results on size control and other additional simulation results.

#### 5.1 Simulation Design

Our simulations are calibrated using the estimated covariance matrix from the 12 recentlypublished papers surveyed in Roth (Forthcoming). For any given paper in the survey, we denote by Σˆ the estimated variance-covariance matrix from the event-study in the paper, calculated using the clustering scheme specified by the authors. For a chosen mean vector β, we simulate event-study coefficients βˆs from a normal model, βˆs „ N ´β, Σˆ¯.25 In simulation

- s, we construct nominal 95% confidence sets for the parameter of interest θ using the pair pβˆs,Σˆq for each proposed procedure. The parameter of interest is the causal effect in the first post-treatment period (θ “ τ1); in the supplementary material, we present simulation results in which the parameter of interest is the average causal effect in the post-treatment periods (θ “ τ¯post), with qualitatively similar results.


25We focus on the normal simulations in the main text since it allows for a tractable computation of the optimal excess length of procedures that control size. In the supplementary material, we show that our procedures perform similarly in simulations based on the empirical distribution in the original paper.

For a given choice of ∆, we compute the identified set Spβ,∆q and calculate the expected excess length for each of the proposed confidence sets. We benchmark the expected excess length of our proposed confidence sets relative to an efficiency bound for confidence sets that satisfy the uniform coverage requirement.26 We report the efficiency ratio of each procedure, which is defined as the ratio of the optimal benchmark relative to the average excess length for the procedure. All results are calculated over 1000 simulations per paper.

| |Parallel Trends Pulse Pre-Trend ∆SDpMq ∆SDPBpMq ∆SDRMpM¯ q ∆RMpM¯ q|
|---|---|
|Conditional and Hybrid Consistent Asymptotically (near-)optimal FLCI Consistent Finite-sample near-optimal<br><br>|ˆ<br><br>ˆ ˆ ˆ ˆ ˆ ˆ|


Table 1: Summary of expected properties for each simulation design

We consider four choices of ∆ to highlight the performance of our proposed confidence sets across a range of conditions: ∆SDpMq, ∆SDPBpMq, ∆RMpM¯ q, and ∆SDRMpM¯ q. We consider simulations under the assumption of zero treatment effects, so that τ “ 0 and thus β “ δ. We consider two forms for δ. First, we consider the baseline case of parallel trends (δ “ 0). Second, we consider a “pulse” pre-trend in which δ´1 is non-zero and the remaining elements of δ are zero. Such a pre-trend might arise in practice if there are confounding policy changes or other events close to the time of treatment. These different choices of δ allow us to highlight the relative strengths of the proposed inference procedures. For example, FLCIs have near-optimal expected length when δ “ 0 and ∆ “ ∆SDpMq, whereas the conditional test has optimal local asymptotic power under the pulse design when ∆ “ ∆SDPBpMq. Table 1 summarizes which of our theoretical results hold for each of the simulation designs when M and M¯ are non-zero.

In practice, we find that for ∆SDpMq and ∆SDPBpMq, the results depend on M but are qualitatively similar across values of δ. By contrast, for ∆SDRMpM¯ q and ∆RMpM¯ q, the choice of δ is more important than the choice of M¯ . Therefore, to highlight the most important

26For choices of ∆ that are convex (e.g., ∆SDpMq and ∆SDPBpMq), we benchmark the expected excess length of our proposed confidence sets against a sharp optimal bound over confidence sets that satisfy the finite-sample coverage requirement (10). This optimal bound is provided in the supplementary materials, and follows as a corollary from results in Armstrong and Kolesár (2018) on the optimal expected length of

- a confidence set satisfying the uniform coverage requirement (10). For choices of ∆ that can be written as the union of convex sets (e.g., ∆RMpM¯ q and ∆SDRMpM¯ q), we compare the expected excess length of our proposed confidence sets against the maximal optimal bound over each set in the union, which is a potentially non-sharp bound for any confidence set with correct coverage.


dimensions for each of the simulation designs, in the main text of the paper we report results for ∆SDpMq and ∆SDPBpMq under different values of M and δ “ 0 (parallel trends), whereas for ∆RMpM¯ q and ∆SDRMpM¯ q we vary the magnitude of the pre-treatment pulse δ´1, holding M¯ “ 1 constant. In the supplementary materials, we report results for additional choices of these parameters.

We report results for three methods for constructing confidence sets: FLCIs, conditional confidence sets, and conditional-least favorable hybrid confidence sets.27 For ∆RMpM¯ q and ∆SDRMpM¯ q, we omit results for the FLCI since the FLCIs have infinite length.

#### 5.2 Simulation Results

To compare results easily across the 12 papers in the simulation study, we normalize the units of δ´1 and M by the standard deviation of βˆ1 (denoted σ1). Large normalized values of M or δ´1 correspond with the case where the identified set is large relative to sampling variation, mimicking our asymptotic power results in which sampling variation grows small relative to the identified set. In the graphs below, we report the median value of excess length efficiency across the papers in the survey. The normalization described above implies that the units of the x-axis correspond with the worst-case bias of the naive estimator βˆ1 divided by its standard error.28

Results for ∆SDpMq: The left panel of Figure 2 plots the efficiency ratio for each procedure as a function of M{σ1 when ∆ “ ∆SDpMq. All procedures perform well as M{σ1 grows large with efficiency ratios approaching 1, illustrating our asymptotic (near-)optimality results for this design. However, the FLCIs perform best for smaller values of M{σ1, including the point-identified case where M “ 0, illustrating the finite-sample near-optimality results for the FLCIs when Assumption 8 holds. Although the conditional and hybrid confidence sets have efficiency approaching the optimal bound for M{σ1 large, their efficiency is only about 50% when M{σ1 “ 0, in which case θ is point identified and thus LICQ does not hold. The conditional and hybrid confidence sets perform similarly.

Results for ∆SDPBpMq: The right panel of Figure 2 plots the efficiency ratio for each procedure as a function of M{σ1 when ∆ “ ∆SDPBpMq. The efficiency ratios for the conditional and hybrid confidence sets are again (near-)optimal as M{σ1 grows large, highlighting

- 27For the conditional-least favorable hybrid confidence sets, we use a first-stage least-favorable test of size

κ “ α{10, following ARP and Romano, Shaikh and Wolf (2014).

- 28For βˆ1 normally distributed, the worst-case coverage of a conventional 95% confidence interval as a


function of the normalized worst-case bias b is Φp1.96 ` bq ´ Φp´1.96 ` bq, which is 0.95 for b “ 0, 0.83 for

- b “ 1, 0.48 for b “ 2, etc.


###### Figure 2: Simulation results for ∆SDpMq and ∆SDPBpMq: Median efficiency ratios for proposed procedures.

![image 1](<hpt-draft_images/imageFile1.png>)

![image 2](<hpt-draft_images/imageFile2.png>)

Note: Median efficiency ratios for our proposed confidence sets over ∆SDpMq and ∆SDPBpMq under the assumption of parallel trends and zero treatment effects (i.e., β “ 0). The efficiency ratio for a procedure is defined as the efficiency bound divided by the procedure’s expected excess length. The results for the FLCI are plotted in purple, conditional-LF (“C-LF Hybrid”) hybrid in blue, and conditional confidence set in green. Results are averaged over 1000 simulations for each of the 12 papers surveyed, and the median across papers is reported here.

###### Figure 3: Simulation results for ∆SDRMpM¯ q and ∆RMpM¯ q: Median efficiency ratios for proposed procedures.

![image 3](<hpt-draft_images/imageFile3.png>)

![image 4](<hpt-draft_images/imageFile4.png>)

Note: Median efficiency ratios for our proposed confidence sets over ∆SDRMpM¯ q and ∆RMpM¯ q with M¯ “ 1 under the assumption of zero treatment effects and a “pulse” pre-trend (i.e., β´1 “ δ´1 and βt “ 0 for all

- t ‰ ´1). The efficiency ratio for a procedure is defined as the efficiency bound divided by the procedure’s expected excess length. The results for the conditional-least favorable (“C-LF”) hybrid are plotted in blue, and conditional confidence set in green. Results are averaged over 1000 simulations for each of the 12 papers surveyed, and the median across papers is reported here.


###### our asymptotic (near-)optimality results for these procedures in this simulation design. By contrast, the efficiency ratios for the FLCIs steadily decrease as M{σ1 increases, reflecting

that the FLCIs are not consistent in this simulation design when M ą 0. The conditional-LF hybrid confidence sets slightly improve efficiency relative to the conditional when M{σ1 is small and retain near-optimal performance as M{σ1 grows large.

Results for ∆SDRMpM¯ q: The left panel of Figure 3 plots the efficiency ratios for the conditional and conditional-least favorable hybrid confidence sets as a function of δ´1{σ1 when ∆ “ ∆SDRMpM¯ q. We omit results for the optimal FLCI since the optimal FLCI has infinite length for this design. Both procedures perform well as δ´1{σ1 grows large with efficiency ratios approaching 1, illustrating our asymptotic (near-) optimality result for this design. Both procedures also have similar power curves, with slightly higher power for the conditional.

Results for ∆RMpM¯ q: The right panel of Figure 3 plots the efficiency ratio for the conditional and conditional-least favorable hybrid confidence sets as a function of δ´1{σ1 when ∆ “ ∆RMpM¯ q. We again omit results for the optimal FLCI since the optimal FLCI has infinite length for this design. The conditions for our asymptotic (near-) optimality result for unions of convex sets do not hold in this simulation design (as the maximum pre-period violation is not unique). Nonetheless, we find that the conditional-least favorable hybrid confidence set and the conditional confidence set perform quite well for large values of δ´1{σ1, with efficiency ratios approaching about 83%. This is encouraging as it shows that these procedures may perform well even in cases where LICQ fails. Once again, we also find that the conditional and conditional-least favorable hybrid have similar power.

Takeaways from Simulations: Two clear patterns emerge from our simulations. First, the conditional and hybrid confidence sets perform well across a wide range of specifications, with particularly good power when the length of the identified set is large relative to sampling variation. Second, the FLCIs have the best performance for ∆SDpMq, particularly when M is small, which aligns with the finite-sample near-optimality results in Section 4. However, FLCIs can perform quite poorly for other classes of ∆.

Overall, we therefore recommend to use the conditional-LF hybrid confidence sets for generic forms of ∆, and optimal FLCIs for the special case of ∆SDpMq (or other special cases where the consistency/finite-sample near-optimality of FLCIs is guaranteed). Although the conditional and hybrid approaches perform similarly in our simulations, we recommend the hybrid approach in general based on the guidance provided in ARP. We implement these recommendations in our applications in the next section.

## 6 Practical Guidance and Empirical Illustrations

#### 6.1 Practical Guidance

We recommend that researchers use our methods to construct robust confidence intervals under restrictions on the possible violations of parallel trends ∆ that are motivated by domain knowledge in their empirical setting. We also suggest that researchers report sensitivity analyses to illustrate the sensitivity of their causal conclusions to alternative assumptions on the possible violations of parallel trends.

Choice of ∆. The choice of ∆ should be motivated by economic knowledge about the types of possible confounding factors that would produce non-parallel trends. We now provide some guidance on how the choice of ∆ can be motivated by domain knowledge, highlighting some cases where our leading examples, ∆RMpM¯ q and ∆SDpMq, would be sensible choices.

In some empirical settings, researchers may be concerned about differential economic shocks to the treated and control groups that generate violations of parallel trends. If the researcher believes that the magnitude of these differential shocks in the post-treatment period is not too different from the magnitude in the pre-treatment period, then it may be reasonable to assume δ P ∆RMpM¯ q, which explicitly bounds the relative magnitudes of violations of parallel trends in the post-treatment based on observed violations in the pretreatment period. In other settings, researchers may be worried about violations of parallel trends that arise due to differences in smoothly evolving secular trends that differentially affect treated and comparison groups. In this case, it may be reasonable to assume δ P ∆SDpMq, which explicitly bounds the extent to which the slope of the difference in trends can vary across consecutive periods. Economic knowledge may imply additional restrictions as well. For example, if the researcher knows of a confounding policy change that would have a positive effect on the outcome, then it is reasonable to further assume that post-treatment difference in trends must be positive (i.e., δt ě 0 for t ą 0).

In our empirical applications below, we illustrate how domain knowledge about the types of possible violations of parallel trends can inform the choice of ∆. We encourage applied researchers to use such domain knowledge to inform the restrictions they impose on the possible choices of parallel trends in their context.

Choice of inference procedure. Based on our theoretical results and Monte Carlo simulations, we recommend the ARP hybrid confidence sets for generic, polyhedral forms of ∆. For the special case of ∆SDpMq — or other choices of ∆ for which the consistency and finite-sample-near-optimality of FLCIs are guaranteed — we recommend FLCIs. Our

recommended choice of inference procedure is implemented in the R package, HonestDiD, that accompanies the paper.29 Furthermore, these confidence sets are quick to compute. Each sensitivity analysis plot in the empirical applications below took less than 9 minutes to compute on a 2012 Macbook Pro.

Sensitivity analyses. Once the researcher has chosen a baseline class of restrictions on the possible violations of trends (e.g. relative magnitudes bounds ∆RMpM¯ q or smoothness bounds ∆SDpMq), we recommend conducting sensitivity analysis over the associated parameter (M¯ ě 0 or M ě 0, respectively) that governs how different the post-treatment violations of parallel trends can be from the pre-trends. It is natural to report both the sensitivity of the researcher’s causal conclusion to the choice of this parameter and the “breakdown” parameter value at which particular hypotheses of interest can no longer be rejected; similar “breakdown” concepts appear in the partial identification settings of Horowitz and Manski (1995); Kline and Santos (2013); Manski and Pepper (2018); Masten and Poirier (2020).30 We illustrate how one can interpret the magnitudes of the breakdown points in our two empirical illustrations below.

#### 6.2 Estimating the incidence of a value-added tax cut

Benzarti and Carloni (2019, henceforth, BC) study the incidence of a decrease in the valueadded tax (VAT) on restaurants in France. France reduced its VAT on sit-down restaurants from 19.6 to 5.5 percent in July of 2009. BC analyze the impact of this change using a dynamic difference-in-differences design that compares restaurants to a control group of other market services firms that were not affected by the VAT change, estimating

Yit “ ÿ

βs ˆ 1rt “ ss ˆ Di ` φi ` λt ` it, (19)

s‰2008

where Yit is the log of (before-tax) profits for firm i in year t; Di is an indicator for whether firm i is a restaurant; φi and λt are firm and year fixed effects; and standard errors are

- 29The latest version of the R package can be downloaded by visiting http://github.com/ asheshrambachan/HonestDiD.
- 30Our main focus in this paper is on constructing robust confidence sets given a particular restriction ∆pMq, rather than inference on the identification breakdown point or breakdown frontier as in e.g. Masten and Poirier (2020). Note, however, that if we define M˚ “ minM s.t. 0 P Spβ,∆pMqq to be the identification breakdown point for a null effect, and Mˆ ˚ “ minM s.t. 0 P Cpβˆn,Σˆn;∆pMqq to be the sample breakdown point, then PpMˆ ˚ ě M˚q ě Pp0 P Cpβˆn,Σˆn;∆pM˚qq. It follows that p´8,Mˆ ˚s is a valid p1 ´ αq-level confidence interval for M˚ provided that our conditions for size control are satisfied for ∆pM˚q. We suspect that our results could be extended to allow for uniform coverage of the breakdown frontier under additional regularity conditions, but leave this to future work.


clustered at the regional level. BC’s main finding is that the VAT reduction had a large, positive effect on restaurant profits. Figure 4 shows the estimated event-study coefficients tβˆsu from specification (19). We can formally reject the hypothesis that βpre “ 0 (p ă 0.01), as there appears to have been a difference in trends between 2006 and 2007. Nevertheless, the changes in profits after the policy change appear to be larger in magnitude than any of the pre-trends.

- Figure 4: Event-study coefficients tβsu for log profits, estimated using the event-study specification in (19).


![image 5](<hpt-draft_images/imageFile5.png>)

A key concern in this empirical setting is that there may be unobserved, industry-specific or macroeconomic shocks that would have affected restaurants differently from other marketservices firms even in the absence of a change in VAT. It seems reasonable to impose that the industry-specific shocks to restaurants in the post-treatment period are not too much larger than those in the pre-treatment period — whereas imposing that industry-specific shocks follow a smooth trend seems unreasonable — and so we base our analysis on bounds on relative magnitudes ∆RMpM¯ q.

The left panel of Figure 5 shows robust confidence sets for the treatment effect in 2009 for ∆RMpM¯ q using different values of M¯ . The figure shows that if we impose M¯ “ 1, meaning that we restrict the post-treatment violations of parallel trends to be no larger than the maximal pre-treatment violation of parallel trends, then we obtain a robust confidence set of r0.07,0.31s for the causal effect on restaurant profits in 2009. This is wider than the original OLS confidence interval which is only valid if parallel trends holds exactly, but nevertheless rules out a null effect on restaurant profits in 2009. Looking further to the right, we see that the “breakdown value” for a null effect is around M¯ “ 2. Thus, our conclusion of a significant effect on restaurant profits depends on whether we are willing to restrict that

the post-treatment violations of parallel trends can be no more than twice as large as the maximal pre-treatment violation. Given that the first year after the treatment coincided with a large recession in France (2009), it may be plausible that the differential factors affecting restaurants were larger in that year than in the pre-treatment period. Our approach helps formalize how much larger they would need to be to reject the conclusion of a null effect (or other hypotheses).

Figure 5: Sensitivity analysis for Benzarti and Carloni (2019)

![image 6](<hpt-draft_images/imageFile6.png>)

![image 7](<hpt-draft_images/imageFile7.png>)

The right panel of Figure 5 shows analogous results when the estimand is the average causal effect on restaurant profits across all four post-treatment periods pτ¯q. When M¯ “ 1, our robust confidence set now includes zero, and is about twice as large as for the first-period effect (notice the difference in scale across the panels). The intuition for why the confidence sets are larger when looking at τ¯ than τ2009 is that ∆RMpM¯ q bounds the violation of parallel trends across consecutive periods by M¯ times the max in the pre-treatment period. Thus, the identified set will be larger for later periods, since the treatment and control groups have more time to diverge (e.g., the identified set for the second period will be twice as larger as for the first period). If we are willing to bound the magnitude of economic shocks by the max in the pre-treatment period, we will thus typically obtain wider confidence sets for parameters involving later periods.

#### 6.3 The effect of duty-to-bargain laws on long-run student outcomes

Lovenheim and Willen (2019, henceforth LW) study the impact of state-level public sector

duty-to-bargain (DTB) laws, which mandated that school districts bargain in good faith with teachers’ unions. LW examine the impacts of these laws on the adult labor market outcomes of people who were students around the time that these laws were passed, comparing individuals across different states and different birth cohorts to exploit the differential timing of the passage of DTB laws across states. The authors estimate the following regression specification separately for men and women, using data from the American Community Survey (ACS),

ÿ21

Dscrβr ` Xsct1 γ ` λct ` φs ` sct. (20)

Ysct “

r“´11

Ysct is an average outcome for the cohort of students born in state s in cohort c in ACS calendar year t. Dscr is an indicator for whether state s passed a DTB law r years before cohort

- c turned age 18.31 The event-study coefficients tβˆru estimate the dynamic treatment effects (or placebo effects) r years after DTB passage.32 The remaining terms include time-varying controls, birth-cohort-by-ACS-year fixed effects, and state fixed effects. We normalize the event-study coefficient β´2 to 0.33 We focus on the results where the outcome is employment.


Figure 6 plots the estimated event-study coefficients tβˆru from specification (20). In the event-study for men (left panel), the pre-period coefficients are relatively close to zero, whereas the longer-run post-period coefficients are negative. By contrast, the results for women (right panel) suggest a downward-sloping pre-existing trend.

LW write that, the “primary concern in our identification strategy is the existence of secular trends that differ systematically with treatment” (p. 318), such as confounding changes in labor supply or educational attainment. Given that the concern is long-run trends that are likely to evolve smoothly over time, smoothness restrictions of the form ∆SD seem natural in this context. Indeed, in some of their robustness checks, LW estimate models with group-specific linear trends, which roughly corresponds with the case ∆SDp0q.34 It thus

- 31Dsc,´11 is set to 1 if state s passed a law 11 years or more after cohort c turned 18. Likewise, Dsc,21 is set to 1 if state s passed a law 21 or more years before cohort c turned 18.
- 32Treatment timing in LW is staggered, and therefore the results in Sun and Abraham (2020) imply that βr can be interpreted as a sensible weighted average of causal effects under parallel trends only if treatment effects are homogeneous across adoption cohorts. For simplicity, we focus on the robustness of the results to violations of parallel trends using the original specification in LW, which is valid under the assumption of homogeneous treatment effects. As discussed in Section 2.1, our sensitivity analysis can also be applied to estimators that are robust to treatment effect heterogeneity.
- 33LW normalize event time -1 to 0, but discuss how cohorts at event time -1 may have been partially treated since LW impute the year that a student starts school with error. Since our robust confidence sets assume that there is no causal effect in the pre-period (τpre “ 0), we instead treat event-time -2 as the reference period in our analysis.
- 34The two are not exactly equivalent, however, because LW include parametric trends into what they call a “parametric event-study” model (see their specification (2)), which imposes that treatment effects are linear in time since treatment, rather than the flexible dynamic event-study specification (20).


seems natural to consider relaxations of the form ∆SDpMq, which allows for deviations from non-linearity of no more than M between consecutive periods.

Figure 6: Event-study coefficient tβru for employment, estimated using the event-study specification in (20).

![image 8](<hpt-draft_images/imageFile8.png>)

Figure 7: Sensitivity analysis for θ “ τ15 using ∆ “ ∆SDpMq

![image 9](<hpt-draft_images/imageFile9.png>)

![image 10](<hpt-draft_images/imageFile10.png>)

Figure 7 reports results for the treatment effect on employment for the cohort 15 years after the passage of a DTB law (as in Table 2 of LW), constructing robust confidence sets about how non-linear the difference in trends can be. In blue, we plot the original OLS confidence intervals for βˆ15 from specification (20). In red, we plot FLCIs when ∆ “ ∆SDpMq for different values of M; recall that M “ 0 corresponds with allowing only for linear violations of parallel trends, and larger values of M allow for larger deviations from linearity. In the analysis for men (left panel), the FLCIs are similar to those from OLS when allowing

for violations of parallel trends that are approximately linear (M « 0), but become wider as we allow for more non-linearity; the breakdown value for a significant effect is M « 0.01. For women (right panel), the original OLS estimates are negative and the confidence interval rules out 0. When we allow for linear violations of parallel trends pM “ 0q, however, the picture changes substantially owing to the pre-existing downward trend that is visible in Figure 6. Indeed, for M ă 0.01 the robust confidence set contains only positive values. Intuitively, this is because the point estimate for t “ 15 lies above a linear extrapolation of the negative pre-trend. Thus, if we were to impose the same smoothness restrictions for men as for women, we would either have to reconcile significant effects of opposite signs by gender (if M ă 0.01) or we would not be able to rule out null effects for both genders pM ě 0.01q.

How can we interpret the magnitudes of M in this example? We consider a calibration exercise based on the magnitudes of possible possible confounds: if violations of parallel trends were driven by confounding changes in education quality, what would a given value of M imply about the evolution of those confounds? Chetty, Friedman and Rockoff (2014) estimate that a 1 standard deviation increase in teacher value-added (VA) corresponds with a 0.4 percentage point increase in adult employment. Hence, a value of M “ 0.01 would correspond with allowing the slope of the differential trend to change by the equivalent of a one-fourtieth of a standard deviation of teacher VA across consecutive periods. Since the robust confidence sets for both men and women begin to include zero around this value of M, the strength with which we can rule out a null effect depends on our assessment of the economic plausibility of such non-linearities.

## 7 Conclusion

This paper considers the problem of conducting inference in difference-in-differences and related designs that is robust to violations of the parallel trends assumption. We introduce a variety of restrictions on the class of possible differences in trends that formalize commonly made arguments in empirical work, generalizing the framework for partial identification in Manski and Pepper (2018). We provide inference procedures that are uniformly valid so long as the difference in trends satisfies these restrictions, and derive novel results on the power of these procedures. We recommend that applied researchers report robust confidence sets under economically-motivated restrictions on parallel trends. We also recommend that researchers conduct formal sensitivity analyses, in which they report confidence sets for the causal effect of interest under a variety of possible restrictions on the underlying trends. Such sensitivity analyses make transparent what assumptions are needed in order to draw particular conclusions.

## References

Abadie, Alberto, “Semiparametric Difference-in-Differences Estimators,” The Review of

Economic Studies, 2005, 72 (1), 1–19.

###### Andrews, Isaiah, Jonathan Roth, and Ariel Pakes, “Inference for Linear Conditional

Moment Inequalities,” arXiv:1909.10062 [econ], December 2021. arXiv: 1909.10062.

###### Armstrong, Timothy and Michal Kolesár, “Optimal Inference in a Class of Regression

Models,” Econometrica, 2018, 86, 655–683.

and , “Sensitivity Analysis using Approximate Moment Condition Models,” Quantitative Economics, 2020. Forthcoming.

and , “Simple and Honest Confidence Intervals in Nonparametric Regression,” Quantitative Economics, 2020, 11 (1), 1–39. arXiv: 1606.01200.

Ashenfelter, Orley, “Estimating the Effect of Training Programs on Earnings,” The Review

of Economics and Statistics, 1978, 60 (1), 47–57. Publisher: The MIT Press.

Athey, Susan and Guido W. Imbens, “Design-based analysis in Difference-In-Differences

settings with staggered adoption,” Journal of Econometrics, April 2021.

Benzarti, Youssef and Dorian Carloni, “Who Really Benefits from Consumption Tax Cuts? Evidence from a Large VAT Reform in France,” American Economic Journal: Economic Policy, February 2019, 11 (1), 38–63.

Bhuller, Manudeep, Tarjei Havnes, Edwin Leuven, and Magne Mogstad, “Broadband Internet: An Information Superhighway to Sex Crime?,” The Review of Economics and Statistics, 2013, 80, 1237—-1266.

Bilinski, Alyssa and Laura A. Hatfield, “Nothing to see here? Non-inferiority approaches to parallel trends and other model assumptions,” arXiv:1805.03273 [stat.ME], 2020.

Borusyak, Kirill and Xavier Jaravel, “Revisiting Event Study Designs,” SSRN Scholarly

Paper ID 2826228, Social Science Research Network, Rochester, NY August 2016.

Bugni, Federico A., Ivan A. Canay, and Xiaoxia Shi, “Inference for subvectors and other functions of partially identified parameters in moment inequality models,” Quantitative Economics, 2017, 8 (1), 1–38.

###### Callaway, Brantly and Pedro H. C. Sant’Anna, “Difference-in-Differences with multiple

time periods,” Journal of Econometrics, December 2020.

Canay, Ivan and Azeem Shaikh, “Practical and Theoretical Advances in Inference for Partially Identified Models,” in Bo Honoré, Ariel Pakes, Monika Piazzesi, and Larry Samuelson, eds., Advances in Economics and Econometrics, 2017, pp. 271–306.

###### Chen, Xiaohong, Timothy M. Christensen, and Elie Tamer, “Monte Carlo Confi-

dence Sets for Identified Sets,” Econometrica, 2018, 86 (6), 1965–2018.

Chernozhukov, Victor, Whitney K. Newey, and Andres Santos, “Constrained Conditional Moment Restriction Models,” arXiv:1509.06311 [math, stat], September 2015. arXiv: 1509.06311.

Chetty, Raj, John N. Friedman, and Jonah E. Rockoff, “Measuring the Impacts of Teachers II: Teacher Value-Added and Student Outcomes in Adulthood,” American Economic Review, September 2014, 104 (9), 2633–2679.

Cho, JoonHwan and Thomas M. Russell, “Simple Inference on Functionals of SetIdentified Parameters Defined by Linear Moments,” arXiv:1810.03180 [econ.EM], 2019.

Cox, Gregory and Xiaoxia Shi, “Simple Adaptive Size-Exact Testing for Full-Vector and Subvector Inference in Moment Inequality Models,” The Review of Economic Studies, March 2022.

de Chaisemartin, Clément and Xavier D’Haultfœuille, “Two-Way Fixed Effects Estimators with Heterogeneous Treatment Effects,” American Economic Review, September 2020, 110 (9), 2964–2996.

and , “Two-Way Fixed Effects and Differences-in-Differences with Heterogeneous Treatment Effects: A Survey,” SSRN Scholarly Paper ID 3980758, Social Science Research Network, Rochester, NY December 2021.

Dette, Holger and Martin Schumann, “Difference-in-Differences Estimation Under Non-

Parallel Trends,” Working paper, 2020.

Dobkin, Carlos, Amy Finkelstein, Raymond Kluender, and Matthew J. Notowidigdo, “The Economic Consequences of Hospital Admissions,” American Economic Review, 2018, 108 (2), 308–352.

Donoho, David L., “Statistical Estimation and Optimal Recovery,” The Annals of Statis-

tics, 1994, 22 (1), 238–270.

Flynn, Zach, “Inference Based on Continuous Linear Inequalities via Semi-Infinite Programming,” SSRN Scholarly Paper ID 3390788, Social Science Research Network, Rochester, NY May 2019.

Frandsen, Brigham R, “The Effects of Collective Bargaining Rights on Public Employee Compensation: Evidence from Teachers, Firefighters, and Police,” ILR Review, 2016, 69

(1), 84–112.

Freyaldenhoven, Simon, Christian Hansen, and Jesse Shapiro, “Pre-event Trends in the Panel Event-study Design,” American Economic Review, 2019, 109 (9), 3307–3338.

Gafarov, Bulat, “Inference in high-dimensional set-identified affine models,”

arXiv:1904.00111 [econ.EM], 2019.

Goodman-Bacon, Andrew, “Public Insurance and Mortality: Evidence from Medicaid

Implementation,” Journal of Public Economics, 2018, 126 (1), 216–262.

, “Difference-in-differences with variation in treatment timing,” Journal of Econometrics, June 2021.

Greenstone, Michael and Rema Hanna, “Environmental Regulations, Air and Water Pollution, and Infant Mortality in India,” American Economic Review, October 2014, 104

(10), 3038–3072.

Hansen, Bruce E. and Seojeong Lee, “Asymptotic theory for clustered samples,” Journal

of Econometrics, June 2019, 210 (2), 268–290.

Hansen, Christian B., “Asymptotic properties of a robust variance matrix estimator for panel data when T is large,” Journal of Econometrics, December 2007, 141 (2), 597–620.

Heckman, James, Hidehiko Ichimura, Jeffrey Smith, and Petra Todd, “Characterizing Selection Bias Using Experimental Data,” Econometrica, 1998, 66 (5), 1017–1098.

Hirano, Keisuke and Jack R. Porter, “Impossibility Results for Nondifferentiable Func-

tionals,” Econometrica, 2012, 80 (4), 1769–1790.

Ho, Kate and Adam Rosen, “Partial Identification in Applied Research: Benefits and Challenges,” in Bo Honoré, Ariel Pakes, Monika Piazzesi, and Larry Samuelson, eds., Advances in Economics and Econometrics, 2017, pp. 307–359.

###### Horowitz, Joel L. and Charles F. Manski, “Identification and Robustness with Con-

taminated and Corrupted Data,” Econometrica, 1995, 63 (2), 281–302.

###### Hudson, Sally, Peter Hull, and Jack Liebersohn, “Interpreting Instrumented

Difference-in-Differences,” Working Paper 2017.

Kadane, Joseph B., “Comparison of k-Class Estimators When the Disturbances Are

Small,” Econometrica, 1971, 39 (5), 723–737.

Kahn-Lang, Ariella and Kevin Lang, “The Promise and Pitfalls of Differences-inDifferences: Reflections on 16 and Pregnant and Other Applications,” Journal of Business and Economic Statistics, 2020, 38 (3), 613–620.

Kaido, Hiroaki and Andres Santos, “Asymptotically Efficient Estimation of Models

Defined by Convex Moment Inequalities,” Econometrica, 2014, 82 (1), 387–413.

, Francesca Molinari, and Jörg Stoye, “Confidence Intervals for Projections of Partially Identified Parameters,” Econometrica, 2019, 87, 1397–1432.

, , and , “CONSTRAINT QUALIFICATIONS IN PARTIAL IDENTIFICATION,” Econometric Theory, June 2021, pp. 1–24. Publisher: Cambridge University Press.

Keele, Luke J., Dylan S. Small, Jesse Y. Hsu, and Colin B. Fogarty, “Patterns of Effects and Sensitivity Analysis for Differences-in-Differences,” arXiv:1901.01869 [stat.AP], 2019.

Kim, Wooyoung, Koohyun Kwon, Soonwoo Kwon, and Sokbae Lee, “The identification power of smoothness assumptions in models with counterfactual outcomes,” Quantitative Economics, 2018, 9 (2), 617–642.

Kline, Patrick and Andres Santos, “Sensitivity to missing data assumptions: Theory and an evaluation of the U.S. wage structure,” Quantitative Economics, 2013, 4 (2), 231–267.

Kolesár, Michal and Christoph Rothe, “Inference in Regression Discontinuity Designs with a Discrete Running Variable,” American Economic Review, 2018, 108 (8), 2277–2304.

Leavitt, Thomas, “Beyond Parallel Trends: Improvements on Estimation and Inference in

the Difference-in-Differences Design,” Working paper, 2020.

Lee, Jin Young and Gary Solon, “The Fragility of Estimated Effects of Unilateral Divorce Laws on Divorce Rates,” The B.E. Journal of Economic Analysis & Policy, 2011, 11 (1).

Lovenheim, Michael F. and Alexander Willen, “The Long-Run Effects of Teacher Collective Bargaining,” American Economic Journal: Economic Policy, 2019, 11 (3), 292– 324.

Low, Mark G., “Bias-Variance Tradeoffs in Functional Estimation Problems,” The Annals

of Statistics, 1995, 23 (3), 824–835.

Manski, Charles F., Partial Identification of Probability Distributions, Springer, 2003.

, Identification for Prediction and Decision, Harvard University Press, 2007.

, Public Policy in an Uncertain World:Analysis and Decisions, Harvard University Press, 2013.

and John V. Pepper, “Deterrence and the Death Penalty: Partial Identification Analysis Using Repeated Cross Sections,” Journal of Quantitative Criminology, March 2013, 29 (1), 123–141.

and , “How Do Right-to-Carry Laws Affect Crime Rates? Coping with Ambiguity Using Bounded-Variation Assumptions,” Review of Economics and Statistics, 2018, 100

(2), 232–244.

###### Masten, Matthew A. and Alexandre Poirier, “Inference on Breakdown Frontiers,”

Quantitative Economics, 2020, 11 (1), 41–111.

Molinari, Francesca, “Chapter 5 - Microeconometrics with partial identification,” in Steven N. Durlauf, Lars Peter Hansen, James J. Heckman, and Rosa L. Matzkin, eds., Handbook of Econometrics, Vol. 7 of Handbook of Econometrics, Volume 7A, Elsevier, January 2020, pp. 355–486.

Moreira, Marcelo J., “A Conditional Likelihood Ratio Test for Structural Models,” Econo-

metrica, 2003, 71 (4), 1027–1048.

and Geert Ridder, “Efficiency Loss of Asymptotically Efficient Tests in an Instrumental Variables Regression,” SSRN Scholarly Paper ID 3348716, Social Science Research Network, Rochester, NY March 2019.

Müller, Ulrich K, “Efficient tests under a weak convergence assumption,” Econometrica,

2011, 79 (2), 395–435.

Noack, Claudia and Christoph Rothe, “Bias-Aware Inference in Fuzzy Regression Dis-

continuity Designs,” arXiv:1906.04631 [econ.EM], 2020.

###### Rambachan, Ashesh and Jonathan Roth, “An Honest Approach to Parallel Trends,”

Working paper, 2021, p. 126.

Romano, Joseph P. and Azeem M. Shaikh, “Inference for identifiable parameters in partially identified econometric models,” Journal of Statistical Planning and Inference, September 2008, 138 (9), 2786–2807.

, , and Michael Wolf, “A Practical Two-Step Method for Testing Moment Inequalities,” Econometrica, 2014, 82 (5), 1979–2002.

Roth, Jonathan, “Pre-test with Caution: Event-study Estimates After Testing for Parallel

Trends,” American Economic Review: Insights, Forthcoming.

, Pedro H. C. Sant’Anna, Alyssa Bilinski, and John Poe, “What’s Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature,” arXiv:2201.01194 [econ, stat], January 2022. arXiv: 2201.01194.

###### Sant’Anna, Pedro H. C. and Jun B. Zhao, “Doubly Robust Difference-in-Differences

Estimators,” Journal of Econometrics, 2020, 219 (1), 101–122.

Schrijver, Alexander, Theory of Linear and Integer Programming, Wiley-Interscience,

1986.

Stock, James and Mark Watson, “Heteroskedasticity-Robust Standard Errors for Fixed

Effects Panel Data Regression,” Econometrica, 2008, 76 (1), 155–174.

Sun, Liyan and Sarah Abraham, “Estimating Dynamic Treatment Effects in Event Stud-

ies with Heterogeneous Treatment Effects,” Journal of Econometrics, 2020.

Tamer, Elie, “Partial Identification in Econometrics,” Annual Review of Economics, 2010,

2, 167–195.

###### van der Vaart, Aad W and Jon A Wellner, “Weak Convergence and Empirical Pro-

cesses: With Applications to Statistics,” 1996.

Wolfers, Justin, “Did Unilateral Divorce Laws Raise Divorce Rates? A Reconciliation and

New Results,” American Economic Review, 2006, 96, 1802–1820.

Ye, Ting, Luke Keele, Raiden Hasegawa, and Dylan S. Small, “A Negative Correlation Strategy for Bracketing in Difference-in-Differences with Application to the Effect of Voter Identification Laws on Voter Turnout,” arXiv:2006.02423 [stat.ME], 2020.

# A More Credible Approach to Parallel Trends

### Online Appendix

##### Ashesh Rambachan Jonathan Roth April 1, 2022

This online appendix contains proofs and additional results for the paper “A More Credible Approach to Parallel Trends” by Ashesh Rambachan and Jonathan Roth. Section A contains proofs and auxilliary lemmas for results stated in the main text. Section B contains additional details and results from our simulations.

## A Proofs of Results in Main Text

Proof of Lemma 2.2 Proof. By equation (7), we can write the coverage requirement as

˜θ P ď

¸

Cn,k1pβˆn,Σnq

Pβˆ

inf

inf

inf

n„Npδ`τ, Σnq

δP∆,τ

θPSpδ`τ,∆kq

k

k1

The left-hand side is bounded below by

ě 1 ´ α.

´θ P Cn,kpβˆn,Σnq¯,

Pβˆ

inf

inf

inf

n„Npδ`τ, Σnq

δP∆,τ

θPSpδ`τ,∆kq

k

which is at least 1 ´ α since Cn,kpβˆn,Σnq satisfies (10) for ∆ “ ∆k for all k.

| |
|---|


###### Proof of Proposition 3.1

Proof. We verify that the conditions of the proposition are sufficient for the conditions for size control for the conditional and hybrid tests given in Proposition 2 of ARP. Note that in our setting, the non-stochastic variable X˜ plays the role of the instruments Z in ARP, so all statements in ARP conditional on Z can be interpreted as unconditional in our context.

First, suppose that Assumption 5(A) holds. Then we can write Y˜npθq “ Aβˆn ´ d ´ A˜p¨,1qθ “ TUnpθq ´ ζpθq, where Unpθq “ Qβˆn and ζpθq “ d ` A˜p¨,1qθ is non-stochastic,

which is the structure required by the first part of Assumption 1 of ARP.35 Note that ΩP :“ V arPpUnpθqq “ QΣPQ1. Since Q is full-rank by assumption and ΣP has eigenvalues bounded away from zero by Assumption 3, so too does ΩP “ QΣPQ1, as required by the latter part of Assumption 1 in ARP. Next, note that our estimate of the variance of Y˜npθq, AΣˆnA1, can be expressed as TΩˆnT, for Ωˆn “ QΣˆnQ1. It is immediate from Assumption 4 that Ωˆn is uniformly consistent for ΩP, as required in Assumption 2 in ARP. Next, note that if f P BL1, then gpxq “ ||G||´op1fpGxq is also in BL1, where ||¨||op is the operator norm. This implies that

?nQpβˆ ´ βPqı ´ ErfpQξPqsˇ ď ||Q||op sup

ˇEP ”fp

?npβˆ ´ βPqı ´ ErfpξPqsˇ.

ˇEP ”fp

sup

fPBL1

fPBL1

Since Unpθq “ Qβˆn, Assumption 2 together with the previous argument implies that

?npUnpθq ´ QβPq‰ ´ E”fpξ˜Pqı

“

ˇEP

fp

ˇ “ 0,

lim

sup

sup

nÑ8

PPP

fPBL1

where ξ˜P „ N p0, ΩPq. This verifies Assumption 3 in ARP. Note that Assumption 5(A) implies that Assumption C.1 in ARP is satisfied, and Assumption C.2 in ARP is trivially satisfied for X “ tX˜u. Hence, Proposition C.1 in ARP implies that Assumption 4 in ARP is satisfied. We have thus verified the conditions for size control in Proposition 2 of ARP.

Second, consider the case where Assumption 5(B) holds. In this case, we can write Y˜npθq “ TUnpθq ´ ζpθq, where now T “ A, Unpθq “ βˆn, and ζpθq “ d ` A˜p¨,1qθ. Assumptions 1-3 in ARP can be verified analogously to the arguments above for the case where T is as given in Assumption 5(A). To verify Assumption 4 in ARP, we must show that

pγ ´ aγ˜q1AΣPA1pγ ´ cγ˜q ą 0,

sup

min

γ,γ˜PV:pΣP q,γ‰γ,a˜ ě0

ΣP PS

where V:pΣq is the subset of vertices in V pΣq that can be optimal when ηˆ ą 0 (see Lemma

- 5 in ARP). By Lemma A.1 below, each γ P V pΣPq can be written as cjpΣPqγ¯j for some element γ¯j P V pIq. Moreover, cjpΣPq “ pγ¯j1σ˜pΣPqq´1, where σ˜pΣPq is the square root of the diagonal elements of ΩP “ AΣPA1. However, the jth diagonal element of ΩP is Apj,¨qΣPA1pj,¨q, where Apj,¨q is the jth row of A. Since the eigenvalues of ΣP are bounded above by λ¯, it follows that Apj,¨qΣPA1pj,¨q is bounded above by λ¯||Apj,¨q||2. The elements of σ˜pΣPq are thus


35Assumption 1 of ARP imposes the structure Yi “ TUi`ζi, where the index i corresponds with individual observations and the sample moments are formed by averaging across i. However, this structure is only used in the proofs of size control to show that the scaled sample moments, denoted Yn,0 in ARP, have the structure Yn,0 “ TUn,0 ` ζn,0pθq, where Un,0 and ζn,0 are sample averages of Ui and ζi. In our setting Y˜n is analogous to ?1nYn,0 in ARP, and we thus verify this structure directly.

bounded above, and hence cjpΣPq is bounded away from zero. Thus, there exists a

c such that cjpΣPq ě ¯

¯

c for all ΣP P S. Hence,

c2 ˆ sup

pγ ´ aγ˜q1AΣPA1pγ ´ aγ˜q˙

pγ ´ aγ˜q1AΣPA1pγ ´ aγ˜q ě ¯

sup

min

min

γ,γ˜PV:pΣP q,γ‰γ,a˜ ě0

γ,γ˜PV pIq,γ‰γ,a˜ ě0

ΣP PS

ΣP PS

c2 ˆ min

λ˙,

||pγ ´ aγ˜q1A||2¯

ě ¯

γ,γ˜PV:pIq,γ‰γ,a˜ ě0

λ. To complete the proof, it thus suffices to show that V:pIq contains only vertices such that γ¯j1A ‰ 0, so that the lower bound obtained in the previous display is strictly positive by Assumption 5(B). To show this, note that if γ¯j1A “ 0, then γ¯j1Y˜npθ¯q “ γ¯j1pAβˆn ´d´A˜p¨,1qθ¯q “ ´γ¯j1d. Since ∆ is non-empty, there exists some δ such that Aδ ´ d ď 0, which implies that ´γ¯j1d “ γ¯j1pAδ ´ dq ď 0 since γ¯j ě 0 by construction. We have thus established that γ¯j1Y˜pθ¯q ď 0, and hence γ¯j can never be optimal when ηˆ ą 0, so γ¯j R V:pIq. We have thus verified that Assumption 4 in ARP holds, as needed.

where the second inequality uses the fact that the minimal eigenvalue of ΣP is at least

¯

| |
|---|


#### A.1 Proof and auxiliary lemmas for uniform consistency

###### Proof of Proposition 3.2

Proof. Towards contradiction, suppose that the conditional test is not consistent. Then there exists an increasing sequence of sample sizes and distributions pnm,Pmq, x ą 0, and ω ą 0 such that

mq ď 1 ´ ω. It is straightforward to verify that the conditional test is invariant to a re-scaling of the units of βˆ, so that ψαCpβˆn

„ψαCpβˆn

1 n

Σˆn

###### EP

,A,d,θPub

` x,

limsup

m

m

m

mÑ8

,A,?nmd,?nmpθPub

?nmβˆn

Σˆn

` xq,Σˆn

mq. Thus, along this sequence,

` x, n1

mq “ ψαCp

,A,d,θPub

m

m

m

m

m

mqı ď 1 ´ ω. Since V is compact, we can extract a further subsequence m1 under which VP

”ψαCp

,A,?nmd,?nmpθPub

?nmβˆn

` xq,Σˆn

###### EP

limsup

m

m

m

mÑ8

Ñ V ˚ for V ˚ P V. Denote the top left block of V ˚ by Σ˚.

m1

To obtain a contradiction, we will construct a further subsequence such that the conditions of Lemma A.2 hold asymptotically with probability at least 1-ω{2. From Lemma A.1, each element γP

q can be written as cjpΣP

qγ¯j, where γ¯1,...,γ¯J are the elements

P V pΣP

m1

m1

m1

c such that cjpΣPq ě ¯

of V pIq. We argued in the proof to Proposition 3.1 that there exists a constant

¯

c for all j whenever ΣP has eigenvalues bounded above by λ¯. By an analogous argument, we can show that there exists a constant c¯ such that cjpΣPq ď c¯ whenever ΣP has eigenvalues bounded below by

c ď cjpΣPq ď c¯ for ΣP P S. For γ P V pΣPq, γ1AΣPA1γ “ cjpΣPq2γ¯j1AΣPA1γ¯j for some j, and thus for ΣP P S, we have that

λ. Thus,

¯

¯

λ ď γ1AΣPA1γ ď c¯2||γ¯j1A||2λ.¯ Thus, either γ1AΣPA1γ “ 0 (if γ¯j1A “ 0), or

c2||γ¯j1A||2¯

¯

||γ¯j1A||2¯

λ ď γ1AΣPA1γ ď c¯2 max

||γ¯j1A||2λ,¯

c2 min

¯

j:¯γj1 A‰0

j:¯γj1 A‰0

where the upper and lower bounds are finite and positive since V pIq is finite. Now consider the vertex γˆm

1,jAΣˆPA1γˆm

1,j “ cjpΣˆn

qγ¯j. By the continuous mapping theorem, γˆm1

1,j Ñp cjpΣ˚q2γ¯j1AΣ˚A1γ¯j. From this convergence and the inequalities in the previous display, it follows that there exist constants

m1

σ2 and σ¯2 such that condition (i) of Lemma A.2 is satisfied w.p.a. 1.

¯

Next, define

ηpβ,A,d,θ,¯ Σq :“ min

η s.t. Aβ ´ d ´ A˜p¨,1qθ¯´ A˜p¨,´1qτ˜ ď ησ,˜ (21)

η,τ˜

where σ˜ is the square root of the diagonal elements of AΣA1. Since θPub P SpβP,∆q, ηpβP,A,d,θPub,ΣPq ď 0. By duality, we can write ηpβP,A,d,θPub,ΣPq “ maxγPVpΣ

Pq γ1pAβP ´ d´A˜p¨,1qθubq. It follows that there exists some γ˜P P V pΣPq such that γ˜P1 pAβP ´d´A˜p¨,1qθubq “ 0 and ´γ˜P1 A˜p¨,1q ą 0, since otherwise for ą 0 sufficiently small we would have that ηpβP,A,d,θPub `  ,ΣPq “ maxγPVpΣ

Pq γ1pAβP ´ d ´ A˜p¨,1qpθub ` qq ď 0, which would imply that θub ` P SpβP,∆q, which is a contradiction. From Lemma A.1, γ˜P

###### q can be written as cjpΣP

###### P V pΣP

m1

m1

c ą 0 for all Σ P S and γ¯1,...,γ¯J are the elements of V pIq. Since V pIq is finite, we can extract a further subsequence pnl,Plq such that γ˜P

qγ¯j, where cjpΣq ě ¯

m1

lqγ˜j˚ for fixed j˚. For ease of notation, without loss of generality we assume j˚ “ 1. It follows that

l “ cj˚pΣP

?nlβˆn

###### ,A,?nld,?nlpθPub

γ1?nlpAβˆn

` xq,Σˆn

l ´ d ´ A˜p¨,1qpθPub

ηp

lq “ max

` xqq

l

l

l

γPV pΣˆnlq

?nlc1pΣˆn

lqγ¯11pAβˆn

l ´ d ´ A˜p¨,1qpθPub

ě

###### ` xqq “ c1pΣˆn

l

?nlc1pΣˆn

?nlγ¯11Apβˆn

lqp´γ˜11A˜p¨,1qqx.

l ´ βP

lq `

lq

By the continuous mapping theorem, c1pΣˆn

lq Ñp c1pΣ˚q ą 0. Assumption 6 and the continuous mapping theorem together imply that the first term in the previous display converges in distribution to a N p0, c1pΣ˚q2γ¯11AΣ˚A1γ¯1q distribution, while the second term converges in probability to 8. It follows that ηp

?nlβˆl,A,?nld,?nlpθPub

` xq,Σˆn

lq Ñp 8, and thus condition (ii) of Lemma A.2 holds w.p.a. 1 for any value of M.

l

To complete the proof, we construct a further subsequence such that condition (iii) of Lemma A.2 holds asymptotically with probability at least 1-ω{2. Let Y˜l “ Aβˆn

l ´ d ´ A˜p¨,1qpθPub

` xq. Recall that any element of V pΣˆn

l ´ d ´ A˜p¨,1qpθPub

lq, say γl,j, takes the form γl,j “ cjpΣˆn

` xq and µ˜l “ AβP

l

l

lqγ¯j, and our argument above implies that γ¯j1µ˜l ď ´γ¯j1A˜p¨,1qx. Since cjpΣˆn

lq Ñp cjpΣ˚q ą 0 by the continuous mapping theorem, and γ¯j1µ˜l is bounded from above, we can extract a subsequence l1 along which γl1

1 Ñp νj P R Y t´8u. The vertex set is finite, and so passing to further subsequences we obtain a subsequence indexed by k such that γk,j1 µ˜k Ñp νj P R Y t´8u for all j. Observe that for distinct vertices i and j with

1,jµ˜l

- γ¯i1A ‰ 0,

pcipΣˆn

kqγ¯i ´ cjpΣˆn

kqγ¯jq1

?nkY˜k “pcipΣˆn

kqγ¯i ´ cjpΣˆn

kqγ¯jq1

?nkpY˜k ´ µ˜kq` ?nkpcipΣˆn

kq ´ cipΣ˚qqγ¯i1µ˜k ´

?nkpcjpΣˆn

kq ´ cjpΣ˚qqγ¯j1µ˜k` ?nkpcipΣ˚qγ¯i1 ´ cjpΣ˚qγ¯j1qµ˜k

Consider first the case where γk,i1 µ˜k and γk,j1 µ˜k both have finite limits νi and νj. Since ?nkpcipΣ˚qγ¯i1 ´ cjpΣ˚qγ¯j1qµ˜k is non-stochastic, we can extra a further subsequence k1 such that ?nk

1pcipΣ˚qγ¯i1 ´ cjpΣ˚qγ¯j1qµ˜k

1 Ñ ν˚ P R Y t˘8u. Assumption 6 and the continuous mapping theorem imply that pcipΣˆn

k1

qγ¯i ´ cjpΣˆn

k1

qγ¯jq1

?nk

1

Y˜k

1

converges in distribution to

ζij “ pcipΣ˚qγ¯i ´ cjpΣ˚qγ¯jq1Aξβ `

νi cipΣ˚q

Dc1iξΣ ´

νj cjpΣ˚q

Dc1jξΣ ` ν˚,

where pξβ1 ,ξΣ1 q1 „ N p0, V ˚q and Dci is the gradient of cipΣ˚q with respect to vecpΣ˚q. The limiting distribution is normal, and limiting variance must be positive since Assumptions

5 and 7 imply that pcipΣ˚qγ¯i ´ cjpΣ˚qγ¯jq1Aξβ has positive variance36 and is not perfectly colinear with ξΣ. It follows that for any ϑ, there exists some ą 0 such that the probability that ζij P p´ , q is less than ϑ. On the other hand, if γ¯i1µ˜k Ñ ´8, then cipΣˆn

kqγ¯i?nkY˜k Ñp ´8, so cipΣˆn

kqγ¯i is optimal for ηˆp

?nkβˆn

k

,?nkd,?nkpθPub

k

` xq,Σˆn

kq w.p.a. 0, whereas if

- γ¯j1µ˜k Ñ ´8, then ηˆp


?nkβˆn

###### ,?nkd,?nkpθPub

kq ´ cjpΣˆkqγj1?nkY˜k Ñp 8. Since there

` xq,Σˆn

k

k

36This is immediate under Assumption 5(ii). Under Assumption 5(i), the proof of Proposition C.2 in ARP shows that if there is a positive constant c such pγ¯i ´ cγ¯jq1A “ 0, then cipΣˆn

kqγ¯i and cjpΣˆn

kqγ¯j can only be optimal vertices if ηˆ ď 0. Since we’ve shown ηˆ Ñp 8, such vertices will be optimal w.p.a. 0, and thus can be ignored when establishing part (iii) of Lemma A.2.

are a finite number of pairs of vertices, we can choose ϑ such that the probability that ζij P p´ , q for any pi,jq is bounded above by ω{2, and thus condition (iii) of Lemma A.2 is satisfied with probability at least ω{2, as we wished to show. The result for the hybrid test is immediate from the fact that the hybrid test rejects whenever the size-α1´´κκ conditional test rejects.

| |
|---|


- Lemma A.1. Let FpΣq :“ tγ : A˜1p¨,´1qγ “ 0,σ˜pΣq1γ “ 1,γ ě 0u be the feasible set of the dual problem, where σ˜pΣq is the vector containing the square-roots of the diagonal elements of AΣA1. Let V pΣq denote the set of vertices of FpΣq. Then, for any Σ positive definite,


V pΣq “ tc1pΣqγ¯1,...,cJpΣqγ¯Ju, where γ¯1,...,γ¯J are the elements of V pIq and cjpΣq “ pγ¯j1σ˜pΣqq´1.

###### Proof of Lemma A.1

Proof. Recall that v is a vertex of the polyhedron P “ tx P RK : Wx ď bu iff v P P and WpJ,¨qx “ bJ for J a set of indices such that WpJ,¨q has K independent rows (see Section 8.5 of Schrijver (1986)). It follows that v P V pΣq iff v ě 0 and there exists J such that

¨ ˚ ˝

˛ ‹ ‚

A˜1p¨,´1q ´IpJ,¨q σ˜1

WJ :“

¨ ˚ ˝

˛ ‹ ‚, where K is the number of rows of A.

0

has row rank equal to K, and WJv “

- 0
- 1


˜

¸ has exactly K ´ 1

A˜1p¨,´1q ´IpJ,¨q

Now, let J be the set of indices J such that W˜J :“

linearly independent rows and there exists a vector vJ ‰ 0 such that W˜Jv “ 0 and vJ ě 0. Since by construction W˜J has rank K ´ 1 and K columns, its nullspace is 1-dimensional. It is then immediate that for each J P J , there is a unique vector v¯J ě 0 such that W˜Jv¯J “ 0 and ι1V¯J “ 1, where ι is the vector of ones. Moreover, J is finite, since there are a finite number of possible subindices of I, and thus we can write tv¯J : J P J u “ tγ¯1,...,γ¯Ju for distinct vectors γ¯1,...,γ¯J.

It now remains to show that V pΣq “ tc1pΣqγ¯1,...,cJpΣqγ¯Ju, for cj as defined above. First, suppose that v “ cjpΣqγ¯j for some j. By construction, A˜1p¨,´1qv “ 0, v ě 0, and σ˜1v “ pσ˜1vjq´1pσ˜1vjq “ 1, and so v P F. Additionally, there exists J such that W˜J “

˜

¸

A˜1p¨,´1q ´IpJ,¨q

has rank K ´1 and W˜Jv “ 0. From the fact that W˜Jv “ 0, whereas σ˜1v “ 1, we see that σ˜1 must be linearly independent from the rows of W˜J, and thus WJ “

˜

¸ has rank K. It follows that v P V pΣq.

W˜J σ˜1

Next, suppose that v P V pΣq. Then v ě 0, and there exists J such that

˛ ‹ ‚

¨ ˚ ˝

A˜1p¨,´1q ´IpJ,¨q σ˜1

WJ :“

˛ ‹ ‚. Let W˜J “

¨ ˚ ˝

˜

¸. Note that since

0

A˜1p¨,´1q ´IpJ,¨q

has row rank equal to K, and WJv “

- 0
- 1


W˜Jv “ 0, whereas σ˜1v “ 1, σ˜1 must be linearly independent of the other rows of WJ, from which it follows that W˜ has row rank K ´ 1. Thus, J P J , and so v “ cγ¯j for some j and c ą 0. Since σ˜1v “ 1, we have cσ˜1γ¯j “ 1, which implies c “ pσ˜1γ¯jq´1, which gives the desired result.

Finally, by construction, γ¯j1ι “ 1, and so cjpIq “ 1 for all j, so γ¯1,...,γ¯J correspond precisely with the elements of V pIq.

| |
|---|


σ2,σ¯2, there exists a finite constant C¯ such that the conditional test ψαCpβ,A,d,θ,ˆ Σq rejects whenever the following conditions are satisfied

- Lemma A.2. For any positive constants  , ¯


- (i) For all γ P V pΣq, either γ1AΣA1γ “ 0 or ¯

σ2 ď γ1AΣA1γ ď σ¯2.

- (ii) ηˆ “ maxγPVpΣq γ1Y˜ ą C¯, where Y˜ “ Aβˆ ´ d ´ A˜p¨,1qθ.
- (iii) If the optimal vertex γ˚ satisfies, γ˚1 AΣA1γ˚ ą 0, then for all γ˜ P V pΣq with γ˜ ‰ γ˚, we have that |γ˚1 Y˜ ´ γ˜1Y˜| ą .


Proof. Let Σ˜ “ AΣA1. If the optimal vertex γ˚ satisfies γ˚1 Σ˜γ˚ “ 0, then the conditional test rejects whenever ηˆ ą 0, so condition (ii) with any C ą 0 suffices. For the remainder of

the proof, we show that conditions (i)-(iii) are sufficient when γ˚1 Σγ˚ ‰ 0. Observe that the conditional test rejects if and only if ηˆ ą 0 and

Φptq ´ Φpzloq Φpzupq ´ Φpzloq

ą 1 ´ α,

, and σ˚ “ bγ1

, zlo “ vσlo˚

, zup “ vσup˚

˚Σ˜γ˚. It is clear that the left-hand side of the previous display is increasing in t and decreasing in zup. It is also decreasing in zlo, since

where t “ σηˆ˚

###### the derivative with respect to zlo is

φpzloqpΦpzupq ´ Φpzloqq pΦpzupq ´ Φpzloqq2

´

ă 0.

From Lemma A.3 below, condition (iii) implies that ηˆ ´ vlo ě , and thus zlo ď t ´ ˜ , for ˜ “ {σ¯. This, combined with the previous discussion, implies that the conditional test rejects whenever ηˆ ą 0 and

Φptq ´ Φpt ´ ˜ q 1 ´ Φpt ´ ˜ q

ą 1 ´ α. By L’Hopitale’s rule, we have that

Φptq ´ Φpt ´ ˜ q 1 ´ Φpt ´ ˜ q

φpt ´ ˜ q ´ φptq φpt ´ ˜ q

###### “ lim

###### “ lim

lim

tÑ8

tÑ8

tÑ8

φptq φpt ´ ˜ q

1 ´

“ 1.

Hence, there exists C˜ ą 0 such that the conditional test rejects whenever t ě C˜. But t “ σηˆ

˚

and thus t ą C˜ whenever ηˆ ą C¯ for C¯ “ C˜σ¯.

| |
|---|


- Lemma A.3. Consider the conditional test ψαCpβ,A,d,θ,ˆ Σq. If the optimal vertex γ˚ is such


|γ˚1 Y˜ ´ γ1Y˜| where Y˜ “ Aβˆ ´ d ´ A˜p¨,1qθ. Similarly, vup ´ ηˆ ě γ

that γ˚1 AΣA1γ˚ ą 0, then ηˆ ´ vlo ě minγPVpΣq,γ‰γ

˚

1 ˚AΣA1γ˚

|γ˚1 Y˜ ´ γ1Y˜|.

maxγPVpΣqγ1AΣA1γ minγPVpΣq,γ‰γ

˚

Proof. Since ηˆ is finite, the results hold trivially when vlo and vup are infinite. For the remainder of the proof, we assume that they are finite. Let Σ˜ “ AΣA1. Lemma 2 in ARP implies that

γ˚1 Σ˜γ˚γ1S γ1

vlo “ min

,

˚Σ˜γ˚ ´ γ1

˚Σ˜γ

γPV pΣq:γ˚1 Σ˜γ˚´γ˚1 Σ˜γą0

where S “ pI ´ Σ˜γ

γ˚1 Σ˜γ˚γ˚1 qY˜. Let γ˜ denote the vertex at which the minimum is obtained. Substituting in the definition of S and re-arranging terms, we obtain that

˚

γ˚1 Σ˜γ˚ γ1

pγ˚1 Y˜ ´ γ˜1Y˜q ě pγ˚1 Y˜ ´ γ˜1Y˜q,

ηˆ ´ vlo “

˚Σ˜˜γ

˚Σ˜γ˚ ´ γ1

from which the result for vlo is immediate. We can analogously show that

γ˚1 Σ˜γ˚ γ1

pγ˚1 Y˜ ´ γ˜1Y˜q,

vup ´ ηˆ “

˚Σ˜˜γ ´ γ1

˚Σ˜γ˚

for a vertex γ˜ such that γ˚1 Σ˜˜γ ´ γ˚1 Σ˜γ˚ ą 0. The result then follows from noting that

γ˚1 Σ˜γ˚ γ1

ě

˚Σ˜˜γ ´ γ1

˚Σ˜γ˚

γ˚1 Σ˜γ˚ γ1

ě

˚Σ˜˜γ

γ˚1 Σ˜γ˚ maxγPVpΣq γ1Σ˜γ

.

| |
|---|


#### A.2 Proof and auxiliary lemmas for uniform local asymptotic power

- Proof of Proposition 3.3 Proof. By an invariance to scale argument as in Proposition 3.2, it is sufficient to show that


?nβˆn,A,?nd,?nθPub ` x,Σˆnqı ´ ρ˚αpP,xqˇ “ 0.

ˇEP ”ψαCp

lim

sup

nÑ8

PPP

To show this, it suffices to establish that for every subsequence pnm,Pmq with nm Ñ 8, there exists a further subsequence l such that

”ψαCp

lqı ´ ρ˚αpPl,xqˇ “ 0.

,A,?nld,?nθPub

?nlβˆn

` x,Σˆn

ˇEP

lim

l

l

l

lÑ8

Since Pm P P , for each m there exists a Bm˚ and a value τ˜m˚ such that

m,´1qτ˜m˚ “ 0 (22) Ap´B˚

´ A˜pB˚

´ A˜pB˚

m,1qθPub

m ´ dB˚

ApB˚

m,¨qβP

m

m

m,´1qτ˜m˚ ă ´ . (23)

´ A˜p´B˚

´ A˜p´B˚

m,1qθPub

m ´ d´B˚

m,¨qβP

m

m

Since there are a finite number of possible values of Bm˚ , we can extract a subsequence m1 along which Bm˚

is constant. For simplicity of notation, we’ll denote the constant value Bm˚

1

by B˚. Similarly, Lemma A.4 implies that there is a unique element γm˚

q such that the elements of γm˚

P V pΣP

m1

1

1

in positions ´B˚ are all 0. By Lemma A.1, we can write γm˚

1

qγ¯j for cjp¨q a continuous function and γ¯j P V pIq. Since V pIq is finite, we can extract a subsequence m2 along which γm˚

“ cjpΣP

m1

1

qγ¯j˚ for a fixed j˚, which without loss of generality we normalize to j˚ “ 1. Moreover, since S is compact, we can extract a further subsequence l along which ΣP

“ cj˚pΣP

m2

2

l Ñ Σ˚. By Assumption 4, Σˆn

l Ñp Σ˚. The continuous mapping theorem then implies that γl˚ “ c1pΣP

lqγ¯1 Ñ c1pΣ˚qγ¯1, and likewise, γˆl˚ :“ c1pΣˆn

lqγ¯1 Ñp c1pΣ˚qγ¯1. From Lemma A.9, we have that

ρ˚αpPl,xq “ Φ˜ ´γl˚1A˜p¨,1qx

A1γl˚ ´ z1´α¸,

a

γl˚1AΣP

l

which combined with the convergences shown above implies that

ρ˚αpPl,xq Ñ Φ˜ ´γ¯11A˜p¨,1qx

´ z1´α¸. (24)

a

γ¯11AΣ˚A1γ¯1

Now, for the function ηp¨q defined in (21), let

?nlβˆn

###### ,A,?nld,?nlθPub

` x,Σˆn

ηˆl “ ηp

lq.

l

l

By duality, we have that

γ1 ´?nAβˆn

´ A˜p¨,1qx¯

?nld ´

###### ?nlA˜p¨,1qθPub

ηˆl “ max

l ´

l

γPV pΣˆnlq

ě γˆl˚1 ´?nAβˆn

´ A˜p¨,1qx¯.

?nld ´

###### ?nlA˜p¨,1qθPub

l ´

l

By construction, γˆl˚ has zero elements in positions ´B˚ and satisfies γˆl˚1A˜p¨,´1q “ 0. This, combined with equation (22) implies that

´ A˜p¨,1qx¯ “ γˆl˚1A?nlpβˆn

γˆl˚1 ´?nlAβˆn

?nld ´

###### ?nlA˜p¨,1qθPub

l ´

l ´ βP

l

From Assumption 2 combined with Slutsky’s lemma, we have that

lq ´ γˆl˚1A˜p¨,1qx.

lq ´ γˆl˚1A˜p¨,1qx Ñd N ´´c1pΣ˚qγ¯11A˜p¨,1qx, c1pΣ˚q2γ¯11AΣ˚A1γ¯1¯.

γˆl˚1A?nlpβˆn

l ´ βP

Now, consider γˆl,j “ cjpΣˆn

lqγ¯j for j ‰ 1. By construction γ¯j ě 0, and Lemma A.4 implies that γ¯j has a non-zero element in at least one component in B˚. But this, combined with equations (22) and (23) and the fact that cjpΣˆn

lq Ñp cjpΣ˚q ą 0, implies that

´ A˜p¨,1qx¯ Ñp ´8,

γˆl,j1 ´?nlAβP

?nld ´

###### ?nlA˜p¨,1qθPub

l ´

l

and thus

γˆl,j1 ´?nlAβˆn

´ A˜p¨,1qx¯ Ñp ´8,

?nld ´

###### ?nlA˜p¨,1qθPub

l ´

l

as well, since as before γˆl,j1 A?npβˆn

lq converges in distribution to a normal distribution with finite variance. This implies that γˆl˚ is the optimizer of the problem for ηˆl with probability approaching 1, and thus

l ´ βP

ηˆl Ñd N ´´c1pΣ˚qγ¯11A˜p¨,1qx, c1pΣ˚q2γ¯11AΣ˚A1γ¯1¯.

?nlAβˆn

?nld ´ ?nlA˜p¨,1qθPub

This also implies that for any j ‰ 1, |ηˆl ´ γˆl,j1 Y˜l| Ñp 8, where Y˜l “

l ´

´ A˜p¨,1qx. Since there are a finite number of vertices, it follows that minj‰1 |ηˆl ´ γˆl,j1 Y˜l| Ñ ´8. This together with the result of Lemma A.3 implies that |ηˆl ´ vllo| Ñp 8 and |ηˆl´vlup| Ñp 8, where vllo,vlup are the values of vlo,vup associated with the ψαCp

l

?nlβˆn

###### ,A,?nld,?nlθPub

` x,Σˆn

l

l

lq test. Since ηˆl is stochastically bounded, and by construction vllo ď ηˆl ď vlup, it follows that vllo Ñp ´8 and vlup Ñp 8. Let σˆl2 “ γ˚1,lAΣˆn

A1γ˚,l denote the variance at the optimal vertex used by the ψαCp

l

?nlβˆn

###### ,A,?nld,?nlθPub

` x,Σˆn

lq test. Since, we’ve shown that γˆl˚ is optimal w.p.a. 1, we have that σˆl2 Ñp c1pΣ˚q2γ¯11AΣ˚A1γ¯1. From another application of the continuous mapping theorem, we have that

l

l

Φpηˆl{σˆlq ´ Φpvllo{σˆlq Φpvlup{σˆlq ´ Φpvllo{σˆlq

Φpξq ´ Φp´8q Φp8q ´ Φp´8q

Ñd

“ Φpξq,

where ξ „ N ´´γ¯11A˜p¨,1qx{a

γ¯11AΣ˚Aγ¯1, 1¯. The limiting distribution is continuous, and thus

ą 1 ´ α˙ Ñ P pΦpξq ą 1 ´ αq “ Φ˜ ´γ¯1A˜p¨,1qx ?γ¯1AΣ˚A1γ¯1 ´ z1´α¸.

ˆ

Φpηˆl{σˆlq ´ Φpvllo{σˆlq Φpvlup{σˆlq ´ Φpvllo{σˆlq

PP

l

Moreover, for α ă 0.5, zlo sufficiently small, and zup sufficiently large, pΦpηˆlq´Φpzloqq{pΦpzupq´ Φpzloqq ą 1 ´ α only if ηˆl ą 0. It follows that

ą 1 ´ α,ηˆl ą 0˙ Ñ Φ˜ ´γ¯1A˜p¨,1qx ?γ¯1AΣ˚A1γ¯1 ´ z1´α¸.

ˆ

Φpηˆl{σˆlq ´ Φpvllo{σˆlq Φpvlup{σˆlq ´ Φpvllo{σˆlq

PP

l

?nlβˆl,A,?nld,?nlθPub` x,Σˆn

However, the event in the previous display is precisely the event that ψαCp

lq “ 1, and thus

lqı Ñ Φ˜ ´γ¯1A˜p¨,1qx

?γ¯1AΣ˚A1γ¯1 ´ z1´α¸. The result is then immediate from the previous display combined with (24).

”ψαCp

?nlβˆl,A,?nld,?nlθPub ` x,Σˆn

EP

l

| |
|---|


- Lemma A.4. If LICQ holds in direction l at βP, then there exists a unique γ¯ P V pΣPq such that γ¯´B˚ “ 0, where B˚ is the set of binding moments at the optimum to (16).


Proof. We first show that there is at most one such γ¯. By definition, any vertex γ P V pΣPq satisfies γ1A˜p¨,´1q “ 0. Recall that A˜ “ Ap¨,postqΓ´1, where Γ is full rank. LICQ implies that ApB˚,postq has full row rank, and thus so does A˜pB˚,¨q. It follows that A˜pB˚,´1q has rank at

A˜pB˚,´1q “ 0, and thus there are no vertices with γ´B˚ “ 0. If the rank is |B˚| ´ 1, then any solution to γ1A˜p¨,´1q “ 0 with γ´B˚ “ 0 takes the form γB˚ “ c ¨ ν for some constant c and ν a vector the generates the one-dimensional nullspace of A˜pB˚,´1q. However, any γ P V pΣPq also must satisfy γ1σ˜ “ 1, which uniquely pins down the constant c. Thus, there is at most one element of the feasible set with γ´B˚ “ 0.

least |B˚| ´ 1. If the rank is |B˚|, then there are no non-zero solutions to γB1 ˚

We next show that there exists such a γ¯. Consider the optimization ηpβP,A,d,θPub,ΣPq for ηp¨q defined in (21). As argued in the proof to Proposition 3.2, since θPub is on the boundary of the identified set, we must have ηpβP,A,d,θPub,ΣPq “ 0. However, LICQ implies that there exists a value τ˜˚ such that

ApB˚,¨qβP ´ dB˚ ´ A˜pB˚,1qθPub ´ A˜pB˚,´1qτ˜˚ “ 0 Ap´B˚,¨qβP ´ d´B˚ ´ A˜p´B˚,1qθPub ´ A˜p´B˚,1qτ˜˚ ă 0.

In particular, this holds for τ˜˚ “ Γp´1,¨qτ˚. It follows that pη,τ˜q “ p0,τ˜˚q is a solution to ηpβP,A,d,θPub,ΣPq. By duality, there is some γ¯ P V pΣPq that is a Lagrange multiplier for this optimization problem. The complementary slackness conditions imply, however, that γ¯´B˚ “ 0, as needed.

| |
|---|


- Lemma A.5. Suppose βˆ „ N pβ, Σq for Σ known. Let B0 be a closed, convex set. Then the most-powerful size α test of H0 : β P B0 against the point alternative HA : β “ βA is equivalent to the most powerful test of H0 : β “ β˜ against HA : β “ βA, where β˜ “

arg minβPB

0

||β´βA||Σ and ||¨||Σ is the Mahalanobis norm in Σ, ||x||Σ “

?

x1Σ´1x. The most powerful test rejects for values of pβA´β˜q1Σ´1βˆ greater than pβA´β˜q1Σ´1β˜`z1´α||βA´β˜||Σ, and has power against the alternative of Φp||βA ´ β˜||Σ ´ z1´αq, for z1´α the 1 ´ α quantile of the standard normal.

Proof. Define ă ¨,¨ ąΣ by ă x,y ąΣ“ x1Σ´1y, and observe that ă ¨,¨ ąΣ is an inner product. The result then follows immediately from the discussion in Section 2.4.3 of Ingster and Suslina (2003), replacing all instances of the usual euclidean inner product with ă ¨,¨ ąΣ.

| |
|---|


- Lemma A.6. Let B be a closed, convex subset of RK, and βA R B. Let β˜ “ arg minβPB ||β ´ βA||Σ, where ||x||2Σ “ x1Σ´1x for some positive definite matrix Σ. Then for any β P B, pβ˜ ´ βAq1Σ´1pβ ´ β˜q ě 0. Proof. Consider any β P B. Define βθ “ θpβ ´β˜q`β˜, and note that since B is convex βθ P B


for any θ P r0,1s. Further,

||βθ ´ βA||2Σ “ θ2||β ´ β˜||2Σ ` 2θpβ˜ ´ βAq1Σ´1pβ ´ β˜q ` ||β˜ ´ βA||2Σ.

Differentiating with respect to θ, we have

B Bθ||βθ ´ βA||2Σ “ 2θ||β ´ β˜||2Σ ` 2pβ˜ ´ βAq1Σ´1pβ ´ β˜q,

from which we see that the derivative evaluated at θ “ 0 is 2pβ˜ ´ βAq1Σ´1pβA ´ β˜q. Since β˜ minimizes the norm, it follows that we must have 2pβ˜ ´ βAq1Σ´1pβA ´ β˜q ě 0, else we could achieve a lower value of the norm at βθ by choosing θ ą 0 sufficiently small.

| |
|---|


- Lemma A.7. Let B “ tβ P RK : v1β ď du for some v P RKzt0u and d P R. Let

β˜ “ arg minβPB ||β ´βA||Σ for some βA R B, where ||x||2Σ “ x1Σ´1x and Σ is positive definite. Then pβA ´ β˜q1Σ´1 “ c ¨ v1 for the positive constant c “ v

1βA´d

v1Σv .

Proof. Note that we can form a basis v,v˜2,...,v˜K such that v1v˜j “ 0 for j “ 2,...,K. It follows by construction that for any j “ 2,..,K and any t P R, β˜ ` t ¨ v˜j P B. Hence, from Lemma A.6, ´pβA ´ β˜q1Σ´1ptv˜jq ě 0. Since we can choose t both positive and negative, it follows that pβA´β˜q1Σ´1v˜j “ 0 for all j. Since pβA´β˜q1Σ´1 is orthogonal to tv˜2,...,v˜Ku, and tv,v˜2,...,v˜Ku form a basis, we have that pβA ´ β˜q1Σ´1 “ c ¨ v1, for some c P R. Multiplying both sides of the equation on the right by Σv, we obtain that pβA ´β˜q1v “ c¨v1Σv. However, since β˜ is the closest point to βA in Mahalanobis distance, it must be on the boundary of B, and so v1β˜ “ d. It follows that c “ pv1βA ´ dq{pv1Σvq, which is clearly positive since βA R B and thus v1βA ą d.

| |
|---|


- Lemma A.8 (Power of optimal test for linear subspace). Let B “ tβ P RK : v1β ď du for some v P RKzt0u and d P R. Suppose βˆ „ N pβ, Σq for Σ positive definite known, and consider the problem of testing H0 : β P B against HA : β “ βA for some βA R B. Then the most powerful size-α test of H0 against HA is a one-sided t-test that rejects for large values


?

of v1βˆ, and has power equal to Φppv1βA ´ dq{

v1Σv ´ z1´αq.

Proof. From Lemma A.5, the most powerful test rejects for large values of pβA ´ β˜q1Σ´1βˆ, where β˜ “ arg minβPB ||β ´ βA||Σ, and has power Φp||βA ´ β˜||Σ ´ z1´αq. By Lemma A.7, pβA ´ β˜q1Σ´1 “ cv1, for c “ pv1βA ´ dq{pv1Σvq. It follows that

||βA ´ β˜||2Σ “ pβA ´ β˜q1Σ´1pβA ´ β˜q “ cv1pβA ´ β˜q “ cpv1βA ´ dq “ pv1βA ´ dq2{pv1Σvq,

where we use the fact that v1β˜ “ d, since β˜ must be on the boundary of B, as argued in the proof to Lemma A.7. The result then follows immediately.

| |
|---|


- Lemma A.9. If P P P , then ρ˚αpP,xq “ Φ˜ ´γ¯1A˜p¨,1qx ?γ¯1AΣPA1γ¯ ´ z1´α¸, where γ¯ P V pΣPq is the


unique element of V pΣPq with γ¯´B˚ “ 0 (see Lemma A.4). Proof. Suppose βˆn „ N pβP, ΣP{nq. Let Bn “ tβ : θPub`x{

?n P Spβ,∆qu be the set of values for β consistent with the null that θ “ θPub ` x{

?n. Observe that Bn “ tβ : ηpβ,A,d,θub ` x{

?n,ΣPq ď 0u, where ηp¨q is defined in (21). From Lemma A.5, the most powerful test of

H0 : β P Bn against H1 : β “ βP rejects for large values of pβP ´ β˜q1Σ´P1βˆn. To derive the optimal test, it is instructive to first consider a simpler testing problem. From Lemma A.4,

there exists a unique γ¯ P V pΣPq such that γ¯´B˚ “ 0, where B˚ are the binding rows at the solution to (16) satisfying LICQ. Define Bnγ¯ “ tβ : γ¯1pAβ ´d´A˜p¨,1qpθPub `x{

?nqq ď 0u. We first consider testing H˜0 : β P Bnγ¯ against H1 : β “ βP. From Lemma A.7, the optimal test rejects for large values of γ¯1Aβˆn and has power Φp? h

´ z1´αq, where

γ¯1AΣP A1γ¯{n

?nqq. (25)

h “ γ¯1pAβP ´ d ´ A˜p¨,1qpθPub ` x{

From the definition of LICQ in direction l, however, there exists a value τ˜˚ such that

ApB˚,¨qβP ´ dB˚ ´ A˜pB,1qθPub ´ A˜pB,´1qτ˜˚ “ 0 (26) Ap´B˚,¨qβP ´ d´B˚ ´ A˜p´B,1qθPub ´ A˜p´B,1qτ˜˚ ă 0 (27)

By construction, γ¯1A˜p¨,´1q “ 0 and γ¯´B˚ “ 0, which combined with the previous two displays implies that h “ ´γ¯1A˜p¨,1qx{

?n, and hence the power of the optimal test of H˜0 is Φ˜ ´γ¯1A˜p¨,1qx

?γ¯1AΣPA1γ¯ ´ z1´α¸.

To complete the proof, it thus suffices to show that the optimal test of H˜0 against H1 is the same as the optimal test of H0 against H1 for n sufficiently large. To this end, note that Bn Ď Bnγ¯, since by duality,

?nqq ě γ¯1pAβ´d´A˜p¨,1qpθPub`x{

?nqq.

?n,ΣPq “ max

γ1pAβ´d´A˜p¨,1qpθPub`x{

ηpβ,A,d,θub`x{

γPV pΣP q

Thus, Lemma A.5 implies that the optimal test under H0 coincides with the optimal test under H1 whenever β˜n “ arg minβPBγ¯

||β ´ βP||ΣP{n is in Bn. From Lemma A.7, however, β˜n1 “ βP1 ` ? h

?n

n

v1pΣP{nq, for h defined in (25). Using the equality h “ ´γ¯1A˜p¨,1qx{

γ¯1AΣP A1γ¯{n

derived above, we see that

β˜n1 “ βP1 ´

γ¯1A˜p¨,1qx ?γ¯1AΣPA1γ¯

1 ?n

γ¯1AΣP,

?n for a finite vector ν. From Lemma A.4, every γ P V pΣPq with γ ‰ γ¯ has γ´B˚ ‰ 0. Since γ ě 0 by construction, equations (26) and (27) imply that

and thus we can write β˜ “ βP ´ ν{

γ1pAβP ´ d ´ A˜p¨,1qθPubq ă 0

for all γ ‰ γ¯, where we use the fact that γ1A˜p¨,´1q “ 0 by construction. We’ve shown, however, that γ¯1pAβP ´ d ´ A˜p¨,1qθPubq “ 0. By continuity arguments, it follows that for n sufficiently large,

?n,ΣPq “ max

ηpβ,A,d,θ˜ Pub ` x{

γPV pΣP q

?nq ´ d ´ A˜p¨,1qpθPub ` x{

?nqq

γ1pApβP ´ ν{

is equal to

?nqq, and thus β˜n P Bn, as we wished to show.

?n ´ d ´ A˜p¨,1qpθPub ` x{

γ¯1pApβP ´ ν{

| |
|---|


#### A.3 Proofs and auxiliary lemmas for FLCIs

###### Proof of Proposition 4.2

˘ Ñ

`pθub ` xq P Cα,nFLCI

Proof. First, suppose Assumption 9 holds. Without loss of generality, we show P

- 0 for any x ą 0. By Lemma A.11 there exists pa,¯ v¯q such that ¯bpa,¯ v¯q “ 12LIDpδpre,∆q “: ¯bmin


”a¯ ` v¯1βˆnı “ 12pθub `θlbq “: θmid. Let C¯n :“ a¯`v¯1βˆn ˘χnpa,¯ v¯q denote the fixed length confidence interval based on pa,¯ v¯q.

and Eβˆ

n„Npδ`τ, Σnq

˘| distribution. Since σv,n¯2 “ n1σv,¯2 1 Ñ 0, the |N `

By construction, χ¯n :“ χnpa,¯ v¯q is the 1 ´ α quantile of the |N `

¯bmin, σv,n¯2

˘| distribution collapses to a point mass at ¯bmin, and thus χ¯n Ñ ¯bmin. By construction, the half-length of the shortest FLCI χn :“ χnpan,vnq must be less than or equal to χ¯n, and so limsupnÑ8 χn ď ¯bmin. Let bn :“ ¯bpan,vnq be the worst-case bias of the optimal FLCI. Since α P p0,0.5s, Lemma A.12 implies that χn ě bn. Additionally, Lemma A.10 implies that bn ě 12LIDpδpre,∆q “ ¯bmin, and thus χn ě ¯bmin. Hence, χn Ñ ¯bmin implies bn Ñ ¯bmin. Additionally, note that for α P p0,0.5s, χnpa,vq is increasing in both ¯bpa,vq and σv,n. Since ¯bmin ď bn and χn ď χ¯n, it must be that σv

¯bmin, σv,n¯2

n,n ď σv,n¯ , from which it follows that σv

n,n Ñ 0.

”an ` vn1 βˆnı converges to θmid :“ 12pθub ` θlbq. To show this, note that µn “ an ` vn1 β for β “ δ ` τ. Since θub,θlb P Spβ,∆q, by the definition of the identified set there exist δub,δlb P ∆ and τub,τlb such that β “ δub ` τub “ δlb ` τlb, θub “ l1τpostub , and θlb “ l1τpostlb . Thus, θub ´ Eβˆ

Now, we claim that µn :“ Eβˆ

n„Npδ`τ, Σnq

”an ` vn1 βˆnı “ θub ´ µn and Eβˆ

n„Npβ, Σnq

”an ` vn1 βˆnı ´ θlb “ µn ´ θlb. This implies that bn ě maxtθub ´ µn,µn ´ θlbu “ ¯bmin ` |µn ´ θmid|, where the equality uses the fact that θub ´ θlb “ LIDpδA,pre,∆q “ 2¯bmin. Since we’ve shown that bn Ñ ¯bmin, it follows that µn Ñ θmid, as desired.

n„Npβ, Σnq

˘

Next, note that if βˆn „ N pδ ` τ, Σnq, then an ` vn1 βˆn „ N `

. Observe that θ¯ P Cα,nFLCI if and only if an ` vn1 βˆn P rθ¯´ χn,θ¯` χns. Thus,

µn, σv2

n,n

˘ “ Φˆθ¯` χn ´ µn

˙ ´ Φˆθ¯´ χn ´ µn

˙.

n„Npβ,Σnq `

θ¯ P Cα,nFLCI

Pβˆ

σv

σv

n,n

n,n

˘ equals

n„Npβ,Σnq `pθub ` xq P Cα,nFLCI

Now, recalling that θub “ θmid`¯bmin by construction, we have Pβˆ

Φˆ

˙. (28) Note that the term inside the second normal CDF in the previous display equals

˙ ´ Φˆ

θmid ` ¯bmin ` x ` χn ´ µn σv

θmid ` ¯bmin ` x ´ χn ´ µn σv

n,n

n,n

χn ´ bn σv

´

`

n,n

x ` θmid ´ µn ` ¯bmin ´ bn σv

.

n,n

However, the first summand above is bounded between ´z1´α{2 and ´z1´α by Lemma A.12. Additionally, we’ve shown that θmid ´ µn Ñ 0 and ¯bmin ´ bn Ñ 0, so the numerator of the second summand converges to x ą 0. Since the denominator σv

n,n Ñ 0, the expression in the previous display diverges to 8, and hence the second normal CDF term in (28) converges to

`pθub ` xq P Cα,nFLCI

˘ Ñ 0, as needed.

- 1, which implies that P


In order to prove the other direction, we proceed via the contrapositive. Towards this, suppose Assumption 9 fails. Let L :“ LIDpδpre,∆q and L¯ :“ supδ˜

preP∆pre LIDpδ˜pre,∆q. By

- Lemma A.10, bn :“ ¯bpan,vnq ě 12L¯ “: ¯bmin. As argued earlier in the proof, since α P p0,.5s,


χn ě bn ě 12L¯. If L¯ “ 8, then Cα,nFLCI is the real line, and thus never rejects, so Cα,nFLCI is trivially inconsistent under the assumption that Spδ ` τ,∆q ‰ R. For the remainder of the proof, we assume L ă L¯ ă 8. From Lemma 2.1, Spδ ` τ,∆q “ rθlb,θubs, where θub ´ θlb “ LIDpδpre,∆q “ L. Let “ 14pL¯ ´ Lq, and set θ1out :“ θub ` and θ2out :“ θlb ´ . Let θmid “ 12pθub ` θlbq be the midpoint of the identified set. By construction, θ1out ´ θmid “ θmid ´ θ2out “ 12L ` ă 12L¯. Since Cα,nFLCI is an interval with half-length at least 12L¯, it follows that if θmid P Cα,nFLCI then at least one of θ1out,θ2out is also in Cα,nFLCI. Hence, P

˘` P

`

θ1out P Cα,nFLCI

`

˘ ě P

`

˘ ě 1 ´ α, where the final bound follows since Cα,nFLCI

θ2out P Cα,nFLCI

θmid P Cα,nFLCI

˘ ě 12p1 ´ αq ą 0 for at least one j P t1,2u.

`

satisfies the coverage requirement (10). It follows that limsupnÑ8 P

θjout P Cα,nFLCI

| |
|---|


- Lemma A.10 (Bounds for worst-case bias). For any pa,vq, ¯bpa,vq ě 12 supδ

preP∆pre LIDpδpre,∆q.

Proof. Since β “ δ ` τ, we can write the bias of the affine estimator a ` v1βˆ as b “ a ` v1δ ` pvpost ´ lq1τpost. Since τpost is unrestricted in the maximization in (17), we see that the worst-case bias will be infinite if vpost ‰ l and the lemma holds trivially. We can thus restrict attention to affine estimators with vpost “ l, in which case the worst-case bias reduces to

¯bpa,vq “ sup

δP∆

|a ` v1δ| “ sup

δP∆

|a ` vpre1 δpre ` l1δpost|. (29)

Now, pick any δpre˚ P ∆pre. First, suppose that the minimum

`

minδ l1δpost, s.t. δ P ∆,δpre “ δpre˚

˘ and the maximum

`

maxδ l1δpost, s.t. δ P ∆,δpre “ δpre˚

˘

are finite. Let δmin and δmax be the

associated solutions. By construction, δpremax “ δpremin “ δpre˚ . For any vpre, we can apply the triangle inequality to show that

ˇa ` vpre1 δpremax ` l1δpostmaxˇ ` ˇa ` vpre1 δpremin ` l1δpostminˇ ě ˇ

`

a ` vpre1 δpremax ` l1δpostmax

˘ ´ `

a ` vpre1 δpremin ` l1δpostmin

˘

ˇ “ |l1δpostmax ´ l1δpostmin| “ LIDpδpre˚ ,∆q.

Note that for any x1,x2 ě 0, maxtx1,x2u ě 12px1 ` x2q. It then follows from the previous display that

maxtˇa ` vpre1 δpremax ` l1δpostmaxˇ,ˇa ` vpre1 δpremin ` l1δpostminˇu ě

- 1

- 2


LIDpδpre˚ ,∆q.

Since δpremax and δpremin are feasible in the maximization (29), we see that ¯b ě 21LIDpδpre˚ ,∆q, as needed. To complete the proof, now suppose without loss of generality that

´max

δ

l1δpost, s.t. δ P ∆,δpre “ δpre˚ ¯ “ 8.

Then, we can replay the argument above replacing δmax with a sequence of values tδju such that l1δj diverges, which gives that ¯b is infinite and the result follows.

| |
|---|


- Lemma A.11. Suppose ∆ is convex, and there exists δ P ∆ such that LIDpδpre,∆q “


preP∆pre LIDpδ˜pre,∆q ă 8. Then there exists pa,vq such that ¯bpa,vq “ 12 supδ˜

preP∆pre LIDpδ˜pre,∆q. Additionally, for any τ and Σn, Eβˆ

supδ˜

”a ` v1βˆnı “ 21pθub ` θlbq, where θub and θlb are the upper and lower bounds of the identified set Spδ ` τ,∆q.

n„Npδ`τ, Σnq

Proof. Let bmaxpδpre˚ q :“ ´maxδ˜l1δ˜post, s.t. δ˜ P ∆,δ˜pre “ δpre˚ ¯, where we define bmax “ ´8 if δpre˚ R ∆pre. Likewise, define bminpδpre˚ q :“ ´minδ˜l1δ˜post, s.t. δ˜ P ∆,δ˜pre “ δpre˚ ¯, where

we define bmin “ 8 if δpre˚ R ∆pre. Note that ∆ convex implies that bmax is concave and bmin is convex. Thus, ´LIDpδpre˚ q “ bminpδpre˚ q ´ bmaxpδpre˚ q is convex (where we define LIDpδpre˚ q “ ´8 if δpre˚ R ∆pre). The domain of ´LIDpδpre˚ q (i.e. the set of values for which it is finite) is ∆pre, since it is infinite for δpre˚ R ∆pre by construction, and by assumption, LIDpδpre˚ q is finite for all δpre˚ P ∆pre. Since ∆ is assumed to be convex, ∆pre is a nonempty convex set, and thus has non-empty relative interior, so the relative interior of the domain of ´LID is non-empty.37 It follows from Theorem 8.2 in Mau Nam (2019) that Bp´LIDq “ Bp´bmaxq ` Bpbminq where for a convex function f, Bf is the subdifferential Bfpx¯q :“ tv : fpx¯q ` v1px ´ x¯q ď fpxq,@xu and Bp´bmaxq ` Bpbminq is the Minkowski sum of the two subdifferentials.

preP∆pre ´LIDpδ˜preq.

preP∆pre LIDpδ˜preq, then ´LIDpδpreq “ infδ˜

Additionally, if LIDpδpreq “ supδ˜

Thus, standard results in convex analysis (see, e.g., Theorem 16.2 in Mau Nam (2019)) give that 0 P Bp´LIDqpδpreq`Np∆;δpreq, where Np∆;δpreq “ tvpre : vpre1 pδ˜pre ´δpreq ď 0,@δ˜pre P ∆preu is the normal cone to ∆pre at δpre. Hence, there exist vectors v¯min,v¯max such that for all δ˜pre P ∆pre,

bminpδpreq ` v¯min1 pδ˜pre ´ δpreq ď bminpδ˜preq (30) ´ bmaxpδpreq ` v¯max1 pδ˜pre ´ δpreq ď ´bmaxpδ˜preq (31) ´ pv¯min ` v¯maxq1pδ˜pre ´ δpreq ď 0. (32)

The inequalities (31) and (32) together imply that for all δ˜pre P ∆pre,

bmaxpδpreq ` v¯min1 pδ˜pre ´ δpreq ě bmaxpδ˜preq. (33) Now, let v be the vector such that vpost “ l and vpre “ ´v¯min. Observe that

ˆa ` vpre1 δ˜pre ` max

l1δ¯post˙ “ max

a ` vpre1 δ˜pre ` l1δ˜post “ max

max

δ˜P∆

δ˜preP∆pre

δ¯P∆,δ¯pre“δ˜pre

a ` vpre1 δ˜pre ` bmaxpδ˜preq

δ˜preP∆pre

ď a ` vpre1 δpre ` bmaxpδpreq, (34)

where the first equality nests the maximization, the second equality uses the definition of

37The relative interior of a set is the interior of the set relative to its affine hull. See, e.g., Mau Nam

(2019), Chapter 5.

bmax, and the inequality follows from (33). An analogous argument using (30) yields that

a ` vpre1 δ˜pre ` bminpδ˜preq

a ` vpre1 δ˜pre ` l1δ˜post “ min

min

δ˜preP∆pre

δ˜P∆

ě a ` vpre1 δpre ` bminpδpreq. (35)

Now, it is apparent from equation (29) that

*, (36)

¯bpa,vq “ max"

a ` vpre1 δ˜pre ` l1δ˜postˇ

a ` vpre1 δ˜pre ` l1δ˜postˇ ,ˇmin

ˇmax

δ˜P∆

δ˜P∆

which is bounded above by max a ` vpre1 δpre ` bmaxpδpreq,´pa ` vpre1 δpre ` bminpδpreq˘u from the results above. Setting a “ ´vpre1 δpre ´ 21pbmaxpδpreq ` bminpδpreqq, this upper bound reduces to 12pbmaxpδpreq ´ bminpδpreqq. Since LIDpδpre,∆q “ bmaxpδpreq ´ bminpδpreq and LIDpδpre,∆q “ supδ˜

preP∆pre LIDpδ˜pre,∆q by assumption, it is then immediate that ¯b ď preP∆pre LIDpδ˜pre,∆q. The inequality in the opposite direction follows from Lemma

- 1

- 2 supδ˜


- A.10. Finally, substituting in the definition of a and v above and simplifying, we see that


”a ` v1βˆnı “ l1βpost ´ 21pbmaxpδpreq ` bminpδpreqq, which from (5) and (6) we see is the midpoint of the identified set.

Eβˆ

n„Npδ`τ, Σnq

| |
|---|


- Lemma A.12. Let χα be the 1 ´ α quantile of the |N pb, σ2q| distribution for b ě 0. Then b ` σz1´α ď χα ď b ` σz1´α{2.


Proof. Since |ξ| ě ξ, we have that q1´αp|ξ||ξ „ N pb, σ2qq ě q1´αpξ |ξ „ N pb, σ2qq “ b ` σz1´α, which yields the first inequality. For the second inequality, observe that

q1´αp|ξ||ξ „ N `

˘q “ q1´αp|ξ ` b||ξ „ N `

b, σ2

0, σ2 q ď b ` q1´αp|ξ||ξ „ N `

˘q “ b ` σz1´α{2

0, σ2

where the first inequality uses the triangle inequality, and the final equality uses the fact that a mean-zero normal distribution is symmetric about 0.

| |
|---|


## B Additional Simulation Results

This section contains additional simulation results that complement the simulations presented in the main text. Section B.1 describes the computation of the optimal bound for expected excess length. Section B.2 contains additional results from the normal data-generating process considered in the main text. Section B.3 presents results from a non-normal datagenerating process in which the covariance matrix is estimated from the data, which show

that our proposed procedures have (approximate) size control, with similar power curves to those in the normal simulations.

#### B.1 Optimal bounds on excess length

We now discuss the computation of optimal bounds on the excess length of confidence intervals that satisfy the uniform coverage requirement (10). In Section 5, we benchmark the performance of our proposed procedures in Monte Carlo simulations relative to these bounds.

The following result restates Theorem 3.2 of Armstrong and Kolesár (2018) in the notation of our paper, which provides a formula for the optimal expected length of a confidence set that satisfies the uniform coverage requirement.

- Lemma B.1. Suppose that ∆ is convex. Let Iα denote the set of confidence sets that satisfy the coverage requirement (10). Then, for any δ˚ P ∆, τpost˚ P RT¯, and Σn positive definite,


n„Npδ˚`Lpostτ˚,Σnq rλpCqs “ p1 ´ αqErω¯pz1´α ´ Zq ´ ¯

Eβˆ

ωpz1´α ´ Zq|Z ă z1´αs,

inf

CPIα

where Z „ N p0, 1q, z1´α is the 1 ´ α quantile of Z, and

ω¯pbq :“ suptl1τ |τ P RT¯,Dδ P ∆ s.t. }δ ` Lpostτ ´ β˚}2Σn ď b2u ¯ ωpbq :“ inftl1τ |τ P RT¯,Dδ P ∆ s.t. }δ ` Lpostτ ´ β˚}2Σn ď b2u,

for β˚ :“ δ˚ ` Lpostτpost˚ , and ||x||Σ “ x1Σ´1x.

The proof of this result follows from observing that the confidence set that optimally directs power against pδ˚,τpost˚ q inverts Neyman-Pearson tests of H0 : δ P ∆,θ “ θ¯ against HA : pδ,τpostq “ pδ˚,τpost˚ q for each value θ¯. The formulas above are then obtained by integrating one minus the power function of these tests over θ¯. By the same argument, the optimal excess length for confidence sets that control size is the integral of one minus the power function over all points θ¯ outside of the identified set. Additionally, for any value θ¯ P Spβ,∆q, the null and alternative hypotheses are observationally equivalent, and so the most powerful test trivially has size α. It follows that the lowest achievable expected excess length is p1 ´ αq ¨ LIDpδpre˚ ,∆q shorter than the lowest achievable expected length, where as in Section 4, LID denotes the length of the identified set.

Corollary B.1. Under the conditions of Lemma B.1,

inf

CPIα

n„Npβ˚,Σnq rELpC;β˚qs “ inf

Eβˆ

CPIα

n„Npβ˚,Σnq rλpCqs ´ p1 ´ αqLIDpβ˚,∆q,

Eβˆ

where ELpC;βq “ λpCzSpβ,∆qq is the excess length of the confidence set C, i.e. the length of the part of the confidence set that falls outside of the identified set.

Recall that when ∆ is the union of polyhedra (∆ “ ŤK

k“1 ∆k), the identified set is the union of the identified sets for each of the ∆k. Thus, any Cα that satisfies (10) for ∆ must also satisfy (10) for each ∆k. It follows that the expected excess length for C is bounded below by the optimal excess length for confidence sets satisfying (10) for ∆k for each k. For ∆s that are unions of polyhedra, we therefore use the largest lower bound implied by the individual ∆k, which is a potentially non-sharp lower bound on the excess length of a procedure that satisfies (10) for ∆.

#### B.2 Additional Results for Normal Simulations

In the main text, we report efficiency in terms of excess length for the parameter θ “ τ1 for ∆SDpMq, ∆SDPBpMq, ∆SDRMpM¯ q and ∆RMpM¯ q. In this section, we provide additional simulation results.

Alternative choices of M¯ for ∆SDRMpM¯ q and ∆RMpM¯ q. The main text reports efficiency in terms of excess length over ∆SDRMpM¯ q and ∆RMpM¯ q for M¯ “ 1. We now report additional results for M¯ “ 1,2,3. The results are qualitatively similarly, suggesting that the choice of M¯ does not appear to have a large effect on the performance of our proposed procedures.

Alternative choice of target parameter. The main text reports efficiency in terms of excess length for the parameter θ “ τ1. We now report additional results using the average of post-period treatment effects, θ “ τ¯post, as the target parameter.

- Figure I2 plots the efficiency results for θ “ τ¯post over ∆SDpMq and ∆SDPBpMq. As in the main text, we conduct these simulations under the assumption of parallel trends and zero treatment effects (i.e., β “ 0), reporting results as M{σ1 varies.
- Figure I3 plots the efficiency results for θ “ τ¯post over ∆SDRMpM¯ q and ∆RMpM¯ q. As in the main text, we conduct these simulations under the assumption of zero treatment effects and a “pulse” pre-trend (i.e., β´1 “ δ´1 and βt “ 0 for all t ‰ ´1), reporting results for M¯ “ 1 over δ´1{σ1 “ 0,1,2,3.38


38We note that over ∆SDRMpM¯ q the median efficiency ratio for our proposed confidence sets is larger than one for M¯ “ 3. For M¯ “ 3, the length of the identified set for θ “ τ¯post can be quite large when there are many post-treatment periods (e.g., as mentioned in the main text, 5 papers in the survey have T¯ ą 10), and so this behavior occurs due to computational constraints on the grid size for the underlying test inversion.

###### Figure I1: ∆SDRMpM¯ q and ∆RMpM¯ q: Median efficiency ratios for proposed procedures when θ “ τ1 as M¯ varies.

![image 11](<hpt-draft_images/imageFile11.png>)

![image 12](<hpt-draft_images/imageFile12.png>)

Note: This figure shows the median efficiency ratio for our proposed confidence sets for θ “ τ1 over ∆SDRMpM¯ q, ∆RMpM¯ q and M¯ “ 1,2,3. The efficiency ratio for a procedure is defined as the excess length bound divided by the procedure’s expected excess length. The results for M¯ “ 1 are plotted in red, M¯ “ 2 are plotted in blue, and M¯ “ 3 are plotted in green. The results for the conditional-least favorable hybrid confidence set (“C-LF Hybrid”) are plotted in the solid line with circles. The results for the conditional confidence set are plotted in the dashed line with triangles. Results are averaged over 1000 simulations for each of the 12 papers surveyed, and the median across papers is reported here.

###### Figure I2: Median efficiency ratios for ∆SDpMq and ∆SDPBpMq when θ “ τ¯post.

![image 13](<hpt-draft_images/imageFile13.png>)

![image 14](<hpt-draft_images/imageFile14.png>)

Note: This figure shows the median efficiency ratios for our proposed confidence sets for ∆SDpMq and ∆SDPBpMq when θ “ τ¯post. The efficiency ratio for a procedure is defined as the optimal bound divided by the procedure’s expected excess length. The results for the FLCI are plotted in purple, the results for the conditional-LF (“C-LF Hybrid”) in blue, and the results for the conditional confidence set are in green. Results are averaged over 1000 simulations for each of the 12 papers surveyed, and the median across papers is reported here.

###### Figure I3: Median efficiency ratios for ∆SDRMpM¯ q and ∆RMpM¯ q when θ “ τ¯post.

![image 15](<hpt-draft_images/imageFile15.png>)

![image 16](<hpt-draft_images/imageFile16.png>)

Note: This figure shows the median efficiency ratios for our proposed confidence sets for ∆SDRMpM¯ q and ∆RMpM¯ q when θ “ τ¯post and M¯ “ 1. The efficiency ratio for a procedure is defined as the optimal bound divided by the procedure’s expected excess length. The results for the conditional-least favorable (“C-LF”) hybrid in blue and the results for the conditional confidence set in green. Results are averaged over 1000 simulations for each of the 12 papers surveyed, and the median across papers is reported here.

#### B.3 Non-normal simulation results with estimated covariance matrix

In the main text, we presented simulations results where βˆ is normally distributed and its covariance matrix is treated as known. In this section, we present Monte Carlo results using

- a data-generating process in which βˆ is not normally distributed and the covariance matrix is estimated from the data. Specifically, we consider simulations based on the empirical distribution in Bailey and Goodman-Bacon (2015). We find that all of our procedures achieve (approximate) size control, and our results on the relative power of the various procedures are quite similar to those presented in the main text.

- B.3.1 Simulation design


The simulations are calibrated using the empirical distribution of the data in Bailey and Goodman-Bacon (2015).39 Let βˆ, Σˆ denote the original, estimated event-study coefficients and variance-covariance matrix from the event-study regression in the paper. We simulate data using a clustered bootstrap sampling scheme at the county level (i.e. the level of clustering used by the authors in their event-study regression). For each bootstrap sample

- b, we re-estimate the event-study coefficients βˆb and the variance-covariance matrix Σˆb also using the clustering scheme specified by the authors. We then re-center the bootstrapped coefficient so that under our simulated data-generating process either parallel trends holds


(i.e., βˆbcentered “ βˆb´βˆ) or the “pulse” pre-trend holds (i.e., βˆbcentered “ βˆb´βˆ`δ´1˚e´1 where e´1 is the (

T ` T¯)-dimensional vector with one in t “ ´1 entry and zeroes everywhere else). We construct our proposed confidence sets for bootstrap draw b using the pair pβˆbcentered,Σˆbq.

¯

As in the main text, we focus on the performance of our proposed confidence sets for ∆SDpMq, ∆SDPBpMq under parallel trends and ∆SDRMpM¯ q, ∆RMpM¯ q under the “pulse” pre-trend. The parameter of interest in these simulations is the causal effect in the first postperiod (θ “ τ1). For ∆SDpMq and ∆SDPBpMq, we report the performance of the FLCI, conditional confidence set, and conditional-least favorable confidence set. For ∆SDRMpM¯ q and ∆RMpM¯ q, we report the performance of the conditional confidence set and the conditionalleast favorable confidence set. All results are averaged over 1000 bootstrap samples.

39Since implementing the bootstrap in practice is logistically challenging, we do so for one paper rather than the full 12 papers in the survey. We chose the first paper alphabetically to minimize concerns about cherry-picking.

###### B.3.2 Size control simulations

Table 2 reports the maximum rejection rate of each procedure over a grid of parameter values θ within the identified set Spβ,∆q for ∆ “ ∆SDpMq and ∆ “ ∆SDPBpMq under parallel trends (i.e., β “ 0). We report results for M{σ1 “ 0,1,2,3,4,5. The table shows that all our procedures approximately control size, with null rejection rates not exceeding 0.08.

∆ M{σ1 Conditional FLCI C-LF Hybrid ∆SDpMq

- 0 0.073 0.078 0.069
- 1 0.046 0.061 0.044
- 2 0.038 0.072 0.037
- 3 0.040 0.072 0.038
- 4 0.049 0.072 0.045
- 5 0.059 0.072 0.051


∆SDPBpMq

- 0 0.079 0.078 0.074
- 1 0.052 0.047 0.048
- 2 0.046 0.055 0.042
- 3 0.051 0.058 0.046
- 4 0.055 0.058 0.051
- 5 0.059 0.058 0.057


- Table 2: Maximum null rejection probability over the identified set Spβ,∆q for ∆ “ ∆SDpMq and ∆ “ ∆SDPBpMq under parallel trends (i.e., β “ 0) using the empirical distribution from Bailey and Goodman-Bacon (2015).


Table 3 reports the maximum rejection rate of the conditional test and the conditionalleast favorable test over a grid of parameter values θ within the identified set Spβ,∆q for ∆ “ ∆SDRMpM¯ q and ∆ “ ∆RMpM¯ q under the “pulse” pre-trend (i.e., β´1 “ δ´1 and βt “ 0 for all t ‰ ´1). We report results for M¯ “ 1 and δ´1{σ1 “ 1,2,3. The table shows that all our procedures approximately control size, with worst-case null rejection probability of 0.058.

###### B.3.3 Comparison with normal simulations

We next compare results from the non-normal simulations with estimated covariance discussed above to the normal model simulations the main text, in which βˆ is normal and Σ is treated as known.

Figures I4-I5 shows the rejection probabilities at different values of the parameter θ using both simulation methods for ∆SDpMq, ∆SDPBpMq at M{σ1 “ 0,5 respectively. The results are quite similar for all values of M{σ1 considered, and we thus omit the intermediate values.

∆ δ´1{σ1 Conditional C-LF Hybrid ∆SDRMpM¯ q

- 1 0.009 0.008
- 2 0.037 0.035
- 3 0.058 0.054


∆RMpM¯ q

- 1 0.005 0.005
- 2 0.017 0.016
- 3 0.024 0.023


- Table 3: Maximum null rejection probability over the identified set Spβ,∆q for ∆ “


∆SDRMpM¯ q and ∆ “ ∆RMpM¯ q under the “pulse” pre-trend (i.e., β´1 “ δ´1 and βt “ 0 for all t ‰ ´1) and M¯ “ 1 using the empirical distribution from Bailey and Goodman-Bacon (2015). We report results for δ´1{σ1 “ 1,2,3.

The estimated average rejection rates of each procedure are quite similar in the non-normal simulations and the normal simulations across each choice of ∆. As a result, the relative rankings of the procedures in terms of power are the same in the non-normal simulations as in the normal simulations discussed in the main text. Similarly, Figures I6-I7 shows the rejection probabilities at different values of the parameter θ using both simulation methods for ∆SDRMpM¯ q, ∆RMpM¯ q at δ´1{σ1 “ 1,2,3 respectively and M¯ “ 1.

###### Results are shown for θ “ τ1, and each choice of ∆ “ ∆SDpMq,∆SDPBpMq, and M{σ1 “ 0. The average rejection rate for the non-normal simulations are in red and the average rejection rate for the normal simulations are in blue; the dashed black lines indicate the identified set bounds. Results are averaged over 1000 simulations.

![image 17](<hpt-draft_images/imageFile17.png>)

###### Results are shown for θ “ τ1, and each choice of ∆ “ ∆SDpMq,∆SDPBpMq, and M{σ1 “ 5. The average rejection rate for the non-normal simulations are in red and the average rejection rate for the normal simulations are in blue; the dashed black lines indicate the identified set bounds. Results are averaged over 1000 simulations.

![image 18](<hpt-draft_images/imageFile18.png>)

###### ∆SDRMpM¯ q and ∆RMpM¯ q. Results are shown for θ “ τ1, M¯ “ 1 and δ´1{σ1 “ 1. The average rejection rate for the non-normal simulations are in red and the average rejection rate for the normal simulations are in blue; the dashed black lines indicate the identified set bounds. Results are averaged over 1000 simulations.

![image 19](<hpt-draft_images/imageFile19.png>)

###### ∆SDRMpM¯ q and ∆RMpM¯ q. Results are shown for θ “ τ1, M¯ “ 1 and δ´1{σ1 “ 3. The average rejection rate for the non-normal simulations are in red and the average rejection rate for the normal simulations are in blue; the dashed black lines indicate the identified set bounds. Results are averaged over 1000 simulations.

![image 20](<hpt-draft_images/imageFile20.png>)

## Appendix References

###### Armstrong, Timothy and Michal Kolesár, “Optimal Inference in a Class of Regression

Models,” Econometrica, 2018, 86, 655–683.

Bailey, Martha J. and Andrew Goodman-Bacon, “The War on Poverty’s Experiment in Public Medicine: Community Health Centers and the Mortality of Older Americans,” American Economic Review, March 2015, 105 (3), 1067–1104.

Ingster, Yuri and I. A. Suslina, Nonparametric Goodness-of-Fit Testing Under Gaussian

Models Lecture Notes in Statistics, New York: Springer-Verlag, 2003.

Nam, Nguyen Mau, “Convex Analysis: An introduction to convexity and nonsmooth

analysis,” https://maunamn.wordpress.com/ 2019.

Schrijver, Alexander, Theory of Linear and Integer Programming, Wiley-Interscience,

1986.

