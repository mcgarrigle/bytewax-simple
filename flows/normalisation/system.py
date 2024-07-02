import re
import json

def recognise(s):
    t = s.split(' ')
    return t[2] == "system"

def normalise(event):
    pattern = r'(.{19}) (\w+) (\w+) (.+)'
    match = re.match(pattern, event)
    if match:
        timestamp, hostname, process, message = match.groups()
        rec = { "timestamp": timestamp, "hostname": hostname, "process": process, "message": message }
        return json.dumps(rec)
    else:
        return None
