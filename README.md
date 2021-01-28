### Project structure

```
── mateo
   ├── api
   │   └── v1
   │       ├── <endpoint>
   │       │   ├── endpoints.py
   │       │   └── utils.py
   │       . 
   │       .
   │       .
   ├── models
   ├── schemas
   ├── migrations
   ├── config.py
   └── app.py
── requirements.txt
```

- `api`: The core logic. All endpoints will be implemented here. Endpoints are organized by API version (e.g. `v1`). 
  Each endpoint (and it's "sub-endpoints" for CRUD) has it's own folder containing two files:
    - `endpoints.py`: Actual endpoint definitions, high-level implementation, and registering. 
    - `utils.py`: Helper functions used by the endpoints. Lower-level logic goes here.
- `models`: Database table definitions. Each table is represented by a single file. 
- `schemas`: Serializers for database objects defined in `models`. Each serializer is represented by a single file.
- `migrations`: Used by `flask-migrate` to generate migration scripts. Leave untouched.
- `config.py`: Stores application configuration variables. 
- `app.py`: Flask application initialization.

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
