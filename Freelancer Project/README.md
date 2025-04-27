# Freelancer Earning Dataset - Data Cleaning & Visualization Project

## 📋 Project Overview

This project focuses on cleaning and visualizing a dataset containing freelancer earnings and work statistics across various platforms and job categories. The aim was to analyze freelancer performance metrics, client engagement, payment trends, and marketing strategies to derive actionable insights.

---

## 🛠️ Project Workflow

### 1. Import Libraries
- Used essential libraries: `NumPy`, `Pandas`, `Matplotlib`, and `Seaborn`.

### 2. Load Dataset
- Loaded `freelancer_earnings_bd.csv` into a pandas DataFrame.

### 3. Data Cleaning
- Reviewed statistical summaries using `df.describe()`.
- Inspected data types with `df.info()`.
- Verified there were no missing values.
- Checked for and confirmed no duplicate entries, including unique `Freelancer_ID`s.
- Final clean data was saved as `Freelancer Cleaned Data.csv`.

---

## 📈 Data Visualization & Insights


1. Question : Earnings distribution? 
   - Approach : Histogram 
   - Insight : Highest earnings concentration around 4000-6000 USD. 

2. Question : Correlation between hourly rate and job success rate? 
   - Approach : Scatter plot 
   - Insight : No strong correlation observed. 

3. Question : Highest earning job category? 
   - Approach : Bar chart 
   - Insight : Digital Marketing leads earnings. 

4. Question : Most completed jobs by category? 
   - Approach : Bar chart 
   - Insight : Graphic Design category has the most completions. 

5. Question : Job duration by experience level? 
   - Approach : Box plot 
   - Insight : Experts complete jobs faster than beginners. 

6. Question : Job category with most freelancers? 
   - Approach : Bar chart 
   - Insight : Graphic Design has the most freelancers. 

7. Question : Relationship between job success rate and client rating? 
   - Approach : Scatter plot 
   - Insight : Positive correlation observed. 

8. Question : Platform with highest median job success rate? 
   - Approach : Box plot 
   - Insight : Platform differences observed; Upwork leading. 

9. Question : Job role distribution?  
   - Approach : Pie chart 
   - Insight : Graphic Design dominates (13.59%). 

10. Question : Platform with most freelancers? 
    - Approach : Bar chart and Pie chart 
    - Insight : Upwork leads with 21.54%. 

11. Question : Region with most clients? 
    - Approach : Bar chart 
    - Insight : Australia has the most clients. 

12. Question : Impact of marketing spend on earnings? 
    - Approach : Scatter plot 
    - Insight : Higher marketing spend correlates with higher earnings. 

13. Question : Payment method preference?  
    - Approach : Pie chart 
    - Insight : Crypto is the most preferred method (26.36%). 

14. Question : Freelancer experience level distribution? 
    - Approach : Pie chart 
    - Insight : 34.26% are Beginners. 

15. Question : Project types by job categories? 
    - Approach : Bar chart 
    - Insight : Graphic Design leads in fixed projects, App Development in hourly projects. 


---

## 📚 Libraries Used

- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Matplotlib** for visualizations
- **Seaborn** for enhanced plotting

---

## 📁 Output Files

- `Freelancer Cleaned Data.csv`

---

## 🚀 How to Run This Project

1. Clone this repository.
2. Install the required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the Jupyter Notebook or `.py` file to replicate the cleaning and visualization steps.

---

## ✅ Conclusion

- Successfully cleaned and explored the freelancer earnings dataset.
- Provided in-depth visual analytics of freelancer success patterns.
- Insights can help freelancers and platforms strategize better.

---

## ✨ Author

- **Project Completed by:** *Pratham Singhal*

