from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Create an engine to connect to the PostgreSQL database
engine = create_engine('postgresql://myuser:mypassword@localhost:5432/mydb')

# Create a session factory
Session = sessionmaker(bind=engine)
