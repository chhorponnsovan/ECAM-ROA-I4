import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def display_regression_analysis(df, y_col, X_cols):
    """
    Performs OLS regression and displays the regression summary, ANOVA table,
    regression equation, and scatter plot(s) with regression line(s).

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.
        y_col (str): The name of the dependent variable column.
        X_cols (list): A list of names of the independent variable columns.

    Returns:
        tuple: (results, anova_table, equation_str)
    """
    # Prepare data for statsmodels
    y = df[y_col]
    X = df[X_cols]
    X_sm = sm.add_constant(X)

    # Create and fit the OLS model
    model_sm = sm.OLS(y, X_sm)
    results = model_sm.fit()

    # Calculate ANOVA components
    df_model = results.df_model
    df_residual = results.df_resid
    df_total = df_model + df_residual

    ss_model = results.ess  # Explained Sum of Squares (Regression SS)
    ss_residual = results.ssr  # Residual Sum of Squares (Error SS)
    ss_total = ss_model + ss_residual  # Total Sum of Squares

    ms_model = ss_model / df_model
    ms_residual = ss_residual / df_residual

    f_statistic = results.fvalue
    p_value_f = results.f_pvalue

    # Create a DataFrame for the ANOVA table
    anova_data = {
        'df': [df_model, df_residual, df_total],
        'SS': [ss_model, ss_residual, ss_total],
        'MS': [ms_model, ms_residual, ''],
        'F': [f_statistic, '', ''],
        'Significance F': [p_value_f, '', '']
    }
    anova_table = pd.DataFrame(anova_data, index=['Regression', 'Residual', 'Total'])

    # Build regression equation string
    equation_parts = [f"{results.params.iloc[0]:.4f}"]
    for i, col in enumerate(X_cols):
        coef = results.params.iloc[i + 1]
        sign = "+" if coef >= 0 else "-"
        equation_parts.append(f"{sign} {abs(coef):.4f}*{col}")
    equation_str = f"{y_col} = {' '.join(equation_parts)}"

    print("\n--- OLS Regression Summary ---")
    print(results.summary())
    print("\n--- Custom ANOVA Table ---")
    print(anova_table.round(4).to_string())
    print("\n--- Regression Equation ---")
    print(equation_str)

    # Plotting scatter plot with regression line(s)
    if len(X_cols) == 1:
        col = X_cols[0]
        plt.figure(figsize=(8, 6))
        plt.scatter(df[col], y, color='blue', label='Data Points', alpha=0.6)

        X_sorted = np.sort(df[col])
        y_line = results.params.iloc[0] + results.params.iloc[1] * X_sorted
        plt.plot(X_sorted, y_line, color='red', linewidth=2, label='Regression Line')

        plt.xlabel(col)
        plt.ylabel(y_col)
        plt.title(f'Scatter Plot of {y_col} vs {col} with Regression Line')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    else:
        for col in X_cols:
            plt.figure(figsize=(8, 6))
            plt.scatter(df[col], y, color='blue', label='Data Points', alpha=0.6)
            plt.xlabel(col)
            plt.ylabel(y_col)
            plt.title(f'Scatter Plot of {y_col} vs {col}')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.show()
        print("\nMultiple independent variables detected. The regression equation is displayed above, but a single 2D regression line plot is only available for one predictor.")

    return

