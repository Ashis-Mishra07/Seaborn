import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



'''
 to see the statistical relation between 2 or more variables.
 Bivariate Analysis
'''

'''
Plots under this section
    scatterplot
    lineplot
'''



tips = sns.load_dataset('tips')
# The below will show u the same plots
# scatter plot -> axes level function
sns.scatterplot(data=tips ,x='total_bill', y='tip')

# scatter plot -> figure level function
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter')

# To add some additional infos
sns.scatterplot(data=tips ,x='total_bill', y='tip' , hue='sex') # this will represent seprately the male and female
sns.scatterplot(data=tips ,x='total_bill', y='tip' , style='time') # this will show who arrives on which time
sns.scatterplot(data=tips ,x='total_bill', y='tip' , size='size') # this will show the size of the group



# Line Plot
# This is basically the scatter plot but with the line connecting the points

gap = px.data.gapminder()
temp_df = gap[gap['country'] == 'India']

# axes level function
sns.lineplot(data=temp_df, x='year', y='lifeExp')
# using relpplot
sns.relplot(data=temp_df, x='year', y='lifeExp', kind='line')


'''
Since relplot has the figure level control so it can kepp the legend outside the graph
but the lineplot has the axes levl control so it will keep it within the graph only
'''




# Facet Plot -> figure level function -> work with relplot
# This is used to plot multiple graphs in a single figure
# instead of hue use col that will separate every sex in different graph
sns.relplot(data=tips, x='total_bill', y='tip', kind='line', col='sex', row='day') # on row based on day and col based on sex

# NOTE:# it will not work with scatterplot and lineplot



# col wrap
# to wrap it , the below will show 3 columns in a row
sns.relplot(data=gap, x='lifeExp', y='gdpPercap', kind='scatter', col='year', col_wrap=3)











