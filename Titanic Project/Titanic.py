# Full Data Analyst Project : Titanic 

# STEP1 :- Import libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Step2 :- Load the Dataset
df = pd.read_csv("D:\\Programming\\python\\A-Z Python Program\\Data analytics\\Datasets\\Project Dataset\\titanic.csv")
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


# filling null value on age col
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Age"].astype("int64")
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Cabin"].fillna("Unknown", inplace=True)

# detecting duplicate values sum
print(df.duplicated().sum())
print(df["PassengerId"].duplicated().sum())




# STEP4 : Data visualization


# How does the survival rate differ between males and females according to the chart?
sex = sns.countplot(data=df, x="Sex", hue="Survived")
sex.bar_label(sex.containers[0])
sex.bar_label(sex.containers[1])
plt.title("Survival Rate By Gender")
plt.show()
# CONCLUSION : The chart highlights that females had significantly higher survival rates compared to males, with 233 females surviving and only 109 males.


# What is the relationship between passenger class and survival rates as shown in the chart?
pclass = sns.countplot(data=df, x="Pclass", palette="bright")
pclass.bar_label(pclass.containers[0])
pclass.bar_label(pclass.containers[1])
pclass.bar_label(pclass.containers[2])
plt.title("Survival Rate by Passenger class")
plt.show()
# CONCLUSION : the survival rate was highest for passengers in Class 3 (491 survivors), followed by Class 1 (216 survivors), and lowest in Class 2 (184 survivors).


# What does the age distribution reveal about the concentration of passengers at different ages?
sns.histplot(data=df, x="Age")
plt.title("Age Distributions")
plt.show()
# CONCLUSION : The chart highlights a notable peak in the population's age distribution at 30 years, indicating a higher concentration of individuals at this age compared to others.


# What does the pie chart suggest about the proportion of males and females in the population?
gender_counts = df["Sex"].value_counts()
plt.pie(gender_counts.values, labels=gender_counts.index, autopct="%.2f", shadow=True, startangle=0)
plt.title("Gender Distributions")
plt.show()
# CONCLUSION : The pie chart reveals that the population consists of 64.76% males and 35.24% females, highlighting a male majority.


# What relationship does the chart reveal between passenger class and fare variability, including the presence of outliers in higher classes?
sns.boxplot(data=df, x="Pclass", y="Fare", palette="deep")
plt.title("Class And Fare Correlation")
plt.show()
# CONCLUSION : The chart demonstrates that higher passenger classes are associated with higher fares, showing greater variability and outliers in first class compared to other classes.



# How does the distribution of fare prices reflect the socio-economic diversity among Titanic passengers?
sns.violinplot(data=df, x="Fare")
plt.title("Fare Distributions")
plt.show()
# CONCLUSION : The chart shows that fare prices are heavily concentrated at lower values, with fewer high-value fares creating a long tail distribution.


# How does the distribution of passengers by embarkation location reflect travel trends aboard the Titanic?
gb = df.groupby("Embarked")["PassengerId"].count()
print(gb)
embark = sns.countplot(data=df, x="Embarked", palette="magma")
embark.bar_label(embark.containers[0])
embark.bar_label(embark.containers[1])
embark.bar_label(embark.containers[2])
plt.title("Passenger Embarkation")
plt.show()
# CONCLUSION : The chart demonstrates that the majority of passengers, 646, embarked from location S, followed by 168 from location C, and 77 from location Q.




# How do gender and passenger class influence survival rates, as highlighted by the chart?
plt.subplot(1, 2, 1)
sex = sns.countplot(data=df, x="Sex", hue="Survived")
sex.bar_label(sex.containers[0])
sex.bar_label(sex.containers[1])
plt.title("Survival Rate By Gender")


plt.subplot(1, 2, 2)
pclass = sns.countplot(data=df, x="Pclass", hue="Survived")
pclass.bar_label(pclass.containers[0])
pclass.bar_label(pclass.containers[1])
# pclass.bar_label(pclass.containers[2])
plt.title("Survival Rate By Passenger Class")
# CONCLUSION : The chart reveals that females and first-class passengers had significantly higher survival rates compared to males and lower-class passengers.

plt.show()



# What does the chart reveal about the relationship between age and survival rates on the Titanic?

# Swarm plot for Age distribution by Survival status
plt.subplot(1, 2, 1)
sns.swarmplot(x='Survived', y='Age', data=df, hue='Survived', dodge=True, palette='inferno')
plt.legend(title='Survival Status')


# Violin plot for Age distribution by Survival status
plt.subplot(1, 2, 2)
sns.violinplot(x='Survived', y='Age', data=df, palette='plasma', inner='quartile')

plt.title('Age Distribution by Survival Status')
plt.show()
# CONCLUSION : The chart highlights distinct age patterns, showing younger passengers had higher survival rates compared to older passengers.




# What does the chart reveal about the relationship between fare amounts paid by passengers and their chances of survival?
sns.boxplot(data=df, x="Survived", y="Fare", hue="Survived")
plt.title("Survival vs. Fare Paid")
plt.show()
# CONCLUSION : : The chart indicates that passengers who survived generally paid higher fares, as shown by the wider spread of fare values for survivors compared to non-survivors.


info()

df.to_csv("Titanic Cleaned Data.csv", index=False)
print("Data Cleaning & Visualized Completed...")
print("Titanic data Cleaning & Visualized Project Done!...")
print()



# ***** Titanic Project *****
# ***** Data Cleaning & Visualized Project *****
