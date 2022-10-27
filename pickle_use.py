# Python program to store list to file using pickle module
import pickle
import numpy as np


# write list to binary file
def write_list(a_list):
    # store list in binary file so 'wb' mode
    with open('listfile', 'wb') as fp:
        pickle.dump(a_list, fp)
        print('Done writing list into a binary file')


# Read list to memory
def read_list(sampleList):
    # for reading also binary mode is important
    with open(sampleList, 'rb') as fp:
        n_list = pickle.load(fp)
        return n_list


dataset = np.array(read_list(r'D:\kailasha\Documents\bhanu\project_work\major\ThemographModel1\dmr_ir'))
print(dataset[10:50])
