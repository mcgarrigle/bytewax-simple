import re
import json

def is_login(s):
    t = s.split(' ')
    return t[2] == "login"

def normalise_login(event):
    pattern = r'(.{19}) (\w+) (\w+) (.+)'
    match = re.match(pattern, event)
    if match:
        timestamp, hostname, process, message = match.groups()
        rec = { "timestamp": timestamp, "hostname": hostname, "process": process, "message": message }
        return json.dumps(rec)
    else:
        return None
