import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

'''
Categorical Scatter Plot
    Stripplot
    Swarmplot
Categorical Distribution Plots
    Boxplot
    Violinplot
Categorical Estimate Plot -> for central tendency
    Barplot
    Pointplot
    Countplot
'''

# Categorical Scatter Plot

# strip plot
# axes level function
sns.stripplot(data=tips,x='day',y='total_bill')
sns.stripplot(data=tips,x='day',y='total_bill',jitter=False ) # jitter -> to avoid overlapping / noise


# using catplot
# figure level function
sns.catplot(data=tips, x='day',y='total_bill',kind='strip')
# jitter
sns.catplot(data=tips, x='day',y='total_bill',kind='strip',jitter=0.2,hue='sex')


# swarmplot
sns.catplot(data=tips, x='day',y='total_bill',kind='swarm') # figure level function
sns.swarmplot(data=tips, x='day',y='total_bill') # axes level function





# Categorical Distribution Plots

# Boxplot
'''
A boxplot is a standardized way of displaying the distribution of data based on a five number summary 
(“minimum”, first quartile [Q1], median, third quartile [Q3] and “maximum”). 

It can tell you about your outliers and what their values are. 
Boxplots can also tell you if your data is symmetrical, how tightly your data is grouped and 
if and how your data is skewed.
'''


# Box plot
sns.boxplot(data=tips,x='day',y='total_bill') # axes level function

# Using catplot
sns.catplot(data=tips,x='day',y='total_bill',kind='box') # figure level function

# single boxplot -> numerical col
sns.boxplot(data=tips,y='total_bill')





# Violinplot = (Boxplot + KDEplot)

# violinplot
sns.violinplot(data=tips,x='day',y='total_bill')
sns.catplot(data=tips,x='day',y='total_bill',kind='violin')




# Categorical Estimate Plot -> for central tendency

# barplot
# some issue with errorbar
import numpy as np
sns.barplot(data=tips, x='sex', y='total_bill',hue='smoker',estimator=np.min)

# When there are multiple observations in each category, it also uses bootstrapping to compute a 
# confidence interval around the estimate, which is plotted using error bars


# point plot
# The point plot basically as like bar plots it does not show u the distribution
# rather like points joining the middle is shown
sns.pointplot(data=tips, x='sex', y='total_bill',hue='smoker',ci=None) # middle bars are not shown



# countplot
'''
A special case for the bar plot is when you want to show the number of observations in each
 category rather than computing a statistic for a second variable. This is similar to a 
 histogram over a categorical, rather than quantitative, variable
'''
sns.countplot(data=tips,x='sex',hue='day')





