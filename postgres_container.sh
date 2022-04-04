docker run -p 5432:5432 -d \
-e POSTGRES_PASSWORD=S3cret \
-e POSTGRES_USER=postgres \
-e POSTGRES_DB=gpa_app \
-v pgdata:/var/lib/postgresql/data \
postgres