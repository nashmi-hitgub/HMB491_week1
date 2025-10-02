import pandas as pd
import matplotlib.pyplot as plt

# TODO: load the dataset as pandas dataframe

df_teeth = pd.read_csv("mammal_teeth.csv")

plt.figure(figsize=(10, 10)) # set figure size
plt.scatter(x=df_teeth['Top incisors'],
y=df_teeth['MAMMAL']) # set figure x, y axis
plt.gca().xaxis.set_visible(True)
plt.gca().yaxis.set_visible(True)
plt.xlabel("Top incisors")
plt.ylabel("MAMMAL")

# TODO: change the title name to include your name
plt.title("mammal_teeth plot_ModharAQ")
plt.savefig("mammal_teeth_scatterplotMAQ.png", dpi=150) # save the figure