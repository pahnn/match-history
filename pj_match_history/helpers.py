import re

def convert_to_snake_case(response):
    for key in response.keys():
        new_key = convert(key)
        if new_key != key:
            response[new_key] = response.pop(key)
        if isinstance(response[new_key], dict):
            convert_to_snake_case(response[new_key])

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()