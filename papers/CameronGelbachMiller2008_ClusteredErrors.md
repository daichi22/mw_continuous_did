NBER TECHNICAL WORKING PAPER SERIES

BOOTSTRAP-BASED IMPROVEMENTS FOR INFERENCE WITH CLUSTERED ERRORS

A. Colin Cameron Jonah B. Gelbach Douglas L. Miller

Technical Working Paper 344 http://www.nber.org/papers/t0344

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 September 2007

We thank an anonymous referee and participants at The Australian National University, UC Berkeley, UC Riverside, Dartmouth College, Florida State University, Indiana University, and MIT for useful comments. Miller acknowledges funding from the National Institute on Aging, through Grant Number T32-AG00186 to the NBER. The views expressed herein are those of the author(s) and do not necessarily reflect the views of the National Bureau of Economic Research.

© 2007 by A. Colin Cameron, Jonah B. Gelbach, and Douglas L. Miller. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source.

Bootstrap-Based Improvements for Inference with Clustered Errors A. Colin Cameron, Jonah B. Gelbach, and Douglas L. Miller NBER Technical Working Paper No. 344 September 2007 JEL No. C12,C15,C21

#### ABSTRACT

Researchers have increasingly realized the need to account for within-group dependence in estimating standard errors of regression parameter estimates. The usual solution is to calculate cluster-robust standard errors that permit heteroskedasticity and within-cluster error correlation, but presume that the number of clusters is large. Standard asymptotic tests can over-reject, however, with few (5-30) clusters. We investigate inference using cluster bootstrap-t procedures that provide asymptotic refinement.

These procedures are evaluated using Monte Carlos, including the example of Bertrand, Duflo and Mullainathan (2004). Rejection rates of ten percent using standard methods can be reduced to the nominal size of five percent using our methods.

A. Colin Cameron Department of Economics UC Davis One Shields Avenue Davis, CA 95616 accameron@ucdavis.edu

Jonah B. Gelbach Department of Economics University of Arizona 1130 E. Helen Street Tucson, AZ 85721-0108 gelbach@email.arizona.edu

Douglas L. Miller UC, Davis Department of Economics One Shields Avenue davis, CA 95616-8578 and NBER dlmiller@ucdavis.edu

# 1 Introduction

Microeconometrics researchers have increasingly realized the essential need to account for any within-group dependence in estimating standard errors of regression parameter estimates. In many settings the default OLS standard errors that ignore such clustering can greatly underestimate the true OLS standard errors, as emphasized by Moulton (1986, 1990).

A common correction is to compute cluster-robust standard errors that generalize the White (1980) heteroskedastic-consistent estimate of OLS standard errors to the clustered setting. This permits both error heteroskedasticity and quite flexible error correlation within cluster, unlike a much more restrictive random effects or error components model. In econometrics this adjustment was proposed by White (1984) and Arellano (1987), and it is implemented in STATA, for example, using the cluster option. In the statistics literature these are called sandwich standard errors, proposed by Liang and Zeger (1986) for generalized estimating equations, and they are implemented in SAS, for example, within the GENMOD procedure. A recent brief survey is given in Wooldridge (2003).

Not all empirical studies use appropriate corrections for clustering. In particular, for fixed effects panel models the errors are usually correlated

even after control for fixed effects, yet many studies either provide no control for serial correlation or erroneously cluster at too fine a level. Kézdi (2004) demonstrated the usefulness of cluster robust standard errors in this setting and contrasted these with other standard errors based on stronger distributional assumptions. Bertrand, Duflo, and Mullainathan (2004), henceforth BDM (2004), focused on implications for difference-in-difference (DID) studies using variation across states and years. Then the regressor of interest is an indicator variable that is highly correlated within cluster (state) so there is great need to correct standard errors for clustering. The clustering should be on state, rather than on state-year.

A practical limitation of inference with cluster-robust standard errors is that the asymptotic justification assumes that the number of clusters goes to infinity. Yet in some applications there may be few clusters. For example, this happens if clustering is on region and there are few regions. With a small number of clusters the cluster-robust standard errors are downwards biased. Bias corrections have been proposed in the statistics literature; see Kauermann and Carroll (2001), Mancl and DeRouen (2001), and Bell and McCaffrey (2002). Angrist and Lavy (2002) in an applied study find that bias adjustment of cluster-robust standard errors can make quite a difference. But

even after appropriate bias correction, with few clusters the usual Wald statistics for hypothesis testing with asymptotic standard normal or chi-square critical values over-reject. BDM (2004) demonstrate through a Monte Carlo experiment that the Wald test based on (unadjusted) cluster-robust standard errors over-rejects if standard normal critical values are used. Donald and Lang (2007) also demonstrate this and propose, for DID studies with policy invariant within state, an alternative two-step GLS estimator that leads to Tdistributed Wald tests in some special circumstances. Ibragimov and Muller (2007) propose an alternate approach based on separate estimation within each group. They separate the data into independent groups, estimate the model within each group, average the separate estimates and divide by the sample standard deviation of these estimates, and then compare against critical values from a T-distribution. This approach holds promise for settings with few groups and where model identification and a central limit theorem holds within each group. Our proposed method does not require the latter two conditions, can be used to test multiple hypotheses, and is based on the parameter estimator commonly used in practice.

In this paper we investigate whether bootstrapping to obtain asymptotic refinement leads to improved inference for OLS estimation with cluster-

robust standard errors when there are few clusters. We focus on cluster bootstrap-t procedures that are generalizations of those proposed for regression with heteroskedastic errors in the nonclustered case.

Several features of our bootstraps are worth emphasizing. First, the bootstraps involve resampling entire clusters. Second, our goal is to use variants of the bootstrap that provide asymptotic refinement, whereas many empirical studies use the bootstrap only to obtain consistent estimates of standard errors. Third, we consider several different cluster resampling schemes: pairs bootstrap, residuals bootstrap and wild bootstrap. Fourth, we consider examples with as few as five clusters. Fifth, we evaluate our bootstrap procedures in a number of settings including examples of others that were used to demonstrate the deficiencies of standard cluster-robust methods.

The paper is organized as follows. Section 2 provides a summary of standard asymptotic methods of inference for OLS with clustered data, and presents small-sample corrections to cluster-robust standard errors that have been recently proposed in the statistics literature. Section 3 presents various possible bootstraps for clustered data, with additional details relegated to an Appendix. Sections 4 to 6 present, respectively, a Monte Carlo experiment using generated data, a Monte Carlo experiment using data from BDM

(2004), and an application using data from Gruber and Poterba (1994).

The primary contribution of this paper is to offer methods for more accurate cluster-robust inference. These methods are fairly simple to implement and matter substantively in both our Monte Carlo experiments and our replications.

A second important contribution of this paper is to offer a careful and precise description of the various bootstraps a researcher might perform, and the similarities and differences between our proposed methods and several commonly-applied methods. Our primary motivation for presenting this description is to be precise about our methods. It also offers empiricists a clearer understanding of the menu of bootstrap choices and their consequences.

# 2 Cluster-Robust Inference

Before considering the bootstrap we present results on inference with clustered errors.1

## 2.1 OLS with Clustered Errors

The model we consider is one with G clusters (subscripted by g), and with Ng observations (subscripted by i) within each cluster. Errors are independent

1For this and subsequent sections, additional details and explanation are provided in (Cameron, Gelbach, and Miller 2006).

across clusters but correlated within clusters. The model can be written at various levels of aggregation as

yig = x0

igβ + uig, i = 1,...,Ng, g = 1,...,G, yg = Xgβ + ug, g = 1,...,G,

(1)

y = Xβ + u,

P

where β is k ×1, xig is k ×1, Xg is Ng ×k, X is N ×k, N =

g Ng, yig and uig are scalar, yg and ug are Ng × 1 vectors and y and u are N × 1 vectors.

Interest lies in inference for the OLS estimator βb = (X0X)−1X0y. Under the assumptions that data are independent over g but errors are correlated

within cluster, with E[ug] = 0, E[ugu0

g] = Σg, and E[ugu0

h] = 0 for cluster h 6= g, we have √N ³

βb − β´

∼a N[0, N V[βb]] where

V[βb] = (X0X)−1 ³XG

XgΣgX0g´(X0X)−1. (2)

g=1

This differs from and is usually larger than the specialization V[βb] = σ2u(X0X)−1 that is based on the assumption of iid errors and leads to the default OLS variance estimate when σ2u is estimated by s2 = ub0ub/(N − k). The underestimation bias is typically increasing in (1) cluster size; (2) withincluster correlation of the regressor; and (3) within-cluster correlation of the error; see Kloek (1981). The bias can be very large (Moulton 1986, 1990, BDM 2004).

One approach to correcting this bias is to model Σg to depend on unknown

parameters, say Σg = Σg(γ), and then use estimate Σbg = Σg(γb). The random effects (RE) model assumes that there are cluster-specific iid random effects, estimates the variance of these effects and of the iid individual shocks, and uses these for Σbg. We call the resulting standard errors Moulton-type standard errors.

## 2.2 Cluster-Robust Variance Estimates

The RE model places restrictions of homoskedasticity and equicorrelation

within cluster, and assumes knowledge of the functional form Σg(γ). A less parametrically restrictive approach is to use the cluster-robust variance estimator (CRVE)

VbCR[βb] = (X0X)−1 ³XG

Xguegue0gX0g´(X0X)−1. (3)

g=1

In the simplest case OLS residuals are used, so ueg = ubg = yg − Xgβb.

