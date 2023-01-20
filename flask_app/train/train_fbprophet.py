import pandas as pd
import numpy as np
from prophet import Prophet
import pickle

df = pd.read_csv("../data/raw_data.csv", sep=",", index_col="DATE")
df = df[df["DCOILBRENTEU"] != "."]

model=Prophet(interval_width=0.95)

df.rename_axis('ds', inplace=True)
df.rename(columns={'DCOILBRENTEU':'y'}, inplace=True)
df.reset_index(inplace=True) 

print("Data:")
print(df.head())

model.fit(df)

future_dataset= model.make_future_dataframe(periods=5, freq='y')

pred = model.predict(future_dataset)
print("Pred:")
print(pred[['ds','yhat', 'yhat_lower', 'yhat_upper']].head())

next_date = "2023-01-25"
date = pd.DataFrame({'ds':pd.date_range(start=next_date, end=next_date)})

print("Next date:")
print(date.head())

pred = model.predict(date)
print("Predicted value:")
print(pred)

print("Saving model:")
with open('../models/fbprophet.pckl', 'wb') as fout:
    pickle.dump(model, fout)
print("Model saved.")