![banner](assets/banner.png)

Banner [source](https://banner.godori.dev/)

![Python version](https://img.shields.io/badge/Python%20version-3.10%2B-lightgrey)
![GitHub last commit](https://img.shields.io/github/last-commit/adin11/mumbai-property-price-estimator)
![Type of ML](https://img.shields.io/badge/Type%20of%20ML-Regression-blue)
![License](https://img.shields.io/badge/License-MIT-green)
[![Flask App](https://img.shields.io/badge/Flask-Web%20App-blue)](https://mumbaipriceteller.on.render.com)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# 🏠 Mumbai Property Price Estimator
#### [MumbaiPriceTeller](https://mumbaipriceteller.onrender.com)

## 🔍 Business Problem
Buying a property in Mumbai is often confusing because prices vary widely depending on the location, property type, size (carpet area), and furnishing status. This lack of clarity makes it difficult for homebuyers to know if they are paying a fair price, for sellers to set the right price, and for investors to identify good opportunities.

## Overview
This project presents a full-stack machine learning solution for real-time property price estimation in Mumbai. It combines dynamic data scraping from MagicBricks API, with ETL workflows and advanced predictive models to deliver accurate price estimations. Built with Flask and deployed on Render, this app makes it easy for users to check property valuations.

## Demo
https://github.com/user-attachments/assets/225ad43f-6176-46ae-9910-f3ad5da2ec14

## Power BI Dashboard:
![dashboard](assets/dashboard.png)
**Power Bi Dashboard for Analyzing How Property Prices Fluctuate across entire mumbai.**

## 🧠 Key Findings: 
1. Majority of the Flat listings are new properties which are Unfurnished.
2. The Western and southern belt of mumbai has high property prices as compared to others.
3. The Northern Belt of mumbai has affordable and less property prices.
4. The Maximum No property were listed from bhandup, andheri, Mulund.
5. Feature engineering, especially `price_per_sqft` and target encoding for `location`, significantly boosted model accuracy and reduced margin of error.  
6. After feature engineering and fine-tuning, XGBoost achieved **99% R² score** and **1% error margin**, making it ideal for real-time price prediction.

## 📊 Data Source
- Data scraped from [MagicBricks](https://www.magicbricks.com/) using Scrapy via MagicBricks Backend Api.
- Stored in SQLite3 database for easy access and analysis.


## Technical Details

- **Data Scraping & Storage:** Scrapy used to pull data from MagicBricks’ backend API. Structured it into a SQLite database. Established connection with the database using sqlite3 library.
- **Data Cleaning and Transformations:**  Imputed Null Values , dropped some null values from different columns also fixed column datatypes and converted transfromed column values.
- **Outlier Handling:** Plotted Box plots for Visualizing Outliers, Handled outliers in different numeric column based on domain knowledge.
- **Univariate & Bivariate Analysis:** Used histograms, scatterplots, and countplots to explore distributions and variable relationships.
- **Correlation Analysis:**  
  - Pearson correlation heatmap for numerical features.  
  - ANOVA F-test for evaluating categorical feature importance.
- **Feature Engineering & Encoding:**
  - Dropped Columns which did not affect the target price.  
  - Added `price_per_sqft` as a derived metric.  
  - Target Encoding applied to `location` for better model input.
- **Model Training & Evaluation:**  
  - Trained and evaluated Linear Regression, Ridge, Random Forest, and XGBoost.  
  - Developed a metric evaluation function for automated comparison.
- **Model Tuning & Performance Boost:**  
  - Fine-tuned XGBoost model with hyperparameters.
  - Saved the Tuned Model for predictions, Calculated residuals and residuals_pct and visualized the margin of error. Using feature engineering handled margin of erorr.  
  - Reduced Margin of Error from **7.14% ➝ 1%**, improved R² from **0.92 ➝ 0.99**.


## 🧱 Tech Stack

- **Python** (3.10+)
- **Scrapy** (for API Scraping)
- **SQLite3** (for Data Storage)
- **Pandas, NumPy, Matplotlib, Seaborn** (EDA & Visualization)
- **Scikit-learn & XGBoost** (model training & tuning)
- **Flask** (API and backend interface)
- **Render** (for app deployment)

### 📈 Visualizng Model Performance, Error Margin, Metrics:

### Model Metrics Without Feature Enginerring:
**We are checking for Error margin >10% , meaning for how many records the model predicted price more or less than 10%**

| Model              | R² Score | Error Margin > 10| 
|--------------------|----------|---------------   |
| XGBoost            | 0.97     | 7.76%            |
| Random Forest      | 0.98     | 7.14%            |
| Linear Regression  | 0.89     | 9.12%            |


### Model Metrics After Feature Enginerring: (Generated price_per_sqrft for better model interpretability) 

| Model              | R² Score | Error Margin > 10|
|--------------------|----------|----------------  |
| XGBoost (tuned)    | 0.93     | 1%               |
| Random Forest      | 0.99     | 2%               |
| Linear Regression  | 1.00     | 4%               | 

✅ Final Model Used: **XGBoost (with hyperparameter tuning)**  
🎯 Metric Used: **R² Score & Error Margin**

## 🔥 Key Results & Visuals

### 1. CountPlot of Categorical variables   
![Count plot](assets/count.png)

### 2. BarChart of Localities with Lowest avg_price of Properties.   
![Barchart](assets/low_avg.png)

### 3. Co-Relation Matrix: Visualizing the Co-relation of different features affecting the target.
![Heatmaps](assets/corelation.png)

### 4. BarChart of Localities with Highest avg_price of Properties.  
![Barchart](assets/high_avg.png)


## 💡 Future Improvements

- Integrate live listings to keep model updated.
- Run the reproducable script to get the trained model as .pkl
- Tinker around the api and expand prediction to other metro cities.

