import pandas as pd
import statsmodels.api as sm

def display_regression_analysis(df, y_col, X_cols):
    """
    Performs OLS regression and displays the regression summary and a cusle.

    Args:        df (pd.DataFrame): The input DataFrame containing the data.
        y_col (str): The name of the dependent variable column.
        X_cols (list): A list of names of the independent variable columns.
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

    ss_model = results.ess # Explained Sum of Squares (Regression SS)
    ss_residual = results.ssr # Residual Sum of Squares (Error SS)
    ss_total = ss_model + ss_residual # Total Sum of Squares

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

    print("\n--- OLS Regression Summary ---")
    print(results.summary())
    print("\n--- Custom ANOVA Table ---")
    # .to_string() helps with formatting in console output
    print(anova_table.round(4).to_string())