The CRVE controls for both error heteroskedasticity across clusters and quite general correlation and heteroskedasticity within cluster, at the expense of requiring that the number of clusters G → ∞. It is implemented for many STATA regression commands using the cluster option (which uses ueg = √cubg where c = GG−1 NN−−k1 ' GG−1 with large N), and is used in SAS in the GENMOD procedure (which uses ueg = ubg).

A weakness of the standard CRVE with ueg = ubg is that it is biased, since E[ubgub0

g] 6= Σg = E[ugu0

g]. The bias depends on the form of Σg but will usually be downwards.2 Several corrected residuals ueg for (3) have been proposed by Kauermann and Carroll (2001) and Bell and McCaffrey (2002). In our simulations we examine a correction proposed by Bell and McCaffrey (2002) which is equivalent to the jackknife estimate of the variance of the OLS estimator. This correction generalizes the HC3 measure (jackknife) of MacKinnon and White (1985), and so we refer to this correction as the CR3 variance estimator.3 For a more detailed discussion of the computation of this estimator, see Cameron, Gelbach, and Miller, (2006). Angrist and Lavy (2002) apply a related (but distinct) correction (which is a cluster generalization of the HC2 measure of MacKinnon and White (1985)) in an application with G = 30 to 40 and find that the correction increases clusterrobust standard errors by between 10 and 50 percent.

- 2For example, Kezdi (2004) uses ueg = ubg and finds in his simulations that with G = 10 the donwards bias is between 9 and 16 percent.
- 3The jackknife drops in turn each observation, here a cluster, computes the leave-oneout estimate βb(g), g = 1,...,G, and then uses variance estimate GG−1


P

g(βb(g) − βb). The CR3 measure for OLS is a multiple of the related measure proposed by Mancl and DeRouen

(2001) in the more general setting of GEE.

## 2.3 Cluster-Robust Wald Tests

We consider two-sided Wald tests of H0 : β1 = β01 against Ha : β1 6= β01 where β1 is a scalar component of β.4 We use the Wald test statistic

w = ³

βb1 − β01´/sβb

, (4)

1

is the square root of the appropriate diagonal entry in VbCR[βb]. This “t” test statistic is asymptotically normal under H0, and we reject H0 at significance level α if |w| > zα/2, where zα/2 is a standard normal critical value.

where sβb

1

Under standard assumptions the Wald test is of correct size as the number of clusters G → ∞. The problem we focus on in this paper is that with few clusters the asymptotic normal critical values can provide a poor approximation to the correct, finite-G critical values for w, even if an unbiased variance matrix estimator is used in calculating sβb.

General small sample results are not possible even if the (clustered) errors are normally distributed. In practice, as a small sample correction some programs use a T distribution to form critical values and p-values. STATA uses

4The generalization to single hypothesis c0β −r = 0 where c is a k ×1 vector is trivial. For multiple hypotheses Cβ − r = 0 the Wald asympototic chisquare test would be used.

the T(G − 1) distribution, which may be better than the standard normal, but may still not be conservative enough to avoid over-rejection. Bell and McCaffrey (2002) and Pan and Wall (2002) propose instead using a T distribution with degrees of freedom determined using an approximation method due to Satterthwaite (1941). Rather than use OLS, Donald and Lang (2007) propose an alternative two-step estimator that leads to a Wald test that in some special cases is T(G−k1) distributed where k1 is the number of regressors that are invariant within cluster and often k1 = 2 (the intercept and the clustered regressor of interest).

We instead continue to use the standard OLS estimator with CRVE, and bootstrap to obtain bootstrap critical values that provide an asymptotic refinement and may work better than other inference methods for OLS when there are few clusters.

# 3 Cluster Bootstraps

Bootstrap methods generate a number of pseudo-samples from the original sample, for each pseudo-sample calculate the statistic of interest, and use the distribution of this statistic across pseudo-samples to infer the distribution

of the original sample statistic.5

There is no single bootstrap as there are different statistics that we may be interested in, different ways to form pseudo-samples, and different ways to use results for statistical inference. In this section we discuss several different bootstraps that are examined in our simulations. We provide greater detail on the bootstrap algorithms in Appendix A.2, and in (Cameron, Gelbach, and Miller, 2006).

Choices that need to be made when bootstrapping include the following: what observational units to sample (individual observations or clusters); what objects to sample in generating bootstrap samples ((y,X) pairs, residuals drawn from the sample residuals, or residuals based on transformations of sample residuals); what statistics to calculate in each bootstrap replication; how to use the resulting bootstrap distribution of the statistics; and whether or not to impose the null hypothesis in generating the bootstrap samples. Some combinations of these choices provide asymptotic refinement; others do not. Some choices in principle provide valid tests, but in fact perform poorly with few clusters and commonly occuring empirical settings.

5The bootstrap was introduced by Efron (1979). Standard book treatments are Hall (1992), Efron and Tibsharani (1993), and Davison and Hinkley (1997). In econometrics see Horowitz (2001), MacKinnon (2002), and the texts by Davidson and MacKinnon (2004) and Cameron and Trivedi (2005).

The statistic considered is the Wald test statistic w defined above. The data are clustered into G independent groups, so the resampling method should be one that assumes independence across clusters but preserves correlation within clusters.

## 3.1 Pairs Cluster Bootstrap-se and Bootstrap-t

The obvious method is to resample the clusters with replacement from the

original sample {(y1,X1),...,(yG,XG)}. This resampling method is called a pairs cluster bootstrap6. A commonly used bootstrap in the empirical literature is to use a pairs bootstrap with the bootstrap-se procedure. The bootstrap-se procedure uses the bootstrap estimates of βb1, denoted βb∗1b, to form the bootstrap estimate of standard error

(βb∗1b − βb∗1)2!1/2 , (5)

1,B = Ã 1

XB

sβb

B − 1

b=1

PB

βb∗1b. This estimated standard error is then used in a typical wald test. This is popular in the applied literature as it enables an estimate of the standard error when the analytic formula for the standard error is difficult to compute. However, in contrast to the bootstrap-t procedure, it does not offer asymptotic refinement, and so may perform worse

where βb∗1 = B1

b=1

6Alternative names used in the literature include cluster bootstrap, case bootstrap, nonparametric bootstrap, and nonoverlapping block bootstrap.

with few clusters.

The bootstrap-t procedure, proposed by Efron (1981) for confidence intervals, computes the following Wald statistic for each bootstrap replication

wb∗ = (βb∗1,b − βb1)/sβb∗

, b = 1,...,B,

1,b

is a cluster-robust standard error for βb∗1,b. Note that w∗

b is centered on βb1. This centering is changed to β01 if the resampling method imposes H0. The resulting distribution of w∗

where sβb∗

1,b

1,...,w∗

B is then used to form inference on the original Wald statistic in (4).7 We offer more details in the appendix A.2.

Both bootstrap-se and bootstrap-t procedures are asymptotically valid. For small number of clusters G, however, the true size will differ from the nominal significance level α. Furthermore, the true size will also differ across the two procedures. An asymptotic approximation yields an actual rejection rate or true size α + O(G−j/2). Then the true size goes to α as G → ∞, provided j > 0. Larger j is preferred, however, as then convergence to α is faster. A bootstrap provides asymptotic refinement if it leads to j larger than that for conventional (first-order) asymptotic methods. Bootstrap-t

7The bootstrap-t procedure is also called a percentile-t procedure, because the “t” test statistic w is bootstrapped, and a studentized bootstrap, since the Wald test statistic is a studentized statistic.

procedures provide an asymptotic refinement, while bootstrap-se procedures do not. Further, as we show in our simulations below, this can matter in actual data settings with few clusters.

Asymptotic refinement is more likely to occur if the bootstrap is applied to an asymptotically pivotal statistic, meaning one with asymptotic distribution that does not depend on unknown parameters; see Appendix A.1 for a more complete discussion. The bootstrap-t procedure directly bootstraps w which is asymptotically pivotal since the standard normal has no unknown parameters.

An alternative method with asymptotic refinement is the bias-corrected accelerated (BCA) procedure, defined in Efron (1987), Hall (1992, pp. 128-

141), and in (Cameron, Gelbach, and Miller, 2006). This bootstraps βb1 which is asymptotically nonpivotal as its asymptotic distribution depends on

unknown σ2βb

, but then provides adjustment for bias and asymmetry. This is a popular method for confidence intervals — STATA reports BCA rather than percentile-t confidence intervals. We adapt BCA to testing by rejecting H0 if w is outside the confidence interval, and include a cluster version of BCA in our simulations.

1

There are just a few studies that we are aware of that consider asymptotic

refinement. Sherman and le Cessie (1997) conduct simulations for OLS with as few as ten clusters. For 90 percent confidence intervals, they find that the pairs cluster bootstrap-t undercovers by considerably less than confidence intervals based on CRVE. Flynn and Peters (2004) consider cluster randomized trials where a pairs cluster bootstrap draws G clusters by separately resampling from the G/2 treatment clusters and the G/2 control clusters. For skewed data and few clusters they find that pairs cluster BCA confidence intervals have considerable undercoverage, even more than conventional robust confidence intervals, though in their Monte Carlo design the robust intervals do remarkably well. The authors also consider a second-stage of resampling within each cluster, using a method for hierarchical data given in Davison and Hinkley (1997) that is applicable if the random effects model is assumed.

In the econometrics literature, BDM (2004) apply a pairs cluster bootstrap using the bootstrap-t procedure. BDM use default OLS standard errors, however, rather than cluster-robust standard errors, in computing both the original data and the resampled data Wald statistics. Because of this their method may not yield asymptotic refinement. The authors find that their bootstrap does better than using default OLS standard errors and standard normal critical values, yet surprisingly does worse than using cluster robust

standard errors with standard normal critical values.

## 3.2 Residual and Wild Cluster Bootstrap-t

For a regression model with additive error, resampling methods other than pairs cluster can be used. In particular, one can hold regressors X constant throughout the pseudo-samples, while resampling the residuals which can be then used to construct new values of the dependent variable y.

The obvious method is a residual cluster bootstrap that resamples with replacement from the original sample residual vectors to give residuals {ub∗

1,...,ub∗

G} and hence pseudo-sample {(yb∗

gβb + ub∗

1,X1),...,(yb∗

G,Xg)} where yb∗

g = X0

g.

This resampling scheme has two weaknesses. First, it assumes that the regression error vectors ug are iid, whereas in Section 2 we were specifically concerned that the variance matrix Σg will differ across clusters. Second, it presumes a balanced data set where all clusters are the same size.

The wild bootstrap relaxes both these restrictions. This procedure creates pseudo-samples based on ub∗

g = ubg with probability 0.5 and ub∗

g = −ubg with probability 0.5, with this assignment at the cluster level. The wild bootstrap was proposed for regression in the nonclustered case (and with different weights) by Wu (1986). Its asymptotic validity and asymptotic refinement were proven by Liu (1988) and Mammen (1993). Horowitz (1997, 2001) pro-

vides a Monte Carlo demonstrating good size properties. The weights we use (+1 with probability 0.5 and −1 with probability 0.5) are called Rademacher weights8. Here we have extended the wild bootstrap to the clustered setting. The only other study to do so that we are aware of is the brief application by Brownstone and Valletta (2001).

Several authors, particularly Davidson and MacKinnon (1999), advocate use of bootstrap resampling methods that impose the null hypothesis. This is possible using both residual and Wild bootstraps. Thus we present results based on bootstraps that impose the null, in which case the bootstrap Wald statistics are centered on β01 rather than βb1, and the residuals bootstrapped are those from the restricted OLS estimator βe that imposes H0 : β1 = β01. For details see Appendix A.2.

## 3.3 Bootstraps with Few Clusters

With few clusters the bootstrap resampling methods produce a distinctly finite number of possible pseudo-samples, so the bootstrap distribution w∗

1,...,w∗

q

will not be smooth even with many bootstrap replications. Furthermore, in

8These weights lead to asymptotic refinement if βb is symmetrically distributed, which is the case if errors are symmetric. If βb is asymmetrically distributed, our version is still asymptotically valid, but different weights provide asymptotic refinement. Davidson and Flachaire (2001) provide theory and simulation to nonetheless support using Rademacher weights even in the asymmetric case.

some pseudo-samples βb1 or sβb

may be inestimable. This is likely to be a problem with pairs cluster bootstrap when there is a binary regressor that is invariant within cluster (so always 0 or always 1 for given g). Then if there are few clusters some bootstrap resamples may have all clusters with the regressor taking only value 0 (or value 1), so that βbk is inestimable. This issue does not arise when regressors and dependent variables take several different values, such as in the Section 4 Monte Carlos. But it does arise in our application to the BDM (2004) and Gruber and Poterba (1994) differences-in-differences examples, because the regressors of interest in those cases are indicator variables. The residual or wild cluster bootstraps do not encounter these problems, as we are not resampling the regressors. In our BDM simulations below we see this issue is problematic for G ≤ 10.

1

## 3.4 Test Methods used in this Paper

In the remainder of the paper we implement the Wald test using nine bootstrap procedures, as well as four non-bootstrap procedures. Table 1 provides a summary.

Our first four methods do not use the bootstrap and differ only in the method from section 2 used to calculate Vb[βb]. They use, respectively, the default variance estimate, the Moulton-type estimate, the cluster-robust es-

timate (3), and the cluster-robust estimate with jackknife corrected residuals. Method 1 is invalid if there is clustering, method 2 is invalid unless the clustering follows a random effects model, while methods 3 and 4 are asymptotically valid provided clusters are independent.

Methods 5 to 7 use the bootstrap-se procedure. We use three different cluster bootstrap resampling methods, respectively, the pairs cluster boot-

strap, the residual clusters bootstrap with H0 imposed, and the wild bootstrap with H0 imposed. For details see Appendix A.2.3. Methods 5-7 do not provide asymptotic refinement, and method 6 is valid only if cluster error vectors are iid.

Method 8 uses the BCA bootstrap with pairs cluster resampling. Methods 9 to 13 use the bootstrap-t procedure. The first three of these methods use pairs cluster resampling with different standard error estimates. Method 9 is the already discussed method of BDM that uses default standard errors rather than CRVE standard errors. Methods 10 and 11 use different variants of the CRVE defined in (3), respectively, the standard CRVE and the CR3 correction. In each case the same variance matrix estimation method is used for both the original sample and bootstrap resamples. Methods 12 and 13 use, respectively, residual and wild bootstraps, and both use the standard

CRVE estimate and impose H0. Method 12 is valid only if cluster error vectors are iid. For details see Appendix A.2.1.

# 4 Monte Carlo Simulations

To examine the finite-sample properties of our methods we conducted several Monte Carlo exercises for dgp a linear model with intercept and single regressor. The error is clustered according to a random effects model, with either constant correlation within cluster or departures from this induced by heteroskedasticity. This design is relevant to a cross-section study of individuals with clustering at the state level, for example. The regressor and dependent variable are continuous and take distinct values across clusters and (usually) within clusters, so that even with few clusters it is unlikely that a pairs cluster bootstrap sample will be inestimable.

Then

yig = β0 + β1xig + uig, (6)

with different generating processes for xig and uig used in subsequent subsec-

tions. Since β1 = 1 in the dgp, the Wald test statistic is w = (βb1 − 1)/sβb

. We perform R replications, where each replication yields a new draw of data from the dgp, and leads to rejection or nonrejection of H0. In each repli-

1

cation there are G groups (g = 1,...,G), with NG individuals (i = 1,...,NG) in each group. We varied the number of groups G from 5 to 30 and usually set NG = 30. The various methods given in each row of Tables 2-4 are then applied to the same generated data. For bootstraps we used B = 399 bootstraps rather than the recommended B = 999 or higher. This lower value is fine for a Monte Carlo exercise, since the bootstrap simulation error will cancel out across Monte Carlo replications.

We estimate the actual rejection rate a, by ba, the fraction of the R replications for which H0 is rejected. This is an estimate of the true size of the test. With a finite number of replications a may be differ from the true size due to simulation error. The simulation standard error is sba = p

ba(1 − ba)/(R − 1).

For example, sba = 0.007 for ba = 0.05 and R = 1000.

## 4.1 Simulations with Homoskedastic Clustered Errors

In the first simulation exercise both regressors and errors are correlated within group, with errors homoskedastic. Data were generated according to:

yig = β0 + β1xig + uig = β0 + β1 (zg + zig) + (εg + εig), (7)

with zg, zig, εg, and εig each an independent N[0,1] draw, and β0 = 0 and β1 = 1. Here the components zg and εg that are common to individuals within a group induce within group correlation of both regressors and errors. The simulation is based on R = 1000 Monte Carlo replications.

Our first results appear in Table 2. Each column gives results for the various number of groups (G = 5, 10, 15, 20, 25, 30) and throughout NG = 30. The first entry is the estimated true size of the test. The Monte Carlo standard error is given in parentheses. Each row presents a different method, detailed in section 3.4. For comparison, we also show the rejection rate that would hold if we used the asymptotic normal critical value of 1.96, but the Wald statistic actually had a T distribution with G − 2 degrees of freedom, Pr[|T| > 1.96|T ∼ TG−2].

We begin with conventional (nonbootstrap) Wald tests using different estimators of standard errors. The default OLS standard errors that assume iid errors do poorly here, with rejection rates given in row 1 of 0.43 to 0.50. This illustrates the need to correct standard errors for clustering. The Moulton-type estimate for standard errors should work well here since this takes advantage of correct knowledge of the dgp. The rejection rates in row 2 are considerably higher than 0.05, especially for low G, though are similar to

those expected if the Wald test statistic is actually T(G−2) distributed. The CRVE is much better than default standard errors, though still over-rejects compared to Moulton-type standard errors. The CR3 correction leads to rejection rates much closer to (but significantly different from) 0.05.

The pairs cluster bootstrap-se method yields rejection rates in row 5 that are very similar to the CRVE, except for G = 5. The residual cluster bootstrap-se method leads to rejection rates in row 6 that are close to 0.05. From row 7, the wild cluster bootstrap-se method under-rejects for G ≤ 10, and rejects at level close to 0.05 for G > 10. The closeness to 0.05 of the latter two bootstrap methods is surprising given that they do not offer an asymptotic refinement. The BCA bootstrap with pairs cluster resampling should provide an asymptotic refinement, yet from row 8 it has rejection rates similar to those using CRVE.

The remainder of Table 2 uses the theoretically preferred bootstrap-t procedure with various resampling methods. Even though it uses default standard errors, the BDM bootstrap (row 9) does better than CRVE and is a great improvement compared to not bootstrapping (row 1). The pairs cluster bootstrap-t has rejection rates in row 10 of 0.08 that are much closer to (but significantly different from) 0.05. The CR3 correction makes little

difference. Both the residual cluster bootstrap-t and wild cluster bootstrap-t rejection rates are not statistically different from 0.05 (with the exception of the residual bootstrap with G = 5).

In summary, Table 2 demonstrates that all the bootstrap-t methods are an improvement on the usual cluster-robust method with standard normal critical values; the BCA method provides no improvement on CRVE; and the residual cluster bootstrap-se also performs well.

## 4.2 Simulations with Heteroskedastic Clustered Errors

The second simulation brings in the additional complication of heteroskedastic errors. Then the Moulton-type correction and the residual bootstrap are no longer valid theoretically.

We generated data according to the process:

yig = β0 + β1xig + uig = β0 + β1 (zg + zig) + (εg + εig), (8)

with zg, zig, and εg again independent N[0,1] draws, but now εig ∼ N[0,9 ∗

(zg + zig)2]. The dgp sets β0 = 1 and β1 = 1.

Results appear in Table 3. Default OLS standard errors again do poorly, with rejection rates around 0.30. The Moulton-type correction breaks down given the heteroskedasticity, as expected. The cluster-robust methods do a

little better than in the preceding table, but rejection rates in rows 3 and

- 4 still generally exceed 0.05. The residual cluster bootstrap-se method now breaks down due to heteroskedasticity, with rejection rates in row 6 in excess of 0.15. The pairs cluster bootstrap-se and wild cluster bootstrap-se methods (rows 5 and 7) perform similarly to Table 2. The BCA bootstrap again has rejection rates in row 8 similar to those using CRVE (row 3).


The results for the bootstrap-t methods in rows 9 to 13 are similar to those in Table 2. The BDM bootstrap-t (row 9) has similar high rejection rates to those in Table 2, aside from marked deterioration for G = 5. The remaining bootstrap-t methods all yield rejection rates less than 0.08, with the residual cluster bootstrap-t and wild cluster bootstrap-t doing best. The good performance of the residual cluster bootstrap-t is surprising given that errors are heteroskedastic.

In summary, the Table 3 results for inference with heteroskedastic clustered errors are similar to those for homoskedastic clustered errors except that, as expected, the Moulton-type correction and residual cluster bootstrapse methods now perform very poorly. The bootstrap-t methods are an improvement on the usual cluster-robust method with standard normal critical values, while the BCA method provides no improvement.

## 4.3 Alternative Critical Values, Cluster Sizes and Regressor Design

We perform a third set of Monte Carlo experiments to examine how the different estimators perform under varying assumptions. These simulations are presented in Table 4 with each simulation based on G = 10 groups.

Column 1 of Table 4 provides a baseline against which the other results are compared. It uses the same dgp as that of Table 2. In column 2 for tests without asymptotic refinement we use critical values from a T distribution with 8 degrees of freedom, an ad hoc finite sample correction, so that we reject H0 if |w| > 2.306 rather than |w| > 1.960. Then the Moulton-type estimator and the CR3 correction lead to rejection rates not statistically significant from 0.05. The CRVE and pairs cluster bootstrap-se still lead to over-rejection, though by not as much. And the residual cluster bootstrap-se and wild cluster bootstrap-se, which seem to do very well when asymptotic normal critical values are used, now lead to great under-rejection.

In columns 3 to 5 of Table 4 we consider alternative cluster sizes of, respectively, 2, 10 and 100 observations. For method 1, the rejection rates increase with cluster size. Once clustering is accounted for, by any of methods 2-13, rejection rates do not vary significantly with cluster size.

In column 6 of Table 3 we examine the performance of the various testing methods when there are there are three additional regressors, each with no clustering component, and we continue to test the first regressor. The four regressors are scaled down by a factor of 1/2, so that the sum of their variances will equal the variance of the single regressor used in the dgp of column 1. The only significant change in rejection rates is an increase in the already high rejection rate for method 1 which neglects clustering.

All preceding regression designs set the intraclass correlation, ρx, of the regressor of interest to be 0.5. In column 7 we increase ρx to ρx = 1 (clusterinvariant regressor with xig = zg) and in column 8 we decrease to ρx = 0 in column 8 (iid regressor with xig = zig). In both cases the regressor is scaled up by √2 to keep V[xig] unchanged.

With cluster-invariant regressor (column 7) the failure to control for clustering is magnified and the row 1 to 3 rejection rates are larger than in the benchmark column 1. For bootstrap-se and bootstrap-t there is little change in rejection rates, except that for reasons unknown the pairs cluster bootstraps (both bootstrap-se and bootstrap-t) now have rejection rates not statistically significantly different from 0.05.

With iid regressor (column 8) the default OLS standard errors are consis-

tent and the rejection rate in row 1 is close to 0.05. The Moulton-type and CRVE also have rejection rates much closer to 0.05. The various bootstrap procedures lead to rejection rates that are all close to those in column 1.

Finally, in column 9 we change the dgp to examine an unbalanced setting, so that one half of the clusters are small (with group size NG = 10) and half of the clusters are large (with group size NG = 50). The residual cluster bootstrap requires equal cluster sizes, so it cannot be used in this design. The remaining methods yield results qualitatively similar to those in column 1, with the main change being that the standard CRVE leads to much larger over-rejection in row 3.

In summary, all the bootstrap-t methods are an improvement on the usual cluster-robust method with standard normal critical values; the BCA method provides no improvement; and the residual cluster bootstrap-se also performs well. Table 4 also indicates that when non-bootstrap methods are used to control for clustering, it is better to use critical values from a T (G − 2) distribution than from a standard normal.

# 5 Bertrand, Duflo and Mullainathan (2004) Simulations

To enable a more practically familiar application of our methods, we now consider the differences-in-differences setup explored in Bertrand, Duflo, and Mullainathan (2004). The main results of this section are that the residual and wild cluster bootstrap methods perform well in cases with as few as 6 clusters. These results stand in contrast to the more pessimistic conclusion about cluster bootstrapping in BDM (2004).

The data set is of U.S. states over time. The dependent variable is the state-by-year average log wage level (after partialling out certain individual characteristics). For such a variable, the error term within cluster is serially correlated, even if state and year fixed effects are included as regressors. The regressor of interest is a state policy dummy variable.

The original data is CPS data on many individuals over time and states. Most of the BDM (2004) study uses a smaller data set that aggregates individual observations to the state-year level. We begin with these data, which have the advantage of being balanced and relatively small, before moving to the individual data.9

9We extracted individual-level data from the relevant CPS data sets and, when appropriate, aggregated these data using the method presented in BDM (2004). This gave data

## 5.1 Aggregated State-year Data

Using our choice of subscripts, the igth observation is for the ith year in the gth state. There are fifty states and twenty-one years. The aggregate model estimated is

yig = αg + γi + β1Iig + uig, where yig is a year-state measure of excess earnings, the regressors are state dummies, year dummies, and a policy change indicator Iig.10

If a policy change occurs in state g at time i∗, then Iig = 0 for i < i∗ and Iig = 1 for i ≥ i∗. BDM’s experiments randomly assign a policy change to occur in half the states, and when it does occur it occurs somewhere between the sixth and fifteenth year. In each simulation a different draw of G states with replacement is made from the original 50 states.

The Wald statistic studied is w = βb1/sβb

. BDM investigate size properties by letting the policy change be a “placebo” regressor that has no effect on

1

yig. They also investigate the power against the alternative Ha : β1 = 0.02

similar to that in BDM (2004). We thank these authors for sharing some of their data with us, enabling this comparison.

10We retain our notation for consistency with the rest of our discussion. However, more obvious subscripts for this problem are i for individual, s for state and t for year. The underlying model is yist = αs + γt + x0

istδ + βIst + uist, where yist is individual log-earnings for women aged 25-50 years, and xist is age and education. BDM use a two-step OLS procedure: (1) regress yist on xist yielding OLS residual ubist; (2) regress ubst = Nst−1

P

i ubist on state dummies, year dummies, and Ist. Thus our yig is their ubst.

by actually increasing yig by 0.02 when Iig = 1. They find that (1) default standard errors do poorly; (2) cluster-robust standard errors do well for all but G = 6; and (3) their bootstrap, which we discuss in our section 3.1, does poorly for low numbers of clusters, with actual rejection rates 0.44, 0.23 and

- 0.13 for G = 6, 10 and 20, respectively. The first two rows of Table 5 show that the default standard errors and


Moulton-type estimator lead to high rejection rates. The third row uses the cluster-robust variance estimator, and gives results very close to those in BDM’s Table 8.

Rows 4 to 6 of our Table 5 give rejection rates when the Wald statistic is calculated using bootstrap standard error estimates. These generally lead to tests with actual size between 0.04 and 0.09. The one notable exception is that the cluster-pairs standard error bootstrap (row 4) produces severe under-rejection (0.001) with G = 6. Informal experimentation suggests to us that this is because many bootstrap replications (with only a couple of states sampled) sample only one “treatment” or “control” state. For these replications, the treatment dummy (or constant) is fit perfectly, and so has zero estimated residuals. When these “zero” residuals are plugged into the CRVE formula (3) the resulting VbCR[βb∗1] is unreasonably small, leading to

Wald statistics in some bootstrap resamples that are too large to consistently represent the Wald statistic’s true distribution. This in turn results in the severe under-rejection.11

The BCA method with pairs cluster resampling in general leads to greater over-rejection than when CRVE is used.

The remaining rows 8 to 11 of Table 5 give rejection rates for various bootstrap-t procedures. From row 8 we find that the BDM bootstrap performs similarly to cluster-robust standard errors. For reasons we cannot explain, the rejection rates we obtain are considerably lower than those given in BDM Table 5. The pairs cluster bootstrap-t under-rejects appreciably for both G = 6 and G = 10 for reasons discussed above. The residual and wild cluster bootstrap-t methods (rows 9 and 10) do very well with actual rejection rates approximately equal to 0.05, even for G = 6.

The discussion so far has focused on size. The last 4 columns in Table

- 5 report power against a fixed alternative. As expected, power increases as the number of clusters increases, since there is then greater precision in


estimation.

11We thank Doug Staiger for suggesting this mechanism to us.

## 5.2 Individual-Level Data

For completeness we additionally consider regression using individual-level data. Recall that we are using g to denote the clustering unit and i to denote year, so we use n to denote individual. Then the model is

ynig = αg + γi + x0nigδ + β1Iig + unig,

where the individual-level regressors xnig are a quartic in age and three education dummies. Iig is generated as before.

Table 6 reports the results of R = 250 simulations with B = 199 replications used for the bootstrap. We consider cases G = 6 and G = 10. The first row reports high rejection rates when we use the CRVE but erroneously cluster on state-year combinations. In the second row of Table 6 we see that using the CRVE and correctly clustering on state considerably reduces the rejection rates, but they are still much too high. The third row of Table

- 6 shows that the bootstrap-t procedure using wild cluster resampling (with clustering on the state) leads to rejection rates not statistically significantly different from 0.05. Because the individual level data are unbalanced we cannot use the residual cluster bootstrap.


In summary, using both aggregate and micro data, the wild cluster bootstrap-

t leads to rejection rates of 0.05. The pairs cluster bootstrap-t works fine for G ≥ 20, but for G ≤ 10 can fail due to problems posed by the binary regressor.

# 6 Gruber and Poterba (1994) Application

Gruber and Poterba (1994, henceforth GP) examine the impact of tax incentives on the decision to purchase health insurance. They analyze differential changes for self-employed and business-employed in the after-tax price of health insurance due to the Tax Reform Act of 1986 (TRA86). The TRA86 extended the tax subsidy for health insurance to self-employed individuals; individuals employed by a business had a tax subsidy both before and after TRA86, and so can serve as a comparison group.

The dependent variable y is whether or not an employed person has private health insurance. Like GP we focus on individuals 25-54 years of age. The model can be written as

yijt = α1 + α2SELFijt + α3POSTijt + β1SELFijt × POSTijt + ujt,

where i denotes individual, j denotes employer type, t denotes year, SELFijt = 1 if individual i is self-employed at time t, and POSTijt = 1 if the year is 1987, 1988 or 1999.

We perform difference-in-difference analysis, controlling for potential clustering of errors of a form considered by Donald and Lang (2007). Like Donald and Lang, we ignore additional regressors (GP examine subtle interactions between pre-tax income, employment status, and the TRA86).

In their preliminary analysis, GP report in their Table IV average insurance rates by year and employer-type for March CPS data on eight years (five before the TRA86 and three after), leading to an aggregated data set with sixteen observations. Our simple difference-in-difference estimate is 0.055, with a standard error of 0.0044.

We next follow Donald and Lang (2007), and treat years as clusters, so that there are G = 8 clusters in our analysis. When we cluster on year, the cluster-robust standard error obtained using (3) is 0.0074. The regressor is highly statistically significant, with βb1/sβb

= 7.46 and very low p-value.

1

To enable more meaningful analysis we test H0 : β1 = 0.040 against Ha : β1 6= 0.040. Then w = (0.055 − 0.040)/0.0074 = 2.02 with p-value of

- 0.043 using standard normal critical values and 0.090 using the T distribution with G − 2 = 6 degrees of freedom.


If we instead bootstrap this Wald statistic with B = 999 replications, the pairs cluster bootstrap-t yields p = 0.209, the residual cluster bootstrap-t

gives p = 0.112, and the wild cluster bootstrap-t gives a p-value of 0.070.12 We believe that the p-value for the pairs cluster bootstrap is implausibly large, for reasons discussed in the BDM replication, while the other two bootstraps lead to plausible p-values that, as expected, are larger than those obtained by using asymptotic normal critical values.

We have also estimated this model on individual-level data (see Cameron, Gelbach, and Miller, 2006), with results very similar to those reported here.

# 7 Conclusion

Many microeconometrics studies use clustered data, with regression errors correlated within cluster and regressors correlated within cluster. Then it is essential that one control for clustering. A good starting point is to use Wald tests (or “t” tests) that use cluster-robust standard errors, provided the appropriate level of clustering is chosen. As made clear in section 2 of BDM (2004), too many studies fail to do even this much.

In this paper we are concerned with the additional complication of having few clusters. Then the use of appropriate cluster-robust standard errors still leads to nontrivial over-rejection by Wald tests. Our Monte Carlo sim-

12The results reported use Mammen weights and do not impose the null hypothesis. Similar results were obtained using Rademacher weights and imposing the null hypothesis.

ulations reveal that at the very least one should provide some small sample correction of standard errors, such as magnifying the residuals in (3) by a factor pG/(G − 1) and using a T distribution with G or fewer degrees of freedom (we arbitrarily used G − 2 in Table 3).

The primary contribution of this paper is to use bootstrap procedures to obtain more accurate cluster-robust inference when there are few clusters. Our discussion and implementations of the bootstrap make it clear that there are many possible variations on a bootstrap. The usual way that the bootstrap is used, to obtain an estimate of the standard error, does not lead to improved inference with few clusters as it does not provide an asymptotic refinement.

We focus on the bootstrap-t procedure, the method most emphasized by theoretical econometricians and statisticians, and which provides asymptotic refinement. We find that the bootstrap-t procedure can lead to considerable improvement, provided the same method is used in calculating the Wald statistic in the original sample and in the bootstrap resamples.

But these improvements depend on the resampling method used and on the discreteness of the data being resampled. The standard method for resampling that preserves the within-cluster features of the error is a pairs

cluster bootstrap that resamples at the cluster level, so that if the gth cluster is selected then all data (dependent and regressor variables) in that cluster appear in the resample. This bootstrap can lead to inestimable models or nearly inestimable models in some bootstrap pseudo-samples when there are few clusters and regressors take a very limited range of values. While not all applications will encounter this problem, it does arise when interest lies in a binary policy variable that is invariant (conditional on other regressors) within cluster.

We find that an alternative cluster bootstrap, the wild cluster bootstrap does especially well. This bootstrap is a cluster generalization of the wild bootstrap for heteroskedastic models. Even when analysis is restricted to a wild cluster bootstrap, several different variations are possible. The variation we use is one that uses equal weights and probability, and uses residuals from OLS estimation that imposes the null hypothesis. This bootstrap works well in our own simulation exercise and when applied to the data of BDM (2004).

The BDM (2004) study is one of the highest profile papers highlighting the importance of cluster robust inference. One important conclusion of BDM (2004) is that for few (six) clusters the cluster-robust estimator performs poorly, and for moderate (ten and twenty) number of clusters their

bootstrap based method also does poorly. We perform a re-analysis of their exercise, and come to much more optimistic conclusions. Using the wild cluster bootstrap-t method our empirical rejection rates are extremely close to the theoretical values, even with as few as six clusters, and there is no noticeable loss of power after accounting for size. Our results offer not only theoretical improvements, but practical ones as well. We hope researchers will take advantage of these improvements in the plentiful cases when clustering among a relatively small number of groups is a real concern.

# A Appendix

Appendix A.1 presents a general discussion of the bootstrap and why it is asymptotically better to bootstrap an asymptotically pivotal statistic (bootstrapt method). Appendix A.2 details the various bootstraps summarized in Table

- 1.


## A.1 Asymptotic Refinement for Bootstrap-t

The theory draws heavily on Hall (1982) and Horowitz (2001). Cameron and Trivedi (2005) provide a more introductory discussion.

- A.1.1 General Bootstrap Procedure


We use the generic notation TN = TN(SN) to denote the statistic of interest, calculated on the basis of a sample SN of size N. We focus on inference for a single regression coefficient β1 from multivariate OLS regression. Then leading examples are TN = βb1, and TN = (βb1 −β01)/sβb

, where we recall that

1

β01 is given by the null hypothesis.

We wish to approximate the finite sample cdf of TN, HN(t) = Pr[TN ≤ t]. The bootstrap does this by obtaining B resamples of the original sample

SN, using methods given in the subsequent subsection. The bth resample is

denoted SNb∗ and is used to form a statistic T∗

Nb = T∗

N(SNb∗ ). The empirical

distribution of T∗

Nb, b = 1,..,B, is used to estimate the distribution of TN, so Pr[TN ≤ t] is estimated by the fraction of the realized values of T∗

N1,...,T∗

Nb

that are less than t, denoted

XB

HbN(t) = B−1

1(TNb∗ ≤ t), (9)

b=1

where 1(·) is the indicator function. This distribution can be used to compute moments such as variance, and also to compute test critical values and pvalues.

General Bootstrap Procedure for a Statistic TN

- 1. Do B iterations of this step. On the bth iteration:

- (a) Re-sample the data from SN using one of the procedures presented

in Appendix A.2. Call the resulting re-sample SNb∗ .

- (b) Use the bootstrap re-sample form T∗


Nb = T∗

N(SNb∗ ), where in some but not all cases T∗

N(·) = TN(·).

- 2. Conduct inference using HbN(t). See Appendix A.2 for further details.


The bootstrap-t method directly approximates the distribution of TN =

(βb1 − β01)/sβb

1

. If the bootstrap resampling method imposes H0 then T∗

Nb =

(βb∗1b−β01)/sβb∗

, where βb∗1b is the estimator of β1 and sβb∗

is the standard error

1b

1b

Nb on β01 since the resampling dgp has β1 = β01. If instead the bootstrap resampling method does not impose H0, the case necessarily for pairs cluster, then T∗

from re-sample SNb∗ . Note that we center T∗

Nb = (βb∗1b − βb1)/sβb∗

. The centering is on βb1 and the bootstrap views the original sample as the population. That is, implicitly we impose β1 = βb1, and the bootstrap resamples are viewed as B samples from a population with β1 = βb1.

1b

By contrast the bootstrap-se, percentile and BCA methods bootstrap

Nb = βb∗1b, where βb∗1b is the estimator of β1 from re-sample SNb∗ .

TN = βb1. Then T∗

- A.1.2 Asymptotic Refinement


For notational simplicity drop the subscript N, so TN(SN) = T has smallsample cdf denoted H(t|F) = Pr[T ≤ t|F] where F is the true cdf generating the underlying data in sample SN. The distribution H usually is analytically intractable. The usual first-order asymptotic theory replaces it with the asymptotic distribution of the test-statistic. The bootstrap instead replaces H with Hb(t|Fb) = Pr[T∗ ≤ t|Fb] where Fb denotes the cdf used to obtain bootstrap resamples. We are concerned with how good an estimate Hb(t|Fb) is of H(t|F).

The bootstrap leads to consistent estimates and hypothesis tests under relatively weak assumptions. Because the bootstrap should be based on a distribution Fb that is consistent for F, one must take care to choose the resampling method so as to mimic the properties of F. For consistency, the bootstrap requires smoothness and continuity in F and in Hb. These assumptions are satisfied for our application for the OLS estimator with clustered errors.

A consistent bootstrap need not have asymptotic refinement, however. A key requirement is that we work with an asymptotically pivotal statistic, as now explained.

To begin with assume that T is standardized to have mean 0 and variance

- 1. The usual asymptotic approximation T ∼a N[0,1] is


Pr[T ≤ t|F] = Φ(t) + O(N−1/2),

where Φ(·) is the standard normal cdf and N is sample size. When one uses the standard normal critical values with a “t” statistic, this is the approximation on which one relies. The Edgeworth expansion gives a better asymptotic approximation

Pr[T ≤ t|F] = Φ(t) + N−1/2a(t)φ(t) + O(N−1),

where φ(·) is the standard normal density and a(·) is an even quadratic polynomial with coefficients that depend on the low-order cumulants (or moments) of the underlying data. One can directly use the preceding result, but computation of the polynomial coefficients in a(t) is theoretically demanding. The bootstrap provides an alternative.

The bootstrap version of T is the statistic T∗, which has Edgeworth expansion

Pr[T∗ ≤ t|Fb] = Φ(t) + N−1/2ba(t)φ(t) + Op(N−1),

where Fb is the empirical distribution function of the sample. If ba(t) =

a(t) + Op(N−1/2), which is often the case, then

Pr[T ≤ t|F] = Pr[T∗ ≤ t|Fb] + Op(N−1). (10) This statement means that the bootstrap cdf Pr[T∗ ≤ t|Fb] is within Op(N−1) of the unknown true cdf Pr[T ≤ t|F], which is a better approximation than one gets using Φ(t), since the standard normal cdf is within O(N−1/2) and Pr[O(N−1/2) − Op(N−1) > 0] gets arbitrarily close to 1 for sufficiently large N.

What if we use a nonpivotal statistic T? Suppose T ∼a N[0,σ2] so that T/s ∼a N[0,1] where s is a consistent estimate of the standard error. Then

Edgeworth expansions still apply, but now

Pr[T ≤ t|F] = Φ(t/σ) + N−1/2b(t/σ)φ(t/σ) + O(N−1),

for some quadratic function b(·) 6= a(·), and similarly for the bootstrap estimates

Pr[T∗ ≤ t|Fb] = Φ(t/s) + N−1/2bb(t/s)φ(t/s) + Op(N−1).

Now, even if bb(·) = b(·) + Op(N−1/2), these functions are evaluated at t/s where usually s = σ + Op(N−1/2). It follows for nonpivotal T that

Pr[T ≤ t|F] = Pr[T∗ ≤ t|Fb] + Op(N−1/2), (11) so there is no asymptotic refinement. Thus nonpivotal statistics bring no improvement in the convergence rate relative to using first-order asymptotic theory.

The main requirement for the asymptotic refinement (10) is that an asymptotically pivotal statistic is the object being bootstrapped. The bootstrapt procedure does this.

The preceding analysis shows that for tests of nominal size α the true size is α + O(N−j/2) where j = 2 using the bootstrap-t procedure, while j = 1 using the usual asymptotic normal approximation and the percentile

and bootstrap-se procedures. These results for are for a one-sided test or a nonsymmetric two-sided test. For a two-sided symmetric test, cancellation occurs because a(t) is an even function, so one further term in the Edgeworth expansion can be used. Then j = 3 using the bootstrap-t procedure and j = 2 using the other procedures.

## A.2 Bootstrap Procedures

- A.2.1 Bootstrap-t Procedures


We begin with the preferred bootstrap-t procedures using three bootstrap sampling schemes - pairs cluster, residual cluster and wild cluster - that are generalizations of pairs, residual and wild resampling for nonclustered data.

Pairs Cluster Bootstrap-t

- 1. From the original sample form w = (βb1−β0)/sβb

1

, where sβb

1

is obtained

using the CRVE in (3) with ueg = (G/(G − 1))ubg.

- 2. Do B iterations of this step. On the bth iteration:


- (a) Form a sample of G clusters {(y∗

1,X∗

1),...,(y∗

G,X∗

G)} by resampling with replacement G times from the original sample of clusters.

- (b) Calculate the Wald test statistic w∗


b = (βb∗1,b −βb1)/sβb∗

, where βb∗1,b

1,b

and its standard error sβb∗

are obtained from OLS estimation us-

1,b

ing the bth pseudo-sample, sβb∗

is obtained using the same method

1,b

as that in step 1, and βb1 is the original OLS estimate.

- 3. Reject H0 at level α if and only if w < w∗


[α/2] or w > w∗

[1−α/2], where w∗

[q] denotes the qth quantile of w∗

1,...,w∗

B.

We consider two variations of this procedure that use alternative estimators of sβb in both step 1 and in step 2b. First, the pairs cluster CR3 bootstrap-t uses the CRVE in (3) with ueg calculated using the CR3 correction. Second, the pairs cluster BDM bootstrap-T uses default OLS standard errors and is a symmetric version of the Wald test, following BDM (2004).

The remaining bootstrap-t procedures use residual cluster and wild cluster resampling schemes that take advantage of the ability to resample with

the null hypothesis β1 = β01 imposed.

Cluster Residual Bootstrap-t with H0 imposed

1. From OLS estimation on the original sample form w = (βb1 − β0)/sβb

,

1

is obtained using the CRVE in (3) with ueg = (G/(G−1))ubg. Also obtain the restricted OLS estimator βbR that imposes H0 : β1 = β01, and the associated restricted OLS residuals {ubR1 ,...,ubRG}.13

where sβb

1

13The restricted estimator can be obtained by regressing yig −β01x1,ig on a constant and all regressors other than x1,ig.

- 2. Do B iterations of this step. On the bth iteration:

- (a) Form a sample of G clusters {(yb∗

1,X1),...,(yb∗

G,XG)} by resampling with replacement G times from {ubR1 ,...,ubRG} to give {ubR∗

1 ,...,ubR∗

G } and then forming yb∗

g = X0

gβbR + ubR∗

g , g = 1,...,G.

- (b) Calculate the Wald test statistic w∗


b = (βb∗1,b − β01)/sβb∗

1,b

, where

βb∗1,b and its standard error sβb∗

1,b

are obtained from unrestricted

OLS estimation using the bth pseudo-sample, with sβb∗

1,b

computed using the same method as that in step 1.

- 3. Reject H0 at level α if and only if w < w∗


[α/2] or w > w∗

[1−α/2], where w∗

[q] denotes the qth quantile of w∗

1,...,w∗

B.

Hall (1992, pp.184-191) provides theoretical justification for the residual bootstrap for clustered errors. This bootstrap is used as a benchmark in Monte Carlo simulations for the other bootstraps. In practice it is too restrictive as it assumes that ug are iid, ruling out heteroskedasticity across clusters, and that clusters are balanced.

Wild Cluster bootstrap-t with H0 imposed The wild cluster bootstrap-t with H0 imposed follows the same steps

as the cluster residual bootstrap-t with H0 imposed, except that step 2a is replaced as follows:

2a Form a sample of G clusters {(yb∗

1,X1),...,(yb∗

G,XG)} by the following method. For each cluster g = 1,...,G, form either ubR∗

g = ubRg with probability 0.5 or ubR∗

g = −ubRg with probability 0.5 and then form yb∗

g = X0

gβbR + ubR∗

g , g = 1,...,G.

- A variety of weights ag have been proposed for the wild bootstrap. The


ones we use, with ag = 1 with probability 0.5 and ag = −1 with probability 0.5 are called Rademacher weights. Mammen (1993) actually proposed an alternative set of weights: ag = (1 −

√5)/2 ' −0.6180 with probability

(1 + √5)/2√5 ' 0.7236 and ag = 1 − (1 −

√5)/2 with probability 1 − (1 + √5)/2√5. These weights are the only two-point distribution that satisfy the

