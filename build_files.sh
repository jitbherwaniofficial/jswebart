echo "BUILD START"

# Use python3 to ensure correct installation
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"




# echo " BUILD START"
# pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
# echo " BUILD END" 

