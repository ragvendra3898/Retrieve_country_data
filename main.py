from fastapi import FastAPI, Security, HTTPException, status, Request, BackgroundTasks, Depends, File, UploadFile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional, Annotated
import uvicorn
from jose import JWTError, jwt
import requests

apiversion = "1.0"
app = FastAPI(title="Demo API", description="This is the demo api only for assignment purpose.", version=apiversion)




# User model 
class User(BaseModel):
    username: str
    password: str

# Hardcoded user data 
users_db = {
    "testuser": {
        "username": "testuser",
        "password": "testpassword"
    }
}


def validate_token(token:str):
    secret_key = "Abcd1234#"
    try:
        decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        # Check if the decoded payload matches the user's identity
        if decoded_payload["pass_word"] == users_db.get("testuser")["password"] and decoded_payload["user_name"] == users_db.get("testuser")["username"]:
            return "valid"
        else:
            return "invalid"
    except jwt.ExpiredSignatureError:
        return "expired"
    except jwt.DecodeError:
        return "None"

# OAuth2 authentication endpoint
@app.post("/token", response_model=dict)
def generate_access_token(username:str, password:str):
    try:
        # Secret key for signing the token
        secret_key = "Abcd1234#"

        # Create a payload for the token 
        payload = {"user_name": username,"pass_word": password}

        # Generate the token
        token = jwt.encode(payload, secret_key, algorithm="HS256")

        return {"response":f"Your access_token is {token}"}
    except Exception as e:
        return {"response":f"An error occured {str(e)}"}  



@app.get("/get_all_countries")
def retrieve_all_countries(access_token:str):
    try:
        validation = validate_token(str(access_token))
        if validation=='valid':
            url = "https://restcountries.com/v3.1/all"

            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            return {"response": f"{response.text}"}
        elif validation=='invalid':
            return {"response":f"Provided value for access token is invalid."}
        elif validation== "expired":
            return {"response":f"Provided access token is expired, Kindly generate new token."}
        elif validation=="None":
            return {"response":"An error occured while decoding the token, Please try again later."}
    except Exception as e:
        return {"response":f"An error occured {str(e)}"}      
    

@app.get("/get_country_by_full_name")
def retrieve_country_by_full_name(access_token:str, country_full_name:str):
    try:
        validation = validate_token(str(access_token))
        if validation=='valid':
            url = f"https://restcountries.com/v3.1/name/{country_full_name}?fullText=true"

            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            return {"response": f"{response.text}"} 
        elif validation=='invalid':
            return {"response":f"Provided value for access token is invalid."}
        elif validation== "expired":
            return {"response":f"Provided access token is expired, Kindly generate new token."}
        elif validation=="None":
            return {"response":"An error occured while decoding the token, Please try again later."}
    except Exception as e:
        return {"response":f"An error occured {str(e)}"}      

@app.get("/get_countries_by_filter")
def retrieve_countries_by_filter(access_token:str, field1:str ='population',field2:str = 'area', field3:str = 'languages',sort_by:str = "ascending"):
    try:
        validation = validate_token(str(access_token))
        if validation=='valid':
            url = f"https://restcountries.com/v3.1/all?fields={field1},{field2},{field3}"

            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            if sort_by == "ascending":
                return {"response": f"{response.text}"}
            elif sort_by == "descending":
                # Sorting in descending order based on 'population'
                sorted_data_descending = sorted(response, key=lambda x: field1, reverse=True)
                return {"response": f"{sorted_data_descending}"} 
            else:
                return {"response":"Provided value for SORT_BY is not correct."}
        elif validation=='invalid':
            return {"response":f"Provided value for access token is invalid."}
        elif validation== "expired":
            return {"response":f"Provided access token is expired, Kindly generate new token."}
        elif validation=="None":
            return {"response":"An error occured while decoding the token, Please try again later."}    
    except Exception as e:
        return {"response":f"An error occured {str(e)}"}    



if __name__ == '__main__':
	uvicorn.run('main:app', host='localhost', port=8000)