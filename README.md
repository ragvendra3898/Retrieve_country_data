# Retrieve_country_data
In this project I have described that how to create a web api to get country data.

# Here is step by step method

# Step1
You should have install conda in your system so that separate environment can be created for separate project which will help considering packages and version no required for your project.

If you do not have conda in your sytem, Please download using below link:
https://docs.conda.io/projects/miniconda/en/latest/

# Step2
After downloading miniconda create an virtual environment which is dedicated to your project so that your existing environment remain unchanged.

First change the directory to the project directory where you have cloned the repository
Use the following command to create a virtual environment named as "project_env" with the python version 3.11
conda create --name project_env python==3.11

this will create a new environment with latest python including pip

To ensure that environment is successfully created or not run the following command and you will see the project_env 
conda info --envs

# Step3
Now to use the project_env run the following command
conda activate project_env

# Step4
Now install the dependencies using pip which we will use in the project
pip install "fastapi[all]"
pip install "python-jose[cryptography]

# Step5
To activating the project_env and running the main.py file just write the following command in terminal
start_api.bat

# Step6
Now copy the following url and paste in your browser, you will get the running api
http://localhost:8000/docs

# Step7
To use any endpoint you should have first click on "Try it out" button available in right corner of every endpoint
In the api using first endpoint generate a access token by providing username as "testuser" and password as "testpassword" to access all other endpoints.
This will generate a new token for you and you can copy this token and paste this in other endpoints in place of "access_token" to use the functionality.

Thank You
