import re

subject_dict = {}
with open("subject.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split(":")
        if len(parts) == 2:
            subject_name = parts[0].strip()
            sessions = parts[1].split()
            total_sessions = 0
            for session in sessions:
                session = re.sub(r'\D', '', session)
                if session.isdigit():
                    total_sessions += int(session)
            subject_dict[subject_name] = total_sessions
print(subject_dict)
