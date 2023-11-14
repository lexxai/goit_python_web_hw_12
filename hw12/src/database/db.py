from pathlib import Path
from fastapi import HTTPException, status
from dotenv import load_dotenv

from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

domain = environ.get("POSTGRES_HOST")
if not domain:
    ENV_FILE = Path(__file__).resolve().parent.parent.parent.parent.joinpath(".env")
    load_dotenv(ENV_FILE)
    domain = environ.get("POSTGRES_HOST")
    # print(f"{ENV_FILE=} {domain=}")

username = environ.get("POSTGRES_USERNAME")
password = environ.get("POSTGRES_PASSWORD")
domain = environ.get("POSTGRES_HOST")
port = environ.get("POSTGRES_PORT")
database = environ.get("POSTGRES_DATABASE")

URI = None
if domain:
    URI = f"postgresql+psycopg2://{username}:{password}@{domain}:{port}/{database}"

SQLALCHEMY_DATABASE_URL = URI

# print(f"{SQLALCHEMY_DATABASE_URL=}")

assert SQLALCHEMY_DATABASE_URL is not None, "SQLALCHEMY_DATABASE_URL UNDEFINED"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = DBSession()
    try:
        yield db
    except SQLAlchemyError as err:
        print(err)
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    finally:
        db.close()


if __name__ == "__main__":
    print(engine)