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

### Authentication

Mateo requires two authentication mechanisms: 

- **User Authentication:** User login and session preservation. For this we use Flask-JWT. To log a user in, the frontend will 
  call the `/auth` endpoint. If the username/password combination is correct, the endpoint will return a JWT that the frontend will 
  store for all subsequent requests. This token allows the backend to know what user is making a particular request. This token
  also doubles as an authorization mechanism, ensuring that only users on our frontend can make requests to our backend.
  However, there are a few requests that need to come from our frontend without a user in place (e.g. user creation on sign up).
  For these cases, the mechanism described in the next bullet point is needed.
- **API Authorization (Not yet implmented):** Requests to our API should only be serviced if they are coming from our frontend 
  application, and should deny any requests from third-parties. This can be accomplished in one of two ways: 
    - Using a user authentication token (described in the first bullet point) with a preexisting user account owned by us.
    - Using flask-rebar to authenticate with a different key/token. 
  This is yet to be decided.
  

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
3. Import the model in the base `__init__.py` file.
4. Run `flask db migrate -m "migration details"`. 
5. Run `flask db upgrade`.
