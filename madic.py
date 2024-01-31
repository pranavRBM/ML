from ucimlrepo import fetch_ucirepo 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# fetch dataset 
magic_gamma_telescope = fetch_ucirepo(id=159) 

# data (as pandas dataframes) 
X = magic_gamma_telescope.data.features 
y = magic_gamma_telescope.data.targets 

# metadata 
print(magic_gamma_telescope.metadata) 

# variable information 
print(magic_gamma_telescope.variables) 
# pd.read_csv("ML/magic04.data")