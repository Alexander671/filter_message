# FILTER_MESSAGE
<p align="center">
<img src="https://img.shields.io/badge/server-drf-red"> 
<img src="https://img.shields.io/badge/mesasge--broker-kafka-black">
<img src="https://img.shields.io/badge/container-docker-blue">
<img src="https://img.shields.io/badge/jwt__auth-rest__framework__simplejwt-blue">
</p>


A REST API python backend service "filter_message". </br>
Created two services:
1. **API** messaging service.
2. **Listener** for checking messages.

Tested on Ubuntu 20.04 and
```Python==3.8.10       
Django==4.0.4
django_environ==0.8.1
djangorestframework==3.13.1
djangorestframework_simplejwt==5.1.0
environ==1.0
kafka==1.3.5
requests==2.27.1
pip==22.0.4
```
# CONTENTS:
[Description](#description) </br>
[Deploy](#deploy)           </br>
[Test](#test)               </br>

## Description <a name="description"></a>
**API methods are divided into two types:** 
- **GET/POST** methods for the user.
- **POST** method for listener/consumer message_confirmation.

**The system has 6 main path:**
-  
+ Standart auth
  + accounts/
    + accounts/login
    + accounts/signup
  
+ JWT auth
  + api/token/
  + api/token/refresh/
  + api/token/verify/
  
+ Message
  + api/message/

+ Message confirmation 
  + api/message_confirmation/ 

**Endpoints example:**

*Request:* 
```
GET http://127.0.0.1:8000/api/message
```
*Response:* 
```
[
{
  "message_text":"Hi",
  "user_to":1},
{
  "message_text":"Hi",
  "user_to":1}
]
```

*Request:*
```
POST http://127.0.0.1:8000/api/token/

Content type: application/json
{
       "username": "alexander",
       "password": 123
}
```
*Response:*
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2..."
}
```
for more info look [Test](#test)               </br>

## Getting Started <a name="deploy"></a>
These instructions will get you a copy of the project up and running on your local machine. There are **two** ways to run a project.

1. run without Docker
2. run with Docker 

### Build Without Docker

#### Git

Clone the repository
```
git clone https:https://github.com/Alexander671/filter_message/
```

Navigate into the `filter_message` directory
```
cd filter_message/filter_message
```
Create user and password in filter_message app to get jwt token
```
python3 manage.py createsuperuser
```


#### .env file

For correct work you need to create .env file in ~/PROJECT_DIR/filter_message/filter_message/.env
with the following content:

```
nano .env 
```

```
# example
# your django_secret_key
SECRET_KEY="django-insecure-8)+2eujbv7(i0if^h%mmjtxzwz8l1br2^sgcx&w0x*@@uy5@nx"

DEBUG=True
ALLOWED_HOSTS=

# message server
HOST_SERVER=http://127.0.0.1:8000/

# need to create user and password
# in filter_message app
# to get jwt
LOGIN=alexander
PASSWORD=1

```

#### Dependencies

Install, using `pip`:

```
pip install -r requirements.txt
```


#### Usage
```
python3 manage.py makemigrations
python3 manage.py migrate
chmod +x start.sh
./start.sh
```

### Build Using Docker

#### Git

Clone the repository
```
git clone https://github.com/Alexander671/filter_message/
```

Navigate into the `filter_message` directory
```
cd filter_message/filter_message
```

Create user and password in filter_message app to get jwt token
```
python3 manage.py createsuperuser
```


#### .env file

For correct work you need to create .env file in ~/PROJECT_DIR/filter_message/filter_message/.env
with the following content:

```
nano .env 
```

```
# example
# your django_secret_key
SECRET_KEY="django-insecure-8)+2eujbv7(i0if^h%mmjtxzwz8l1br2^sgcx&w0x*@@uy5@nx"

DEBUG=True
ALLOWED_HOSTS=

# message server
HOST_SERVER=http://127.0.0.1:8000/

# need to create user and password
# in filter_message app
# to get jwt
LOGIN=alexander
PASSWORD=1

```

#### Usage

1. Build the image

`docker build .`

2. Сompiling the image with the team

`docker-compose build`

3. Run container:

`docker-compose up -d`

## Some examples and test <a name="test"></a>

Some edge-cases examples are available on the [test_postman](https://github.com/Alexander671/filter_message/tree/main/test_postman)

## Authors

* **Alexander Matveev** - *Initial work* - [Alexander671](https://github.com/Alexander671)

