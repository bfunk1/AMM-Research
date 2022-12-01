import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from eth_simulation import eth_data
import random

pd.set_option('display.float_format', lambda x: '%.3f' % x)

count = 0

def ethq_amm_simulation(_ethp, _k):
    return np.sqrt(_k/_ethp)

def usdcq_amm_simulation(_ethq, _k):
    return _k/_ethq

def portfolio_size():
    return 50000 #random.randint(10000, 1000000)

def portfolio_size_2():
    old = portfolio_size()
    return 0.8 * old
    
df = pd.DataFrame()

days = []
for x in range(len(eth_data.iloc[: , -1])):
    days.append(x + 1)

df["days"] = days

df["ethp"] = eth_data.iloc[: , -1]

df["ethv"] = eth_data.iloc[: , 1]

df['ethv'] = df['ethv']**1.5

df["k"] = (portfolio_size()/2) * ((portfolio_size()/2) / df.iloc[0][1])

df["ethq"] = df.apply(lambda x: ethq_amm_simulation(x.ethp, x.k), axis=1)

df["usdcq"] = df.apply(lambda x: usdcq_amm_simulation(x.ethq, x.k), axis=1)

df["LP Value"] = (df["ethp"] * df["ethq"]) + df["usdcq"]

df["Hold Value"] = df.iloc[0][5] + (df["ethp"] * df.iloc[0][4])

df["Impermanent Loss"] = df["Hold Value"] - df["LP Value"]

df["Vol Portfolio"] = ((portfolio_size() - (portfolio_size_2())) / df["ethv"][0]) * df["ethv"]

df["new_k"] = (portfolio_size_2()/2) * ((portfolio_size_2()/2) / df.iloc[0][1])

df["new_ethq"] = df.apply(lambda x: ethq_amm_simulation(x.ethp, x.new_k), axis=1)

df["new_usdcq"] = df.apply(lambda x: usdcq_amm_simulation(x.new_ethq, x.new_k), axis=1)

df["LP Value V2"] = (df["ethp"] * df["new_ethq"]) + df["new_usdcq"]

df["vol_k"] = (df["Vol Portfolio"]/2) * ((df["Vol Portfolio"]/2) / df.iloc[0][2])

df["volq"] = df.apply(lambda x: ethq_amm_simulation(x.ethv, x.vol_k), axis=1)

df["vol_usdcq"] = df.apply(lambda x: usdcq_amm_simulation(x.volq, x.vol_k), axis=1)

df["LP Value Vol"] = (df["ethv"] * df["volq"]) + df["vol_usdcq"]

df["IL V2"] =  df["Hold Value"] - (df["LP Value V2"] + df["LP Value Vol"])

df["IL Improvement"] = df["Impermanent Loss"] - df["IL V2"]

avg = df["IL Improvement"].mean()

# pd.set_option('display.max_rows', None)

print(avg)

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
line1, = plt.plot(df["Impermanent Loss"], label = "IL V1")
line2, = plt.plot(df["IL V2"], label="IL V2")
leg = plt.legend(loc='upper center')


plt.show()