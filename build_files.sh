# echo " BUILD START"
# pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
# echo " BUILD END"

#!/bin/bash
echo " BUILD START"
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo " BUILD END"