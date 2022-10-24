# Data Scientist Salary Estimator

## Project Goal
Created a tool that estimated data scientist salaries to help users negotiate their income when they get a job.

## What's in the Project
- Scraped over 1000 jobs from Glassdoor using Python and Selenium.
- Cleaned data and engineered features from the job title and job description, quantifying these data as job positions, seniorities, and required skills.
- Performed exploratory data analysis(EDA) and visualized the findings.
- Optimized Linear, Lasso, and Random Forest Regression using GridSearchCV to reach the best model.
- Built a client-facing API using Flask.

## Code and Resources Used
Python Version: 3.8 <br>
Packages: selenium, numpy, pandas, sklearn, re, matplotlib, seaborn, nltk, wordcloud, flask, json, pickle

Glassdoor Scraper Article: [Selenium Tutorial: Scraping Glassdoor.com in 10 Minutes](https://mersakarya.medium.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905) <br>
Glassdoor Scraper Github: [Selenium Tutorial: Scraping Glassdoor.com](https://github.com/arapfaik/scraping-glassdoor-selenium) <br>
Flask Productionize: [Productionize a Machine Learning model with Flask and Heroku](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2) <br>
Youtube Project Walk-Through: [Data Science Project From Scratch](https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t)

## Web Scraping
The Glassdoor scraper was from 2019, and part of the code is outdated. I Updated and modified the scraper to scrape job postings from Glassdoor.com. With each job posting, we scraped the following:
- Job Title
- Estimated Salary
- Job Description
- Company Rating
- Company Name
- Job Location
- Company Size
- Comapny Founded Year
- Type of Ownership
- Industry
- Sector
- Revenue

## Data Cleaning
Other than fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset, we also made the following changes:
- According to the keyword in the job title, created a seniority column that classified jobs into three categories: Low, High, and Unknown.
- Simplified job titles to six categories: Data Analyst, Data Scientist, Data Engineer, ML Engineer, Manager, and Others.
- Created a description_len column for the length of the job description.
- Created six skill columns which having 1 if that specific skill is mentioned in the job description and 0 otherwise:
  - Big Data(Spark or Hadoop)
  - Cloud(AWS or Azure)
  - Excel
  - ML(Machine Learning or Deep Learning)
  - RPython(R or Python)
  - SQL
  - Viztool(Tableau or PowerBI)
Transformed the company founded year into the age of the company.

## EDA
This analysis aims to help me learn more about the data science industry. It interests me because I am seeking a data analyst/scientist job and some of questions are:
- What are their salaries?
- How many jobs are there available in different locations?
- What professional skills are more worth to invest or what do companies need?
- What are common keywords that I should put on my resume?

<p align="left" width="100%">
    <img width="48%" height=280 src="image/salary.png"> 
    <img width="48%" height=280 src="image/job_counts.png"> 
    
</p>
<p align="center" width="100%">    
    <img width="48%" height=280 src="image/skills.png"> 
    <img width="48%" height=280 src="image/keywords.png"> 
</p>

## Model Building
First, encoded categorical columns using pd.get_dummies. Then, split the data into 80% training set and 20% test set. Finally, built three models and evaluated them using Mean Absolte Error(MAE). Three models are:
- Linear Regression: MAE = $22.25K
- Lasso Regression: MAE = $20.67K
- Random Forest Regression: MAE = $19.27K

## Productionize
Built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in user inputs and returns an estimated salary.

<p align="left" width="100%">    
    <img width="55%" height=250 src="image/input.png">
    <img width="25%" height=40 src="image/result.png" align="top">
</p>
