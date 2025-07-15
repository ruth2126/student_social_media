import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv("C:/Users/Ruthf/Documents/student social media/Students Social Media Addiction.csv")
#df1 = df.drop(columns=["Student_ID"], inplace = True)
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.dtypes)

missing_values = df.isnull().sum()
print(missing_values)
categorical_columns = df.select_dtypes(include=['object']).columns
unique_values = {col: df[col].nunique() for col in categorical_columns}
print(unique_values)

df['affect_academic_performance'] = df['Affects_Academic_Performance'].map({'Yes': 1, 'No' : 0})
correlation_matrix = df.corr(numeric_only= True)
print(correlation_matrix)

sns.histplot(df['Avg_Daily_Usage_Hours'], kde=True)
plt.xlabel('hours per day')
plt.ylabel('number of students')
plt.show()

sns.countplot(data=df, y='Most_Used_Platform')

sns.boxplot(data=df, x='Gender', y='Addicted_Score')

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

avg_addiction_score =df.groupby('Most_Used_Platform')['Addicted_Score'].mean()
print(avg_addiction_score)

usage_by_academic_impact=df.groupby('Affects_Academic_Performance')['Avg_Daily_Usage_Hours'].mean()
print(usage_by_academic_impact)

sleep_mental_by_impact=df.groupby('Affects_Academic_Performance')[['Sleep_Hours_Per_Night', 'Mental_Health_Score']].mean()
print(sleep_mental_by_impact)

