

import random
import time 
from datetime import datetime

sample_events = [
    "192.168.1.10,LOGIN_SUCCESS,alice",
    "10.0.0.5,LOGIN_FAILED,bob",
    "172.16.0.8,LOGIN_SUCCESS,charlie",
    "10.0.0.5,LOGIN_FAILED,admin",
    "10.0.0.5,LOGIN_FAILED,bob"
]

# for event in sample_events:
#     parts = event.strip().split(",")

#     ip = parts[0]
#     status = parts[1]
#     name = parts[2]

#     print(ip, status, name)

failed_by_ip = {}

print("=======REAL TIME LOG ANALYZER ===========")
print("press Ctrl+C to stop\n")

try:
    while True:
        event = random.choice(sample_events)

        parts = event.strip().split(",")

        ip = parts[0]
        status = parts[1]
        name = parts[2]

        current_time = datetime.now().strftime("%Y-%m-d &H:&M:%S")

        print(
            f"[{current_time}]"
            f"IP: {ip:<16}"
            f"User: {name:<10}"
            f"Status: {status}"
        )       

        if status == "LOGIN_FAILED":
            failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1
            if failed_by_ip[ip] == 5:
                print(
                    f"WARNING {ip} has reached "
                    f"5 failed login attempts!"
                )

        print("Failed logins: ", failed_by_ip)
        print("-"*70)
        time.sleep(2)
except KeyboardInterrupt:
    print("\nLog ananlyzer stopped")
    print("Final failed login counts: ", failed_by_ip)