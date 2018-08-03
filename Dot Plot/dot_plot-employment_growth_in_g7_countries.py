#Temp
import matplotlib.ticker as plticker
import pandas as pd
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
plt.xkcd();
#Load data
data_source = 'Path to Employment Growth in G-7 Countries.xlsx'
df = pd.read_excel(data_source)
df['Employment Share'] = df['Employment Share'] * 100
df['Net Employment Growth Share'] = df['Net Employment Growth Share'] * 100
df['Difference'] = df['Employment Share'] - df['Net Employment Growth Share']
df = df.sort(columns='Difference').reset_index(drop=True)
#Prepare Data
y_labels = df['Country'].tolist()
y_pos = np.arange(len(y_labels))
x1 = df['Employment Share'].tolist()
x2 = df['Net Employment Growth Share'].tolist()
gs = gridspec.GridSpec(1, 1)
gs.update(wspace=0.1, hspace=0.4)
#Actual Plot
ax = plt.subplot(gs[0, 0])
for i in range(0, len(y_labels)):
    ax.plot((x1[i]),(y_pos[i]), 'o', color='dodgerblue', zorder=5, label='Employment Share' if i == 0 else "")
    ax.plot((x2[i]), (y_pos[i]), 'o', color='darkblue', zorder=5,  label='Net Employment Growth' if i == 0 else "")
    if x1[i] > x2[i]:
        color = 'grey'
        linestyle = '-'
    else:
        color='black'
        linestyle = '--'
    if 'United Kingdom' in y_labels[i]:
        ax.text(x1[i]-6, y_pos[i], y_labels[i])
    elif 'Japan' in y_labels[i]:
        ax.text(x2[i] - 3, y_pos[i], y_labels[i])
    elif 'Italy' in y_labels[i]:
        ax.text(x2[i] - 3, y_pos[i], y_labels[i])
    elif 'Germany' in y_labels[i]:
        ax.text(x1[i] - 4, y_pos[i], y_labels[i])
    elif 'France' in y_labels[i]:
        ax.text(x2[i] - 3, y_pos[i], y_labels[i])
    elif 'Canada' in y_labels[i]:
        ax.text(x1[i] - 3, y_pos[i], y_labels[i])
    else:
        ax.text(x1[i] - 6, y_pos[i], y_labels[i])
    if i==0 or i==4:
        ax.plot((x1[i], x2[i]), (y_pos[i],  y_pos[i]), color=color, linestyle=linestyle, linewidth=1.5,
            label='Employment is greater than Net Employment Growth' if 'grey' in color else 'Employment is lesser than Net Employment Growth')
    else:
        ax.plot((x1[i], x2[i]), (y_pos[i], y_pos[i]), color=color, linestyle=linestyle,linewidth=1.5)
ax.legend(loc='best')
ax.annotate('Canada has the lowest difference with\nEmployment Contribution at 5.1% and Net Employment Growth at 5.2%', xy=(5.5, 3), xytext=(15,3.2),arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3,angleA=0,angleB=-90"))
ax.annotate('USA has the highest difference with\nEmployment Contribution at 42.0% and Net Employment Growth at 55.9%', xy=(40, 0.2), xytext=(40,1.4),arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3,angleA=0,angleB=-90"))
ax.text(-2, -1, 'Note: Countries ordered by decreasing Employment Contribution (%)', color='red')
ax.set_title('Comparison of Actual Employment and Net Employment Growth in G-7 Countries\n(Source : Business Insider)')

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(left=False)
ax.tick_params(labelleft=False)
ax.xaxis.set_major_formatter(plticker.FormatStrFormatter('%.0f%%'))

plt.show()