constraints E[ag] = 0 and E[a2g] = 1 and the additional constraint E[a3g] = 1, which is necessary to achieve asymptotic refinement if βb is asymmetrically distributed.

- A.2.2 Bootstrap-se Methods


We present the bootstrap-se for pairs cluster resampling.

Pairs Cluster Bootstrap-se

- 1. From the original sample form βb1.
- 2. Do B iterations of this step. On the bth iteration:

- (a) Form a sample of G clusters {(y∗

1,X∗

1),...,(y∗

G,X∗

G)} by resampling with replacement G times from the original sample.

- (b) Calculate the OLS estimate βb∗1,b.


- 3. Reject H0 at level α if and only if |wBSE| > zα/2, where


wBSE = βb1 − β01 sβb

,

1,B

1,B is the bootstrap estimate of the standard error

sβb

(βb∗1b − βb∗1)2!1/2 ,

1,B = Ã 1

XB

sβb

B − 1

b=1

PB

and βb∗1 = B1

βb∗1b.

b=1

This method is easily adapted to the other resampling schemes by appropriately amending steps 1 and 2a.

# B References

Angrist, J. and V. Lavy (2002), “The Effect of High School Matriculation Awards: Evidence from Randomized Trials”, NBER Working Paper Number 9389.

Arellano, M. (1987), “Computing Robust Standard Errors for Within-Group Estimators,” Oxford Bulletin of Economics and Statistics, 49, 431-434.

