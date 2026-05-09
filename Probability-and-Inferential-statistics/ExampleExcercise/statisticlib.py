import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def regression_summary(df, y_col, X_cols, print_summary=True):
    """
    Fits an OLS regression model and returns the results, ANOVA summary,
    and regression equation.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.
        y_col (str): The name of the dependent variable column.
        X_cols (list): A list of names of the independent variable columns.
        print_summary (bool): Whether to print the summary output.

    Returns:
        tuple: (results, anova_table, equation_str)
    """
    y = df[y_col]
    X = sm.add_constant(df[X_cols])
    model_sm = sm.OLS(y, X)
    results = model_sm.fit()

    anova_table = anova_summary(results)
    equation_str = regression_equation(results, y_col, X_cols)

    if print_summary:
        print("\n--- OLS Regression Summary ---")
        print(results.summary())
        print("\n--- ANOVA Summary ---")
        print(anova_table.round(4).to_string())
        print("\n--- Regression Equation ---")
        print(equation_str)

    return


def regression_equation(results, y_col, X_cols):
    """
    Builds a human-readable regression equation string from the fitted model.

    Args:
        results: The fitted statsmodels regression results object.
        y_col (str): The name of the dependent variable.
        X_cols (list): A list of independent variable names.

    Returns:
        str: The regression equation.
    """
    params = results.params
    intercept = params.get('const', 0.0)
    equation_parts = [f"{intercept:.4f}"]

    for col in X_cols:
        coef = params.get(col, 0.0)
        sign = "+" if coef >= 0 else "-"
        equation_parts.append(f"{sign} {abs(coef):.4f}*{col}")

    return f"{y_col} = {' '.join(equation_parts)}"


def anova_summary(results):
    """
    Creates an ANOVA table from fitted regression results.

    Args:
        results: The fitted statsmodels regression results object.

    Returns:
        pd.DataFrame: ANOVA summary table with df, SS, MS, F, and Significance F.
    """
    df_model = results.df_model
    df_residual = results.df_resid
    df_total = df_model + df_residual

    ss_model = results.ess
    ss_residual = results.ssr
    ss_total = ss_model + ss_residual

    ms_model = ss_model / df_model if df_model != 0 else np.nan
    ms_residual = ss_residual / df_residual if df_residual != 0 else np.nan

    anova_data = {
        'df': [df_model, df_residual, df_total],
        'SS': [ss_model, ss_residual, ss_total],
        'MS': [ms_model, ms_residual, ''],
        'F': [results.fvalue, '', ''],
        'Significance F': [results.f_pvalue, '', '']
    }

    return pd.DataFrame(anova_data, index=['Regression', 'Residual', 'Total'])


def regression_scatterplot(df, y_col, X_cols, results=None, show_plot=True):
    """
    Plots scatter plot(s) of the dependent variable against each predictor and
    overlays the regression line(s). The legend includes the regression equation.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.
        y_col (str): The dependent variable name.
        X_cols (list): A list of independent variable names.
        results: Optional fitted statsmodels regression results object.
        show_plot (bool): Whether to display the plot immediately.

    Returns:
        list: Matplotlib figure objects for the created plots.
    """
    if results is None:
        _, _, _ = regression_summary(df, y_col, X_cols, print_summary=False)
        y = df[y_col]
        X = sm.add_constant(df[X_cols])
        results = sm.OLS(y, X).fit()

    equation_str = regression_equation(results, y_col, X_cols)
    figs = []
    y = df[y_col]

    if len(X_cols) == 1:
        col = X_cols[0]
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(df[col], y, color='blue', label='Data Points', alpha=0.6)

        x_sorted = np.sort(df[col])
        y_line = results.params['const'] + results.params[col] * x_sorted
        ax.plot(x_sorted, y_line, color='red', linewidth=2, label=f'Regression Line ({equation_str})')

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
            y_line = results.params['const'] + results.params[col] * x_sorted

            for other_col in X_cols:
                if other_col != col:
                    y_line += results.params[other_col] * means[other_col]

            ax.plot(x_sorted, y_line, color='red', linewidth=2, label=f'Partial Regression Line ({equation_str})')
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

def correlation(df, *cols, method='pearson', show_heatmap=False):
    """
    Computes and displays the correlation matrix for the specified columns.

    Args:
        df (pd.DataFrame): The input DataFrame.
        *cols: Column names to include in the correlation matrix. If none are
            provided, all numeric columns are used.
        method (str): Correlation method to use ('pearson', 'spearman', 'kendall').
        show_heatmap (bool): Whether to display a heatmap of the correlation matrix.

    Returns:
        pd.DataFrame: The correlation matrix.
    """
    if len(cols) == 0:
        corr_data = df.select_dtypes(include=[np.number])
    else:
        corr_data = df[list(cols)]

    corr_matrix = corr_data.corr(method=method)
    print("\n--- Correlation Matrix ---")
    print(corr_matrix.round(4).to_string())

    if show_heatmap:
        fig, ax = plt.subplots(figsize=(8, 6))
        cax = ax.matshow(corr_matrix, cmap='coolwarm')
        fig.colorbar(cax)
        ax.set_xticks(range(len(corr_matrix.columns)))
        ax.set_yticks(range(len(corr_matrix.index)))
        ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='left')
        ax.set_yticklabels(corr_matrix.index)
        ax.set_title('Correlation Matrix Heatmap')
        plt.tight_layout()
        plt.show()

    return corr_matrix

def regression_intervals(df, y_col, x_cols, predict_values, alpha=0.05):
    """
    Calculates confidence and prediction intervals for a new observation.

    Args:
        df (pd.DataFrame): The pandas DataFrame.
        y_col (str): String name of the dependent variable.
        x_cols (list): List of string names for independent variables.
        predict_values (list): List of values corresponding to x_cols to predict for.
        alpha (float): Significance level (default 0.05 for 95% intervals).

    Returns:
        dict: Predicted value with confidence and prediction intervals.
    """
    X = sm.add_constant(df[x_cols])
    y = df[y_col]
    model = sm.OLS(y, X).fit()
    prediction_input = [1] + list(predict_values)
    prediction_obj = model.get_prediction(prediction_input)
    results_frame = prediction_obj.summary_frame(alpha=alpha)

    return {
        'Predicted Value': results_frame['mean'].iloc[0],
        'Conf. Interval Lower': results_frame['mean_ci_lower'].iloc[0],
        'Conf. Interval Upper': results_frame['mean_ci_upper'].iloc[0],
        'Pred. Interval Lower': results_frame['obs_ci_lower'].iloc[0],
        'Pred. Interval Upper': results_frame['obs_ci_upper'].iloc[0]
    }

