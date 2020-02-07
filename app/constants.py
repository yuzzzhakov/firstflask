import json
import os


data = {'secret_key': 'secret_value'}
json_data = json.dumps(data)

TBOT_TOKEN = os.environ["YUZTESTBOT_TOKEN"]