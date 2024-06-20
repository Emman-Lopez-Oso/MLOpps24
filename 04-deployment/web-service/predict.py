import pickle 
import pandas as pd
from flask import Flask, request, jsonify

with open('model.bin', 'rb') as f_in: # 'rb' means read-binary
    (dv, model) = pickle.load(f_in)

def read_prep_data(year, month):
    categorical = ['PULocationID', 'DOLocationID']
    filename= f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02d}.parquet"
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

    return df

def predict(df):
   categorical = ['PULocationID', 'DOLocationID']
   features = df[categorical].to_dict(orient='records')
   X = dv.transform(features)
   model.predict(X)
   preds= model.predict(X)
   return preds

def prep_output(df,preds):
    df_results = df[['ride_id']].copy()
    df_results.loc[:, 'predictions'] = preds.tolist()

    return df_results

app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')

    df = read_prep_data(year, month)
    preds = predict(df)
    results = prep_output(df,preds)

    
    return jsonify(results.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)