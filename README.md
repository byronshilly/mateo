### Local deployment 

1. Create a PSQL database and user.
2. In the `/mateo` directory, create a file called `.env`. Populate it with the following:
   ```
   SQLALCHEMY_DATABASE_URI="postgresql://<username>:<password>@localhost:5432/<database_name>"
   ```
3. Run `flask run` in the same directory to launch the app on port 5000.  

### Creating tables

1. Create a file for the table in the models directory, defining all of it's columns.
2. Create a file for the table in the schema directory, defining how to serialize its objects.
2. Run `flask db migrate -m "migration details"`. 
3. Run `flask db upgrade`.
