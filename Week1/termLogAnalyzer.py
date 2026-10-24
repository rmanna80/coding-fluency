




# total_event = 0
# successful_logins = 0
# failed_logins = 0

# logs = [
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED",
#     "LOGIN_FAILED",
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED",
#     "LOGIN_FAILED"
# ]

# for i in logs:
#     if i == "LOGIN_SUCCESS":
#         successful_logins += 1
#     elif i == "LOGIN_FAILED":
#         failed_logins += 1
#     total_event += 1

# print(f"total events: {total_event}", " | Successful Logins: {successful_logins}", " | Failed logins: {failed_logins}",)


def count_file():
        
    total_event = 0
    successful_logins = 0
    failed_logins = 0

    with open("server.log", "r") as file:
        content = file.read()
        print(content)
    for i in content:
        clean_line = i.strip()

        if clean_line == "LOGIN_SUCCESS":
            successful_logins += 1
        elif clean_line == "LOGIN_FAILED":
            failed_logins += 1
        total_event += 1
    
    return f"total events: {total_event} | Successful Logins: {successful_logins} | Failed logins: {failed_logins}"
# print(file())


def dictLog():
    failed_by_ip = {}
    count = 0
    events = []
    suc = "LOGIN_SUCCESS"
    fail = "LOGIN_FAIL"
    with open('server.log', 'r') as file:
        for line in file:
            parts = line.strip().split(",")
            events.append(parts)
            print("this is events", events)
            if parts[1] == suc or parts[1] == fail:
                count+=1
            if events:
                ip = parts[0]
                failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1
        for key, value in failed_by_ip.items():
            print(f"IP: {key} | Count: {value}")
dictLog()
        

def file():
    events = []
    with open("server.log", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            events.append(parts)
    return events
             

print("==================================        ===========================")
def failed_login(logs):
    
    ip_log = {}
    normal = "192.168.1.10"
    for i in logs:
        ip = i[0]
        event = i[1]

        if event == "LOGIN_FAILED":
            ip_log[ip] = ip_log.get(ip, 0) + 1
    for ip, count in ip_log.items():
        if ip == normal:
            status = "NORMAL"
        else:
            status = "ALERT"
        print(f"IP: {ip:<16} | Count: {count} | Status: {status}")
        
logs = file()
failed_login(logs)