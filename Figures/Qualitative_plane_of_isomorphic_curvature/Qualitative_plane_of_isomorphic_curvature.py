"""

This python script creates the Diverging Bar Chart used to represent the qualitative data
observed in Figure 18 of Siegfried Thomas Bok's 1929 work “Der Einfluß der in den Furchen und 
Windungen auftretenden Krümmungen der Großhirnrinde auf die Rindenarchitektur” (“The Influence of
the Curvature Occurring in the Folds and Turns of the Cerebral Cortex on Cortical Architecture”).

Figure 18 is used to qualitiatively provide proof of the “plane of isomorphic curvature” being 
located primarily in the forth lamina in gyral folds and the second lamina in sulcal folds.

"""
#///// Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.spines as sp
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter

#///// Figure 18 thickness categories
category_names = ['--', '-',
                  '0', '+', '++']

#///// Figure 18 qualitative thickness measurements for all fold regions 
# NOTE 1: This goes in order of decreased to increased thickness
# NOTE 2: "Temperopolar area, right, very curved" was excluded because: stark deviation 
#         from other folds, extraneous previously unnoticed curvature at the fold bottom

# Sulci
sulci_df_less_curv_temp_r_removed = pd.DataFrame({
    "--": [0, 0, 28,26, 28, 29],
    "-": [1, 1, 1, 1, 1, 0],
    "0": [1, 19, 0, 0, 0, 0],
    "+": [1, 7, 0, 0, 0,0],
    "++": [26,2,0,0, 0, 0]
    }, 
    index=['I', 'II', 'III', 'IV', 'V', 'VI'])
sulci_title = 'sulcal'

# Gyri
gyri_df_less_curv_temp_r_removed = pd.DataFrame({
    "--": [17, 13, 17, 0, 0, 0],
    "-": [3, 6, 2, 3, 0, 0],
    "0": [4, 9, 1, 16, 1, 1],
    "+": [4, 0, 1, 2, 5, 0],
    "++": [0,0,6,5, 22, 27]
    }, 
    index=['I', 'II', 'III', 'IV', 'V', 'VI'])
gyri_title = 'gyral'

#///// Plotting function
def stacked_bar(df, title):
    sns.set(style='white')
    sns.set_style('ticks')
    plt.rcParams["figure.figsize"] = [8, 4]
    plt.rcParams['savefig.dpi'] = 500
    plotdata = df
    plotdata.plot(kind="bar", stacked=True, color=['#0000FF', '#7879FF', '#FDFD96', 
        '#F07470', '#DC1C13'], edgecolor = 'black').legend(bbox_to_anchor=(0.06, 1.0), 
        ncol=5, fontsize=15)
    plt.xticks(rotation=0, horizontalalignment="center", color='black', size=15)
    plt.tick_params(axis='x', labelcolor='black', direction='out', length=8, width=1.5, labelsize=15)
    plt.yticks(np.arange(0, 30, step=4))
    plt.tick_params(axis='y', labelcolor='black', direction='out', length=8, width=1.5, labelsize=15)
    plt.xlabel('Lamina', size=15)
    plt.ylabel('# of ' + title + ' folds' , size=15)
    sns.despine(left=False, bottom=False, right=True, top=True)
    plt.savefig('isomorphic_curvature_'+ title + '.png', bbox_inches='tight', pad_inches=1)
    plt.show()

#///// Plot the stacked bar charts
stacked_bar(sulci_df_less_curv_temp_r_removed, sulci_title)
stacked_bar(gyri_df_less_curv_temp_r_removed, gyri_title)

