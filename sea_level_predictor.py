import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(12,8))

    plt.scatter(
        df['Year'], 
        df['CSIRO Adjusted Sea Level']
    )

    # Create first line of best fit

    ## Returns tuple=(slope, intercept, rvalue, pvalue)
    lr = linregress(
        df['Year'], 
        df['CSIRO Adjusted Sea Level'],
    )
    
    x = pd.Series([i for i in range(df['Year'].min(), 2050, 1) ])

    ## y = mx + c == y = slope*x + intercept
    plt.plot(
        x, 
        (lr.slope)*x + lr.intercept,
        c = 'r'
    )

    # Create second line of best fit
    x2 = pd.Series([i for i in range(2000, 2051, 1) ])

    lr2 = linregress(
        df[df['Year'] >= 2000]['Year'], 
        df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'],
    )

    plt.plot(
        x2, 
        (lr2.slope)*x2 + lr2.intercept,
        c = 'purple'
    )

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()