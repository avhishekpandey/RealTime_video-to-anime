#!/bin/sh

# Check if the environment file exists
if [ ! -f venv ]; then

    # Create the environment
    python3 -m venv venv

fi

# Activate the environment
source venv/bin/activate

# Check if the app.py file exists
if [ ! -f app.py ]; then

    echo "No app.py file found."
    exit 1

fi

# Launch the app.py file
python app.py

