# from ucimlrepo import fetch_ucirepo 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # fetch dataset 
# magic_gamma_telescope = fetch_ucirepo(id=159) 

# # data (as pandas dataframes) 
# X = magic_gamma_telescope.data.features 
# y = magic_gamma_telescope.data.targets 

# # metadata 
# print(magic_gamma_telescope.metadata) 

# # variable information 
# print(magic_gamma_telescope.variables) 
cols=["fLength","fWidth","fSize","fConc","fConc1","fAsym","fM3Long","fM3Trans","fAlpha","fDist","class"]
df=pd.read_csv("ML/magic04.data",names=cols)
# print(df)
# print(df['class'].unique())
df['class']=(df['class']=='g').astype(int)
print(df)