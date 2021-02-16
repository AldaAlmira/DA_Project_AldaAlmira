#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse the top 3 countries in the region over a span of 10 years. 
#Name: ALDA ALMIRA
#Group Name: PYTHON_AMIGOS
#Class: PN2004L
#Date: 10/02/2021
#Version: Version 3
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #show specific country dataframe
    MonthlyVisitor()
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def MonthlyVisitor():

  #load excel data (CSV format) to dataframe - 'df'
  df = pd.read_csv('MonthyVisitors.csv')
  df.columns
  print(df.columns)

  #Picking out specific countries and years
  #Picking out years from 1998 to 2008
  years = df[['Year', 'Month', ' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']][240:371]
  print(years)

  #Picking out countries from Europe Region
  countries = df[[' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']][240:371]

  #Total number of visitors from region
  TotalVisitors = countries.sum(axis=0)
  print()
  print("The total visitor from Europe region: ")
  print()
  print(TotalVisitors)

  #Sort value from descending (biggest on top)
  Top11 = TotalVisitors.sort_values(ascending=False)

  #Top 3 countries
  print()
  print("The top 3 countries with the most number of visitors visiting Singapore: ")
  print()
  print(Top11.head(3))

 
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################