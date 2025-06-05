import pandas as pd
import streamlit as st

df = pd.read_csv("C:/Users/Ruthf/Documents/student social media/Students Social Media Addiction.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.dtypes)
