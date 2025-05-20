import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Example: paste your data here as a multiline string (tab or comma separated)
data_text = """
White,Black,Asian,Latino,Native,Other
80-100%,0-20%,0-20%,0-20%,0-20%,0-20%
60-80%,0-20%,20-40%,0-20%,0-20%,0-20%
60-80%,20-40%,20-40%,20-40%,20-40%,0-20%
80-100%,0-20%,0-20%,0-20%,0-20%,0-20%
60-80%,20-40%,40-60%,0-20%,0-20%,0-20%
"""

# Replace this by loading from CSV or your full data

# Load data into DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data_text))

# Mapping from ranges to numeric midpoints
range_to_midpoint = {
    '0-20%': 0.1,
    '20-40%': 0.3,
    '40-60%': 0.5,
    '60-80%': 0.7,
    '80-100%': 0.9,
}

# Convert all values in df using the mapping
df_num = df.applymap(lambda x: range_to_midpoint.get(x.strip(), np.nan))

# Calculate average weighted percentage per group (column)
averages = df_num.mean()

print("Weighted average percentage per group:")
print(averages)

# Plot bar chart of averages
plt.figure(figsize=(8,5))
sns.barplot(x=averages.index, y=averages.values)
plt.ylabel("Weighted Average Percentage")
plt.title("Estimated Average Percentage of US Skiers/Snowboarders by Group")
plt.ylim(0,1)
plt.show()

# For boxplot + jittered points, reshape data to long format
df_long = df_num.melt(var_name='Group', value_name='WeightedPercent')

plt.figure(figsize=(10,6))
sns.boxplot(x='Group', y='WeightedPercent', data=df_long, showfliers=False)
sns.stripplot(x='Group', y='WeightedPercent', data=df_long, color='black', alpha=0.5, jitter=True)
plt.ylabel("Weighted Percentage")
plt.title("Distribution of Estimated Percentages by Group")
plt.ylim(0,1)
plt.show()