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

**d. Write out the null and alternative hypotheses.**

* $$H_0: \mu_1 = \mu_2 = \mu_3$$ (The means of all treatments are equal)
* $$H_1$$: At least one treatment mean is different from the others.

**e. What is your conclusion regarding the null hypothesis?**

We compare the calculated F-statistic to the critical value:

* Calculated $$F$$: 8.00
* Critical $$F$$: 4.26

Since the calculated $$F (8.00)$$is greater than the critical value$$(4.26)$$, we reject the null hypothesis. There is sufficient evidence at the 0.05 significance level to conclude that there is a significant difference between the treatment means.
