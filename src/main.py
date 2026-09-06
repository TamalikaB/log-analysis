import re

invalid_count = 0
status_counts = {}
category_counts = {}
client_counts = {}
client_4xx_counts = {}
client_403_counts = {}
client_404_counts = {}
request_counts = {}
path_counts = {}
path_404_counts = {}
path_403_counts = {}
hour_counts = {}
hour_4xx_counts = {}

def parse_log_line(line):
    match = re.search(
        r'^(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+|-)', 
        line
    )

    if not match:
        return None

    return {
        "client": match.group(1),
        "timestamp": match.group(2),
        "request": match.group(3),
        "status": match.group(4),
        "bytes_sent": match.group(5)
    }


with open("data/raw/nasa_aug95.log", "r", encoding="latin-1") as file:
    for line in file:

        result = parse_log_line(line)

        if not result:
            invalid_count += 1

        else:
            status = result["status"]
            client = result["client"]
            request = result["request"]
            timestamp = result["timestamp"]

            client_counts[client] = client_counts.get(client, 0) + 1
            status_counts[status] = status_counts.get(status, 0) + 1

            hour = timestamp[12:14]
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

            request_counts[request] = request_counts.get(request,0) + 1

            parts = request.split()
            if len(parts) >= 2:
                path = parts[1]
                path_counts[path] = path_counts.get(path, 0) + 1

                if status == "404":
                    path_404_counts[path] = path_404_counts.get(path, 0) + 1
                if status == "403":
                    path_403_counts[path] = path_403_counts.get(path, 0) + 1

            category = status[0] + "xx"
            category_counts[category] = category_counts.get(category, 0) + 1

            if status.startswith("4"):
                client_4xx_counts[client] = client_4xx_counts.get(client, 0) + 1

            if status == "403":
                client_403_counts[client] = client_403_counts.get(client, 0) + 1

            if status == "404":
                client_404_counts[client] = client_404_counts.get(client, 0) + 1

            if status.startswith("4"):
                hour_4xx_counts[hour] = hour_4xx_counts.get(hour, 0) + 1

print(category_counts)

total = sum(status_counts.values())

print(f"Parsed successfully: {total:,} lines")
print(f"Skipped corrupt lines: {invalid_count}")

for status, count in sorted(
    status_counts.items(),
    key=lambda item: item[1],
    reverse=True
):
    percentage = (count / total) * 100
    print(status, ":", count, f"({percentage:.2f}%)")


client_error_rates = []

for client, errors in client_4xx_counts.items():
    total_requests = client_counts[client]

    if total_requests >= 20:
        error_rate = (errors / total_requests) * 100

        client_error_rates.append(
            (client, total_requests, errors, error_rate)
        )


print("\nTop 10 clients by 4xx error rate:")

for client, total_requests, errors, error_rate in sorted(
    client_error_rates,
    key=lambda item: item[3],
    reverse=True
)[:10]:

    print(
        client,
        "| Requests:", total_requests,
        "| 4xx:", errors,
        f"| Error rate: {error_rate:.2f}%"
    )


print("\nClients generating 403 responses:")

for client, count in sorted(
    client_403_counts.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]:
    print(client, ":", count)

if status == "404":
    client_404_counts[client] = client_404_counts.get(client, 0) + 1

print("\nTop 10 clients generating 404 responses:")

for client, count in sorted(
    client_404_counts.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]:
    print(client, ":", count)

print("\nTop 10 requested resources:")

for request, count in sorted(
    request_counts.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]:
    print(request, ":", count)

print("\nTop 10 requested paths:")

for path, count in sorted(
    path_counts.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]:
    print(path, ":", count)

print("\nTop 10 paths generating 404 responses:")

for path, count in sorted(
    path_404_counts.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]:
    print(path, ":", count)

print("\nTop 10 paths generating 403 responses:")

for path, count in sorted(
    path_403_counts.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]:
    print(path, ":", count)

print("\nRequests by hour:")

for hour, count in sorted(hour_counts.items()):
    print(hour, ":", count)

print("\n4xx errors by hour:")

for hour, count in sorted(hour_4xx_counts.items()):
    print(hour, ":", count)

print("\n4xx error rate by hour:")

for hour in sorted(hour_counts):
    total_requests = hour_counts[hour]
    errors = hour_4xx_counts.get(hour, 0)
    error_rate = (errors / total_requests) * 100

    print(
        hour,
        "| Requests:", total_requests,
        "| 4xx:", errors,
        f"| Error rate: {error_rate:.2f}%"
    )