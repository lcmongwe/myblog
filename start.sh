export SECRET_KEY=myblog
export DATABASE_URL='postgresql+psycopg2://lucy:4444@localhost/myblog'
# python3 manage.py db init
# python3 manage.py db migrate -m "initia Migration"
# python3 manage.py db upgrade

python3.8 manage.py server
# python3.8 manage.py shell