import re

def converse_to_float(value):
    try:
        return float(value)
    except ValueError:
        return float(re.sub(r'[^\d.]+', '', value))