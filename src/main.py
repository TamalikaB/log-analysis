import re
invalid_count = 0
status_counts = {}
category_counts = {}
client_counts = {}
error_client_counts = {}
client_4xx_counts = {}
def parse_log_line(line):
    match = re.search(
        r'^(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+|-)', 
        line)
    if not match:
        return None
    return {
        "client" : match.group(1),
        "timestamp": match.group(2),
        "request": match.group(3),
        "status" : match.group(4),
        "bytes_sent": match.group(5)
    }

with open("data/raw/nasa_aug95.log", "r", encoding="latin-1") as file:
    for line in file:   
        result = parse_log_line(line)
        if not result:
            invalid_count += 1
        else:
            status= result["status"]
            client = result["client"]
            client_counts[client] = client_counts.get(client, 0) + 1
            status_counts[status] = status_counts.get(status, 0) + 1
            category = status[0] + "xx"
            category_counts[category] = category_counts.get(category, 0) + 1
            # if status.startswith("4") or status.startswith("5"):
            #     client = result["client"]
            #     error_client_counts[client] = error_client_counts.get(client, 0) + 1
            if status.startswith("4"):
                client = result["client"]
                client_4xx_counts[client] = client_4xx_counts.get(client, 0) + 1

print(category_counts)
total=sum(status_counts.values())
print(f"Parsed successfully: {total:,} lines")
print(f"Skipped corrupt lines: {invalid_count}")
for status, count in sorted(status_counts.items(), key=lambda item: item[1], reverse=True):
    percentage = (count / total) * 100
    print(status, ":", count, f"({percentage:.2f}%)")

# print("\nTop 10 clients generating errors:")

# for client, count in sorted(
#     error_client_counts.items(),
#     key=lambda item: item[1],
#     reverse=True
#     )[:10]:
#     print(client, ":", count)

print("\nTop 10 clients generating 4xx errors:")

for client, count in sorted(
    client_4xx_counts.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]:
    print(client, ":", count)


# one client 4xx error check
client = "dialip-217.den.mmc.com"

total_requests = client_counts.get(client, 0)
errors = client_4xx_counts.get(client, 0)

error_rate = (errors / total_requests) * 100

print("\nClient analysis:")
print("Client:", client)
print("Total requests:", total_requests)
print("4xx errors:", errors)
print(f"4xx error rate: {error_rate:.2f}%")