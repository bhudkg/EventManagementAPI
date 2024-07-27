echo "---migrations"
python3 manage.py makemigrations
echo "---migrate"
python3 manage.py migrate
echo "---runsever"
python3 manage.py runserver
    