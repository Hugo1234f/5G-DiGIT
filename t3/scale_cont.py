from sklearn.preprocessing import StandardScaler

headers = []

data = {}

print("Reading data...")
with open('./data/scrubbed_campaigns.csv', 'r') as file:
    headers = file.readline().split(',')
    headers[-1] = headers[-1][:-1]

    for h in headers:
        data[h] = []

    for line in file:
        parts = line.split(',')
        if len(parts) < len(headers):
            continue
        
        parts[-1] = parts[-1][:-1]

        for i in range(len(headers)):
            data[headers[i]].append(float(parts[i]))


print("Mapping frequencies...")
df = []
for col in data:
    if col == "Frequency":
        for j in range(len(data['Frequency'])):
            if str(data['Frequency'][j])[1] == '6':
                data['Frequency'][j] = 0
            else:
                data['Frequency'][j] = 1
    else:
        df.append(data[col])

print('Scaling...')
scaler = StandardScaler()
scaled = scaler.fit_transform(df)
scaled = scaled.T

print('Writing...')

training_data = []

with open('./data/scaled.csv', 'w') as file:
    file.write(','.join(headers) + '\n')
    n = 0
    for i in range(len(data['SSS-RSRP'])):
        s = str(data['Frequency'][i]) + ','
        s += ','.join(map(str, scaled[i].tolist())) + '\n'
        file.write(s)
        n += 1
        if n % 10 == 0:
            training_data.append([str(data['Frequency'][i])] + list(map(str, scaled[i].tolist())))
    #for i in range(len(data['SSS-RSRP'])):
        
        #file.write(s)
with open('./data/training_data.csv', 'w') as file:
    file.write(','.join(headers) + '\n')
    for i in training_data:
        file.write(','.join(i) + '\n')
        