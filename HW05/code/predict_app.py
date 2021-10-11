from flask import Flask
from flask import request
from flask import jsonify
import pickle

with open('model1.bin', 'rb') as f_in_model:
    model = pickle.load(f_in_model)

with open('dv.bin', 'rb') as f_in_dv:
    dv = pickle.load(f_in_dv)

app = Flask('predict_app') # give an identity to your web service

@app.route('/predict',methods=['POST'])
def predict():
    customer = request.get_json()
    
    X = dv.transform(customer)

    y_pred = round(model.predict_proba(X)[0,1],3)

    result = {
        'churn_probability': y_pred
    }
    
    return jsonify(result)

if __name__=='__main__':
   app.run(debug=True, host='0.0.0.0', port=9696)