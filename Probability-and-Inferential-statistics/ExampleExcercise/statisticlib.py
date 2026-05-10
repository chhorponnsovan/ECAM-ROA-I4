import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# ─────────────────────────────────────────────────────────────────────────────
# REGRESSION EQUATION
# ─────────────────────────────────────────────────────────────────────────────

def regression_equation(df, y_col, X_cols):
    """
    Fits its own OLS and returns a human-readable regression equation string.

    Args:
        df (pd.DataFrame): Input data.
        y_col (str): Dependent variable column name.
        X_cols (list): Independent variable column names.

    Returns:
        str: e.g. 'Sales = 3.1416 + 0.7200*Price - 1.0500*Cost'
    """
    y      = df[y_col]
    X      = sm.add_constant(df[X_cols])
    params = sm.OLS(y, X).fit().params

    intercept      = params.get('const', 0.0)
    equation_parts = [f"{intercept:.4f}"]

    for col in X_cols:
        coef = params.get(col, 0.0)
        sign = "+" if coef >= 0 else "-"
        equation_parts.append(f"{sign} {abs(coef):.4f}*{col}")

    return f"{y_col} = {' '.join(equation_parts)}"


# ─────────────────────────────────────────────────────────────────────────────
# REGRESSION SUMMARY
# ─────────────────────────────────────────────────────────────────────────────

def regression_summary(df, y_col, X_cols, print_summary=True):
    """
    Fits OLS and prints Excel-style Regression output:
      • Regression Statistics block
      • ANOVA block
      • Coefficients block (coef, SE, t Stat, p, Lower/Upper 95%)

    Args:
        df (pd.DataFrame): Input data.
        y_col (str): Dependent variable column name.
        X_cols (list): Independent variable column names.
        print_summary (bool): Whether to print the formatted output.

    Returns:
        tuple: (results, reg_stats_df, anova_df, coef_df, equation_str)
    """
    y       = df[y_col]
    X       = sm.add_constant(df[X_cols])
    results = sm.OLS(y, X).fit()
    n       = int(results.nobs)

    # ── Regression Statistics ─────────────────────────────────────────────
    reg_stats_df = pd.DataFrame(
        {
            'Value': [
                round(np.sqrt(results.rsquared), 4),
                round(results.rsquared,          4),
                round(results.rsquared_adj,      4),
                round(np.sqrt(results.mse_resid),4),
                n,
            ]
        },
        index=[
            'Multiple R',
            'R Square',
            'Adjusted R Square',
            'Standard Error',
            'Observations',
        ],
    )

    # ── ANOVA block ───────────────────────────────────────────────────────
    df_model = int(results.df_model)
    df_resid = int(results.df_resid)
    df_total = df_model + df_resid
    ss_reg   = round(results.ess,               4)
    ss_res   = round(results.ssr,               4)
    ss_tot   = round(results.ess + results.ssr, 4)
    ms_reg   = round(results.ess / df_model,    4)
    ms_res   = round(results.ssr / df_resid,    4)
    f_val    = round(results.fvalue,            4)
    f_sig    = round(results.f_pvalue,          4)

    anova_df = pd.DataFrame(
        {
            'df': [df_model,  df_resid, df_total],
            'SS': [ss_reg,    ss_res,   ss_tot],
            'MS': [ms_reg,    ms_res,   ''],
            'F':  [f_val,     '',       ''],
            'Significance F': [f_sig,   '',       ''],
        },
        index=['Regression', 'Residual', 'Total'],
    )

    # ── Coefficients block ────────────────────────────────────────────────
    conf        = results.conf_int(alpha=0.05)
    coef_labels = ['Intercept'] + list(X_cols)
    param_keys  = ['const']     + list(X_cols)

    coef_rows = []
    for label, key in zip(coef_labels, param_keys):
        coef_rows.append([
            round(results.params[key],  4),
            round(results.bse[key],     4),
            round(results.tvalues[key], 4),
            round(results.pvalues[key], 4),
            round(conf.loc[key, 0],     4),
            round(conf.loc[key, 1],     4),
        ])

    coef_df = pd.DataFrame(
        coef_rows,
        columns=['Coefficients', 'Standard Error', 't Stat',
                 'P-value', 'Lower 95%', 'Upper 95%'],
        index=coef_labels,
    )

    # ── Equation ──────────────────────────────────────────────────────────
    intercept      = results.params.get('const', 0.0)
    equation_parts = [f"{intercept:.4f}"]
    for col in X_cols:
        coef = results.params.get(col, 0.0)
        sign = "+" if coef >= 0 else "-"
        equation_parts.append(f"{sign} {abs(coef):.4f}*{col}")
    eq = f"{y_col} = {' '.join(equation_parts)}"

    if print_summary:
        sep = "-" * 68
        print(f"\n{'=' * 68}")
        print("  SUMMARY OUTPUT")
        print(f"{'=' * 68}")
        print("\nRegression Statistics")
        print(reg_stats_df.to_string(header=False))
        print(f"\n{sep}")
        print("ANOVA")
        print(anova_df.to_string())
        print(f"\n{sep}")
        print(coef_df.to_string())
        print(f"\n{sep}")
        print(f"Regression Equation: {eq}")
        print(f"{'=' * 68}\n")

    return results, reg_stats_df, anova_df, coef_df, eq


