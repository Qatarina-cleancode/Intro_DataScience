import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
# 1. Load and clean dataset 
df = pd.read_csv('Export_Stunting_Prevalence_(Children_&lt;5_Years).csv') 
df_clean = df.drop(columns=['Age Group', 'Gender']) 
df_regions = df_clean[df_clean['Location'] != 'Uganda'] 

# 2. Reshape data: Create a Pivot Table (Location vs Period) 
pivot_table = df_regions.pivot_table(index='Location', columns='Period', 
values='Value', aggfunc='mean') 
print("--- PIVOT TABLE (LOCATION VS YEAR) ---") 
print(pivot_table.head()) 

# 3. Calculate yearly statistical summary 
yearly_stats = df_regions.groupby('Period')['Value'].agg(['mean', 'median', 'std', 
'min', 'max']) 
print("\n--- YEARLY STATISTICAL SUMMARY ---") 
print(yearly_stats) 

# Set global Seaborn style 
sns.set_theme(style="whitegrid") 

# Set global Seaborn style 
sns.set_theme(style="whitegrid") 

# 4.isualization 1: Time-Series Line Plot across regions 
plt.figure(figsize=(10, 5)) 
sns.lineplot(data=df_regions, x='Period', y='Value', hue='Location', marker='o') 
plt.title("Stunting Prevalence Trends Over Time by Region (2016-2024)") 
plt.xlabel("Year (Period)") 
plt.ylabel("Prevalence Value (%)") 
plt.tight_layout() 
plt.savefig("stunting_time_series.png") 
plt.close() 

# 5. Visualization 2: Boxplot for Distribution & Outliers per Year 
plt.figure(figsize=(9, 5)) 
sns.boxplot(data=df_regions, x='Period', y='Value', palette="Set2") 
plt.title("Yearly Stunting Value Distributions Across Ugandan Regions") 
plt.xlabel("Year") 
plt.ylabel("Prevalence Value (%)") 
plt.tight_layout() 
plt.savefig("stunting_yearly_boxplot.png") 
plt.close()

