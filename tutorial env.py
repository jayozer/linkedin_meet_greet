import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(os.getenv("MYSECRET_KEY"))
print(os.getenv("COMBINED"))
print(os.getenv("MAIL"))


load_dotenv(OVERRIDE=True)
MY_KEY = "Mykey"  # This will override the load_dotenv() value

# load all as a dictionary
config = dotenv_values(".env")
print(config)

# Access individual keys
print(config["MYSECRET_KEY"])

