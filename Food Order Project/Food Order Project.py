# Full Data Analyst Project : Food Order New Delhi  
# STEP1 :- Import libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Step2 :- Load the Dataset
df = pd.read_csv("D:\\Programming\\python\\A-Z Python Program\\Data analytics\\projects\\Food Order Project\\food_orders_new_delhi (1).csv")
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

df["Discounts and Offers"].fillna("None", inplace=True)


# STEP4 : Data visualization

# 1
# convert date-time column into data-time format 
df["Order Date and Time"] = pd.to_datetime(df["Order Date and Time"])
df["Delivery Date and Time"] = pd.to_datetime(df["Delivery Date and Time"])

# calculate delivery duration (in minutes)
df["Delivery Duration"] = (df["Delivery Date and Time"] - df["Order Date and Time"])

# Groupby day and calculate average delivery duration
df["Order Day"] = df["Order Date and Time"].dt.date
daily_avg = df.groupby("Order Day")["Delivery Duration"].mean()



# line plot

# Question: How does the average delivery duration vary across the observed dates?
plt.plot(daily_avg.index, daily_avg.values, color='blue')
plt.title(label='Average Delivery Duration')
plt.xlabel('Order Date')
plt.ylabel('Average Delivery Duration (Minutes)')
plt.grid()
plt.show()
# The chart depicts the fluctuating average delivery duration in minutes over the period from January 1, 2024, to February 5, 2024.


# 2
# Question: What are the percentage shares of each payment method depicted in the pie chart?
payment_dist = df.groupby("Payment Method")["Payment Method"].count()
print(payment_dist)
plt.pie(payment_dist, labels=payment_dist.index, autopct="%.2f", startangle=0)
plt.title("Distributions of Payment Methods")
plt.show()
# The pie chart shows the distribution of payment methods, with Cash on Delivery (35.70%), Credit Card (33.70%), and Digital Wallet (30.60%) as the three options.


# 3
# Question: Which order value range has the highest frequency in the chart?
sns.histplot(data=df, x="Order Value")
plt.title("Frequency of Order Value")
plt.show()
# The chart illustrates the frequency of order values, showing that the 1000-value range has the highest frequency.


# 4
# Question: How do order values differ across various discount and offer categories represented in the chart?
sns.scatterplot(data=df, y="Order Value", x="Discounts and Offers", palette="cividis", alpha=0.3)
plt.title("Correlation between Discounts & Offers and Order Values")
plt.show()
# The chart demonstrates the relationship between discounts and offers and the corresponding order values, showing varied impacts across discount categories.


# 5
# Question: How do the discounts and offers vary across payment methods in the chart?
sns.violinplot(data=df, x="Discounts and Offers", y="Payment Method")
plt.title("Discounts & Offers vary by Payment Methods")
plt.show()
# The chart shows how discounts and offers are distributed across different payment methods, such as Credit Card, Digital Wallet, and Cash on Delivery.


# 6
# Question: What is the percentage distribution of refunds/chargebacks among the payment methods represented in the chart?
refund = df.groupby("Payment Method")["Refunds/Chargebacks"].count()
print(refund)
plt.pie(refund, labels=refund.index, autopct="%.2f", startangle=0)
plt.title("Proportions of Refunds/Chargebacks by Payment Methods")
plt.show()
# The chart highlights the proportions of refunds/chargebacks distributed across payment methods, showing Cash on Delivery at 35.70%, Credit Card at 33.70%, and Digital Wallet at 30.60%.



# 7
# Question: How does the scatter plot illustrate the correlation between commission fees and payment processing fees?
sns.scatterplot(data=df, x="Commission Fee", y="Payment Processing Fee", hue="Payment Processing Fee", palette="viridis")
plt.title("Commission fees vs. Payment Processing fee")
plt.show()
# The chart displays a scatter plot showing the relationship between commission fees and payment processing fees, with data points color-coded based on payment processing fee values.


# 8
# Question: Which discount type has the highest percentage in the chart?
offer = df.groupby("Discounts and Offers")["Discounts and Offers"].count()
print(offer)
plt.pie(offer, labels=offer.index, autopct="%.2f", startangle=0)
plt.title("Proportions of Discounts and Offers")
plt.show()
# The chart represents proportions of different discount types, with the highest being 23.30% for a 10% discount and the lowest at 18.30% for a 5% discount on the app.


# 9
# Question: How does the scatter plot illustrate fixed delivery fees at specific values relative to order values?
sns.scatterplot(data=df, x="Order Value", y="Delivery Fee")
plt.title("Delivery Fee vs. Order Value")
plt.show()
# The scatter plot reveals fixed delivery fees (0, 20, 30, 40, and 50) distributed across varying order values.



# 10
# Question: Which payment method has the highest count in the bar chart?
payment = sns.countplot(data=df, x="Payment Method", palette="bright")
for i in range(0, 3):
    payment.bar_label(payment.containers[i])
plt.title("Payment Method Comparison")
plt.show()
# The bar chart shows the count of three payment methods: Cash on Delivery (357), Credit Card (337), and Digital Wallet (306), with Cash on Delivery being the most commonly used.


# 11
# Question: Which discount or offer has the highest count of users according to the chart?
payment = sns.countplot(data=df, x="Discounts and Offers", palette="cividis")
for i in range(0, 5):
    payment.bar_label(payment.containers[i])
plt.title("Discount Preferences Chart")
plt.show()
# The bar chart shows the count of users availing different discounts/offers, with the highest count being 233 for the 10% discount.


info()


# STEP5 : save clean data
df.to_csv("Food Order ND Cleaned Data.csv", index=False)
print("Data Cleaning & Visualized Completed...")
print("Food Order New Delhi data Cleaning & Visualized Project Done!...")
print()


# ***** Food Order Project Completed *****
# ***** Data Cleaning & Visualization COmpleted *****
