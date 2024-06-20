import requests
import predict
import numpy as np

period = {
    'year':2023,
    'month':5
}

# df = predict.read_prep_data(year, month)

# pred = predict.predict(df)

# df_results = predict.prep_output(df,pred)
# df_results = df_results.tolist()

url='http://localhost:9696/predict'
response = requests.post(url, json=period)
results = response.json()

predictions = [result['predictions'] for result in results]
mean_duration = np.mean(predictions)
print(f"Mean predicted duration for May 2023: {mean_duration:.2f} minutes")

