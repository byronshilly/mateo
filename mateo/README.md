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
   ├── auth.py
   ├── extensions.py
   └── app.py
```

- `api`: The core logic. All endpoints will be implemented here. Endpoints are organized by API version (e.g. `v1`). 
  Each endpoint (and it's "sub-endpoints" for CRUD) has it's own folder containing two files:
    - `endpoints.py`: Actual endpoint definitions, high-level implementation, and registering. 
    - `utils.py`: Helper functions used by the endpoints. Lower-level logic goes here.
- `models`: Database table definitions. Each table is represented by a single file. 
- `schemas`: Serializers for database objects defined in `models`. Each serializer is represented by a single file.
- `migrations`: Used by `flask-migrate` to generate migration scripts. Leave untouched.
- `config.py`: Stores application configuration variables. 
- `auth.py`: Endpoints used for the authentication scheme.
- `extensions.py`: Flask extension initialization.
- `app.py`: Flask application initialization.

### Authentication and Authorization

Mateo utilizes token-based authentication using JSON Web Tokens (JWT). The frontend will use auth endpoints to 
authenticate a user's credentials and receive tokens that can be used to make requests to protected endpoints 
on behalf of the user. There are two tokens involved in Mateo's authentication scheme: 

- Access token: The primary token used to authenticate users. Expires quickly. 
- Refresh token: A secondary token used to receive new access tokens, rather than using the user's credentials.

To login a user, a call to `POST /auth/login` with the following request body is required: 

```
{
    'username': <username>,
    'password': <password>
}
```

If the credentials are correct, a response will be returned that will set two `httpOnly` cookies in the browser: 

- `access_token`: Contains the token used to access protected endpoints. 
- `refresh_token`: Used to refresh the access token after it is expired. 

To protect against CSRF, CSRF tokens are also returned in the response body: 

```
{
    'access_csrf_token': <token>,
    'refresh_csrf_token': <token>
}
```

Any subsequent requests to protected endpoints require that the `access_token` cookie is present, and that the 
`access_csrf_token` value is passed in the `X-CSRF-Token` header.

To refresh an access token, a call to `POST /auth/refresh` is required with the `refresh_token` cookie present, 
and the `refresh_csrf_token` value passed via the `X-CSRF-Token` header. 

While cookies are automatically passed via the browser, it is the responsibility of the frontend application to 
save the CSRF tokens and pass them with subsequent requests accordingly: 

- The `access_csrf_token` should be stored in-memory, and never persisted somewhere that would enable CSRF attacks.
  Because of this, the token will be lost when the user restarts the browser, or when visiting the frontend on a different tab. 
  For these cases, the `refresh_csrf_token` can be used. 
- The `refresh_csrf_token` should be persisted somewhere, either in browser local storage, or in a cookie. Whenever 
  authentication with the access token fails, either because the token has expired or because `access_csrf_token` is
  not present (new tab, new browser instance), the persisted value of `refresh_csrf_token` should be passed with the
  request to receive a new `access_token` cookie and a new `access_csrf_token` value to be stored in-memory. If the 
  refresh token values cannot be found, the user must be loggined in again.

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
