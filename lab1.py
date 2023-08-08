# -*- coding: utf-8 -*-
"""lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12q2ZMZ9zBjL9oxHGCaFPbXrHNaKwG0g_
"""

import numpy as np

# Generate a 4x4 random array from exponential distribution
random_array_4x4 = np.random.exponential(scale=1.0, size=(4, 4))
print("Random 4x4 Array:")
print(random_array_4x4)

import matplotlib.pyplot as plt

# Generate a random 100000x1 array from exponential distribution
random_array_100000 = np.random.exponential(scale=1.0, size=(100000, 1))

# Plot histograms for exponential, uniform, and normal distributions
plt.hist(random_array_100000, density=True, bins=100, histtype="step", color="blue", label="Exponential")
plt.hist(np.random.rand(100000), density=True, bins=100, histtype="step", color="red", label="Uniform")
plt.hist(np.random.randn(100000), density=True, bins=100, histtype="step", color="green", label="Normal")

plt.axis([0, 10, 0, 1.1])
plt.legend(loc="upper right")
plt.title("Random Distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate random data for X and Y within the range [-5, 5]
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)

# Calculate Z = X**2 + Y**2
Z = X**2 + Y**2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z)

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title for the plot
ax.set_title('Z = X^2 + Y^2')

plt.show()

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr


df = pd.read_csv('Pokemon.csv', index_col=0, encoding='latin')


selected_columns = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
selected_df = df[selected_columns]

pearson_corr_matrix = selected_df.corr(method='pearson')


spearman_corr_matrix = selected_df.corr(method='spearman')

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.heatmap(pearson_corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Pearson Correlation')

plt.subplot(1, 2, 2)
sns.heatmap(spearman_corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Spearman Correlation')

plt.tight_layout()
plt.show()

import pandas as pd


df = pd.read_csv('Pokemon.csv', index_col=0, encoding='latin')


new_df = df[['N_total', 'N_bulk', 'N_surface', 'R_avg']]


print("First 20 samples of the DataFrame:")
print(new_df.head(20))


print("Mean for each feature:")
print(new_df.mean())

print("\nStandard Deviation for each feature:")
print(new_df.std())

print("\nQuartile Values for each feature:")
print(new_df.quantile([0.25, 0.50, 0.75]))


import matplotlib.pyplot as plt

plt.figure(figsize=(14, 4))
for i, column in enumerate(new_df.columns):
    plt.subplot(1, 4, i + 1)
    plt.hist(new_df[column], bins=20, edgecolor='black')
    plt.xlabel(column)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


import seaborn as sns

g = sns.PairGrid(new_df)
g.map_upper(sns.histplot)
g.map_diag(sns.histplot, kde=True)
g.map_lower(sns.kdeplot)
plt.show()