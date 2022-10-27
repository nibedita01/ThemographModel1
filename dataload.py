# Import Module
import pandas as pd
import os
import random
import gc

from pickle_use import write_list

# Folder Path
path = r"E:\research\nibedita\data\thermo_graphy_data\DMR-IR_dataset\HEALTHY"


# Change the directory
# os.chdir(path)

# my_arr = np.empty((2, 2), dtype=float)

def matrix_injector(path):
    df = pd.read_csv(path, sep='\s+', header=None)
    mat1 = df.to_numpy()
    #print(mat1)

    print(mat1.shape)
    #print(type(mat1))
    gc.collect()
    return mat1


# folder path
dir_path = r"E:\\research\\nibedita\\data\\thermo_graphy_data\\DMR-IR_dataset\\HEALTHY\\"
pre = dir_path
post = r'\\Matrizes'

sickdir = r"E:\\research\\nibedita\\data\\thermo_graphy_data\\DMR-IR_dataset\\SICK\\"
sickpre = sickdir
sickpost = r'\\Matrizes'

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

#print(healthy_example)
#print(sick_example)

rows.append(healthy_example)
rows.append(sick_example)

# random.shuffle(rows)
print(rows)
#print(len(rows))

dmr_ir = []


# split data matrix file
def generate_instance(rows):
    temp = []
    for row in rows:
        if len(row) != 0:
            for path1 in os.listdir(row[1]):
                print(path1)
                temp.append(row[0])
                temp.append(matrix_injector(row[1] + "\\" + path1))
                temp.append(row[2])
                dmr_ir.append(temp)
                temp = []
    pass


generate_instance(rows)
# print(dmr_ir)
print(len(dmr_ir))
write_list(dmr_ir)
# writing to csv file
# with open(dataset_name, 'w') as csvfile:
# creating a csv writer object
#   csvwriter = csv.writer(csvfile)

# writing the data rows
# csvwriter.writerows(rows)
