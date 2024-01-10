from turtle import shape
import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

print(list(df))

print(df.shape)

del df["id.1"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Luminosity"]

print(df.shape)

df.to_csv('main.csv')