# ─────────────────────────────────────────────────────────────────────────────
# REGRESSION SCATTERPLOT
# ─────────────────────────────────────────────────────────────────────────────

def regression_scatterplot(df, y_col, X_cols, show_plot=True):
    """
    Fits its own OLS and plots scatter plot(s) of the dependent variable
    against each predictor with the regression line overlaid.

    Args:
        df (pd.DataFrame): Input data.
        y_col (str): Dependent variable name.
        X_cols (list): Independent variable names.
        show_plot (bool): Whether to display the plot immediately.

    Returns:
        list: Matplotlib figure objects.
    """
    y       = df[y_col]
    X       = sm.add_constant(df[X_cols])
    results = sm.OLS(y, X).fit()

    # Build equation string internally
    intercept      = results.params.get('const', 0.0)
    equation_parts = [f"{intercept:.4f}"]
    for col in X_cols:
        coef = results.params.get(col, 0.0)
        sign = "+" if coef >= 0 else "-"
        equation_parts.append(f"{sign} {abs(coef):.4f}*{col}")
    equation_str = f"{y_col} = {' '.join(equation_parts)}"

    figs = []

    if len(X_cols) == 1:
        col = X_cols[0]
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(df[col], y, color='blue', label='Data Points', alpha=0.6)
        x_sorted = np.sort(df[col])
        y_line   = results.params['const'] + results.params[col] * x_sorted
        ax.plot(x_sorted, y_line, color='red', linewidth=2,
                label=f'Regression Line\n{equation_str}')
        ax.set_xlabel(col)
        ax.set_ylabel(y_col)
        ax.set_title(f'{y_col} vs {col} with Regression Line')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)
        figs.append(fig)

    else:
        means = df[X_cols].mean()
        for col in X_cols:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.scatter(df[col], y, color='blue', label='Data Points', alpha=0.6)
            x_sorted = np.sort(df[col])
            y_line   = results.params['const'] + results.params[col] * x_sorted
            for other in X_cols:
                if other != col:
                    y_line += results.params[other] * means[other]
            ax.plot(x_sorted, y_line, color='red', linewidth=2,
                    label=f'Partial Regression Line\n{equation_str}')
            ax.set_xlabel(col)
            ax.set_ylabel(y_col)
            ax.set_title(f'{y_col} vs {col} with Partial Regression Line')
            ax.legend(loc='best')
            ax.grid(True, alpha=0.3)
            figs.append(fig)

    if show_plot:
        for fig in figs:
            fig.tight_layout()
            fig.show()

    return figs


