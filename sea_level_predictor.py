import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit
    lin_1 = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(1880, 2051))
    y1 = lin_1.intercept + lin_1.slope * x1
    plt.plot(x1, y1, color='red')

    # Create second line of best fit
    lin_2 = linregress(data[data['Year'] >= 2000]['Year'], data[data['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = lin_2.intercept + lin_2.slope * x2
    plt.plot(x2, y2, color='green')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
