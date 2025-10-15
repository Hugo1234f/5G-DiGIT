unique_campaigns = []

gaming_campaigns = []
speedtest_campaigns = []
other_campaigns = []

headers = ""

def map_campaigns(parts):
    parts = [x.replace('campaign_17_OW_5G_speedtest', '0') for x in parts]
    parts = [x.replace('campaign_27_OW_5G_speedtest', '1') for x in parts]
    parts = [x.replace('campaign_21_OW_5G_speedtest', '2') for x in parts]
    parts = [x.replace('campaign_7_OW_5G_speedtest', '3') for x in parts]
    parts = [x.replace('campaign_5_OW_5G_speedtest', '4') for x in parts]
    parts = [x.replace('campaign_22_OW_5G_speedtest', '5') for x in parts]
    parts = [x.replace('campaign_40_OW_5G_speedtest', '6') for x in parts]
    parts = [x.replace('campaign_23_OW_5G_speedtest', '7') for x in parts]
    parts = [x.replace('campaign_39_OW_5G_speedtest', '8') for x in parts]

    parts = [x.replace('campaign_6_OW_5G_gaming', '9') for x in parts]
    parts = [x.replace('campaign_28_OW_5G_gaming', '10') for x in parts]
    parts = [x.replace('campaign_20_OW_5G_gaming', '11') for x in parts]
    parts = [x.replace('campaign_5_OW_5G_gaming', '12') for x in parts]
    parts = [x.replace('campaign_13_OW_5G_gaming', '13') for x in parts]
    parts = [x.replace('campaign_24_OW_5G_gaming', '14') for x in parts]
    parts = [x.replace('campaign_31_OW_5G_gaming', '15') for x in parts]
    parts = [x.replace('campaign_25_OW_5G_gaming', '16') for x in parts]
    parts = [x.replace('campaign_19_OW_5G_gaming', '17') for x in parts]

    parts = [x.replace('campaign_1_OW_5G', '18') for x in parts]
    parts = [x.replace('campaign_2_OW_5G', '19') for x in parts]
    parts = [x.replace('campaign_17_OW_5G', '20') for x in parts]
    parts = [x.replace('campaign_18_OW_5G', '21') for x in parts]
    parts = [x.replace('campaign_19_OW_5G', '22') for x in parts]
    parts = [x.replace('campaign_21_OW_5G', '23') for x in parts]
    parts = [x.replace('campaign_22_OW_5G', '24') for x in parts]
    parts = [x.replace('campaign_23_OW_5G', '25') for x in parts]
    parts = [x.replace('campaign_24_OW_5G', '26') for x in parts]
    parts = [x.replace('campaign_25_OW_5G', '27') for x in parts]
    parts = [x.replace('campaign_35_OW_5G', '28') for x in parts]
    parts = [x.replace('campaign_36_OW_5G', '29') for x in parts]
    parts = [x.replace('campaign_37_OW_5G', '30') for x in parts]
    parts = [x.replace('campaign_38_OW_5G', '31') for x in parts]
    parts = [x.replace('campaign_39_OW_5G', '32') for x in parts]
    parts = [x.replace('campaign_40_OW_5G', '33') for x in parts]
    parts = [x.replace('campaign_41_OW_5G', '34') for x in parts]
    parts = [x.replace('campaign_42_OW_5G', '35') for x in parts]
    parts = [x.replace('campaign_43_OW_5G', '36') for x in parts]
    parts = [x.replace('campaign_46_OW_5G', '37') for x in parts]
    parts = [x.replace('campaign_57_OW_5G', '38') for x in parts]
    parts = [x.replace('campaign_58_OW_5G', '39') for x in parts]
    parts = [x.replace('campaign_67_OW_5G', '40') for x in parts]
    parts = [x.replace('campaign_90_OW_5G', '41') for x in parts]
    parts = [x.replace('campaign_91_OW_5G', '42') for x in parts]
    parts = [x.replace('campaign_92_OW_5G', '43') for x in parts]
    parts = [x.replace('campaign_93_OW_5G', '44') for x in parts]
    parts = [x.replace('campaign_94_OW_5G', '45') for x in parts]
    parts = [x.replace('campaign_101_OW_5G', '46') for x in parts]
    
    return parts

with open('data/5G - Passive Measurements.csv', 'r') as file:
    headers = file.readline().split(',')
    headers[0] = "id"
    headers[-1] = headers[-1][:-2] + '\n'

    headers = [x.strip('"') for x in headers]

    headers.remove('scenario')
    headers.remove('distance_w')
    headers.remove('id')
    headers.remove('Time')

    #i = 0
    for line in file:
        #if i > 10:
        #i += 1

        campaign = line.split(',')[-1][:-1]

        if "OW" not in campaign:
            continue

        #Clean the data
        parts = line.split(',')
        
            #Strip quotes
        parts = [x.strip('"') for x in parts]
        parts = [x.strip('"') for x in parts]
            #Convert country location
        parts = [x.replace('Op""[2]', '2') for x in parts]
        parts = [x.replace('Op""[1]', '1') for x in parts]
            #Strip scenario
        parts.remove('OW')
            #Strip w_distance
        del parts[-2]
            #Strip quote of scenario
        parts[-1] = parts[-1][:-2] + '\n'
            #Strip ID
        del parts[0]
            #Strip Time
        del parts[1]
            #Campaign mappings
        parts = map_campaigns(parts)
        

        #Sort by campaign
        if campaign not in unique_campaigns:
            unique_campaigns.append(campaign)
        if 'gaming' in campaign:
            gaming_campaigns.append(','.join(parts))
        elif 'speedtest' in campaign:
            speedtest_campaigns.append(','.join(parts))
        else:
            other_campaigns.append(','.join(parts))



print(f"Found {len(gaming_campaigns)} gaming campaigns...")

with open('data/gaming_campaigns.csv', 'w') as file:
    file.write(','.join(headers))
    for line in gaming_campaigns:
        file.write(line)

print(f"Found {len(speedtest_campaigns)} speedtest campaigns...")

with open('data/speedtest_campaigns.csv', 'w') as file:
    file.write(','.join(headers))
    for line in speedtest_campaigns:
        file.write(line)

print(f"Found {len(other_campaigns)} other campaigns...")

with open('data/other_campaigns.csv', 'w') as file:
    file.write(','.join(headers))
    for line in other_campaigns:
        file.write(line)

print(f"Found {len(unique_campaigns)} unique campaigns...")

with open('data/unique_campaigns.txt', 'w') as file:
    for line in unique_campaigns:
        file.write(line + '\n')