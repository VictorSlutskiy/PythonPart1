import pandas as pd
from math import pi
from matplotlib import pyplot as plt

info = pd.read_csv("test.csv")
info = info.head(1000)
print(info)
n = info.isnull().sum()
print(info.groupby(info["Rooms"]).agg(len))
print(n)
print(info[info["LifeSquare"].isnull()])
plt.plot(info["Id"], info["Square"])
plt.yscale(value="log")
plt.show()
plt.boxplot(x=info["HouseYear"])
plt.show()
info["LifeSquare"] = info["LifeSquare"].fillna(pi * info["Square"])
info["Healthcare_1"] = info["Healthcare_1"].fillna(info["Helthcare_2"])
n = info.isnull().sum()
print(n)
b = info.pivot_table(info, index=info["DistrictId"], columns=info["Rooms"], aggfunc=len, fill_value=0)
print(b)