# ─────────────────────────────────────────────────────────────────────────────
# CORRELATION
# ─────────────────────────────────────────────────────────────────────────────

def correlation(df, *cols):
    """
    Computes and prints the Pearson correlation matrix in Excel's lower-triangle
    layout (Data Analysis > Correlation).

    Args:
        df (pd.DataFrame): Input data.
        *cols: Column names to include. Defaults to all numeric columns.

    Returns:
        pd.DataFrame: Full correlation matrix.
    """
    corr_data   = df[list(cols)] if cols else df.select_dtypes(include=[np.number])
    corr_matrix = corr_data.corr(method='pearson').round(4)

    # Excel shows lower triangle only
    display = corr_matrix.astype(object)
    for r in range(len(display)):
        for c in range(len(display.columns)):
            if c > r:
                display.iloc[r, c] = ''

    print(f"\n{'=' * 60}")
    print("  Correlation")
    print(f"{'=' * 60}")
    print(display.to_string())
    print(f"{'=' * 60}\n")

    return corr_matrix


# ─────────────────────────────────────────────────────────────────────────────
# REGRESSION INTERVALS
# ─────────────────────────────────────────────────────────────────────────────

def regression_intervals(df, y_col, x_cols, predict_values, alpha=0.05):
    """
    Fits its own OLS and prints confidence and prediction intervals for a new
    observation in Excel Data Analysis style.

    Args:
        df (pd.DataFrame): Input data.
        y_col (str): Dependent variable column name.
        x_cols (list): Independent variable column names.
        predict_values (list): Values for x_cols to predict at.
        alpha (float): Significance level (default 0.05).

    Returns:
        dict: Predicted value with confidence and prediction intervals.
    """
    y       = df[y_col]
    X       = sm.add_constant(df[x_cols])
    results = sm.OLS(y, X).fit()

    pred_input = [1] + list(predict_values)
    frame      = results.get_prediction(pred_input).summary_frame(alpha=alpha)
    pct        = int((1 - alpha) * 100)

    result = {
        'Predicted Value':                      round(frame['mean'].iloc[0],          4),
        f'Lower {pct}% Confidence Interval':    round(frame['mean_ci_lower'].iloc[0], 4),
        f'Upper {pct}% Confidence Interval':    round(frame['mean_ci_upper'].iloc[0], 4),
        f'Lower {pct}% Prediction Interval':    round(frame['obs_ci_lower'].iloc[0],  4),
        f'Upper {pct}% Prediction Interval':    round(frame['obs_ci_upper'].iloc[0],  4),
    }

    input_df  = pd.DataFrame({'Input Value': predict_values}, index=x_cols)
    result_df = pd.DataFrame({'': list(result.values())}, index=list(result.keys()))

    print(f"\n{'=' * 60}")
    print("  Prediction & Intervals")
    print(f"{'=' * 60}")
    print("\nPredictor Input Values")
    print(input_df.to_string())
    print()
    print(result_df.to_string(header=False))
    print(f"{'=' * 60}\n")

    return result


# ─────────────────────────────────────────────────────────────────────────────
# T-TEST
# ─────────────────────────────────────────────────────────────────────────────

