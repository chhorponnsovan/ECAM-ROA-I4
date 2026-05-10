# Final Preparation
- [Final Preparation](#final-preparation)
  - [Exercise 1.](#exercise-1)
    - [Solution - 1](#solution---1)
  - [Exercise 2.](#exercise-2)
    - [Solution - 2](#solution---2)
  - [Exercise 3.](#exercise-3)
    - [Solution - 3](#solution---3)
  - [Exercise 4](#exercise-4)
    - [Solution](#solution)
- [Table](#table)
  - [F-Distribution Table ($$\\alpha = 0.05$$)](#f-distribution-table-alpha--005)

 ---
 ---

## Exercise 1. 
The following table is a partial ANOVA Table

| Source | Sum of Squares | df | Mean Square | F |
|---|---|---|---|---|
| Treatment | | 2 | | |
| Error | | | 20 | |
| Total | 500 | 11 | | |

Complete the table and answer the following questions. Use the $$\alpha = 0.05$$ significance level.

a. How many treatments are there?

b. What is the total sample size?

c. What is the critical value of $$F$$?

d. Write out the null and alternative hypotheses.

e. What is your conclusion regarding the null hypothesis?


---


### Solution - 1

The Completed ANOVA Table

To complete the table, we use the following relationships:

1. Degrees of Freedom for Error $$(df_{Error})$$: $$df_{Total} - df_{Treatment} = 11 - 2 = 9$$
2. Sum of Squares for Error (SSE): $$MSE \times df_{Error} = 20 \times 9 = 180$$
3. Sum of Squares for Treatment (SST): $$SSTotal - SSE = 500 - 180 = 320$$
4. Mean Square for Treatment (MST): $$SST / df_{Treatment} = 320 / 2 = 160$$
5. F-statistic (F): $$MST / MSE = 160 / 20 = 8.00$$

| Source | Sum of Squares | df | Mean Square | F |
|---|---|---|---|---|
| **Treatment** | 320 | 2 | 160 | 8.00 |
| **Error** | 180 | 9 | 20 | |
| **Total** | 500 | 11 | | |

**a. How many treatments are there?**

The degrees of freedom for treatment is $$k - 1$$, where $$k$$ is the number of treatments.
$$2 = k - 1 \implies k = 3$$
There are 3 treatments.

**b. What is the total sample size?**

The total degrees of freedom is $$n - 1$$, where $$n$$ is the total sample size.
$$11 = n - 1 \implies n = 12$$
The total sample size is 12.

**c. What is the critical value of F?**

Using the F-distribution table with $$\alpha = 0.05$$, numerator $$df = 2$$, and denominator $$df = 9$$:
$$F_{0.05}(2, 9) \approx 4.26$$



**d. Write out the null and alternative hypotheses.**

* $$H_0: \mu_1 = \mu_2 = \mu_3$$ (The means of all treatments are equal)
* $$H_1$$: At least one treatment mean is different from the others.

**e. What is your conclusion regarding the null hypothesis?**

We compare the calculated F-statistic to the critical value:

* Calculated $$F$$: 8.00
* Critical $$F$$: 4.26

Since the calculated $$F$$: 8.00 is greater than the critical value $$(4.26)$$, we reject the null hypothesis. There is sufficient evidence at the 0.05 significance level to conclude that there is a significant difference between the treatment means.


---
---


## Exercise 2. 

The results of a one-way ANOVA are reported below.

| Source of Variation | SS | df | MS | F |
| :--- | :--- | :--- | :--- | :--- |
| Between Groups | 6.90 | 2 | 3.45 | 5.15 |
| Within Groups | 12.04 | 18 | 0.67 | |
| Total | 18.94 | 20 | | |

Answer the following questions.

a. How many treatments are in the study?

b. What is the total sample size?

c. What is the critical value of $$F$$? (Using $$\alpha = 0.05$$)

d. Write out the null hypothesis and the alternative hypothesis.

e. What is your decision regarding the null hypothesis?

f. Can we conclude that any of the treatment means differ?

---

### Solution - 2

**a. How many treatments are in the study?**

The degrees of freedom for Between Groups is $$k - 1$$, where $$k$$ is the number of treatments (groups).
$$2 = k - 1 \implies k = 3$$
There are 3 treatments in the study.

**b. What is the total sample size?**

The total degrees of freedom is $$n - 1$$, where $$n$$ is the total sample size.
$$20 = n - 1 \implies n = 21$$
The total sample size is 21.

**c. What is the critical value of $$F$$?**

Using an F-distribution table with $$\alpha = 0.05$$, numerator degrees of freedom ($$df_{Between}$$) = 2, and denominator degrees of freedom ($$df_{Within}$$) = 18:
$$F_{0.05}(2, 18) = 3.55$$

**d. Write out the null hypothesis and the alternative hypothesis.**

* $$H_0$$: $$\mu_1 = \mu_2 = \mu_3$$ (The means of all treatments are equal)
* $$H_1$$: At least one treatment mean is different from the others.

**e. What is your decision regarding the null hypothesis?**

We compare the calculated F-statistic from the table to the critical value:
* Calculated $$F$$: 5.15
* Critical $$F$$: 3.55

Since the calculated $$F (5.15)$$ is greater than the critical value $$(3.55)$$, we reject the null hypothesis.

**f. Can we conclude that any of the treatment means differ?**

Yes. Because we rejected the null hypothesis, there is sufficient evidence at the 0.05 significance level to conclude that there is a statistically significant difference between at least two of the treatment means.


---
---


## Exercise 3. 
**Fuel Efficiency ANOVA Analysis**

The fuel efficiencies for a sample of 27 compact, midsize, and large cars are analyzed using ANOVA to investigate whether there is a difference in the mean miles per gallon (MPG) for the three car sizes.

Significance Level: $$\alpha = 0.01$$

**Summary Statistics**
| Group | Sample Size | Sum | Average | Variance |
| :--- | :--- | :--- | :--- | :--- |
| Compact | 12 | 268.3 | 22.35833 | 9.388106 |
| Midsize | 9 | 172.4 | 19.15556 | 7.315278 |
| Large | 6 | 100.5 | 16.75 | 7.303 |

**ANOVA Table**
| Source of Variation | SS | df | MS | F | p-value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Between Groups | 136.4803 | 2 | 68.24014 | 8.258752 | 0.001866 |
| Within Groups | 198.3064 | 24 | 8.262766 | | |
| Total | 334.7867 | 26 | | | |

---

### Solution - 3

**A. State the null hypothesis and the alternative hypothesis.**

* **$$H_0$$:** $$\mu_{Compact} = \mu_{Midsize} = \mu_{Large}$$ (The mean fuel efficiency is the same for all three car sizes)
* **$$H_1$$:** At least one of the mean fuel efficiencies is different from the others.

**B. What is the value of the test statistic $$F$$?**

From the ANOVA table provided:
$$F = 8.258752$$

**C. What is the $$p$$-value?**

From the ANOVA table provided:
$$p\text{-value} = 0.001866$$

**D. State the decision rule at the $$\alpha = 0.01$$ level.**

The decision rule for a $$p$$-value approach is:
* Reject $$H_0$$ if $$p\text{-value} \le \alpha$$
* Fail to reject $$H_0$$ if $$p\text{-value} > \alpha$$

In this case: Reject $$H_0$$ if $$0.001866 \le 0.01$$ .

(Alternatively, using the critical value approach: For $$df_1 = 2, df_2 = 24$$ at $$\alpha = 0.01$$, the critical $$F$$ is approximately $$5.61$$. We reject $$H_0$$ if $$F_{calculated} > 5.61$$).

**E. What is your conclusion regarding the mean miles per gallon for the three car sizes?**

Since the $$p\text{-value} (0.001866)$$ is less than the significance level $$\alpha (0.01)$$, we reject the null hypothesis.

Thus, there is sufficient evidence at the 0.01 significance level to conclude that there is a statistically significant difference in the mean fuel efficiency (miles per gallon) between compact, midsize, and large cars.


---
---


## Exercise 4


The *Mozart effect* refers to a boost of average performance on tests for elementary school students if the students listen to Mozart's chamber music for a period of time immediately before the test. Many educators believe that such an effect is not necessarily due to Mozart's music *per se* but rather to a relaxation period before the test.

To support this belief, an elementary school teacher conducted an experiment by dividing her third-grade class of 15 students into three groups of 5 students each:

* **Group 1:** Self-administered facial massage before the test.
* **Group 2:** Listened to Mozart's chamber music for 15 minutes before the test.
* **Group 3:** Listened to Schubert's chamber music for 15 minutes before the test.

The test scores of the 15 students are given below:

| Group 1 | Group 2 | Group 3 |
| :---: | :---: | :---: |
| 79 | 82 | 80 |
| 81 | 84 | 81 |
| 80 | 86 | 71 |
| 89 | 91 | 90 |
| 86 | 82 | 86 |

Using the one-way ANOVA $$F$$-test at the $$10\%$$ level of significance, answer the following questions:

a. How many treatments are in the study?

b. What is the total sample size?

c. What is the critical value of $$F$$?

d. Write out the null hypothesis and the alternative hypothesis.

e. What is your decision regarding the null hypothesis?

f. Does the data provide sufficient evidence to conclude that any of the three relaxation methods performs better than the others?

---

### Solution

**Completed ANOVA Table**

First, we calculate the necessary sums and means:
* **Group 1 Mean ($$\bar{x}_1$$):** $$83.0$$
* **Group 2 Mean ($$\bar{x}_2$$):** $$85.0$$
* **Group 3 Mean ($$\bar{x}_3$$):** $$81.6$$
* **Grand Mean ($$\bar{x}_G$$):** $$83.2$$

**Calculations:**
1.  **$$SS_{Between}$$:** $$5 \times [(83.0 - 83.2)^2 + (85.0 - 83.2)^2 + (81.6 - 83.2)^2] = 29.20$$
2.  **$$SS_{Within}$$:** Sum of squared deviations within each group = $$335.20$$
3.  **$$MS_{Between}$$:** $$SS_{Between} / df_{Between} = 29.20 / 2 = 14.60$$
4.  **$$MS_{Within}$$:** $$SS_{Within} / df_{Within} = 335.20 / 12 \approx 27.933$$
5.  **$$F$$-statistic:** $$14.60 / 27.933 \approx 0.523$$

| Source of Variation | Sum of Squares | df | Mean Square | F |
| :--- | :--- | :--- | :--- | :--- |
| Between Groups | 29.20 | 2 | 14.60 | 0.523 |
| Within Groups | 335.20 | 12 | 27.93 | |
| **Total** | 364.40 | 14 | | |

**Answers to Questions**

**a. How many treatments are in the study?**


There are 3 treatments (Group 1, Group 2, and Group 3).

**b. What is the total sample size?**


There are 5 students in each of the 3 groups, so $$n = 15$$.

**c. What is the critical value of $$F$$?**


Using the F-distribution table with $$\alpha = 0.10$$, numerator $$df = 2$$, and denominator $$df = 12$$:
$$F_{0.10}(2, 12) \approx 2.81$$

**d. Write out the null hypothesis and the alternative hypothesis.**
* $$H_0$$: $$\mu_1 = \mu_2 = \mu_3$$ (The mean test scores are equal for all relaxation methods)
* $$H_1$$: At least one treatment mean is different from the others.

**e. What is your decision regarding the null hypothesis?**
Compare the calculated $$F$$ to the critical value:
* Calculated $$F$$: $$0.523$$
* Critical $$F$$: $$2.81$$

Since the calculated $$F (0.523)$$ is less than the critical value $$(2.81)$$, we fail to reject the null hypothesis.

**f. Does the data provide sufficient evidence to conclude that any of the three relaxation methods performs better than the others?**


No. At the $$10\%$$ significance level, there is not enough evidence to conclude that there is a significant difference in performance between the relaxation methods.


















# Table 
## F-Distribution Table ($$\alpha = 0.05$$)

| $$df_2 \setminus df_1$$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 161.45 | 199.50 | 215.71 | 224.58 | 230.16 | 233.99 | 236.77 | 238.88 | 240.54 | 241.88 |
| **2** | 18.51 | 19.00 | 19.16 | 19.25 | 19.30 | 19.33 | 19.35 | 19.37 | 19.38 | 19.40 |
| **3** | 10.13 | 9.55 | 9.28 | 9.12 | 9.01 | 8.94 | 8.89 | 8.85 | 8.81 | 8.79 |
| **4** | 7.71 | 6.94 | 6.59 | 6.39 | 6.26 | 6.16 | 6.09 | 6.04 | 6.00 | 5.96 |
| **5** | 6.61 | 5.79 | 5.41 | 5.19 | 5.05 | 4.95 | 4.88 | 4.82 | 4.77 | 4.74 |
| **6** | 5.99 | 5.14 | 4.76 | 4.53 | 4.39 | 4.28 | 4.21 | 4.15 | 4.10 | 4.06 |
| **7** | 5.59 | 4.74 | 4.35 | 4.12 | 3.97 | 3.87 | 3.79 | 3.73 | 3.68 | 3.64 |
| **8** | 5.32 | 4.46 | 4.07 | 3.84 | 3.69 | 3.58 | 3.50 | 3.44 | 3.39 | 3.35 |
| **9** | 5.12 | 4.26 | 3.86 | 3.63 | 3.48 | 3.37 | 3.29 | 3.23 | 3.18 | 3.14 |
| **10** | 4.96 | 4.10 | 3.71 | 3.48 | 3.33 | 3.22 | 3.14 | 3.07 | 3.02 | 2.98 |
| **11** | 4.84 | 3.98 | 3.59 | 3.36 | 3.20 | 3.09 | 3.01 | 2.95 | 2.90 | 2.85 |
| **12** | 4.75 | 3.89 | 3.49 | 3.26 | 3.11 | 3.00 | 2.91 | 2.85 | 2.80 | 2.75 |
| **13** | 4.67 | 3.81 | 3.41 | 3.18 | 3.03 | 2.92 | 2.83 | 2.77 | 2.71 | 2.67 |
| **14** | 4.60 | 3.74 | 3.34 | 3.11 | 2.96 | 2.85 | 2.76 | 2.70 | 2.65 | 2.60 |
| **15** | 4.54 | 3.68 | 3.29 | 3.06 | 2.90 | 2.79 | 2.71 | 2.64 | 2.59 | 2.54 |
| **16** | 4.49 | 3.63 | 3.24 | 3.01 | 2.85 | 2.74 | 2.66 | 2.59 | 2.54 | 2.49 |
| **17** | 4.45 | 3.59 | 3.20 | 2.96 | 2.81 | 2.70 | 2.61 | 2.55 | 2.49 | 2.45 |
| **18** | 4.41 | 3.55 | 3.16 | 2.93 | 2.77 | 2.66 | 2.58 | 2.51 | 2.46 | 2.41 |
| **19** | 4.38 | 3.52 | 3.13 | 2.90 | 2.74 | 2.63 | 2.54 | 2.48 | 2.42 | 2.38 |
| **20** | 4.35 | 3.49 | 3.10 | 2.87 | 2.71 | 2.60 | 2.51 | 2.45 | 2.39 | 2.35 |
