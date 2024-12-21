from nsetools import Nse
from datetime import date
import io
import os
from jugaad_data.nse import stock_df , full_bhavcopy_raw
import pandas as pd



# Get symbols
# Define the date for the bhavcopy
bhav_date = date(2024, 12, 1)  # Use a recent working market date for accuracy
output_file = "./data/instruments.csv"
# Download the bhavcopy for the specified date
raw_data = full_bhavcopy_raw(bhav_date)
df = pd.read_csv(io.StringIO(raw_data))
df["SYMBOL"].to_csv(output_file, index=False)
# 

for symbol in df["SYMBOL"]:
    print("symbol", symbol)

# Specify the file path and name where you want to save the CSV
output_directory = "./data"
os.makedirs(output_directory, exist_ok=True)  # Ensure the directory exists


SCRIP_SYMBOL = "RAMASTEEL"
output_file_path = os.path.join(output_directory, f"stock_data_{SCRIP_SYMBOL}.csv")
# Download stock data to pandas dataframe
df = stock_df(symbol=SCRIP_SYMBOL, from_date=date(2000,1,1),
            to_date=date(2024,1,30), series="EQ")

# Save the DataFrame to a CSV file
df.to_csv(output_file_path, index=False)
print(df.tail())