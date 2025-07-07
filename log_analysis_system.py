# Task 4: Log Analysis System
def analyze_log(file_path):
    ip_count = {}
    url_count = {}
    status_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 9:
                continue
            ip = parts[0]
            url = parts[6]
            status = parts[8]

            ip_count[ip] = ip_count.get(ip, 0) + 1
            url_count[url] = url_count.get(url, 0) + 1
            status_count[status] = status_count.get(status, 0) + 1

    print("Top IPs:", sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5])
    print("Top URLs:", sorted(url_count.items(), key=lambda x: x[1], reverse=True)[:5])
    print("Status Codes:", status_count)

if __name__ == "__main__":
    file_path = input("Enter path to log file: ")
    analyze_log(file_path)
