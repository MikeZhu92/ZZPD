import os, csv, sys, pickle
import numpy as np

file_path = 'rawdata/USDT-BTC.csv'
with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)  # skip the headers
    next(reader, None)  # skip the headers
    title = next(reader)
    all_info = {item.strip()[1:-1]: [] for item in title}
    for line in reader:
        if len(line) == 7:
            for i in range(7):
                if i == 0:
                    all_info[title[i].strip()[1:-1]].append(line[i])
                else:
                    all_info[title[i].strip()[1:-1]].append(float(line[i]))
        else:
            print('Length error in ' + file_path)
# Save file
data_output = open('D:/all_info.pkl', 'wb')
pickle.dump(all_info, data_output, -1)
data_output.close()

# Directly use
# pkl_file = open('D:/all_info.pkl', 'rb')
# usd_btc_info = pickle.load(pkl_file)
# pkl_file.close()
# print(usd_btc_info.keys())

sys.exit()