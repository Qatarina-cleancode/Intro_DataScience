#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load data
df = pd.read_csv("Export_Stunting_Prevalence_(Children_&lt;5_Years).csv")
#inspecting missing data
print("missing values in the dataset")
print(df.isnull().sum())
# Remove empty columns
df_clean = df.drop(columns=['Age Group', 'Gender'])
#clean
df_regions = df_clean[df_clean['Location'] != 'Uganda']

#Aggregate average stunting prevalence values per region
regional_avg = df_regions.groupby('Location')['Value'].mean().sort_values(ascending=False)
print("\n--- Average Prevalence by Region (%) ---")
print('regional_average')

# visualize the data
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 5))

# Pass hue parameter to avoid Seaborn palette deprecation warning
ax = sns.barplot(
x=regional_avg.values,
y=regional_avg.index,
hue=regional_avg.index,
palette="Blues_r"
)
if ax.legend_:
    ax.legend_.remove()
plt.title("Average Stunting Indicator Value by Region in Uganda")
plt.xlabel("Average Value (%)")
plt.ylabel("Region")
plt.tight_layout()
# Save image directly to disk so it can be viewed in terminal environments
plt.savefig("stunting_regional_analysis.png")
print("\nChart saved successfully as 'stunting_regional_analysis.png'")
# Display plot GUI
plt.show()


