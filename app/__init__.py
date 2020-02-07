from flask import Flask
from .config import Configuration
import logging

app = Flask(__name__)
app.config.from_object(Configuration)

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
)

from .api_resources import *
