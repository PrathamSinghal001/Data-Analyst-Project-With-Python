# 📱 Google Play Store Dataset - Data Cleaning & Visualization Project

## 📋 Project Overview

This project involves cleaning, preprocessing, and analyzing the Google Play Store dataset to uncover business insights. Through exploratory data analysis (EDA), the project focuses on app ratings, installs, prices, categories, and other important attributes to help understand trends in the Play Store ecosystem.

---

## 🛠️ Project Workflow

### Step 1: Load and Explore the Dataset
- Imported libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`.
- Loaded dataset: `googleplaystore.csv`.

### Step 2: Data Cleaning

- **Convert Data Types:**
  - Converted `Installs`, `Price`, and `Last Updated` columns into appropriate formats (numeric and datetime).

- **Handle Missing Values:**
  - Filled missing values with median or mode based on column type.

- **Remove Duplicates:**
  - Removed 483 duplicate entries from the dataset.

- **Detect and Handle Outliers:**
  - Removed ratings greater than 5.
  - Applied capping to prices using the 95th percentile.

---

## 📊 Business Questions and Insights

### 1. Univariate Analysis

- **Q1:** Average rating of apps → **4.20**
- **Q2:** Percentage of Free vs Paid apps → **Free: 92.61%**, **Paid: 7.39%**
- **Q3:** Most common app category → **FAMILY**

### 2. Univariate Visualizations (Categorical Variables)

- **Q4:** Highest number of apps → **FAMILY category**
- **Q5:** Most common content rating → **Everyone**
- **Q6:** Top 5 most popular categories → FAMILY, GAME, TOOLS, BUSINESS, MEDICAL

### 3. Univariate Visualizations (Numerical Variables)

- **Q7:** Most common app rating → around **4.3**
- **Q8:** Price distribution → Most apps are **free or inexpensive**.

### 4. Bivariate Analysis (Numerical vs Categorical)

- **Q9:** Free vs Paid apps ratings → Paid apps have a slightly higher average rating (**4.27**) than Free apps (**4.20**).
- **Q10:** Categories with highest average ratings → **Events** and **Education**.

### 5. Bivariate Visualizations (Numerical vs Numerical)

- **Q11:** Installs vs Rating → No strong correlation found.
- **Q12:** Average installs → Free apps significantly outperform Paid apps in installs.
- **Q13:** Price vs Rating → No strong positive correlation observed.

### 6. Bivariate Visualizations (Categorical vs Categorical)

- **Q14:** Categories with the most paid apps → **Games**, **Medical**, and **Family**.

---

## 📚 Libraries Used

- **Pandas**: Data manipulation
- **NumPy**: Numerical operations
- **Matplotlib**: Data visualization
- **Seaborn**: Advanced data visualization

---

## 📁 Output Files

- Cleaned dataset saved as `googleplaystore_cleaned.csv`.

---

## 🚀 How to Run This Project

1. Clone this repository.
2. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the Jupyter Notebook or Python script.

---

## ✅ Conclusion

- Successfully cleaned and preprocessed the Google Play Store dataset.
- Extracted actionable insights regarding app categories, user ratings, pricing strategies, and installation patterns.
- Created various univariate and bivariate visualizations to understand the dataset better.

---

## ✨ Author

- **Project Completed by:** *Pratham Singhal*
