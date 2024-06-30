import re
import json

def normalise_login(event):
    pattern = r'(.{19}) (\w+) (.+)'
    match = re.match(pattern, event)
    if match:
        timestamp, process, message = match.groups()
        rec = { "timestamp": timestamp, "process": process, "message": message }
        return json.dumps(rec)
    else:
        return None
