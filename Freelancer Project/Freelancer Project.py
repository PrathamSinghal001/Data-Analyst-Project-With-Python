# Full Data Analyst Project : Freelencer 

# STEP1 :- Import libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Step2 :- Load the Dataset
df = pd.read_csv("D:\\Programming\\python\\A-Z Python Program\\Data analytics\\projects\\Freelancer Project\\freelancer_earnings_bd.csv")
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

# check duplicate value along freelencer id 
print(df["Freelancer_ID"].duplicated().sum())


# STEP4 :- Data Visualization

# generate a summary on a chart in 1 line ans also write quetion according to a chart and also write a best title for charts


# 1
# Question: Which earning interval has the highest frequency in this distribution?
sns.histplot(data=df, x="Earnings_USD")
plt.title("Earning in USD Distributions")
plt.show()
# CONCLUSION : The bar chart reveals the frequency distribution of earnings in USD across different income intervals, with counts ranging from approximately 125 to 175.



# 2
# Question: Does the chart suggest any correlation between hourly rate and job success rate?
sns.scatterplot(data=df, x="Hourly_Rate", y="Job_Success_Rate", hue="Earnings_USD", palette="viridis", alpha=0.5)
plt.title("Impact of Hourly Rate on Job Success Rate with Earnings Representation")
plt.show()
# CONCLUSION : The chart explores the relationship between hourly rates and job success rates, showing no clear connection as the data points are widely scattered.



# 3
# Question: Which job category shown in the chart has the highest earnings?
sns.barplot(data=df, x="Job_Category", y="Earnings_USD", palette="bright", errorbar=("ci",0))
plt.title("Earnings by Job Categories")
plt.show()
# CONCLUSION : The bar chart displays earnings in USD across various job categories, with Digital Marketing having the highest earnings among them.


# 4
# Question: Which category has the most completed jobs according to the chart?
gb = df.groupby("Job_Category")["Job_Completed"].count().reset_index()
print(gb)
sns.barplot(data=gb, x="Job_Category", y="Job_Completed", palette="colorblind", errorbar=("ci",0))
plt.title("Job Completed by Categories")
sns.despine()
plt.show()
# CONCLUSION : The bar chart titled "Job Completed by Categories" shows the number of jobs completed across various fields, ranging from approximately 200 to 250 jobs per category.




# 5
# Question: How does job duration vary among beginners, intermediates, and experts in the chart?
sns.boxplot(data=df, x="Experience_Level", y="Job_Duration_Days", palette="muted")
plt.title("Job Duration Trends for Experience levels")
plt.show()
# CONCLUSION : The chart highlights that job duration tends to decrease as experience level increases, with experts showing the shortest job durations on average.



# 6
# Question: Which job category has the highest number of freelancers, as per the chart?
sns.countplot(data=df, x="Job_Category", palette="cividis")
plt.title("Freelencers count by Job Category")
plt.show()
# CONCLUSION : The chart reveals that Graphic Design has the highest count of freelancers, while Digital Marketing has the lowest, with other categories distributed in between.



# 7
# Question: What does the chart suggest about the relationship between job success rates and client ratings?
sns.scatterplot(data=df, y="Client_Rating", x="Job_Success_Rate", hue="Job_Success_Rate", palette="plasma")
plt.title("Client Rating vs. Job Success Rate")
plt.show()
# CONCLUSION : The scatter plot reveals that higher job success rates generally correspond with higher client ratings, indicating a positive correlation.



# 8
# Question: Which freelancing platform has the highest median job success rate in the chart?
sns.boxplot(data=df, y="Platform", x="Job_Success_Rate", palette="inferno")
plt.title("Job Success Rate Distributions by Platform")
plt.show()
# CONCLUSION : The box plot displays the job success rate distributions for five freelancing platforms, highlighting variations in median, range, and potential outliers.



