# this makes list of folders which are in folder
import os
folders=os.listdir("data")
print(folders)
for folder in folders:
    print(folders)
print(os.listdir(f"data/{folders}"))