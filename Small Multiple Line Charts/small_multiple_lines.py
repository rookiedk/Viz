#Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#Make a Dataframe
data_dict = {
    'Region' : ['Asia Pacific', 'Asia Pacific', 'North America', 'North America', 'Europe', 'Europe', 'Middle East', 'Middle East', 'Latin America', 'Latin America', 'Other', 'Other'],
    'Year' : [2000, 2016, 2000, 2016, 2000, 2016, 2000, 2016, 2000, 2016, 2000, 2016],
    'contribution': [21, 31, 27, 25, 35, 27, 3, 3.4, 4, 4.4, 10, 9]
}
df = pd.DataFrame.from_dict(data_dict)

#Initialize the figure
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(17, 9))
gs = gridspec.GridSpec(2, 3)
gs.update(wspace=0.1, hspace=0.4)
#Create a color palette
palette = plt.get_cmap('Set1')

#Multiple Line Plot
counter = 0
row = 0
column = 0

for region in df['Region'].unique():
    ax = plt.subplot(gs[row, column])

    #Plot all other Regions
    df2 = df[~(df['Region']==region)]
    df2.groupby('Region').plot(x='Year', y='contribution', color='grey', ax=ax, linewidth=0.7, alpha=0.5, legend=False)
    # Plot required Region's line
    df1 = df[df['Region'] == region]
    legend1 = df[df['Region']==region]['contribution'].iloc[1] - df[df['Region']==region]['contribution'].iloc[0]
    df1.groupby('Region').plot(x='Year', y='contribution', label='{}% change between 2000 and 2016'.format(legend1), color=palette(counter), ax=ax, linewidth=2.4, alpha=0.9)
    #Highlight the beginning of the line plot, Tourism % in 2000
    ax.plot(ax.dataLim.xmin, df1['contribution'][df['Year'] == 2000].values, 'o', color=palette(counter))
    ax.text(ax.dataLim.xmin - 0.5, df1['contribution'][df['Year'] == 2000].values - 2.5, df1['contribution'][df['Year'] == 2000].values[0], color=palette(counter))
    # Highlight the end of the line plot, Tourism % in 2016
    ax.plot(ax.dataLim.xmax, df1['contribution'][df['Year']==2016].values, 'o', color=palette(counter))
    ax.text(ax.dataLim.xmax + 0.1, df1['contribution'][df['Year'] == 2016].values + 0.5, df1['contribution'][df['Year'] == 2016].values[0], color=palette(counter))
    ax.xaxis.label.set_visible(False)
    plt.xlim([1999, 2017])
    xticks = plt.gca().get_xticks().tolist()  # get list of ticks
    xticks = ['',2000, '', '', '', '', '', '', '', 2016, '']
    ax.set_xticklabels(xticks)
    #Add Title
    plt.title(region, loc='left', fontsize=12, fontweight=0, color=palette(counter))
    #Add margins for zooming in
    ax.margins(0.05)
    column+=1
    if column>2:
        column=0
        row+=1
    counter += 1

    #Write text for source, author and note below the bottom 3 plots
    if region == 'Middle East':
        ax.text(ax.dataLim.xmin - 1.5, df1['contribution'][df['Year'] == 2016].values - 7.5, 'Data source:', color='royalblue')
        ax.text(ax.dataLim.xmin + 1.6, df1['contribution'][df['Year'] == 2016].values - 7.5, 'World Travel & Tourism Council', color='black')
    elif region == 'Latin America':
        ax.text(ax.dataLim.xmin - 1.5, df1['contribution'][df['Year'] == 2016].values - 8.5, 'Created by:', color='royalblue')
        ax.text(ax.dataLim.xmin + 1.55, df1['contribution'][df['Year'] == 2016].values - 8.5, 'Deepika A (@rookiedk)', color='black')
    elif region == 'Other':
        ax.text(ax.dataLim.xmin - 1.0, df1['contribution'][df['Year'] == 2016].values - 12.6, 'Created for:', color='royalblue')
        ax.text(ax.dataLim.xmin + 2.2, df1['contribution'][df['Year'] == 2016].values - 12.5, '#SWDChallenge', color='black')
#plt.show()
#Add title
plt.suptitle('What has changed in the Tourism Industry since 2000?\nWho are the top performers in 2016?', fontsize=14, fontweight=3)
pass



