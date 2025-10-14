unique_campaigns = []

gaming_campaigns = []
speedtest_campaigns = []
other_campaigns = []

headers = ""

with open('./5G - Passive Measurements.csv', 'r') as file:
    headers = file.readline()
    print(headers)
    i = 0
    for line in file:
        campaign = line.split(',')[-1][:-1]

        if "OW" not in campaign:
            continue

        if campaign not in unique_campaigns:
            unique_campaigns.append(campaign)
        if 'gaming' in campaign:
            gaming_campaigns.append(line)
        elif 'speedtest' in campaign:
            speedtest_campaigns.append(line)
        else:
            other_campaigns.append(line)

print(f"Found {len(gaming_campaigns)} gaming campaigns...")

with open('./gaming_campaigns.csv', 'w') as file:
    file.write(headers)
    for line in gaming_campaigns:
        file.write(line)

print(f"Found {len(speedtest_campaigns)} speedtest campaigns...")

with open('./speedtest_campaigns.csv', 'w') as file:
    file.write(headers)
    for line in speedtest_campaigns:
        file.write(line)

print(f"Found {len(other_campaigns)} other campaigns...")

with open('./other_campaigns.csv', 'w') as file:
    file.write(headers)
    for line in other_campaigns:
        file.write(line)

print(f"Found {len(unique_campaigns)} unique campaigns...")

with open('./unique_campaigns.txt', 'w') as file:
    for line in unique_campaigns:
        file.write(line + '\n')