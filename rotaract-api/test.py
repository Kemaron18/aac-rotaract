import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv('user'), os.getenv('password'), os.getenv('host'), os.getenv('port'), os.getenv('dbname'))
pipenv