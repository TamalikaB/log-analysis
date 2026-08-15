import re
count =0
def parse_log_line(line):
    match = re.search(
        r'^(.*?) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+|-)', 
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

with open("data/raw/nasa_aug95.log", "r") as file:
    for line in file:   
        result = parse_log_line(line)
        count += 1
        if count<= 5:
            print(result)
        else:
            break
