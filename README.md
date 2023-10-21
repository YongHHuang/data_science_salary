# ***Data Science Job Market Analysis***<br><br>

## ***Software and Language***
Python 3.8 <br>

## ***Project Overview***
This project aimed to enhance my prospects of securing a data analyst/scientist role by comprehensively understanding the job market. I achieved this by scraping job listings from platforms like Glassdoor using Selenium. The primary objectives were:
- Identified in-demand skills highly sought after by employers.
- Extracted crucial keywords to enhance resume quality and effectiveness.
- Examined average salary benchmarks, categorized by job titles and geographical regions.
- Evaluated job opening distribution across various states.

## ***Results***
**1. Top 3 In-Demand Skills for Employers:<br><br>**
Most companies require candidates to have proficiency in R/Python, SQL, and machine learning. Some also seek expertise in big data (Spark or Hadoop), cloud platforms (AWS or Azure), Excel, and data visualization tools like Tableau or Power BI.


<p align="2000px" width="50%" >
    <img width="40%" height=300 src="image/skills.png">
</p> <br>  

**2. Common keywords in job descriptions:<br><br>**

<p align="left" width="50%"> 
    <img width="55%" height=500 src="image/keywords.png">
</p> <br>
3. 
4. 

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
1. What are their salaries?
2. How many job openings are there?
3. What professional skills do companies need?
4. What are common keywords that I should put on my resume? <br><br>

<h3> 1. What are their salaries? </h3>
A data scientist's average salary is about 80K ~ 140K. Washington, California, and New York States have the highest salaries.

<p align="left" width="50%"> <br><br>
    <img width="55%" height=500 src="image/salary.png"> 
</p> <br>  
    
<h3> 2. How many job openings are there? </h3>
California and work from home positions have the most openings.

<p align="left" width="50%"> <br><br>
    <img width="55%" height=500 src="image/job_counts.png">
</p> <br>

<h3> 3. What professional skills do companies need? </h3>
Most companies require candidates to have R/Python, SQL, and machine learning skills.

<p align="left" width="50%"> <br><br>
    <img width="55%" height=500 src="image/skills.png">
</p> <br>  

<h3> 4. What are common keywords in job descriptions? </h3>
The keywords that appear most in all job descriptions are team, data science/scientist, and machine learning.

<p align="left" width="50%"> <br><br>
    <img width="55%" height=500 src="image/keywords.png">
</p> <br>
    

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
