# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:39:43 2019

@author: naveenn
"""

# Plots for explanatory analysis
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Insurance_data_cleansed.csv')
df = df[:500]

#==== To find Linear relationship =====
#==== Scatter plot graph =====
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV', data = df)

# Coloring the points according to a third variable (Categorical)
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            hue = 'Coverage', data = df)

# Different marker style for each class
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            hue = 'Coverage', style = 'Coverage', data = df)

# Represent four variables by changing the hue and style of each point independently
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            hue = 'Coverage', style = 'Gender', data = df)

# Coloring the points according to a third variable (Numerical)
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            hue="Total Claim Amount", data=df)

# customize the color palette using the string interface to cubehelix_palette()
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            hue="Total Claim Amount", palette="ch:r=-.6,l=.75", data=df)

# Sizing the points according to a third variable (Numerical)
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            size="Total Claim Amount", data=df)

# Size range can be customized
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            size="Total Claim Amount", sizes = (15,200), data=df)

#==== Continuity with line plots =====
# Plotting the aggregated mean and the 95% confidence interval around the mean
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            kind="line", data=df)

# Disable confidance interval 
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            kind="line", ci = None, data=df)

# Plotting the mean and the SD of each datapoint
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            kind="line", ci = 'sd', data=df)

# Turn off aggregation altogether
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            kind="line", estimator = None, data=df) # produce a strange effect when the data have multiple observations at each point

#===== Plotting subsets of data with semantic mappings =====
# Different lines for each class
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
            kind="line", hue = 'Gender', data=df)

# Adding a style semantic to a line plot changes the pattern of dashes
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV', kind="line", 
            hue = 'Coverage', style = 'Gender', data=df)

# Identify subsets by the markers used at each observation
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV', kind="line", 
            hue = 'Coverage', markers = True, style = 'Gender', data=df)

# Alter both the color and style of the lines
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV', kind="line", 
            hue = 'Gender', style = 'Gender', data=df)

# We can select one class and see the plot
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV', kind="line", 
            hue = 'Gender', style = 'Gender', 
            data=df.query('Coverage == "Extended"'))

# When hue is continues variable
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV', kind="line", 
            hue = 'Total Claim Amount', style = 'Gender', data=df.query('Coverage == "Extended"'))

#===== Multiple relationships with facets =====
# Multiple rows
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
           hue = 'Coverage', col = 'Gender', data = df)

# To see across different levels
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
           hue = 'Coverage', col = 'Gender', row = 'Location Code',
           height = 3, data = df)

# using line chart 
sns.relplot(x = 'Monthly Premium Auto', y = 'CLV',
           hue = 'Gender', style = 'Gender', col = 'Employment_Status',
           col_wrap=2, height = 3, kind = 'line', 
           aspect=.75, linewidth=2, data = df)

#===== Categorical Scatter plots =====
# Plot categorical variable 
sns.catplot(x = 'Coverage', y = 'Total Claim Amount', data = df)

# without jitter
sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            jitter = False, data = df)

# Plot without overlapping with distribution
sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            kind = 'swarm', data = df)

# Using hue
sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            hue = 'Gender', kind = 'swarm', data = df)

#===== Distributions of observations within categories =====
# Boxplot of each groups
sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            kind = 'box', data = df)
# Boxplot with hue
sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            hue = 'Gender', kind = 'box', data = df)

# Boxplot like giving more clarity on distribution
sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            hue = 'Gender', kind = 'boxen', data = df)

sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            hue = 'Gender', kind = 'violin', data = df)

sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            hue = 'Gender', kind = 'violin', 
            split = True, data = df)

# Observation along with the summary
g = sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
                kind="violin", inner=None, data=df)
sns.swarmplot(x = 'Coverage', y = 'Total Claim Amount', 
              color="k", size=3, data=df, ax=g.ax);

#=== BarPlot ====
# Simple categorical data
sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            kind = 'bar', data = df)

# With hue              
sns.catplot(x = 'Coverage', y = 'Total Claim Amount', 
            hue = 'Gender', kind = 'bar', data = df)
              
# Count plot showing the count of each group
sns.catplot(x = 'Coverage', palette="ch:.25", kind = 'count', data = df)
# With hue
sns.catplot(x = 'Coverage', hue = 'Gender', 
            palette="ch:.25", kind = 'count', data = df)

#====== Combo chart with mean =====
fig = plt.figure()
ax = fig.gca()

xs = df['Coverage'].unique()
ys = df.groupby(['Coverage']).mean()['Total Claim Amount']

ax.bar(xs, ys)
ax.plot(xs, ys, color='r', marker='o', 
        linestyle='dashed', linewidth=2, markersize=12)
plt.show()       

# Combo chart with grand mean
fig = plt.figure()
ax = fig.gca()

xs = df['Education'].unique()
ys = df.groupby(['Education']).mean()['Total Claim Amount']
grand_mean = [df['Total Claim Amount'].mean()]*len(xs)

ax.bar(xs, ys, color='g', edgecolor = 'b', linewidth = 2, width = 0.5)
ax.plot(xs, grand_mean, color='r', marker='o', 
        linestyle='dashed', linewidth=2, markersize=12)
plt.show()       

#===== Visualizing the distribution of a dataset ======
# Univarient distribution
sns.distplot(df['Total Claim Amount'])

# Histograms
sns.distplot(df['Total Claim Amount'], rug = True)
# Removing line
sns.distplot(df['Total Claim Amount'], rug = True, kde = False)

sns.distplot(df['Total Claim Amount'], bins = 20, rug = True, kde = False)
# Only line
sns.distplot(df['Total Claim Amount'], hist = False, rug = True)

sns.kdeplot(df['Total Claim Amount'])
sns.kdeplot(df['CLV'])

# Joint plots with scatter plot and Histogram
sns.jointplot(x = df['CLV'], y = df['Total Claim Amount'])
# To compare all numerical variables
sns.pairplot(df)

#======== Visualizing linear relationships =======
# Linear regression
sns.regplot(x = 'CLV', y = 'Total Claim Amount', data = df)

sns.lmplot(x = 'CLV', y = 'Total Claim Amount', data = df)

# Conditioning on other variable
sns.lmplot(x = 'CLV', y = 'Total Claim Amount', hue = 'Coverage', data = df)


#====== Pie Chart ====
labels = df.Education.unique()
sizes = df.groupby(['Education']).sum()['Total Claim Amount']
explode = (0, 0.08, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()








