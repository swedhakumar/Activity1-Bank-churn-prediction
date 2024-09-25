from flask import Flask, request, render_template
import pickle
import numpy as np


path='bcp.pkl'
model = pickle.load(open(path, 'rb'))

app=Flask(__name__)
@app.route('/')
def submit():
    return render_template('Bank Churn.html')

@app.route('/input',methods=['GET','POST'])
def input():
    details=request.form
    msg=""
    cs= int(details['cs'])
    geo= int(details['geo'])
    gender = int(details['gender'])
    age=int(details['age'])
    tenure = int(details['tenure'])
    balance=float(details['balance'])
    np=int(details['np'])
    crd=int(details['crd'])
    active=int(details['active'])
    salary=float(details['salary'])
    germany=spain=0
    if(geo==1):
        spain=1
    elif(geo==2):
        germany=1

    prediction=model.predict([[cs , age, tenure, balance, np, crd, active,salary,germany,spain,gender]])
    
    if prediction==0:
        msg="Not Exited"
    else:
        msg="Exited"
    
    return render_template('output.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)