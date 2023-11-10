# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:20:13 2023

@author: CHIZOBA MARYANN. ID NO: 
"""

# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# defining functions

# Line Plot Function
def population_growth_line_plot(data):
    
    '''
    This function takes up an argument(country) and plots its population 
    over a period of selected years for ease of understanding in trend
    '''
    
    plt.figure()
    countries = data['Country'].unique()
    
    for country in countries:
        country_data = data[data['Country'] == country]
        plt.plot(country_data['Year'], country_data['Population'], 
                 label=country)
    
    plt.xlabel('Year')
    plt.ylabel('Population in billions')
    plt.title('Population Growth (2015-2020)')
    plt.legend()
    plt.show()
    return


# Bar Plot Function
def total_population_bar_plot(data):
    '''
    This function plots a bar chart to understand the total population 
    of each of the countries over the selected period of time
    '''
    plt.figure()
    plt.subplot(1,2,1)
    total_population = data.groupby('Country')['Population'].sum().sort_values(
        ascending=False)
    
    plt.bar(x=total_population.index, height=total_population.values)
    plt.xlabel('Country')
    plt.ylabel('Total Population in Billions')
    plt.title('Total Population of Each Country')
    plt.xticks(rotation=45)
    plt.show()
    
    plt.subplot(1,2,2)
    total_population = data.groupby('Country')['Density (P/Km²)'].sum().sort_values(
        ascending=False)
    
    plt.bar(x=total_population.index, height=total_population.values)
    plt.xlabel('Country')
    plt.ylabel('Density (P/Km²)')
    plt.title('Density of the country')
    plt.xticks(rotation=45)
    plt.show()
    return

# Scatter Plot Function
def scatter_plots_impact_on_population(data):
    '''
    The scatter plot function will be used to visualize the relationship
    between migrants, median age and fertiity rate to better understand 
    possible drivers of population growth
    '''
    
    plt.figure(figsize=(10,5))

    # Scatter plot: Migrants (net) vs. Population
    plt.subplot(131)
    plt.scatter(data['Migrants (net)'], data['Population'], alpha=0.7)
    plt.xlabel('Migrants (net)')
    plt.ylabel('Population')
    plt.title('Migrants (net) vs. Population')

    # Scatter plot: Median Age vs. Population
    plt.subplot(132)
    plt.scatter(data['Median Age'], data['Population'], alpha=0.7)
    plt.xlabel('Median Age')
    plt.ylabel('Population')
    plt.title('Median Age vs. Population')

    # Scatter plot: Fertility Rate vs. Population
    plt.subplot(133)
    plt.scatter(data['Fertility Rate'], data['Population'], 
                alpha=0.7)
    plt.xlabel('Fertility Rate')
    plt.ylabel('Population')
    plt.title('Fertility Rate vs. Population')

    plt.show()
    return
    
# Reading the dataset
df_pop = pd.read_excel(r"C:\Users\A\OneDrive\Desktop\COUNTRY POPULATION2.xlsx")

# Checking the columns of the data set
print(df_pop.columns)

# Checking the data types in the dataset
print(df_pop.info())

# Checking the statistical distribution of the dataset
print(df_pop.describe())

# Checking for missing values
print(df_pop.isnull().sum())

# Call the functions to display the plots
population_growth_line_plot(df_pop)
total_population_bar_plot(df_pop)
scatter_plots_impact_on_population(df_pop)

