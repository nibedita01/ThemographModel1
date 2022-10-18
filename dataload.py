# Import Module
import os
import numpy as np
import pandas as pd

# Folder Path
path = "E:\\datasets\\DMR-IR_dataset\\HEALTHY\\42\\Matrizes\\PAC_11_DN0.txt"

# Change the directory
# os.chdir(path)

# my_arr = np.empty((2, 2), dtype=float)
df = pd.read_csv(path, sep='\s+', header=None)
mat1 = df.to_numpy()
print(mat1)
print(mat1.shape)
print(type(mat1))
