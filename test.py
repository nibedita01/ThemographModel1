import os
import csv

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
    healthy_file_list.append(pre+path+post)
print(healthy_file_list)

sick_patient_list = []
for path in os.listdir(sickdir):
    sick_patient_list.append(path)
    sick_file_list.append(sickpre+path+sickpost)
print(sick_file_list)

dataset_name = 'dmr_ir'

rows = []
healthy_example = []

i = 0
for name in healthy_file_list:
    healthy_example.append(healthy_patient_list[i])
    healthy_example.append(healthy_file_list[i])
    healthy_example.append(0)
    healthy_example.append('\n')
    i += 1

i = 0
sick_example = []
for name in sick_file_list:
    sick_example.append(sick_patient_list[i])
    sick_example.append(sick_file_list[i])
    sick_example.append(1)
    sick_example.append('\n')
    i += 1

print(healthy_example)
print(sick_example)

rows.append(healthy_example)
rows.append(sick_example)

print(rows)

# writing to csv file
with open(dataset_name, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the data rows
    csvwriter.writerows(rows)
