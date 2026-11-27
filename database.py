from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# DATABASE_URL = "postgresql+psycopg://yogeshmandawat2004gmail.com@localhost:5432/job_management"

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

with engine.connect() as connection:
    print("Database:", connection.engine.url.database)
    print("Host:", connection.engine.url.host)
    print("Port:", connection.engine.url.port)
    print("URL:", connection.engine.url.render_as_string(hide_password=True))