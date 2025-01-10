# Bash Script to setup the project

#!/bin/bash

# Install pyenv
if pyenv versions | grep -q "3.12.0"; then
  echo "Python 3.12.0 is already installed."
else
  # Install Python version 3.12.0 using Pyenv
  pyenv install 3.12.0
fi


# Setup pyenv

pyenv global 3.12.0
pyenv local 3.12.0
pyenv shell 3.12.0

# Upgrade pip and install virtualenv
python -m pip install --upgrade pip
pip install virtualenv

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

echo "Environment setup complete and dependencies installed."