import pandas as pd
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

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

    # Plotting the scatter plot of the dependent variable vs independent variables
    for col in X_cols:
        plt.figure(figsize=(8, 6))
        plt.scatter(df[col], y, color='blue', label='Data Points')
        plt.xlabel(col)
        plt.ylabel(y_col)
        plt.title(f'Scatter Plot of {y_col} vs {col}')
        plt.legend()
        plt.grid()
        plt.show()

    # show the regression line 
    #print y = b0 + b1*x1 + b2*x2 + ... + bn*xn
    print("\n--- Regression Equation ---")
    coefficients = results.params
    equation = f"{y_col} = {coefficients[0]:.4f}"
    for i, col in enumerate(X_cols):
        equation += f" + ({coefficients[i+1]:.4f} * {col})"
    print(equation)
    # first check the xcols ifs there is only one independent variable then we can plot the regression line
    if len(X_cols) == 1:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model_lr = LinearRegression()
        model_lr.fit(X_train, y_train)
        y_pred = model_lr.predict(X_test)

        plt.figure(figsize=(8, 6))
        plt.scatter(X_test, y_test, color='blue', label='Actual')
        plt.plot(X_test, y_pred, color='red', label='Predicted')
        plt.xlabel(X_cols[0])
        plt.ylabel(y_col)
        plt.title(f'Regression Line for {y_col} vs {X_cols[0]}')
        plt.legend()
        plt.grid()
        plt.show()

    ## If there are multiple independent variables, just break the loop and do not plot the regression line as it is not possible to plot in 2D
    else:
        print("\nMultiple independent variables detected. Skipping regression line plot.")