# 9
# Question: Which job role holds the highest percentage in the distribution?
gb = df.groupby("Job_Category")["Job_Category"].count()
print(gb)
plt.pie(gb.values, labels=gb.index, startangle=0, shadow=True, autopct="%.2f")
plt.title("Freelancer Job Role Distribution")
plt.show()
# CONCLUSION : The pie chart depicts the percentage distribution of various job roles, with Graphic Design having the highest share (13.59%) and Content Writing and Digital Marketing tying for the lowest (11.85%).



# 10
# Question: Which platform has the highest number of freelancers according to the chart?
platform = sns.countplot(data=df, x="Platform", palette="magma")
for i in range(0, 5):
    platform.bar_label(platform.containers[i])
plt.title("Freelancer presents on platfrom")
plt.show()
# CONCLUSION : The bar chart compares freelancer numbers across five platforms, with Upwork leading at 420 and PeoplePerHour trailing at 358.



# 11
# Question: Which region has the highest number of clients according to the chart?
cl_Region = sns.countplot(data=df, x="Client_Region", palette="coolwarm")
for i in range(0, 7):
    cl_Region.bar_label(cl_Region.containers[i])
plt.title("Client Counts by Region")
plt.show()
# CONCLUSION : The bar chart shows the number of clients from various regions, with Australia leading at 298 and Canada trailing at 246.



# 12
# Question: How does marketing spend impact earnings according to the scatter plot?
sns.scatterplot(data=df, x="Marketing_Spend", y="Earnings_USD", hue="Earnings_USD", palette="gist_heat_r")
plt.title("Marketing Speds vs. Earnings")
plt.show()
# CONCLUSION : The scatter plot shows the relationship between marketing spend and earnings, with higher marketing spend generally associated with increased earnings.



# 13
# Question: What percentage of users prefer Crypto as their payment method according to the chart?
gb = df.groupby("Payment_Method")["Payment_Method"].count()
print(gb)
plt.pie(gb.values, labels=gb.index, startangle=0, shadow=True, autopct="%.2f")
plt.title("Most Common Payment Methods")
plt.show()
# CONCLUSION : The chart showcases the percentage split of common payment methods, with Crypto emerging as the top choice at 26.36%.



# 14
# Question: Which platform has the largest percentage of freelancers according to the pie chart?
gb = df.groupby("Platform")["Platform"].count()
print(gb)
plt.pie(gb.values, labels=gb.index, startangle=0, shadow=True, autopct="%.2f")
plt.title("Most Freelencers Platform")
plt.show()
# CONCLUSION : The pie chart displays the distribution of freelancers across five platforms, with Upwork leading at 21.54% and PeoplePerHour having the smallest share at 18.36%.



# 15
# Question: What percentage of freelancers fall into the Beginner category according to the pie chart?
gb = df.groupby("Experience_Level")["Experience_Level"].count()
print(gb)
plt.pie(gb.values, labels=gb.index, startangle=0, shadow=True, autopct="%.2f")
plt.title("Freelencers Experience level")
plt.show()
# CONCLUSION : The pie chart depicts the distribution of freelancers based on experience levels, showing Beginners at 34.26%, with Intermediate and Experts each at 32.87%.



# 16
# Question: Which job categories have the highest counts for fixed and hourly projects according to the chart?
project_type = sns.countplot(data=df, x="Job_Category", hue="Project_Type")
for i in range(0, 2):
    project_type.bar_label(project_type.containers[i])
plt.title("Project Type by Job Category")
plt.show()
# CONCLUSION : The bar chart compares fixed and hourly projects across job categories, with Graphic Design leading in fixed projects and App Development in hourly projects.

print() # for space 

info()

print() # for space 

# STEP5 : save clean data
df.to_csv("Freelancer Cleaned Data.csv", index=False)
print("Data Cleaning & Visualized Completed...")
print("Freelancer data Cleaning & Visualized Project Done!...")
print()

# ***** Freelancer Project *****
# ***** Data Cleaning & Visualization Project Completed *****