def t_test(df, col1, col2,
           paired=False,
           equal_var=True,
           hypothesized_mean_diff=0,
           alpha=0.05):
    """
    Runs a t-test and prints results matching Excel's Data Analysis ToolPak.
    Supports paired, equal-variance (pooled), and unequal-variance (Welch).

    Args:
        df (pd.DataFrame): Input data.
        col1 (str): First variable column name.
        col2 (str): Second variable column name.
        paired (bool): True → paired t-test.
        equal_var (bool): True → pooled (equal variances); False → Welch.
        hypothesized_mean_diff (float): H₀ mean difference (default 0).
        alpha (float): Significance level (default 0.05).

    Returns:
        pd.DataFrame: Full t-test results table.
    """
    x  = df[col1].dropna().values
    y  = df[col2].dropna().values
    n1 = len(x)
    n2 = len(y)

    if paired:
        title     = "t-Test: Paired Two Sample for Means"
        diff      = x - y
        se        = np.std(diff, ddof=1) / np.sqrt(n1)
        df_t      = n1 - 1
        t_stat    = (np.mean(diff) - hypothesized_mean_diff) / se
        pearson_r = np.corrcoef(x, y)[0, 1]

    elif equal_var:
        title  = "t-Test: Two-Sample Assuming Equal Variances"
        sp2    = ((n1-1)*np.var(x, ddof=1) + (n2-1)*np.var(y, ddof=1)) / (n1+n2-2)
        se     = np.sqrt(sp2 * (1/n1 + 1/n2))
        df_t   = n1 + n2 - 2
        t_stat = (np.mean(x) - np.mean(y) - hypothesized_mean_diff) / se
        pearson_r = None

    else:
        title  = "t-Test: Two-Sample Assuming Unequal Variances"
        s1, s2 = np.var(x, ddof=1), np.var(y, ddof=1)
        se     = np.sqrt(s1/n1 + s2/n2)
        df_t   = (s1/n1 + s2/n2)**2 / ((s1/n1)**2/(n1-1) + (s2/n2)**2/(n2-1))
        t_stat = (np.mean(x) - np.mean(y) - hypothesized_mean_diff) / se
        pearson_r = None

    p_two      = 2 * stats.t.sf(abs(t_stat), df_t)
    p_one      = p_two / 2
    t_crit_one = stats.t.ppf(1 - alpha,   df_t)
    t_crit_two = stats.t.ppf(1 - alpha/2, df_t)

    rows = {
        'Mean':                          [round(np.mean(x), 4),        round(np.mean(y), 4)],
        'Variance':                      [round(np.var(x, ddof=1), 4), round(np.var(y, ddof=1), 4)],
        'Observations':                  [n1,                           n2],
    }
    if paired:
        rows['Pearson Correlation']      = [round(pearson_r, 4),        '']
    if equal_var and not paired:
        pooled_var = ((n1-1)*np.var(x, ddof=1) + (n2-1)*np.var(y, ddof=1)) / (n1+n2-2)
        rows['Pooled Variance']          = [round(pooled_var, 4),        '']

    rows['Hypothesized Mean Difference'] = [hypothesized_mean_diff,      '']
    rows['df']                           = [int(round(df_t)),             '']
    rows['t Stat']                       = [round(t_stat, 4),             '']
    rows['P(T<=t) one-tail']             = [round(p_one, 4),              '']
    rows['t Critical one-tail']          = [round(t_crit_one, 4),         '']
    rows['P(T<=t) two-tail']             = [round(p_two, 4),              '']
    rows['t Critical two-tail']          = [round(t_crit_two, 4),         '']

    result_df = pd.DataFrame(rows, index=[col1, col2]).T

    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")
    print(result_df.to_string())
    print(f"{'=' * 60}\n")

    return result_df


# ─────────────────────────────────────────────────────────────────────────────
# F-TEST
# ─────────────────────────────────────────────────────────────────────────────

