
# Retrieve_country_data
In this project I have described that how to create a web api to get country data.

# Here is step by step method
For the Rest countries data I am using following Rest API Data  
https://restcountries.com/

# Step1
You should have install conda in your system so that separate environment can be created for separate project which will help considering packages and version no required for your project.

If you do not have conda in your sytem, Please download using below link:
https://docs.conda.io/projects/miniconda/en/latest/

# Step2
After downloading miniconda create an virtual environment which is dedicated to your project so that your existing environment remain unchanged.

First change the directory to the project directory where you have cloned this repository
Use the following command to create a virtual environment named as "project_env" with the python version 3.11
conda create --name project_env python==3.11

this will create a new environment with latest python including pip

To ensure that environment is successfully created or not, run the following command and you will see the project_env 
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
In my case I had named my environment assignment_env so just changed the name in start_api.bat but you do not need to change this as you are following my steps.  
![src0](https://github.com/ragvendra3898/Retrieve_country_data/assets/62380006/fe242ffb-14c5-4f11-8c13-a4af5929e00f)


# Step6
Now copy the following url and paste in your browser, you will get the running api  
http://localhost:8000/docs

# Step7
To use any endpoint you should have first click on "Try it out" button available in right corner of every endpoint
In the api using first endpoint generate a access token by providing username as "testuser" and password as "testpassword" to access all other endpoints.
This will generate a new token for you and you can copy this token and paste this in other endpoints in place of "access_token" to use the functionality.

# Step8
See from the screenshots

![scr1](https://github.com/ragvendra3898/Retrieve_country_data/assets/62380006/fd7fc332-7d38-421e-bcc4-689a1b3ffd1a)
![scr2](https://github.com/ragvendra3898/Retrieve_country_data/assets/62380006/a5160be6-6c08-4bee-8997-ebf703b2a77b)
![scr3](https://github.com/ragvendra3898/Retrieve_country_data/assets/62380006/88678e5e-ce74-49fe-9cd6-e187916d762f)
![scr4](https://github.com/ragvendra3898/Retrieve_country_data/assets/62380006/be38abed-5cb2-48fc-81dc-272e819a8cf7)
![scr5](https://github.com/ragvendra3898/Retrieve_country_data/assets/62380006/30f7fbf2-1188-4fe8-9614-97164b642968)

Thank You