Bell, R.M. and D.F. McCaffrey (2002), “Bias Reduction in Standard Errors for Linear Regression with Multi-Stage Samples,” Survey Methodology, 169179.

Bertrand, M., E. Duflo and S. Mullainathan (2004), “How Much Should We Trust Differences-in-Differences Estimates?” Quarterly Journal of Economics, 119, 249-275.

Brownstone, D. and Valletta (2001), “The Bootstrap and Multiple Imputations: Harnessing Increased Computing Power for Improved Statistical Tests, Journal of Economic Perspectives, 15(4), 129-141.

Cameron, A.C., Gelbach, J.G., and D.L. Miller (2006), “Bootstrap-Based Improvements for Inference with Clustered Errors,” UC Davis Working Paper

#06-21. Cameron, A.C. and P.K. Trivedi (2005), Microeconometrics: Methods and Applications, Cambridge: Cambridge University Press.

Davidson, R. and E. Flachaire (2001), “The Wild Bootstrap, Tamed at Last,” unpublished manuscript. Davidson, R. and J.G. MacKinnon (1999), “The Size Distortion of Bootstrap Tests,” Econometric Theory, 15, 361-376. Davidson, R. and J.G. MacKinnon (2004), Econometric Theory and Methods, Oxford, Oxford University Press. Davison, A.C. and D.V. Hinkley (1997), Bootstrap Methods and their Application, New York, Cambridge University Press.

