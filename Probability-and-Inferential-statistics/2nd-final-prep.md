# Final Preparation

## Exercise 1. The following table is a partial ANOVA Table

The following table is a **partial ANOVA table**.

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

## Solution

### Completed ANOVA Table

To complete the table, we use the following relationships:

1. **Degrees of Freedom for Error $$(df_{Error})$$:** $$df_{Total} - df_{Treatment} = 11 - 2 = 9$$
2. **Sum of Squares for Error (SSE):** $$MSE \times df_{Error} = 20 \times 9 = 180$$
3. **Sum of Squares for Treatment (SST):** $$SSTotal - SSE = 500 - 180 = 320$$
4. **Mean Square for Treatment (MST):** $$SST / df_{Treatment} = 320 / 2 = 160$$
5. **F-statistic (F):** $$MST / MSE = 160 / 20 = 8.00$$

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

### F-Distribution Table ($$\alpha = 0.05$$)

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



**d. Write out the null and alternative hypotheses.**

* $$H_0: \mu_1 = \mu_2 = \mu_3$$ (The means of all treatments are equal)
* $$H_1$$: At least one treatment mean is different from the others.

**e. What is your conclusion regarding the null hypothesis?**

We compare the calculated F-statistic to the critical value:

* Calculated $$F$$: 8.00
* Critical $$F$$: 4.26

Since the calculated $$F (8.00)$$is greater than the critical value$$(4.26)$$, we reject the null hypothesis. There is sufficient evidence at the 0.05 significance level to conclude that there is a significant difference between the treatment means.
