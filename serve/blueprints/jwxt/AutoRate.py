from bs4 import BeautifulSoup as bs4
from app import app
from Response import Success, Error

session = app.config["SESSION"]
