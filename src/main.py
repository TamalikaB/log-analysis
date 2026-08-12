import re
with open("data/raw/nasa_aug95.log", "r") as file:
    # status_counts = {}
    # count = 0
    # for line in file:
    #     parts = line.split()
    #     if len(parts)>= 10:
    #         client = parts[0]
    #         status = parts[8]
    #         bytes_sent = parts[9]
    #     #     print(client, status, bytes_sent)
    #         status = status.strip(".,!?:;\"'")

    #         if status.isdigit():
    #             status_counts[status] = status_counts.get(status,0) + 1
    #         else:
    #             if count < 6:
    #                 print(line)
    #                 count +=1
    # print(status_counts)
    first_line = file.readline()
Timestamp = re.search(r"\[(.*?)\]", first_line)
Request = re.search(r'"(.*?)"', first_line)
print(Timestamp.group(1))
print(Request.group(1))
      

