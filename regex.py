import re

patterns = {
    "email": re.compile(r"\S+@\S+"),
    "api_key": re.compile(r"sk-\w+"),
    "password": re.compile(r"password\s*=\s*\S+")
}