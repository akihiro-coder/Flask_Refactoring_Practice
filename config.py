import os

from dotenv import load_dotenv


load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "data.sqlite")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")