import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



'''
Distribution Plots

    used for univariate analysis
    used to find out the distribution
    Range of the observation
    Central Tendency
    is the data bimodal?
    Are there outliers?


Plots under distribution plot

    histplot
    kdeplot
    rugplot
'''

# figure level -> displot
# axes level -> histplot -> kdeplot -> rugplot


# plotting univariate histogram
sns.histplot(data=tips, x='total_bill')
sns.displot(data=tips, x='total_bill', kind='hist')

# bins parameter
sns.displot(data=tips, x='total_bill', kind='hist',bins=2)

# It’s also possible to visualize the distribution of a categorical variable using the logic of a histogram. 
# Discrete bins are automatically set for categorical variables

# countplot
sns.displot(data=tips, x='day', kind='hist') 

# hue parameter
sns.displot(data=tips, x='tip', kind='hist',hue='sex')

# element -> step
# If graph is not clear then use element='step' to make the block clear make only the outline
sns.displot(data=tips, x='tip', kind='hist',hue='sex',element='step')




# KDE Plot
# Kernel Density Estimation Plot

# Rather than using discrete bins, a KDE plot smooths the observations with a Gaussian kernel, producing a continuous density estimate
sns.kdeplot(data=tips,x='total_bill')
sns.displot(data=tips,x='total_bill',kind='kde')

# hue -> fill
sns.displot(data=tips,x='total_bill',kind='kde',hue='sex',fill=True,height=10,aspect=2)



# Rugplot

# Plot marginal distributions by drawing ticks along the x and y axes.

# This function is intended to complement other plots by showing the location of individual observations in an unobtrusive way.
sns.kdeplot(data=tips,x='total_bill')
sns.rugplot(data=tips,x='total_bill')




# Bivariate histogram
# A bivariate histogram bins the data within rectangles that tile the plot 
# and then shows the count of observations within each rectangle with the fill color

# sns.histplot(data=tips, x='total_bill', y='tip')
sns.displot(data=tips, x='total_bill', y='tip',kind='hist')


# Bivariate Kdeplot
# a bivariate KDE plot smoothes the (x, y) observations with a 2D Gaussian
sns.kdeplot(data=tips, x='total_bill', y='tip')