Donald, S.G. and K. Lang. (2007), “Inference with Difference-in-Differences and Other Panel Data”, The Review of Economics and Statistics, 89(2), 221233.

Efron, B. (1979), “Bootstrapping Methods: Another Look at the Jackknife,” Annals of Statistics, 7, 1-26. Efron, B. (1981), “Nonparametric Standard Errors and Confidence Inter-

vals,” Canadian Journal of Statistics, 9, 139—172. Efron, B. (1987), “Better Bootstrap Confidence Intervals (with Discussion),” Journal of the American Statistical Association, 82, 171-200.

Efron, B., and J. Tibsharani (1993), An Introduction to the Bootstrap, London, Chapman and Hall.

Flynn, T.N., and Peters, T.J. (2004), “Use of the bootstrap in analysing cost data from cluster randomised trials: some simulation results," BMC Health Services Research, 4:33.

Gruber, J. and J. Poterba (1994), “Tax Incentives and the Decision to Purchase Health Insurance: Evidence from the Self-Employed,” Quarterly Journal of Economics, 109, 701-733.

Hall, P. (1992), The Bootstrap and Edgeworth Expansion, New York: SpringerVerlag.

Horowitz, J.L. (1997), “Bootstrap Methods in Econometrics: Theory and Numerical Performance,” in Advances in Economics and Econometrics: Theory and Applications, Seventh World Congress, D.M. Kreps and K.F.Wallis (Eds.), Volume 3, 188-222, Cambridge, UK, Cambridge University Press.

