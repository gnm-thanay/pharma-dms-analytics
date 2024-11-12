# module to generate simulated data

import pandas as pd
import numpy as np
import random
import os

# # defining the output path
# output_path = 'pharma-dms-analytics/data/raw'

# # Ensure output directory exists
# os.makedirs(output_path, exist_ok=True)

# Set seed for reproducibility
np.random.seed(68)
random.seed(68)

class DataGenerator:
    def __init__(self, num_records=1000):
        self.num_records = num_records

    def generate_physician_data(self):
        specialties = ["Oncology", "General Practice", "Hematology", "GP", "General_Practice"]
        regions = ["Northeast", "Midwest", "Southeast", "West"]

        data = {
            "Physician_ID": [f"P{str(i).zfill(4)}" for i in range(1, self.num_records + 1)],
            "Specialty": [random.choice(specialties) for _ in range(self.num_records)],
            "Years_of_Experience": np.random.normal(15, 10, self.num_records).astype(int),
            "Region": [random.choice(regions) for _ in range(self.num_records)],
            "Previous_Prescriptions": np.random.poisson(50, self.num_records),
            "Engagement_Score": np.random.randint(20, 101, self.num_records)
        }
        df = pd.DataFrame(data)

        for col in ["Years_of_Experience", "Previous_Prescriptions", "Engagement_Score"]:
            df.loc[df.sample(frac=0.1).index, col] = np.nan

        df.loc[df.sample(frac=0.05).index, "Years_of_Experience"] = np.random.choice([-1, 100, 150], size=int(self.num_records * 0.05))
        
        self.save_to_csv(df, "pharma-dms-analytics/data/raw/physician_data.csv")


    def generate_sales_prescription_data(self):
        physician_ids = [f"P{str(i).zfill(4)}" for i in range(1, self.num_records + 1)]
        dates = pd.date_range(start="2024-01-01", periods=self.num_records, freq="D")
        
        data = {
            "Date": np.random.choice(dates, self.num_records),
            "Physician_ID": np.random.choice(physician_ids, self.num_records),
            "Drug_Prescribed": ["NewDrug"] * self.num_records,
            "Units_Sold": np.random.poisson(5, self.num_records),
            "Prescription": np.random.choice([0, 1], self.num_records)
        }
        df = pd.DataFrame(data)

        df.loc[df.sample(frac=0.1).index, "Units_Sold"] = np.nan
        df.loc[df.sample(frac=0.05).index, "Drug_Prescribed"] = None
        
        self.save_to_csv(df, "pharma-dms-analytics/data/raw/sales_prescription_data.csv")


    def generate_marketing_campaign_data(self):
        campaign_types = ["Email", "Phone Call", "Event"]
        engagement_levels = ["High", "Medium", "Low"]
        physician_ids = [f"P{str(i).zfill(4)}" for i in range(1, self.num_records + 1)]
        dates = pd.date_range(start="2023-11-01", periods=self.num_records, freq="D")
        
        data = {
            "Campaign_ID": [f"C{str(i).zfill(4)}" for i in range(1, self.num_records + 1)],
            "Physician_ID": np.random.choice(physician_ids, self.num_records),
            "Campaign_Type": np.random.choice(campaign_types, self.num_records),
            "Contact_Frequency": np.random.poisson(3, self.num_records),
            "Last_Contact_Date": np.random.choice(dates, self.num_records),
            "Engagement_Response": np.random.choice(engagement_levels, self.num_records)
        }
        df = pd.DataFrame(data)

        for col in ["Campaign_Type", "Contact_Frequency", "Engagement_Response"]:
            df.loc[df.sample(frac=0.1).index, col] = np.nan

        self.save_to_csv(df, "pharma-dms-analytics/data/raw/marketing_campaign_data.csv")


    def generate_inventory_data(self):
        centers = ["DC001", "DC002", "DC003", "DC004", "DC005"]
        regions = ["Northeast", "Midwest", "Southeast", "West"]
        dates = pd.date_range(start="2024-01-01", periods=self.num_records, freq="D")
        
        data = {
            "Date": np.random.choice(dates, self.num_records),
            "Distribution_Center": np.random.choice(centers, self.num_records),
            "Region": np.random.choice(regions, self.num_records),
            "Inventory_Level": np.random.randint(0, 800, self.num_records),
            "Stockout": np.random.choice(["Yes", "No"], self.num_records),
            "Reorder_Quantity": np.random.randint(0, 500, self.num_records),
            "Lead_Time_Days": np.random.randint(5, 15, self.num_records)
        }
        df = pd.DataFrame(data)

        for col in ["Inventory_Level", "Reorder_Quantity", "Lead_Time_Days"]:
            df.loc[df.sample(frac=0.1).index, col] = np.nan

        df.loc[df.sample(frac=0.05).index, "Inventory_Level"] = np.random.choice([-50, 0, 8000], size=int(self.num_records * 0.05))

        self.save_to_csv(df, "pharma-dms-analytics/data/raw/inventory_data.csv")


    def generate_historical_sales_forecast_data(self):
        regions = ["Northeast", "Midwest", "Southeast", "West"]
        dates = pd.date_range(start="2023-11-01", periods=self.num_records, freq="W")
        
        data = {
            "Date": np.random.choice(dates, self.num_records),
            "Region": np.random.choice(regions, self.num_records),
            "Units_Sold": np.random.poisson(400, self.num_records),
            "Forecasted_Demand": np.random.poisson(420, self.num_records)
        }
        df = pd.DataFrame(data)

        for col in ["Units_Sold", "Forecasted_Demand"]:
            df.loc[df.sample(frac=0.1).index, col] = np.nan

        df.loc[df.sample(frac=0.05).index, "Units_Sold"] = np.random.choice([-50, 0, 3000], size=int(self.num_records * 0.05))

        self.save_to_csv(df, "pharma-dms-analytics/data/raw/historical_sales_forecast_data.csv")


    def save_to_csv(self, df, filename):
        """Append the dataframe to a CSV file if it exists; create a new file if it doesn't."""
        if os.path.exists(filename):
            df.to_csv(filename, mode='a', header=False, index=False)
        else:
            df.to_csv(filename, index=False)
