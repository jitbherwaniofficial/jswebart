# echo " BUILD START"
# pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
# echo " BUILD END"

#!/bin/bash

echo "BUILD START"

# Upgrade pip and install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"
