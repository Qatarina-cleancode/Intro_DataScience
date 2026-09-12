import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Load data
df= pd.read_csv('healthcare_dataset.csv')

#Inspecting the data
print("shape",df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.head)

#Cleaning capitalisation
df["Name"]= df["Name"].str.title()
print(df["Name"].head(20))
print(df.head)

#date
print(df['Discharge Date'].head(20))
print(df['Discharge Date'].dtype)
print(df[df['Discharge Date'].apply(lambda x: callable(x))])
df['Discharge Date']= pd.to_datetime(df['Discharge Date'])
df['Date of Admission']= pd.to_datetime(df['Date of Admission'])
print(df.dtypes)
#remove duplicates if any
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after:", df.duplicated().sum())

#Data validation
print("Age range:", df['Age'].min(), "-", df['Age'].max())
print("Billing Amount range:", df['Billing Amount'].min(), "-", df['Billing Amount'].max())
# Negative billing
print("Negative billing amounts:", (df['Billing Amount'] < 0).sum())

negative_bills = df[df['Billing Amount'] < 0]
print(negative_bills)

#days of stay
df['Days of Stay']=(df['Discharge Date']-df['Date of Admission']).dt.days
print(df[['Date of Admission','Discharge Date','Days of Stay']])

df['Age Group'] = pd.cut( df['Age'],
    bins=[0, 18, 35, 50, 65, 100],
    labels=['0-18', '19-35', '36-50', '51-65', '66+']
)
print(df[['Age Group','Age']])

#Average billing by medical condition

avg_billing=df.groupby('Medical Condition')['Billing Amount'].mean().sort_values(ascending=False)
print("\nAverage Billing by Condition\n",avg_billing)

#Visualisation
sns.set_theme(style="whitegrid")
#Distribution of Medical conditions
plt.figure(figsize=(10,5))
df['Medical Condition'].value_counts().plot(kind='bar')
plt.title('Medical Condition Cases')
plt.ylabel('Count')
plt.xlabel('Cases')
plt.tight_layout()
plt.savefig('Medical Condition Cases')
plt.close()

#Average billing by condition
plt.figure(figsize=(10,5))
avg_billing.plot(kind='bar',color=['blue','yellow','green','red','gold'])
plt.title('Average Billing by medical condition')
plt.ylabel("average billing $")
plt.xlabel("medical condition")
plt.tight_layout()
plt.savefig("Average Billing by Medical condition")
plt.close()

#age condition
age_condition = pd.crosstab(
    df['Age Group'],
    df['Medical Condition']
)
print(age_condition)
# #Age group by medical condition
plt.figure(figsize=(12,6))
pd.crosstab(df['Age Group'], df['Medical Condition']).plot(kind='bar',color=['skyblue','yellow','green','orange','red','purple'])
plt.title('Age Group by medical cases')
plt.xlabel('Age Group')
plt.legend(title='Medical condition', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.ylabel('Medical Conditions')
plt.tight_layout()
plt.savefig('Age Group by Medical cases')
plt.close()

#Average stay
avg_stay=df.groupby('Admission Type')['Days of Stay'].mean().sort_values(ascending=False)
print("\nAverage Length of Stay by Admission Type:\n", avg_stay)

#Crosstab
crosstab = pd.crosstab(df['Age Group'], df['Test Results'], normalize='index') * 100
print("\nTest Result % by Age Group:\n", crosstab.round(1))
 
plt.figure(figsize=(10, 6))
crosstab.plot(kind='bar', stacked=True)
plt.title("Test Result Distribution by Age Group (%)")
plt.ylabel("Percentage")
plt.legend(title='Test Result', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("test_results_by_age_group.png")
plt.close()
 
print("\nSaved 3 charts: condition_counts.png, avg_billing_by_condition.png, test_results_by_age_group.png")






