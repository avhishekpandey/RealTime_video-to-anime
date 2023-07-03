@echo off

rem Check if the environment file exists
if not exist venv (

    rem Create the environment
    python -m venv venv

)

rem Activate the environment
call venv\Scripts\activate

rem Check if the app.py file exists
if not exist app.py (

    echo "No app.py file found."
    exit /b

)

rem Launch the app.py file
python app.py

rem Deactivate the environment
call venv\Scripts\deactivate