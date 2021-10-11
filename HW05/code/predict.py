import pickle

with open('model1.bin', 'rb') as f_in_model:
    model = pickle.load(f_in_model)

with open('dv.bin', 'rb') as f_in_dv:
    dv = pickle.load(f_in_dv)

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

X = dv.transform(customer)

pred_customer = round(model.predict_proba(X)[0,1],3)

print(customer)
print("probability of churning: ", pred_customer)
