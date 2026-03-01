import re
from collections import Counter

log_file = "logs/failed_attempts.txt"

failed_count = 0
ip_addresses = []
usernames = []

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_count += 1

            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if ip_match:
                ip_addresses.append(ip_match.group())

            user_match = re.search(r'for (\w+)', line)
            if user_match:
                usernames.append(user_match.group(1))

ip_count = Counter(ip_addresses)

print("==== SSH Log Analysis Report ====")
print(f"Total Failed Attempts: {failed_count}")
print(f"Unique IP Addresses: {set(ip_addresses)}")
print(f"Targeted Usernames: {set(usernames)}")
print(f"Attempts Per IP: {ip_count}")
