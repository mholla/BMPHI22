"""

This python script creates the scatter plots of the quantitative relative laminar 
thickness and volume data included in Table 1 of Siegfried Thomas Bok's 1929 work “Der Einfluß 
der in den Furchen und Windungen auftretenden Krümmungen der Großhirnrinde auf die 
Rindenarchitektur” (“The Influence of the Curvature Occurring in the Folds and Turns of the 
Cerebral Cortex on Cortical Architecture”).

Table 1 includes relative laminar thickness and volume measurements taken by Bok. The scatter plots
have been created to more accessibly display how the relative laminar volume barely changes when 
curving from gyri to sulci. Additionally, this script has been written to compare the relative 
laminar thickness between the wall and gyral, and wall and sulcal sections. The associated scatter
plots give quantitative evidence for the existance of a plane of isomorphic curvature. 

This script plots the data found in the associated .csv files for Bok 1929's relative laminar
volume and thickness data.

"""

#///// Imports
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

#///// Scatter plot
def dot_scatter(fileName, evaluation, title, analysis, yticks):
   # Create figure
   plt.figure(dpi=2400)
   # Color palette
   sns.set(style = 'white', palette=['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black', 'black','black','black','black','black','black','black', 'black'])
   # Figure size
   f, ax = plt.subplots(figsize=(25, 25))
   # Data set
   dataframe = pd.read_csv(fileName, error_bad_lines=False, encoding='ISO-8859-1')
   # Draw scatterplot
   sns.stripplot(x='Lamina', y=evaluation, data=dataframe, hue="Lamina", jitter=True, s=20.0, marker="o", c='black', alpha=0.5)
   # Zero line
   x = ['I', 'II', 'III', 'IV', 'V', 'VI']
   y = [0, 0, 0, 0, 0, 0]
   ax.plot(x, y, color='grey',linestyle='dashed', linewidth=12.0)
   # Plot labeling
   f.suptitle(title, fontsize=30, fontweight=1, color='black')
   # x-axis
   ax.tick_params(axis='x', labelcolor='black', direction='out', length=35, width=8, labelsize=60, rotation=0, colors='black')
   ax.set_xticklabels(['I', 'II', 'III', 'IV', 'V', 'VI'])
   ax.set_xlabel('Lamina',size = 60, alpha=1, color='black')
   ax.xaxis.set_label_coords(0.5, -0.08)
   # y-axis
   ax.tick_params(axis='y', labelcolor='black', labelsize = 60, direction='out', length=30, width=6, colors='black')
   ax.set_ylabel(analysis, size = 60, alpha=1, color='black')
   ax.set_yticks(yticks)
   ax.yaxis.set_label_coords(-0.10, 0.5)
   # Secondary axis
   ax2 = ax.secondary_xaxis('bottom')
   secax = ax.twinx()
   ax3 = ax.secondary_yaxis('left')
   # Setting up secondary x-axis
   ax2.tick_params(axis='x', labelcolor='black', direction='out', length=30, width=6, labelsize=0)
   ax3.tick_params(axis='y', labelcolor='black', direction='out', length=0, width=1.5, labelsize=0)
   secax.tick_params(axis='y', labelcolor='black', direction='out', length=0, width=1.5, labelsize=0)
   ax.spines[['left', 'top', 'right','bottom']].set_linewidth(6)
   # Legend
   ax.legend().set_visible(False)
   # Save figure as .PNG
   plt.savefig('Quantitative_recreation_of_'+ evaluation + '.png', bbox_inches='tight', pad_inches=1)

#///// Scatter plot for quantitative law of volume constancy figures
def quantitative_law_of_volume_constancy():
    outputFile = 'Quantitative_law_of_volume_constancy.csv'
    # Order of measured folds
    hue_order_english = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
    yticks = np.arange(-90, 100, step=30)
    # First creating the relative laminar volume figure, then the relative laminar thickness
    analysis = [r'$\overline{V}_g$ - $\overline{V}_s$ (%)', r'$\overline{T}_g$ - $\overline{T}_s$ (%)']
    # Temporary titles for figures
    evaluationList = ['Bok_1929_relative_laminar_volume_difference', 'Bok_1929_relative_laminar_thickness_difference']
    for i, j in zip(analysis, evaluationList):
        title = j + ' (' + outputFile + ')'
        dot_scatter(outputFile, j, title, i, yticks)

#///// Scatter plot for quantitative plane of isomorphic curvature figures
def quantitative_plane_of_isomorphic_curvature():
    outputFile = 'Quantitative_plane_of_isomorphic_curvature.csv'
    # Order of measured folds
    hue_order_english = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
    yticks = np.arange(-90, 100, step=30)
    # First creating the relative laminar volume figure, then the relative laminar thickness
    analysis = [r'$\overline{T}_w$ - $\overline{T}_g$ (%)', r'$\overline{T}_w$ - $\overline{T}_s$ (%)']
    # Temporary titles for figures
    evaluationList = ['Bok_1929_gyri_to_wall_thickness_difference', 'Bok_1929_sulci_to_wall_thickness_difference']
    for i, j in zip(analysis, evaluationList):
        title = j + ' (' + outputFile + ')'
        dot_scatter(outputFile, j, title, i, yticks)

#///// Plot
quantitative_law_of_volume_constancy()
quantitative_plane_of_isomorphic_curvature()
