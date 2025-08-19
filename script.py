# Reproducable script created after prototyping in jupyter

import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.simplefilter(action="ignore", category=RuntimeWarning)

# function for loading dataset from SQLite database
def load_data(db_path="real_estate.db", table="properties"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    conn.close()
    return df

# function for cleaning dataset
def preprocess_data(df):
    df['bedrooms'] = pd.to_numeric(df['bedrooms'], errors="coerce").astype("Int64")
    df['carpet_area'] = pd.to_numeric(df['carpet_area'], errors="coerce").astype("Int64")
    df['balconies'] = pd.to_numeric(df['balconies'], errors="coerce").astype("Int64")
    df['price'] = pd.to_numeric(df['price'], errors="coerce").astype("Int64")
    df['bathrooms'] = pd.to_numeric(df['bathrooms'], errors="coerce").astype("Int64")

    df['balconies'].fillna(0, inplace=True)
    df['bedrooms'].fillna(0, inplace=True)
    df.dropna(subset=['price'], inplace=True)
    df.dropna(inplace=True)

    # Fix property type
    df['property_type'].replace({'Other': 'Resale'}, inplace=True)
    df = df.query('property_type != "Rent"')

    # Fix possession status
    df['poss_status'] = df['poss_status'].apply(
        lambda x: x if x in ['Under Construction', 'Immediately', 'Ongoing', 'Ready To Move', 'Ready to Move']
        else 'Under Construction'
    )
    df['poss_status'].replace(
        {'Ready To Move': 'Ready to Move', 'Ongoing': 'Under Construction'}, inplace=True
    )
    df.loc[(df['property_type'] == 'Resale') & (df['poss_status'] == 'Under Construction'),
           'poss_status'] = 'Ready to Move'

    # Drop bad locations
    df = df[df['location'].map(df['location'].value_counts()) > 1]

    # Handle outliers
    df = df.query("bedrooms <= 5 and carpet_area >= 140 and bathrooms <= 6")
    df = df.query("price <= 150000000 or location == 'Juhu'")
    return df


# function for feature engineering & encoding
def feature_engineering(df):
    df['price_per_sqrft'] = (df['price'] / df['carpet_area']).astype(int)

    df['property_type'] = df['property_type'].map({'Resale': 0, 'New Property': 1})
    df['furnish_status'] = df['furnish_status'].map(
        {'Unfurnished': 0, 'Semi-Furnished': 1, 'Furnished': 2}
    )
    df['poss_status'] = df['poss_status'].map({'Under Construction': 0, 'Ready to Move': 1})

    # Target encoding for location
    avg_price_location = df.groupby('location')['price'].mean().astype(int)
    df['location_encoded'] = df['location'].map(avg_price_location)
    df.drop(columns=['location', 'latitude', 'longitude'], inplace=True)

    return df


# function for splitting dataset
def split_data(df):
    X = df.drop('price', axis=1)
    y = df['price']
    return train_test_split(X, y, test_size=0.3, random_state=42)


# function for training & evaluating model
def train_evaluate_model(model, X_train, X_test, y_train, y_test,save_as=None):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(f"Model: {model.__class__.__name__}")
    print(f"Train R²: {round(train_score, 2)} | Test R²: {round(test_score, 2)}")
    print(f"RMSE: {round(rmse, 2)} | R² Score: {round(r2, 2)}\n")

    if save_as:
        import joblib
        joblib.dump(model,save_as)
        print(f"model saved as {save_as}")

    return model

# function for running pipeline
def main():
    df = load_data()
    print("Initial shape:", df.shape)

    df = preprocess_data(df)
    print("Shape after cleaning:", df.shape)

    df = feature_engineering(df)
    print("Shape after feature engineering:", df.shape)

    X_train, X_test, y_train, y_test = split_data(df)
    
    # Try different models
    train_evaluate_model(LinearRegression(), X_train, X_test, y_train, y_test)
    train_evaluate_model(Ridge(), X_train, X_test, y_train, y_test)
    train_evaluate_model(RandomForestRegressor(), X_train, X_test, y_train, y_test)
    best_model = train_evaluate_model(XGBRegressor(n_estimators=500, learning_rate=0.05, max_depth=6),
                        X_train, X_test, y_train, y_test,save_as='final_model1.pkl')


if __name__ == "__main__":
    main()
