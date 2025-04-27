# Food Order New Delhi - Data Cleaning & Visualization Project

## 📄 Project Overview

This project focuses on cleaning and visualizing a dataset containing food delivery orders from New Delhi. The goal was to perform comprehensive data preprocessing, extract insights, and create meaningful visualizations to better understand delivery patterns, payment behaviors, discounts, and other key trends.

---

## 🛠️ Steps Performed

### 1. Import Libraries
- Imported essential Python libraries: `NumPy`, `Pandas`, `Matplotlib`, and `Seaborn`.

### 2. Load Dataset
- Loaded the dataset: `food_orders_new_delhi (1).csv`.

### 3. Data Cleaning
- Displayed the first and last 5 rows using `df.head()` and `df.tail()`.
- Generated statistical summaries using `df.describe()`.
- Inspected data types and checked for missing or duplicated values.
- Handled missing values in the `Discounts and Offers` column by replacing `NaN` with `"None"`.
- Verified the dataset was clean with no null values remaining.

### 4. Data Visualization and Insights

1. Question : How does the average delivery duration vary over time? 
   Approach : Line plot 
   Insight : Delivery duration fluctuates between January , 2024, and February 5, 2024. 

 2. Question : What are the percentage shares of each payment method? 
    Approach : Pie chart 
    Insight : Cash on Delivery (35.70%), Credit Card (33.70%), Digital Wallet (30.60%). 

 3. Question : Which order value range has the highest frequency? 
    Approach : Histogram 
    Insight : Orders around 000 value are the most frequent. 

 4. Question : How do order values differ across discount categories? 
    Approach : Scatter plot 
    Insight : Discounts show varied impacts on order values. 

 5. Question : How do discounts vary across payment methods? 
    Approach : Violin plot 
    Insight : Different patterns observed for different payment methods. 

 6. Question : What is the refund/chargeback distribution among payment methods? 
    Approach : Pie chart 
    Insight : Refunds/chargebacks distributed similarly to payment method shares. 

 7. Question : How are commission fees correlated to payment processing fees? 
    Approach : Scatter plot 
    Insight : Positive correlation observed. 

 8. Question : Which discount type has the highest percentage? 
    Approach : Pie chart 
    Insight : 0% Discount was the most common (23.3%). 

 9. Question : How does delivery fee vary relative to order value? 
    Approach : Scatter plot 
    Insight : Delivery fees are fixed at intervals (0, 20, 30, 40, 50). 

 10. Question : Which payment method is most common? 
     Approach : Bar chart 
     Insight : Cash on Delivery is the most popular. 

 11. Question : Which discount has the highest user count? 
     Approach : Bar chart 
     Insight : 0% discount had the most users. 

### 5. Save Cleaned Data
- Saved the cleaned dataset as `Food Order ND Cleaned Data.csv`.

---

## 📊 Libraries Used

- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization

---

## 📈 Conclusion

- Successfully cleaned and visualized the New Delhi food order dataset.
- Gained valuable insights into customer behavior, delivery patterns, and payment preferences.
- Prepared the data for further use in machine learning or deeper statistical analysis.

---

## 📁 Output Files

- `Food Order ND Cleaned Data.csv`

---

## 🚀 How to Run

1. Clone this repository.
2. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```
3. Run the notebook or script to replicate the cleaning and visualization steps.

---

## ✨ Author

- **Project Completed by:** *Pratham Singhal*

