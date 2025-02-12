<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-%2320232a.svg?logo=react&logoColor=%2361DAFB)](https://react.dev/)
[![Tailwind-CSS](https://img.shields.io/badge/Tailwind%20CSS-%2338B2AC.svg?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=fff)](https://www.mysql.com/)
[![OpenAI](https://img.shields.io/badge/AWS-%23FF9900.svg?logo=amazon-web-services&logoColor=white)](https://openai.com/)

</div>

# log-A-plant
The perfect learning and journalling platform for gardeners! This project was built to push environmentally friendly and sustainable practices to novice and veteran gardeners. We accomplished such learning platform because of our openAI integration, giving gardeners tailored answers to any sustainability question, and unique plant-based recipes to the very plants they've harvested!

- <a target="_blank" href="https://devpost.com/software/log-a-plant">SparkHacks Devpost</a>
- <a target="_blank" href="https://youtu.be/PCS7RNPUsiU?si=bgCWPWpDD9DA39-Z">Demo video</a>
- <a target="_blank" href="https://docs.google.com/presentation/d/1y6puVJ0gbNaMPv7t1iGAgy-hxGHG56sTiLH2ScbE0nY/edit?usp=sharing">Demo Presentation</a>

1. Clone the repository:
    ```sh
    git clone https://github.com/westconn24/garden-app
    cd garden-app
    ```
2. Ensure you have Python installed
   - While this step is dependent on your OS, you can check if it exists by typing: ```python3 --version``` or ```python --version```
   - If Python is not installed, you can view the installation at <a>https://www.python.org/downloads/</a>

3. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    While this step is not required, it is recomended for lower dependency conflicts.
    
4. Install the required packages:
    If you are not already in the backend directory, cd into the backend folder:
    ```sh
    backend
    ```
    
    When its ensured that you're within the backend directory, install the requirements.txt file using the following command: 
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application
After ensuring you have cloned the repo and have python installed, cd into the backend folder and download the required packages.

To run the Flask application, make sure you are still within the backend folder and execute the `app.py` script. This will start a local flask server where you can interact with the RDS database and AI integration.

```sh
python app.py
```

After doing so, you can open another terminal. If you are still within the backend folder run cd ..

Make sure if you have not done so to run the npm install command

```sh
npm install
```

After doing so you may run npm start to start the local web application

```sh
npm start
```



## Endpoints

- `/` - Main menu



## .env dependency

Our program uses a group of API's that are dependent on private keys.

We rely on private keys that are gathered and inputted into the .env file within the backend directory.
The .env file structure is as follows :

ALLOWED_ORIGINS=""

SECRET_KEY=""
OPENAI_API_KEY=""

DEVELOPMENT=""

PORT=""

DB_HOST=""
DB_USER=""
DB_PASS=""
DB_SCHEMA=""

AWS_KEY=""
AWS_SECRET=""
AWS_REGION=""

UNSPLASH_ACCESS=""
UNSPLASH_KEY=""

SPOONACULAR_ACCESS=""

You must develop the cooresponding API keys for OpenAI, AWS RDS and SPOONIFY

