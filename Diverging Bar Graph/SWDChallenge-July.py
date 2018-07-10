import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
import matplotlib.gridspec as gridspec
rc('text', usetex=True)

#Data Prep
Temp_dict_men = {'Men':[18.3,14.7,7.6,4.2,9.3,9.5,9.8,7.1,4.0,3.2,12.3]}
Temp_dict_women = {'Women':[2.4, 6.8,4.2,9.5,3.1,7.1,26.3,10.4,8.4,16.6,5.2]}
Temp_index = ['Road Rage', 'Eating or Drinking', 'Texting', 'Navigation', 'Reading', 'Passenger Distraction','Kids In Car', 'Radio or Music','Weather', 'Shaving or Makeup', 'Other']
df = pd.DataFrame(columns=['Men', 'Women'])
df['Men'] = Temp_dict_men['Men']
df['Women'] = Temp_dict_women['Women']
df['Causes'] = Temp_index
df.set_index('Causes', inplace=True)
#Data Plot
plt.figure(figsize=(3, 2))
gs = gridspec.GridSpec(len(Temp_index)+ 5, 3)
row = 0
loc = gs[row, 0]
ax = plt.subplot(loc)
plt.text(0, 0, r'\underline{Most Common Driving Distractions - Survey Results by Gender}', fontsize=15, weight = 'bold')
plt.axis('off')
highest_cause_men = max(df['Men'])
highest_cause_women = max(df['Women'])

for index in range(len(Temp_index)):
    loc = gs[row+2, 0]
    ax = plt.subplot(loc)
    plt.axis('off')
    if 'Road Rage' in Temp_index[index]:
        req_color = 'cornflowerblue'
    elif 'Eating' in Temp_index[index]:
        req_color = 'orangered'
    elif 'Texting' in Temp_index[index]:
        req_color = 'darkturquoise'
    elif 'Navigation' in Temp_index[index]:
        req_color = 'slateblue'
    elif 'Reading' in Temp_index[index]:
        req_color = 'purple'
    elif 'Passenger' in Temp_index[index]:
        req_color = 'indigo'
    elif 'Kids' in Temp_index[index]:
        req_color = 'blue'
    elif 'Radio' in Temp_index[index]:
        req_color = 'crimson'
    elif 'Weather' in Temp_index[index]:
        req_color = 'dodgerblue'
    elif 'Shaving' in Temp_index[index]:
        req_color = 'navy'
    elif 'Other' in Temp_index[index]:
        req_color = 'limegreen'
    ax.text(0, 0, Temp_index[index])
    if index==0:
        loc = gs[row+1, 1]
        ax = plt.subplot(loc)
        ax.text(0.7, 0, r'\textbf{Men}')
        plt.axis('off')
        loc = gs[row+1, 2]
        ax = plt.subplot(loc)
        ax.text(0, 0, r'\textbf{Women}')
        plt.axis('off')
    loc = gs[row+2, 1]
    ax = plt.subplot(loc)
    ax.set_xlim(0, 35)
    ax.axvspan(0, df['Men'][index], alpha=0.8, color=req_color)
    ax.invert_xaxis()
    if df['Men'][index] == highest_cause_men:
        ax.text(30, 0, str(df['Men'][index]) + "%", fontsize=17, color=req_color)
    else:
        ax.text(30, 0, str(df['Men'][index]) + "%")

    plt.axis('off')
    loc = gs[row+2, 2]
    ax = plt.subplot(loc)
    ax.set_xlim(0, 35)
    ax.axvspan(0, df['Women'][index], alpha=0.8, color=req_color)
    if df['Women'][index] == highest_cause_women:
        ax.text(30, 0, str(df['Women'][index]) + "%", fontsize=17, color=req_color)
    else:
        ax.text(30, 0, str(df['Women'][index]) + "%")

    plt.axis('off')
    row += 1

loc = gs[row+3, 2]
ax = plt.subplot(loc)
plt.text(0,0,'Source:kids4kars.org')
plt.axis('off')
plt.show()