Horowitz, J.L. (2001), “The Bootstrap,” in Handbook of Econometrics, Volume 5, J.J. Heckman and E. Leamer (Eds.), 3159-3228, Amsterdam, NorthHolland.

Kauermann, G. and R.J. Carroll (2001), “A Note on the Efficiency of Sandwich Covariance Matrix Estimation,” Journal of the American Statistical Association, 96, 1387-1396.

Kézdi, G. (2004), “Robust Standard Error Estimation in Fixed-Effects Models,” Robust Standard Error Estimation in Fixed-Effects Panel Models,” Hungarian Statistical Review, Special Number 9, 95-116.

Kloek, T. (1981), “OLS Estimation in a Model where a Microvariable is Explained by Aggregates and Contemporaneous Disturbances are Equicorrelated,” Econometrica, 49, 205-07.

Liang, K.-Y., and S.L. Zeger (1986), “Longitudinal Data Analysis Using Generalized Linear Models,” Biometrika, 73, 13-22. Liu, R.Y. (1988), “Bootstrap Procedures under Some Non-iid Models,” Annals of Statistics, 16, 1696-1708. MacKinnon, J.G. (2002), “Bootstrap Inference in Econometrics,” Canadian Journal of Economics, 35, 615-645.

MacKinnon, J.G., and H. White (1985), “Some Heteroskedasticity-Consistent Covariance Matrix Estimators with Improved Finite Sample Properties,” Journal of Econometrics, 29, 305-325.

