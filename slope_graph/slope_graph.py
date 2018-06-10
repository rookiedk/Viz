from itertools import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import pandas as pd
import numpy as np


df = pd.read_excel(r'/home/adeepika/Desktop/Viz/Temp/Internet users per 100 ppl.xlsx')
pdf = PdfPages('/home/adeepika/Desktop/test.pdf')
df.dropna()

african_countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde',
    'Cameroon',
    'Central African Republic',
    'Chad',
    'Comoros',
    'Democratic Republic of the Congo',
    'Republic of the Congo',
    'Cote d\'Ivoire',
    'Djibouti',
    'Egypt',
    'Equatorial Guinea',
    'Eritrea',
    'Eswatini',
    'Ethiopia',

    'Gabon',
    'Gambia',
    'Ghana',
    'Guinea',
    'Guinea-Bissau',

    'Kenya',
    'Lesotho',
    'Liberia',
    'Libya',

    'Madagascar',
    'Malawi',
    'Mali',
    'Mauritania',
    'Mauritius',
    'Morocco',
    'Mozambique',

    'Namibia',
    'Niger',
    'Nigeria',

    'Rwanda',
    'Sao Tome and Principe',
    'Senegal',
    'Seychelles',
    'Sierra Leone',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Sudan',
    'Swaziland',
    'Tanzania',
    'Togo',
    'Tunisia',
    'Uganda',
    'Zambia',
    'Zimbabwe']
africa_df = (df.loc[df['Country'].isin(african_countries)]).dropna()
africa_df.reset_index(drop=True, inplace=True)
africa_df_2005 = (africa_df.loc[africa_df['Year'] == africa_df['Year'].unique()[2]]).reset_index(drop=True)

africa_df_2015 = africa_df.loc[africa_df['Year'] == africa_df['Year'].unique()[-1]].reset_index(drop=True)
#One missing country data adjusted through next line
africa_df_2015 = africa_df_2015[africa_df_2015['Country'].isin(africa_df_2005['Country'])].reset_index(drop=True)
#
plt.figure()
ax = plt.subplot(111)
plt.subplots_adjust(right=0.70)

ax.set_xlabel("Year")
#Remove Y-Axis and set background color to white
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.axis('off')
# Highlight the start, middle and end point and begin writing table details
#ax.plot(africa_df_2015['Year'], africa_df_2015['Internet users per 100 people'])
count = 0
for row in zip(africa_df_2005['Internet users per 100 people'], africa_df_2015['Internet users per 100 people']):
    x1, y1 = [2005, 2015], [row[0], row[1]]
    if 'South Africa' in africa_df_2005['Country'].iloc[count]:
        color = 'green'
        marker = 'o'
        linewidth = 2.0
        label = 'South Africa'
    elif 'Egypt' in africa_df_2005['Country'].iloc[count]:
        color = 'red'
        marker = 'o'
        linewidth = 2.0
        label = 'Egypt'
    else:
        color = 'grey'
        marker = None
        linewidth = 0.5
        label = None
    ax.plot(x1, y1, marker=marker, color=color, linewidth=linewidth, label=label)
    count += 1
ax.legend(loc='best')
ax.text(0, 0, 'test')
pdf.savefig()
pass