# a postgresql script to create a new database for a project
# Usage: ./start_project_db.sh <project_name> <db_user> <db_password>
# Example: ./start_project_db.sh my_project my_user my_password

# Check if the user has provided the project name, db user and db password
if [ $# -ne 3 ]; then
    echo "Usage: ./start_project_db.sh <project_name> <db_user> <db_password>"
    exit 1
fi

# Assign the arguments to variables
project_name=$1
db_user=$2
db_password=$3

# Create a new database for the project
sudo -u postgres psql -c "CREATE DATABASE $project_name;"
sudo -u postgres psql -c "CREATE USER $db_user WITH PASSWORD '$db_password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $project_name TO $db_user;"
sudo -u postgres psql -c "ALTER USER $db_user CREATEDB;" # Allow the user to create databases

echo "Database $project_name has been created successfully."
echo "User $db_user has been created successfully."
echo "User $db_user has been granted all privileges on database $project_name."
echo "User $db_user has been granted the permission to create databases."

# to install the postgresql client on the server, run the following command
# sudo apt-get install postgresql-client

# to start the postgresql server, run the following command
# sudo service postgresql start # or sudo systemctl start postgresql

# to stop the postgresql server, run the following command
# sudo service postgresql stop

# to restart the postgresql server, run the following command
# sudo service postgresql restart

# to check the status of the postgresql server, run the following command
# sudo service postgresql status



# to connect to the database, run the following command
# psql -h localhost -U my_user -d my_project

# to list all databases, run the following command
# \l

# to list all tables in a database, run the following command   
# \dt

# to list all users, run the following command
# \du

# to exit the database, run the following command
# \q



# to create a new table, run the following command
# CREATE TABLE my_table (my_column1 VARCHAR(255), my_column2 VARCHAR(255));

# to create a new user, run the following command
# CREATE USER my_user WITH PASSWORD 'my_password';

# to grant all privileges on a database to a user, run the following command    
# GRANT ALL PRIVILEGES ON DATABASE my_project TO my_user; 

# to grant the permission to create databases to a user, run the following command
# ALTER USER my_user CREATEDB;

# to drop a database, run the following command
# sudo -u postgres psql -c "DROP DATABASE my_project;"

# to drop a user, run the following command
# sudo -u postgres psql -c "DROP USER my_user;"

# to drop a table, run the following command
# sudo -u postgres psql -c "DROP TABLE my_table;"

# to drop a column, run the following command
# sudo -u postgres psql -c "ALTER TABLE my_table DROP COLUMN my_column;"

# to add a column, run the following command
# sudo -u postgres psql -c "ALTER TABLE my_table ADD COLUMN my_column VARCHAR(255);"

# to rename a column, run the following command
# sudo -u postgres psql -c "ALTER TABLE my_table RENAME COLUMN my_column TO my_new_column;"

# to rename a table, run the following command
# sudo -u postgres psql -c "ALTER TABLE my_table RENAME TO my_new_table;"



# to list all columns in a table, run the following command
# \d my_table

# to list all rows in a table, run the following command
# SELECT * FROM my_table;

# to insert a row into a table, run the following command
# INSERT INTO my_table (my_column1, my_column2) VALUES ('value1', 'value2');

# to update a row in a table, run the following command
# UPDATE my_table SET my_column1 = 'new_value1', my_column2 = 'new_value2' WHERE my_column1 = 'value1';

# to delete a row from a table, run the following command
# DELETE FROM my_table WHERE my_column1 = 'value1';