Mammen, E. (1993), “Bootstrap and Wild Bootstrap for High Dimensional Linear Models,” Annals of Statistics, 21, 255-285. Mancl, L.A. and T.A. DeRouen (2001), “A Covariance Estimator for GEE with Improved Finite- Sample Properties,” Biometrics, 57, 126-134. Moulton, B.R. (1986), “Random Group Effects and the Precision of Regression Estimates,” Journal of Econometrics, 32, 385-397.

Moulton, B.R. (1990), “An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units,” Review of Economics and Statistics, 72, 334-38.

Pan, W. and M. Wall (2002), “Small-sample Adjustments in Using the Sandwich Variance Estimator in Generalized Estimating Equation,” Statistics in Medicine, 21, 1429-1441.

Satterthwaite, F.F. (1941), “Synthesis of Variance,” Psychometrika, 6, 309316.

Sherman, M. and S. le Cressie (1997), “A Comparison Between Bootstrap Methods and Generalized Estimating Equations for Correlated Outcomes in Generalized Linear Models,” Communications in Statistics - Simulation and Communication, 26, 901-925.

White, H. (1980), “A Heteroskedasticity-Consistent Covariance Matrix Estimator and a Direct Test for Heteroskedasticity,” Econometrica, 48, 817-838. White, H. (1984), Asymptotic Theory for Econometricians, San Diego: Academic Press. Wooldridge, J.M. (2003), “Cluster-Sample Methods in Applied Econometrics,” American Economic Review, 93, 133-138. Wu, C.F.G. (1986), “Jackknife, Bootstrap and Other Resampling Methods in Regression Analysis,” Annals of Statistics, 14, 1261-1295.

### Table 1: Different Methods for Wald Test

Method Bootstrap? Refinement? H0 imposed? Conventional Wald

- 1. Default (iid errors) No - -
- 2. Moulton type No - -
- 3. Cluster-robust No - -
- 4. Cluster-robust CR3 No - Wald bootstrap-se

- 5. Pairs cluster Yes No -
- 6. Residuals cluster H0 Yes No -
- 7. Wild cluster H0 Yes No BCA test

- 8. Pairs cluster Yes Yes Wald bootstrap-t

- 9. BDM Yes No No
- 10. Pairs cluster Yes Yes No
- 11. Pairs CR3 cluster Yes Yes No
- 12. Residuals cluster H0 Yes Yes Yes
- 13. Wild cluster H0 Yes Yes Yes


Table 2: 1,000 simulations from dgp with group level random errors. Rejection rates for tests of nominal size 0.05 with simulation se's in parentheses.

Number of Groups (G) Estimator 5 10 15 20 25 30 # Method

- 1 Assume iid 0.426 0.479 0.489 0.490 0.504 0.472 (0.016) (0.016) (0.016) (0.016) (0.016) (0.016)
- 2 Moulton-type estimator 0.130 0.084 0.086 0.074 0.080 0.052 (0.011) (0.009) (0.009) (0.008) (0.009) (0.007)
- 3 Cluster Robust 0.195 0.132 0.096 0.093 0.095 0.069 (0.013) (0.011) (0.009) (0.009) (0.009) (0.008)
- 4 CR3 Residual Correction 0.088 0.084 0.065 0.072 0.067 0.057 (0.009) (0.009) (0.008) (0.008) (0.008) (0.007)
- 5 Pairs Cluster Bootstrap - se 0.152 0.122 0.095 0.096 0.100 0.072 (0.011) (0.010) (0.009) (0.009) (0.009) (0.008)
- 6 Residual Cluster Bootstrap - se 0.047 0.049 0.063 0.062 0.066 0.043 (0.007) (0.007) (0.008) (0.008) (0.008) (0.006)
- 7 Wild Cluster Bootstrap - se 0.012 0.031 0.039 0.041 0.056 0.040 (0.003) (0.005) (0.006) (0.006) (0.007) (0.006)
- 8 Pairs Cluster Bootstrap - BCA 0.161 0.106 0.101 0.087 0.094 0.068 (0.012) (0.010) (0.010) (0.009) (0.009) (0.008)
- 9 BDM Bootstrap - t 0.117 0.109 0.094 0.094 0.095 0.068 (0.010) (0.010) (0.009) (0.009) (0.009) (0.008)
- 10 Pairs Cluster Bootstrap - t 0.081 0.082 0.075 0.073 0.070 0.054 (0.009) (0.009) (0.008) (0.008) (0.008) (0.007)
- 11 Pairs CR3 Bootstrap - t 0.081 0.085 0.070 0.072 0.069 0.051 (0.009) (0.009) (0.008) (0.008) (0.008) (0.007)
- 12 Residual Cluster Bootstrap - t 0.034 0.052 0.049 0.044 0.056 0.050

- (0.006) (0.007) (0.007) (0.006) (0.007) (0.007)

13 Wild Cluster Bootstrap - t 0.054 0.062 0.056 0.045 0.060 0.045

