import yfinance as yf
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

# Get data

ethvol_data = pd.read_csv(r"/Users/benjaminfunk/Downloads/ethv.csv")
ethvol_data['snapped_at'] = ethvol_data['snapped_at'].apply(lambda x: x[:-4])
ethvol_data['snapped_at'] = pd.to_datetime(ethvol_data['snapped_at'])

def testing_range(year_b, month_b, day_b, year_e, month_e, day_e):
    start = dt.datetime((year_b), (month_b), (day_b))
    end = dt.datetime((year_e), (month_e), (day_e))
    ethp_data = yf.download('ETH-USD', start, end).reset_index()
    ethp_data['Date'] = pd.to_datetime(ethp_data['Date'])
    ethvol_data.rename(columns={'snapped_at': 'Date'}, inplace=True)
    mask = (ethvol_data['Date'] >= ethp_data['Date'].min()) & (ethvol_data['Date'] <= ethp_data['Date'].max())
    ethv = ethvol_data.loc[mask]
    merged_data = ethv.merge(ethp_data, how = "inner", on = 'Date')
    merged_data.drop(["Open", "High", "Low", "Adj Close", "Volume", "market_cap", "total_volume"], inplace=True, axis=1)
    merged_data.rename(columns={'Close': 'ethp', 'price': 'ethv'}, inplace=True)
    return merged_data

eth_data = (testing_range(2021, 6, 28, 2022, 10, 28))
    


