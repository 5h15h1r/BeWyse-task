# Auth-API
REST API for user authentication


## Assignment

Creating the project

1. Run your code with Python (3.9) and Django (3.2).
2. Setup a local mongodb database for storing the data.
3. Use Firebase to authorise (create and verify custom token) the User using Middleware 





## Installation and Usage

## Local setup

1) Clone the project

```bash
  git clone https://github.com/5h15h1r/BeWyse-task
```

2) Go to the project directory

```bash
  cd BeWyse-task
```
3) Create a Virtual Environment (Optional/Preferred)

```bash
  python3 -m venv /path/to/new/virtual/environment
```
4) Install dependencies

```bash
  pip install -r requirements.txt
```

5) Get the service account JSON file from your firebase project console and store it. Rename it with the "creds.json"

6) Start a mongodb instance using docker 
```bash 
  docker run -d -p 27017:27017 --name=mongo mongo:latest
```
7) Change the name of your database in settings.py 

8) Apply the migrations and run the server
```bash 
  python3 manage.py runserver
```

<p align="right">(<a href="#top">back to top</a>)</p>



[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
