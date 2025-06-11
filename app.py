# import flask
# initialize flask
# add route to application
# define the logic
# run the application

from flask import Flask,redirect,url_for,render_template,request,send_file,jsonify,flash
import pandas as pd 
import numpy as np
#from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename
import pickle

app = Flask(__name__)

@app.route('/') #localhost:5000
def home():
    return render_template('home.html')


@app.route('/abstract') #localhost:5000
def abstract():
    return render_template('abstract.html')

#creating different url paths
@app.route('/login') #localhost:5000/login
def login():
    return render_template('login.html')

@app.route('/upload') #localhost:5000/login
def upload():
    return render_template('upload.html') 

@app.route('/read_data',methods=['post'])
def read_data():
    data = request.files['file']
    data = pd.read_csv(data)
    print(data)
    return render_template('preview.html',data=data)

load = pickle.load(open('model.pkl','rb'))
#scaler = MinMaxScaler()


@app.route('/predict',methods=['POST'])
def predict():
	int_feature = [x for x in request.form.values()]
	print(int_feature)
	int_feature = [float(i) for i in int_feature]
	final_features = [np.array(int_feature)]
	prediction = load.predict(final_features)

	output = format(prediction[0])
	print(output)
	return render_template('prediction.html', prediction_text= output)

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/future') #localhost:5000
def future():
    return render_template('future.html')

@app.route('/charts') #localhost:5000
def charts():
    return render_template('chart.html')

if __name__=='__main__':
    app.run(debug=True)