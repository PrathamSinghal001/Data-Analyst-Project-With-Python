# 🚢 Titanic Dataset - Data Cleaning & Visualization Project

## 📋 Project Overview

This project focuses on cleaning, preprocessing, and visualizing the Titanic dataset to uncover survival patterns and insights. Through exploratory data analysis (EDA), we investigate relationships between passenger features like age, gender, fare, and survival status.

---

## 🛠️ Project Workflow

### Step 1: Import Libraries
- Imported essential Python libraries: `numpy`, `pandas`, `matplotlib`, and `seaborn`.

### Step 2: Load Dataset
- Loaded the dataset: `titanic.csv`.

### Step 3: Data Cleaning

- **Statistical Summary:** Generated using `describe()`.
- **Data Types Inspection:** Reviewed using `info()`.
- **Handling Missing Values:**
  - Filled missing `Age` values with the mean.
  - Filled missing `Embarked` values with the mode.
  - Replaced missing `Cabin` values with `"Unknown"`.
- **Remove Duplicates:** Verified there were no duplicate `PassengerId`s.
- **Null Value Verification:** Confirmed all missing values were handled.

### Step 4: Data Visualization and Insights

1. Question : How does survival rate differ between genders? 
   - Approach : Countplot 
   - Insight : Females had a much higher survival rate than males. 

2. Question : How does passenger class affect survival rate? 
   - Approach : Countplot 
   - Insight : Survival highest in 1st class, lowest in 3rd class. 

3. Question : What is the age distribution of passengers? 
   - Approach : Histogram 
   - Insight : Peak concentration around 30 years old. 

4. Question : Gender distribution among passengers? 
   - Approach : Pie Chart 
   - Insight : 64.76% male, 35.24% female. 

5. Question : Correlation between passenger class and fare? 
   - Approach : Boxplot 
   - Insight : Higher classes paid higher fares with more variability. 

6. Question : How is fare distributed among passengers? 
   - Approach : Violin plot 
   - Insight : Most fares concentrated at lower values. 

7. Question : Embarkation locations? 
   - Approach : Countplot 
   - Insight : Majority (646 passengers) embarked from 'S'. 

8. Question : How do gender and class together affect survival? 
   - Approach : Subplots 
   - Insight : Females and 1st class passengers had better chances. 

9. Question : Relationship between age and survival? 
   - Approach : Swarm & Violin plots 
   - Insight : Younger passengers had better survival rates. 

10. Question : Fare amounts and survival chance? 
    - Approach : Boxplot 
    - Insight : Survivors generally paid higher fares. 


---

## 📚 Libraries Used

- **Pandas**: Data analysis and manipulation
- **NumPy**: Numerical operations
- **Matplotlib**: Data visualization
- **Seaborn**: Advanced statistical plots

---

## 📁 Output Files

- Cleaned data saved as: `Titanic Cleaned Data.csv`

---

## 🚀 How to Run This Project

1. Clone this repository.
2. Install the required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Open the Jupyter Notebook or run the script to replicate the data cleaning and visualizations.

---

## ✅ Conclusion

- Successfully cleaned and visualized the Titanic dataset.
- Identified critical factors influencing survival such as gender, class, and fare.
- Created meaningful visualizations to support data-driven conclusions.

---

## ✨ Author

- **Project Completed by:** *Pratham Singhal*

