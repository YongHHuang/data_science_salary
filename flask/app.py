import flask
from flask import Flask, jsonify, request, render_template
import json
import pickle
import re
import pandas as pd

app = Flask(__name__)

loaded_model = pickle.load(open("models/model_file.p", "rb"))['model']
model_col = pd.Series(loaded_model.feature_names_in_)
    
    
def input_tr(col, new_input):   
    # return rating
    if col == 'rating':
        return new_input['rating']
    
    # return age
    if col == 'age':
        return new_input['age']
    
    # return length of job description
    job_description = new_input['job_description']
    if col == 'description_len':
        return len(job_description)
    
    # if col matches the skill in job description, return 1
    keywords = ['Spark|Hadoop', 'AWS|Azure', '\WExcel\W', 'machine learning|deep learning', 
                '\W(R|Python)\W', 'SQL', 'Tableau|PowerBI|Power BI']
    skills = ['bigdata', 'cloud', 'excel', 'ml', 'rpython', 'sql', 'viztool']
    for i in range(len(keywords)):        
        if i == 3 or i == 5:
            jd = job_description.lower()
        else:
            jd = job_description
        
        if re.search(keywords[i], jd) and skills[i] in col:
            return 1
    
    # if col matches the categorical name, return 1 
    for item in new_input['categorical']:
        if col == item:  
            return 1
    
    # return 0 if nothing matches     
    return 0


def get_model_input(user_input):
    new_input = dict(job_description = user_input.pop('job_description'),
                     rating = float(user_input.pop('rating')),
                     age = float(user_input.pop('age')),
                     categorical = ['_'.join([item[0], item[1]]) for item in user_input.items()])
    
    model_input = model_col.apply(input_tr, new_input=new_input)
    return model_input
 

@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        user_input = request.form.to_dict()
        model_input = get_model_input(user_input)
        prediction = loaded_model.predict(model_input.values.reshape(1, -1))
        
        return render_template("predict.html", prediction=prediction)

    
if __name__ == '__main__':
    application.run(debug=True)