- (0.007) (0.008) (0.007) (0.007) (0.008) (0.007)




T_distribution(G-k) 0.145 0.086 0.072 0.066 0.062 0.060

Table 3: 1,000 simulations from dgp with group level random errors and heteroskedasticity. Rejection rates for tests of nominal size 0.05 with simulation se's in parentheses.

Number of Groups (G)

- Estimator 5 10 15 20 25 30 # Method 1 Assume iid 0.302 0.288 0.307 0.295 0.287 0.297


(0.015) (0.014) (0.015) (0.014) (0.014) (0.014) 2 Moulton-type estimator 0.261 0.214 0.206 0.175 0.174 0.180

(0.014) (0.013) (0.013) (0.012) (0.012) (0.012) 3 Cluster Robust 0.208 0.118 0.110 0.081 0.072 0.068

(0.013) (0.010) (0.010) (0.009) (0.008) (0.008) 4 CR3 Residual Correction 0.138 0.092 0.086 0.070 0.062 0.062

- (0.011) (0.009) (0.009) (0.008) (0.008) (0.008)

5 Pairs Cluster Bootstrap - se 0.174 0.111 0.109 0.085 0.074 0.070

- (0.012) (0.010) (0.010) (0.009) (0.008) (0.008)


6 Residual Cluster Bootstrap - se 0.181 0.169 0.183 0.157 0.149 0.163

(0.012) (0.012) (0.012) (0.012) (0.011) (0.012) 7 Wild Cluster Bootstrap - se 0.019 0.041 0.057 0.040 0.038 0.043

(0.004) (0.006) (0.007) (0.006) (0.006) (0.006) 8 Pairs Cluster Bootstrap - BCA 0.183 0.103 0.099 0.082 0.070 0.064

- (0.012) (0.010) (0.009) (0.009) (0.008) (0.008)

9 BDM Bootstrap - t 0.181 0.108 0.110 0.090 0.070 0.068

- (0.012) (0.010) (0.010) (0.009) (0.008) (0.008)


10 Pairs Cluster Bootstrap - t 0.079 0.067 0.074 0.058 0.054 0.053

(0.009) (0.008) (0.008) (0.007) (0.007) (0.007) 11 Pairs CR3 Bootstrap - t 0.064 0.062 0.072 0.057 0.050 0.048

(0.008) (0.008) (0.008) (0.007) (0.007) (0.007) 12 Residual Cluster Bootstrap - t 0.066 0.057 0.066 0.049 0.043 0.047

(0.008) (0.007) (0.008) (0.007) (0.006) (0.007) 13 Wild Cluster Bootstrap - t 0.053 0.056 0.058 0.048 0.041 0.044

(0.007) (0.007) (0.007) (0.007) (0.006) (0.006) T_distribution(G-k) 0.145 0.086 0.072 0.066 0.062 0.060

Table 4: 1,000 simulations from different dgps (see text) and G = 10 groups. Rejection rates for tests of nominal size 0.05 with simulation se's in parentheses.

Unbala nced group sizes (10,50) Estimator Column number 1 2 3 4 5 6 7 8 9

X's are consta nt within group

Reject based on T (8 dof)

4 RHS variabl es

Cluster size = 100

Cluster size = 10

Cluster size = 2

Main from Table 2

X's are iid

# Method

- 1 Assume iid 0.491 0.106 0.268 0.679 0.687 0.770 0.054 0.524 (0.016) (0.010) (0.014) (0.015) (0.015) (0.013) (0.007) (0.016)
- 2 Moulton-type estimator 0.092 0.044 0.095 0.098 0.088 0.089 0.125 0.061 0.129

- (0.009) (0.006) (0.009) (0.009) (0.009) (0.009) (0.010) (0.008) (0.011)

3 Cluster Robust 0.129 0.082 0.137 0.126 0.115 0.129 0.183 0.103 0.183

- (0.010) (0.009) (0.010) (0.010) (0.010) (0.010) (0.013) (0.010) (0.012)


- 4 CR3 Residual Correction 0.090 0.054 0.094 0.086 0.077 0.080 0.090 0.086 0.091

- (0.009) (0.007) (0.009) (0.009) (0.008) (0.009) (0.009) (0.009) (0.009)

5 Pairs Cluster Bootstrap - se 0.120 0.071 0.100 0.114 0.120 0.128 0.063 0.122 0.138

- (0.010) (0.008) (0.009) (0.010) (0.010) (0.010) (0.008) (0.010) (0.011)


- 6 Residual Cluster Bootstrap - se 0.058 0.013 0.069 0.068 0.060 0.057 0.054 0.080 (0.007) (0.004) (0.008) (0.008) (0.008) (0.007) (0.007) (0.009)
- 7 Wild Cluster Bootstrap - se 0.028 0.006 0.048 0.044 0.032 0.030 0.036 0.053 0.019 (0.005) (0.002) (0.007) (0.006) (0.006) (0.005) (0.006) (0.007) (0.004)
- 8 Pairs Cluster Bootstrap - BCA 0.111 0.125 0.112 0.109 0.112 0.100 0.134 0.140 (0.010) (0.010) (0.010) (0.010) (0.010) (0.009) (0.011) (0.011)
- 9 BDM Bootstrap - t 0.119 0.086 0.115 0.112 0.119 0.121 0.097 0.128 (0.010) (0.009) (0.010) (0.010) (0.010) (0.010) (0.009) (0.011)
- 10 Pairs Cluster Bootstrap - t 0.096 0.085 0.083 0.086 0.090 0.066 0.079 0.120 (0.009) (0.009) (0.009) (0.009) (0.009) (0.008) (0.009) (0.010)
- 11 Pairs CR3 Bootstrap - t 0.090 0.075 0.077 0.081 0.084 0.050 0.082 0.110 (0.009) (0.008) (0.008) (0.009) (0.009) (0.007) (0.009) (0.010)
- 12 Residual Cluster Bootstrap - t 0.055 0.052 0.056 0.050 0.043 0.043 0.065

- (0.007) (0.007) (0.007) (0.007) (0.006) (0.006) (0.008)

13 Wild Cluster Bootstrap - t 0.055 0.064 0.056 0.048 0.052 0.045 0.064 0.061

- (0.007) (0.008) (0.007) (0.007) (0.007) (0.007) (0.008) (0.008)




T_distribution(8) 0.086

Table 5: 1,000 simulations from BDM (2004) design. Rejection rates for tests of nominal size 0.05 with simulation se's in parentheses. Size column measures size and power column measures power.

Number of States (G)

- Estimator 6 10 20 50 6 10 20 50 Size Size Size Size Power Power Power Power


# Method

- 1 Assume iid 0.459 0.438 0.461 0.439 0.515 0.506 0.574 0.692 (0.016) (0.016) (0.016) (0.016) (0.016) (0.016) (0.016) (0.015)
- 2 Moulton-type estimator 0.449 0.428 0.454 0.429 0.510 0.490 0.565 0.686 (0.016) (0.016) (0.016) (0.016) (0.016) (0.016) (0.016) (0.015)
- 3 Cluster Robust 0.109 0.088 0.049 0.048 0.165 0.110 0.142 0.254 (0.010) (0.009) (0.007) (0.007) (0.012) (0.010) (0.011) (0.014)
- 4 Pairs Cluster Bootstrap - se 0.001 0.087 0.060 0.058 0.001 0.103 0.161 0.275 (0.001) (0.009) (0.008) (0.007) (0.001) (0.010) (0.012) (0.014)
- 5 Residual Cluster Bootstrap - se 0.043 0.055 0.045 0.048 0.079 0.069 0.127 0.260 (0.006) (0.007) (0.007) (0.007) (0.009) (0.008) (0.011) (0.014)
- 6 Wild Cluster Bootstrap - se 0.043 0.056 0.046 0.047 0.076 0.075 0.134 0.262 (0.006) (0.007) (0.007) (0.007) (0.008) (0.008) (0.011) (0.014)
- 7 Pairs Cluster Bootstrap - BCA 0.087 0.111 0.067 0.061 0.147 0.134 0.166 0.276 (0.009) (0.010) (0.008) (0.008) (0.011) (0.011) (0.012) (0.014)
- 8 BDM Bootstrap - t 0.111 0.086 0.053 0.054 0.161 0.113 0.153 0.270 (0.010) (0.009) (0.007) (0.007) (0.012) (0.010) (0.011) (0.014)
- 9 Pairs Cluster Bootstrap - t 0.006 0.022 0.043 0.061 0.007 0.033 0.112 0.255 (0.002) (0.005) (0.006) (0.008) (0.003) (0.006) (0.010) (0.014)
- 10 Residual Cluster Bootstrap - t 0.046 0.051 0.039 0.044 0.081 0.065 0.118 0.256

- (0.007) (0.007) (0.006) (0.006) (0.009) (0.008) (0.010) (0.014)

11 Wild Cluster Bootstrap - t 0.067 0.053 0.041 0.045 0.110 0.078 0.124 0.247

- (0.008) (0.007) (0.006) (0.007) (0.010) (0.008) (0.010) (0.014)




Table 6: 250 simulations from BDM (2004) design using micro data. Rejection rates for tests of nominal size 0.05 with simulation se's in parentheses.

Number of States (G) Estimator 6 10

Size Size

# Method 1 CRVE cluster on state-year 0.440 0.444

(0.031) (0.031) 3 CRVE cluster on state 0.148 0.100

(0.023) (0.019) 11 Wild Bootstrap-t cluster on state 0.080 0.048

(0.017) (0.014)

Note: Micro regressions control for a quartic in age, three education dummies, and state and year fixed effects. Number of Monte Carlo replications R=250. Nummber of boostrap replications B=199.

