# Full Data Analyst Project : Google Play Store 

# STEP1 :- Import libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Step2 :- Load the Dataset
df = pd.read_csv("D:\\Programming\\python\\A-Z Python Program\\Data analytics\\projects\\Google Play Store\\googleplaystore.csv")
# print(df)
print()

# STEP3 :- Data Cleaning
def info():
    print(df.head(10))
    print()
    print("Duplicated value : ", df.duplicated().sum())
    print()
    print(df.isna().sum())
    print()
    print(df.info())
    print()
    print(df.describe())
    print()


# 1: convert data types for better analysis
# price column 
df["Price"] = df["Price"].str.replace("Everyone", "0")
df["Price"] = df["Price"].str.replace(r"[^\d]", " ", regex=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")


# installs column 
df["Installs"] = df["Installs"].str.replace("Free", "0")
df["Installs"] = df["Installs"].str.replace(r"[+,]", " ", regex=True)
df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")


# installs column 
df["Last Updated"] = pd.to_datetime(df["Last Updated"], errors="coerce")



# 2: filling Dataset NaN/Null/None values 
df["Rating"].fillna(df["Rating"].median(), inplace=True)
df["Type"].fillna(df["Type"].mode()[0], inplace=True)
df["Content Rating"].fillna(df["Content Rating"].mode()[0], inplace=True)
df["Last Updated"].fillna(df["Last Updated"].mode()[0], inplace=True)
df["Current Ver"].fillna(df["Current Ver"].mode()[0], inplace=True)
df["Android Ver"].fillna(df["Android Ver"].mode()[0], inplace=True)
df["Installs"].fillna(df["Installs"].median(), inplace=True)
df["Price"].fillna(df["Price"].mean(), inplace=True)



# 3: remove duplicates values 
df.drop_duplicates(keep="first", inplace=True)
print()


# showing outliers
plt.title(label="Before Removing Outliers Rating values")
plt.subplot(1,2,1)
sns.boxplot(df["Rating"])
plt.subplot(1,2,2)
sns.boxplot(df["Price"])
plt.show()



# sum of outliers
df = df[df["Rating"]<=5]
print((df["Rating"]>5).sum())



plt.figure(figsize=(10,5))
sns.boxplot(x = df["Rating"], color="skyblue")
plt.title(label="After Removing Outliers Rating values")
plt.show()


# QUE1: What is the average rating of apps on the Play Store?
avg_rating = df["Rating"].mean()
print("Average Ration on Google Play Store : ", avg_rating)
print()



# QUE2: What percentage of apps are free vs paid?
total_apps = df.shape[0]
free_apps = df[df["Type"] == "Free"].shape[0]
paid_apps = df[df["Type"] == "Paid"].shape[0]
free_apps_perc = (free_apps/total_apps)*100
paid_apps_perc = (paid_apps/total_apps)*100
print(f"Free Apps Percentage on Google Play Store : {free_apps_perc:.2f}")
print(f"Paid Apps Percentage on Google Play Store : {paid_apps_perc:.2f}")
print()



# QUE3: What is the most common app category?
most_common_cat = df["Category"].value_counts().idxmax()
print("The Most Apps Category on Google Play Store : ", most_common_cat)
print()



most_common_cat = df["Category"].value_counts().head(10)
# QUE4: Which app category has the highest number of apps?
sns.barplot(x=most_common_cat.index, y=most_common_cat.values, palette="inferno")
plt.xlabel("Apps Categories")
plt.ylabel("No. of Apps")
plt.xticks(rotation=10)
plt.title(label="Categories Has Highest Number of Apps")
plt.show()



# QUE5: What is the distribution of content ratings?
sns.histplot(data=df, x="Content Rating")
plt.title(label="Distributions of Content Ratings")
plt.show()



# QUE6: How many apps belong to the top 5 most popular categories?
most_common_cat = df["Category"].value_counts().head(5)
sns.barplot(x=most_common_cat.index, y=most_common_cat.values, palette="colorblind")
plt.xlabel("Apps Categories")
plt.ylabel("No. of Apps")
plt.xticks(rotation=10)
plt.title(label="Top 5 Most Popular Categories")
plt.show()



# QUE7: What is the most common rating given to apps?
sns.histplot(data=df, x="Rating")
plt.title(label="Most Common Ratings to Apps")
plt.show()



# Q8: How are app prices distributed?
sns.boxplot(df["Price"])
plt.title(label="Prices Distributions to Apps")
plt.xlabel("Prices")
plt.show()



# QUE9: Do free apps have better ratings than paid apps?
free_apps_avg_rating = df[df["Type"] == "Free"]["Rating"].mean()
paid_apps_avg_rating = df[df["Type"] == "Paid"]["Rating"].mean()
print(f"Free Apps Average rating : {free_apps_avg_rating:.2f}")
print(f"Paid Apps Average rating : {paid_apps_avg_rating:.2f}")
print()
sns.barplot(data=df, x="Type", y="Rating", palette="dark")
plt.show()



# QUE10: Which app categories have the highest average ratings?
category_avg_rating = df.groupby("Category")["Rating"].mean().sort_values(ascending=False)
print(f"Apps Categories Have Highest Average Ratings {category_avg_rating}")
print()


# QUE11: Does a higher number of installs correlate with higher ratings?
# sns.scatterplot(data=df, x="Installs", y="Rating")
sns.scatterplot(x=df["Installs"], y=df["Rating"], alpha=0.5)
plt.xscale("log") #--> show log form
plt.title(label="Installs vs. Rating")
plt.xlabel("No. of Installs")
plt.ylabel("Ratings")
plt.show()



# QUE12: Do paid apps generate more installs than free apps?
free_apps_installs = df[df["Type"] == "Free"]["Installs"].mean()
paid_apps_installs = df[df["Type"] == "Paid"]["Installs"].mean()
print(f"Free Apps Installs : {free_apps_installs:.2f}")
print(f"Paid Apps Installs : {paid_apps_installs:.2f}")
print()



# QUE13: Are expensive apps rated higher than free apps?
sns.scatterplot(data=df, x="Price", y="Rating")
plt.title("Price vs. Rating")
plt.show()



# QUE14: Which categories have the most paid apps?
sns.countplot(data=df, x="Category", hue="Type")
plt.xticks(rotation=45)
plt.show()



print()
# info()
df.to_csv("Google Play Stored Cleaned Data.csv", index=False)
print("Data Cleaning & Visualized Completed...")
print("Google Play Store Data Cleaning & Visualized Project Done!...")
print()

# ***** Google Play Store Projecct *****
# ***** Data Cleaning & Visualization Project *****
