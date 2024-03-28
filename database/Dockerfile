# Use the official PostgreSQL Docker image
FROM postgres:14.1

# Set environment variables
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydb

# Copy any additional files or scripts needed
COPY schema.sql /docker-entrypoint-initdb.d/1.sql
COPY moakup.sql /docker-entrypoint-initdb.d/2.sql

# Expose the PostgreSQL port
EXPOSE 5432

# Start the PostgreSQL server
CMD ["postgres"]

# docker build -t my-postgres-image .
# docker run --name my-postgres-container -p 5432:5432 -d my-postgres-image

# docker run --rm -p 5432:5432 $(docker build -q .)