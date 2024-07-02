import re

def recognise(s):
    t = s.split(' ')
    return t[2] == "login"

def normalise(event):
    pattern = r'(.{19}) (\w+) (\w+) (.+)'
    match = re.match(pattern, event)
    if match:
        timestamp, hostname, process, message = match.groups()
        event = { "timestamp": timestamp, "_type": "syslog.login", "hostname": hostname, "process": process, "message": message }
        return event
    else:
        return None
