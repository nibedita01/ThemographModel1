from torch.utils.data import Dataset

from pickle_use import read_list


class DMRIRDataset(Dataset):
    def __init__(self):
        data_loc = r"E:\code\ThemographModel\dmr_ir_dataset";
        dataset = read_list(data_loc)
        self.timg = dataset['timg']
        self.label = dataset['label']
        self.shape = dataset.shape[0]

    def __len__(self):
        return self.shape

    def __getitem__(self, idx):
        return self.timg[idx], self.label[idx]


class DMRIRTestDataset(Dataset):
    def __init__(self):
        data_loc = r"E:\code\ThemographModel\dmr_ir_dataset";
        dataset = read_list(data_loc)
        self.timg = dataset['timg']
        # self.label = dataset['label']
        self.shape = dataset.shape[0]

    def __len__(self):
        return self.shape

    def __getitem__(self, idx):
        return self.timg[idx]
        # return self.timg[idx], self.label[idx]