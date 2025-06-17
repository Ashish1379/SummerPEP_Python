from collections import defaultdict , deque 
from typing import List,Dict

recent_log = deque(maxlen = 5)
user_info = defaultdict(list)
log_level_count = defaultdict(int)

logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]


def add_log(line: str) -> None:
    line1  = line.split(' ',3)
    timestamp = line1[0][1:len(line1[0])-1]
    level = line1[1]
    user = line1[2][:len(line1[2])-1]
    message = line1[3]

    log = {
        'timestamp' : timestamp,
        'level'     : level,
        'user'      : user,
        'message'   :message.lower()
    }
    recent_log.append(line)
    user_info[user].append(log)
    log_level_count[level] += 1
    return

def get_user_logs(user_id: str) -> List[Dict]:
        return user_info.get(user_id, [])

def count_levels() -> Dict[str , int]:
    return dict(log_level_count)

def filter_logs(keyword: str) -> List[Dict]:
    keyword = keyword.lower()
    return [log for log in recent_log if keyword in log['message'].lower()]

def get_recent_logs() -> List[Dict]:
    return list(recent_log)


for line in logs:
    add_log(line)


# print("Recent Logs:")
# print(get_recent_logs())

# print("\nLogs for user1:")
# print(get_user_logs("user1"))

# print("\nLevel Counts:")
# print(count_levels())

# print("\nFilter Logs with keyword 'connect':")
# print(filter_logs("connect"))





