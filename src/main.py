# Driver code

from data_generator import DataGenerator
# from data_preprocessor import DataPreprocessor

if __name__ == "__main__":
    generator = DataGenerator(num_records=1000)
    generator.generate_physician_data()
    generator.generate_sales_prescription_data()
    generator.generate_marketing_campaign_data()
    generator.generate_inventory_data()
    generator.generate_historical_sales_forecast_data()

    print("Simulated data for all datasets has been generated and saved to CSV files.")

    # data_processor = DataPreprocessor()
    # data_processor.run_preprocessing()

    # print("Simulated data for all datasets has been cleaned and saved to CSV files.")
