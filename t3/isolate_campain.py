unique_campaigns = []

gaming_campaigns = []
speedtest_campaigns = []
other_campaigns = []

headers = ""

with open('data/RawData', 'r') as file:
    headers = file.readline().split(',')
    headers[0] = "id"
    headers[-1] = headers[-1][:-2] + '\n'

    headers = [x.strip('"') for x in headers]

    headers.remove('scenario')
    headers.remove('distance_w')
    headers.remove('id')
    headers.remove('Time')
    headers.remove('Date')
    headers.remove('UTC')
    headers.remove('campaign\n')
    headers.remove('Latitude')
    headers.remove('Longitude')
    headers.remove('Altitude')
    headers.remove('Speed')
    headers.remove('EARFCN')
    headers.remove('Band')
    headers.remove('PCI')
    headers.remove('MNC')
    headers.remove('SSBIdx')
    headers.remove('SSS-SINR')
    headers.remove('DM_RS-SINR')
    headers.remove('PBCH-SINR')
    headers.remove('PSS-SINR')
    headers.remove('SS_PBCH-SINR')

    headers[-1] += '\n'

    #i = 0
    for line in file:
        #if i > 10:
        #i += 1

        campaign = line.split(',')[-1][:-1]

        if "OW" not in campaign:
            continue
        

            #Clean the data
        parts = line.split(',')
        
        if "NA" in parts or "NA\n" in parts:
            continue

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
        #del parts[-1]
        #parts[-1] += '\n'
            #Strip UTC
        del parts[0]
            #Strip Lat,Long,Alt,Spd,EARFCN
        del parts[0:6]
            #Strip Band & PCI
        del parts[1:3]
            #Strip MNC
        del parts[6]
            #Strip SSBIdx
        del parts[1:3]
        del parts[4]
        del parts[7]
        del parts[10]
        del parts[-4]

          #Sort by campaign
        if campaign not in unique_campaigns:
            unique_campaigns.append(campaign)
        del parts[-1]
        parts[-1] += '\n'
        gaming_campaigns.append(','.join(parts))



print(f"Found {len(gaming_campaigns)} campaigns...")

with open('data/scrubbed_campaigns.csv', 'w') as file:
    file.write(','.join(headers))
    for line in gaming_campaigns:
        file.write(line)
