import os

import random

# folder path
dir_path = r'E:\\datasets\\DMR-IR_dataset\\HEALTHY\\'
pre = 'E:\\datasets\\DMR-IR_dataset\\HEALTHY\\'
post = '\\Matrizes'

sickdir = r'E:\\datasets\\DMR-IR_dataset\\SICK'
sickpre = 'E:\\datasets\\DMR-IR_dataset\\SICK\\'
sickpost = '\\Matrizes'

# list to store files
healthy_file_list = []
sick_file_list = []
healthy_patient_list = []

# Iterate directory
for path in os.listdir(dir_path):
    healthy_patient_list.append(path)
    healthy_file_list.append(pre + path + post)
print(healthy_file_list)

sick_patient_list = []
for path in os.listdir(sickdir):
    sick_patient_list.append(path)
    sick_file_list.append(sickpre + path + sickpost)
print(sick_file_list)

dataset_name = 'dmr_ir'

rows = []
healthy_example = []

i = 0
for name in healthy_file_list:
    healthy_example.append(healthy_patient_list[i])
    healthy_example.append(name)
    healthy_example.append(0)
    rows.append(healthy_example)
    healthy_example = []
    i += 1

i = 0
sick_example = []
for name in sick_file_list:
    sick_example.append(sick_patient_list[i])
    sick_example.append(name)
    sick_example.append(1)
    rows.append(sick_example)
    sick_example = []
    i += 1

print(healthy_example)
print(sick_example)

rows.append(healthy_example)
rows.append(sick_example)

random.shuffle(rows)
print(rows)
print(len(rows))

dmr_ir = []


# split data matrix file
def generate_instance(rows):
    temp = []
    for row in rows:
        if len(row) != 0:
            for path1 in os.listdir(row[1]):
                print(path1)
                temp.append(row[0])
                temp.append(row[1] + "\\" + path1)
                temp.append(row[2])
                dmr_ir.append(temp)
                temp = []
    pass


# pass data as a list
def toDataFrame(data):
    pid = []
    timg = []
    label = []
    for item in data:
        pid.append(item[0])
        timg.append(item[1])
        label.append(item[2])
    return pid, timg, label


pid, timg, label = toDataFrame(data)
df = pd.DataFrame([pid, timg, label]).transpose()
df.columns = ['pid', 'timg', 'label']

write_list(df, 'dmr_ir_dataset')

generate_instance(rows)
print(dmr_ir)
print(len(dmr_ir))
# writing to csv file
# with open(dataset_name, 'w') as csvfile:
# creating a csv writer object
#   csvwriter = csv.writer(csvfile)

# writing the data rows
# csvwriter.writerows(rows)
