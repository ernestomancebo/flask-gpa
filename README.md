# flask-gpa

This is a sample GPA app built with Flask, Angular, and PostgreSQL; glued and spinned up via `docker-compose`.

## Serve this

To serve this app just type at the console:

``` bash
docker-compose build
docker-compose up -d
```

## Architecture

### Backend
The backend is built using Flask, a Python library that wraps several tools such as SQLAlchemy, Marshmallow, Click, etc. taking up the heavy lift and leting you focus on what's important to your app: the business logic. More of this at https://palletsprojects.com/.
This app is architected under the concept of clean architecture, a paradigm that is detailed at https://www.thedigitalcatbooks.com/pycabook-introduction/.

Features and implementations that you can find in this app are:
- CLI interface for environment/database set up. 
- JWT authentication.
- MD5 password encription.
- Swagger endpoint.
- Serialization/Deserialization with Marshmallow.
- Database modeling with SQLAlchemy.
- Built-in database migration.
- Flask blueprints for better business domains segmentation.
- Flask RESTful endpoints.
- Environment isolation with dotenv (testing, production, others).
- Production serving with Gunicorn.
- Soon: Unit testing with pytest (don't kill me).

### Frontend
The front is a basic Angular app. Some particularities of this app is that uses a JWT token to track the user session and permisions; also, uses https://tachyons.io/ for styling (why did I picked it? I just love it.)

### Database
The data is stored in a PostgreSQL database. Is the de facto database for python projects, offers what anyother db offers, and has several NoSQL features (HStore, just to mention one).

### Reverse Proxy
The system is wired via `docker-compose` as I mentioned earlier. Angular can't be serverd by itsel, so, an Nginx image is used to serve it; but wait, the communication with the backend might throw an CORS error. I could have added a middleware in both apps, but I put a reverse proxy when serving the Angular app and problem solved; ALSO, this masks the endpoint.