def f_test(df, col1, col2, alpha=0.05):
    """
    Runs an F-test for equality of variances and prints results matching
    Excel's Data Analysis > F-Test Two-Sample for Variances.

    Args:
        df (pd.DataFrame): Input data.
        col1 (str): First variable column name (higher variance assumed).
        col2 (str): Second variable column name.
        alpha (float): Significance level (default 0.05).

    Returns:
        pd.DataFrame: F-test results table.
    """
    x  = df[col1].dropna().values
    y  = df[col2].dropna().values

    var1, var2 = np.var(x, ddof=1), np.var(y, ddof=1)
    f_stat     = var1 / var2
    df1, df2   = len(x) - 1, len(y) - 1
    p_one      = stats.f.sf(f_stat, df1, df2)
    f_crit     = stats.f.ppf(1 - alpha, df1, df2)

    rows = {
        'Mean':                [round(np.mean(x), 4), round(np.mean(y), 4)],
        'Variance':            [round(var1, 4),        round(var2, 4)],
        'Observations':        [len(x),                len(y)],
        'df':                  [df1,                   df2],
        'F':                   [round(f_stat, 4),      ''],
        'P(F<=f) one-tail':    [round(p_one, 4),       ''],
        'F Critical one-tail': [round(f_crit, 4),      ''],
    }

    result_df = pd.DataFrame(rows, index=[col1, col2]).T

    print(f"\n{'=' * 60}")
    print("  F-Test: Two-Sample for Variances")
    print(f"{'=' * 60}")
    print(result_df.to_string())
    print(f"{'=' * 60}\n")

    return result_df


# ─────────────────────────────────────────────────────────────────────────────
# ONE-WAY ANOVA
# ─────────────────────────────────────────────────────────────────────────────

def anova_one_way(df, *cols, alpha=0.05):
    """
    Runs a one-way ANOVA and prints results matching Excel's
    Data Analysis > Anova: Single Factor (Summary + ANOVA table).

    Args:
        df (pd.DataFrame): Input data.
        *cols: Two or more column names (each column = one group).
        alpha (float): Significance level (default 0.05).

    Returns:
        tuple: (summary_df, anova_df)
    """
    if len(cols) < 2:
        raise ValueError("Provide at least two column names.")

    groups = [df[c].dropna().values for c in cols]

    # ── Summary block ─────────────────────────────────────────────────────
    summary_rows = []
    for name, g in zip(cols, groups):
        summary_rows.append({
            'Groups':   name,
            'Count':    len(g),
            'Sum':      round(float(g.sum()), 4),
            'Average':  round(float(np.mean(g)), 4),
            'Variance': round(float(np.var(g, ddof=1)), 4),
        })
    summary_df = pd.DataFrame(summary_rows).set_index('Groups')

    # ── ANOVA calculations ────────────────────────────────────────────────
    all_vals   = np.concatenate(groups)
    grand_mean = np.mean(all_vals)
    k          = len(groups)
    n_total    = len(all_vals)

    ss_between = float(sum(len(g) * (np.mean(g) - grand_mean)**2 for g in groups))
    ss_within  = float(sum(np.sum((g - np.mean(g))**2)           for g in groups))
    ss_total   = ss_between + ss_within

    df_between = k - 1
    df_within  = n_total - k
    df_total   = n_total - 1

    ms_between = ss_between / df_between
    ms_within  = ss_within  / df_within
    f_stat     = ms_between / ms_within
    p_val      = float(stats.f.sf(f_stat, df_between, df_within))
    f_crit     = float(stats.f.ppf(1 - alpha, df_between, df_within))

    anova_df = pd.DataFrame(
        {
            'Source of Variation': ['Between Groups', 'Within Groups', 'Total'],
            'SS':      [round(ss_between, 4), round(ss_within, 4), round(ss_total, 4)],
            'df':      [df_between,            df_within,            df_total],
            'MS':      [round(ms_between, 4),  round(ms_within, 4),  ''],
            'F':       [round(f_stat, 4),       '',                   ''],
            'P-value': [round(p_val, 4),        '',                   ''],
            'F crit':  [round(f_crit, 4),       '',                   ''],
        }
    ).set_index('Source of Variation')

    print(f"\n{'=' * 60}")
    print("  Anova: Single Factor")
    print(f"{'=' * 60}")
    print("\nSUMMARY")
    print(summary_df.to_string())
    print(f"\nANOVA")
    print(anova_df.to_string())
    print(f"\n  alpha = {alpha}")
    print(f"{'=' * 60}\n")

    return summary_df, anova_df