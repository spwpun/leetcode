import sys

records = {}
for line in sys.stdin:
    file_path, line_num = line.split(" ")
    file = file_path.split("\\")[-1]
    if len(file) > 16:
        file = file[-16:len(file)]
    rd = file + " " + line_num[:-1] # remove the '\n'
    if rd in records.keys():
        records[rd] += 1
    else:
        records.update({rd:1})
keys = list(records.keys())
last_8_keys = keys[-8:len(keys)]
for key in last_8_keys:
    print(key,records[key], sep=" ")