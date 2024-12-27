import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


'''
Regression Plots
    regplot
    lmplot

In the simplest invocation, both functions draw a scatterplot of two variables, x and y, 
and then fit the regression model y ~ x and plot the resulting regression line and 
a 95% confidence interval for that regression.
'''


# axes level
# hue parameter is not available
sns.regplot(data=tips,x='total_bill',y='tip')

# figure level
sns.lmplot(data=tips,x='total_bill',y='tip',hue='sex')



# residplot
sns.residplot(data=tips,x='total_bill',y='tip')















































