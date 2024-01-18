import torch
from torch.utils.data import Dataset
import os

class PrecomputeDataset(Dataset):
	def __init__(self, dir, precompute, dataset):
		self.dir = dir
		self.precompute = precompute
		self.dataset = dataset

	def __len__(self):
		return len(self.dataset)

	def __getitem__(self, item):
		path = os.path.join(self.dir, f"{item}.pt")
		if os.path.exists(path):
			return torch.load(path)
		else:
			original = self.dataset[item]
			if (isinstance(original, tuple)):
				original = tuple(x.to(self.precompute.device) for x in original)	
			computed = self.precompute(original)
			torch.save(computed, path)
			return computed
