import re
with open("data/raw/nasa_aug95.log", "r") as file:
    # for line in file:   
    first_line = file.readline()
    def parse_log_line(line):
        parts = line.split()
        client = parts[0]
        match = re.search(
            r'^(.*?) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+|-)', 
            first_line)
        if not match:
            return None
        return {
            "client" : match.group(1),
            "timestamp": match.group(2),
            "request": match.group(3),
            "status" : match.group(4),
            "bytes_sent": match.group(5)
        }
result = parse_log_line(first_line)
print(result)
