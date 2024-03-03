import os
files=os.listdir("E:\code with abdullah\python by code with harry\FOREXERCISE7")
i=1
for file in files:
    if (file.startswith("png")):
        print(file)
        os.rename(f"E:\code with abdullah\python by code with harry\FOREXERCISE7/{file}",f"DAY {i} .png")
        i=i+1