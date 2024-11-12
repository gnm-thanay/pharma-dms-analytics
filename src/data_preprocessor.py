import pandas as pd
import numpy as np
import os

# Define input and output paths
input_path = 'pharma-dms-analytics/data/raw'           # Original generated data
output_path = 'pharma-dms-analytics/data/cleaned'  # Folder to save cleaned data

# Ensure output directory exists
os.makedirs(output_path, exist_ok=True)

# Function to clean and preprocess physician data
def clean_physician_data():
    df = pd.read_csv(f"{input_path}/physician_data.csv")
    
    # Fill missing 'Years_of_Experience' with median and correct negative and extreme outliers
    df['Years_of_Experience'] = df['Years_of_Experience'].apply(lambda x: np.nan if x < 0 or x > 50 else x)
    df['Years_of_Experience'].fillna(df['Years_of_Experience'].median(), inplace=True)
    
    # Fill missing 'Previous_Prescriptions' and 'Engagement_Score' with their respective medians
    df['Previous_Prescriptions'].fillna(df['Previous_Prescriptions'].median(), inplace=True)
    df['Engagement_Score'].fillna(df['Engagement_Score'].median(), inplace=True)
    
    # Standardize specialty names
    df['Specialty'] = df['Specialty'].replace({"GP": "General Practice", "General_Practice": "General Practice"})
    
    df.to_csv(f"{output_path}/cleaned_physician_data.csv", index=False)
    print("Physician data cleaned and saved.")

# Function to clean and preprocess sales and prescription data
def clean_sales_prescription_data():
    df = pd.read_csv(f"{input_path}/sales_prescription_data.csv")
    
    # Drop rows with missing 'Date' or 'Drug_Prescribed'
    df.dropna(subset=['Date', 'Drug_Prescribed'], inplace=True)
    
    # Fill missing 'Units_Sold' with median value
    df['Units_Sold'].fillna(df['Units_Sold'].median(), inplace=True)
    
    # Convert 'Date' to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    df.to_csv(f"{output_path}/cleaned_sales_prescription_data.csv", index=False)
    print("Sales and prescription data cleaned and saved.")

# Function to clean and preprocess marketing campaign data
def clean_marketing_campaign_data():
    df = pd.read_csv(f"{input_path}/marketing_campaign_data.csv")
    
    # Fill missing 'Campaign_Type' and 'Engagement_Response' with mode
    df['Campaign_Type'].fillna(df['Campaign_Type'].mode()[0], inplace=True)
    df['Engagement_Response'].fillna(df['Engagement_Response'].mode()[0], inplace=True)
    
    # Limit 'Contact_Frequency' outliers to a max reasonable value (e.g., 10)
    df['Contact_Frequency'] = df['Contact_Frequency'].apply(lambda x: 10 if x > 10 else x)
    df['Contact_Frequency'].fillna(df['Contact_Frequency'].median(), inplace=True)
    
    # Convert 'Last_Contact_Date' to datetime format
    df['Last_Contact_Date'] = pd.to_datetime(df['Last_Contact_Date'])
    
    df.to_csv(f"{output_path}/cleaned_marketing_campaign_data.csv", index=False)
    print("Marketing campaign data cleaned and saved.")

# Function to clean and preprocess inventory data
def clean_inventory_data():
    df = pd.read_csv(f"{input_path}/inventory_data.csv")
    
    # Drop rows with missing 'Date' or 'Distribution_Center'
    df.dropna(subset=['Date', 'Distribution_Center'], inplace=True)
    
    # Handle missing values and outliers
    df['Inventory_Level'] = df['Inventory_Level'].apply(lambda x: 0 if x < 0 else x)
    df['Inventory_Level'].fillna(df['Inventory_Level'].median(), inplace=True)
    df['Reorder_Quantity'].fillna(df['Reorder_Quantity'].median(), inplace=True)
    df['Lead_Time_Days'].fillna(df['Lead_Time_Days'].median(), inplace=True)
    
    # Convert 'Date' to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    df.to_csv(f"{output_path}/cleaned_inventory_data.csv", index=False)
    print("Inventory data cleaned and saved.")

# Function to clean and preprocess historical sales and forecast data
def clean_historical_sales_forecast_data():
    df = pd.read_csv(f"{input_path}/historical_sales_forecast_data.csv")
    
    # Drop rows with missing 'Date' or 'Region'
    df.dropna(subset=['Date', 'Region'], inplace=True)
    
    # Fill missing 'Units_Sold' and 'Forecasted_Demand' with median values
    df['Units_Sold'] = df['Units_Sold'].apply(lambda x: np.nan if x < 0 else x)
    df['Units_Sold'].fillna(df['Units_Sold'].median(), inplace=True)
    df['Forecasted_Demand'] = df['Forecasted_Demand'].apply(lambda x: np.nan if x < 0 else x)
    df['Forecasted_Demand'].fillna(df['Forecasted_Demand'].median(), inplace=True)
    
    # Convert 'Date' to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    df.to_csv(f"{output_path}/cleaned_historical_sales_forecast_data.csv", index=False)
    print("Historical sales and forecast data cleaned and saved.")

# Driver code to clean all datasets
clean_physician_data()
clean_sales_prescription_data()
clean_marketing_campaign_data()
clean_inventory_data()
clean_historical_sales_forecast_data()

print("All datasets have been cleaned and saved to '../data/cleaned'.")
