import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset
df= pd.read_csv("healthcare_dataset.csv")

#Analyse the data set
print(df.shape)
print(df.columns)
print(df.info())
print(df.head)

#cleaning the data
#removing the negative biiling amount
df_clean= df[df["Billing Amount"]>=0].copy()

#changing date from str to dateTime

#df['Date of Adimission']=pd.to_datetime(df_clean['Date of Adimission'])
df_clean['Date of Admission']=pd.to_datetime(df_clean["Date of Admission"])
df_clean["Discharge Date"]=pd.to_datetime(df_clean["Discharge Date"])
#print(df_clean['Date of Admission'], df_clean["Discharge Date"])

# days of stay
df_clean['Days of Stay']=(df_clean["Discharge Date"]-df_clean["Date of Admission"]).dt.days
df_clean=df_clean[df_clean['Days of Stay']>=0]
print(df_clean)

#condition summary billing amount by medical condition
print('mean and median billing by medical condition')

condition_summary=df_clean.groupby('Medical Condition')['Billing Amount'].agg(['mean','median','count','std'])
print(condition_summary)

#plotting
sns.set_theme(style='white')
plt.figure(figsize=(12,6))
sns.barplot(x='Medical Condition',data=df_clean, palette='Set2')
plt.title('The billing Amount distribution by medical condition',fontsize=14, fontweight='bold')
plt.tight_layout()
plt.xlabel('Medical Condition',fontsize=12,fontstyle='italic')
plt.ylabel('Billing Amount (ugx)',fontsize=12,fontstyle='italic')
plt.savefig('BillingAmount.png')
plt.close()

#Age_group by medical condition
bins=[0,18,30,60,100]
labels=['0-18 (child)','19-30(Youth)','31-60(Adult)','61+(Elderly)']
df_clean['Age Group']=pd.cut(df_clean['Age'],bins=bins,labels=labels)
print(df_clean['Age Group'].value_counts())

#Medical condition by Age group
sns.set_theme(style='whitegrid')
plt.figure(figsize=(10,5))
sns.countplot(x='Age Group',data=df_clean,palette='Set2')
plt.title('Age Group by Medical condition')
plt.tight_layout
#plt.savefig('Medical condition.png')
#plt.close()

#Cross_tabulation
#Average group and medical condition
print(pd.crosstab(df_clean['Age Group'],df_clean['Medical Condition']))