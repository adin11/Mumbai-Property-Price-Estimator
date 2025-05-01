![banner](assets/banner.png)

Banner [source](https://banner.godori.dev/)

![Python version](https://img.shields.io/badge/Python%20version-3.10%2B-lightgrey)
![GitHub last commit](https://img.shields.io/github/last-commit/adin11/mumbai-property-price-estimator)
![Type of ML](https://img.shields.io/badge/Type%20of%20ML-Regression-blue)
![License](https://img.shields.io/badge/License-MIT-green)
[![Flask App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mumbaipriceteller.on.render.com)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

---
# 🏠 Mumbai Property Price Estimator
### https://mumbaipriceteller.onrender.com

🎥 **[Watch Demo Video](link_to_your_video_here)** – See the app in action predicting Mumbai property prices in real time!

## 🔍 Business Problem
Property buying in Mumbai can be confusing with significant price variation across locations, property types, and builder reputations. This app helps homebuyers, sellers, and investors make informed pricing decisions by estimating property prices using machine learning — in real-time and without manual guesswork.

## 🧠 **Key Findings:**  
> Properties located in central Mumbai with higher square footage and proximity to transit hubs command premium prices.  
> Feature engineering, especially `price_per_sqft` and target encoding for `location`, significantly boosted model accuracy.  
> After tuning, XGBoost achieved **99% R² score** and **1% error margin**, making it ideal for real-time price prediction.

---
## 📊 Data Source

- Data scraped from [MagicBricks](https://www.magicbricks.com/) using Scrapy via MagicBricks Backend Api.
- Stored in SQLite3 database for easy access and analysis.

---

## ⚙️ Methods

- **Data Scraping & Storage:** Scrapy used to pull data from MagicBricks’ backend API. Structured into SQLite database.
- **Univariate & Bivariate Analysis:** Used histograms, scatterplots, and countplots to explore distributions and variable relationships.
- **Correlation Analysis:**  
  - Pearson correlation heatmap for numerical features.  
  - ANOVA F-test for evaluating categorical feature importance.
- **Feature Engineering & Encoding:**  
  - Added `price_per_sqft` as a derived metric.  
  - Target Encoding applied to `location` for better model input.
- **Model Training & Evaluation:**  
  - Trained and evaluated Linear Regression, Ridge, Random Forest, and XGBoost.  
  - Developed a metric evaluation function for automated comparison.
- **Model Tuning & Performance Boost:**  
  - Fine-tuned XGBoost model with hyperparameters.  
  - Reduced error from **7.14% ➝ 1%**, improved R² from **0.92 ➝ 0.99**.

---

## 🧱 Tech Stack

- **Python** (3.10+)
- **Scrapy** (for API scraping)
- **SQLite3** (for data storage)
- **Pandas, NumPy, Matplotlib, Seaborn** (EDA & visualization)
- **Scikit-learn & XGBoost** (model training & tuning)
- **Flask** (API and backend interface)
- **Render** (for app deployment)

---

## 🔥 Key Results & Visuals

### 1. Correlation Heatmap  
*(Add your heatmap image here)*  
![heatmap](assets/heatmap.png)

### 2. Model Evaluation  
*(Add your performance summary or metric comparison table screenshot here)*  
![model_eval](assets/model_eval.png)

### 3. Web App Screenshot  
*(Add screenshot of your deployed Flask app here)*  
![app_screenshot](assets/app_ui.png)

### 📈 Top Performing Model:

| Model              | R² Score | Error Margin |
|--------------------|----------|---------------|
| XGBoost (tuned)    | 0.99     | 1%            |
| Random Forest      | 0.96     | ~2.5%         |
| Linear Regression  | 0.92     | ~7.14%        |

✅ Final Model Used: **XGBoost (with hyperparameter tuning)**  
🎯 Metric Used: **R² Score & Error Margin**

---

## 🚀 Deployment

- The model is deployed using Flask and hosted on **Render**.
- REST API created for real-time price predictions.
- Scalable architecture to allow future city integrations.

---

## 💡 Future Improvements

- Integrate live listings to keep model updated.
- Expand prediction to other metro cities.
- Add filters for user preferences like floor number, facing, etc.
- Move toward a full frontend interface with map-based insights.

---

## 🧾 License
This project is licensed under the MIT License. Feel free to use, fork, and improve upon it.
---

### 👤 Author
Created by **Adin Raja** – [LinkedIn]((https://www.linkedin.com/in/adinraja78/))
---
