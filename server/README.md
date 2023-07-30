# FastAPI & SQLAlchemy Mysql REST API

# install requirements.txt
pip3 install -r requirements.txt

# run mysql server
1. mysql.server start 
2. connect: mysql -u root -p
3. enter default password
(make sure to change the password of the DATABASE_URL variable at config/db.py file ->
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';)

# create db
create a DB called postsdb: 
1. CREATE DATABASE postsdb;
2. USE postsdb

# run the server 
uvicorn main:app --host localhost --port 8000

# open fastapi swagger 
http://localhost:8000/docs#

Create Hp Data API
/api/create_hp_data

Add Post API
/api/create_post

