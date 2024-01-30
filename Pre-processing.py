import pandas as pd
import seaborn as sns
import numpy as np

## Loading Data file
df=pd.read_csv("E commerece data.csv")
df.head(3)

## Checking shape
df.shape

## Checking overall info
df.info()

## Checking Sum etc
df.describe()

## Columns of data 
df.columns

## Checking null values
df.isnull().sum()

## Dropping null values
new_df=df.dropna()

## Dropping null values
df.dropna()

## Taking sample from data if its big
sampled_data = new_df.sample(n=5000, random_state=42)

## Converting to other format 
sampled_data.to_excel('complaints.xlsx')

## Subset of data can be any columns
new_df = df[[ 'Consumer disputed?']].copy()

## Renaming columns names 
new_df.rename(columns={'Consumer disputed?': 'consumer'}, inplace=True)
new_df.head(3)



