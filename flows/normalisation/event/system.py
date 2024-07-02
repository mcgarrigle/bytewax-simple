import re

def recognise(s):
    t = s.split(' ')
    return t[2] == "system"

def normalise(event):
    pattern = r'(.{19}) (\w+) (\w+) (.+)'
    match = re.match(pattern, event)
    if match:
        timestamp, hostname, process, message = match.groups()
        event = { "timestamp": timestamp, "_type": "syslog.system", "hostname": hostname, "process": process, "message": message }
        return event
    else:
        return None
