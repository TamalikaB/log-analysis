with open("data/raw/nasa_aug95.log", "r") as file:
    # line_count = 0
#     for line in file:
#         line_count += 1
#         print(line)
# print(f"total line: {line_count}")
    # first_line = file.readline()
    # print(first_line)
    # print(first_line.split())
    # parts = first_line.split()
    # print(parts)
    # print(len(parts))
    # print(parts[0])
    # print(parts[8])
    # print(parts[9])
    count = 0
    for line in file:
        parts = line.split()
        # print([parts])
        if len(parts)>= 10:
            client = parts[0]
            status = parts[8]
            bytes_sent = parts[9]
            print(client, status, bytes_sent)
        count +=1
        if count == 5:
            break

