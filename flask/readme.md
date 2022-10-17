# Create a FLASK API
Navigate to the main directory <br>
`cd ~/.../main` <br>

Create a folder to store the app <br>
`mkdir flask` <br>

Navigate to the new folder <br>
`cd flask` <br>

Create a virtual environment <br>
`python3 -m venv vir_env` <br>

Activate the virtual environment <br>
`source vir_env/Scripts/activate` <br>

Install all the packages we’ll need <br>
`pip3 install flask pandas sklearn` <br>

Save a list of packages and versions that production will need to install <br>
`pip3 freeze > requirements.txt` <br>

Create new files <br>
`touch app.py` <br>
`touch Procfile` <br>
`touch wsgi.py` <br>
`mkdir models` <br>
`mkdir templates` <br>

Move the pickle file `model_file.p` into `models` file. Store html files in `templates` file. 

# Run the app
Run the command: <br>
`python wsgi.py` <br>

And you'll see this: <br>
![result](images/run.png) <br>

It shows the application is running locally on the URL http://127.0.0.1:5000. Navigate to the URL in the browser and an user-input form will show up. <br>
![form](images/input.png) <br>




