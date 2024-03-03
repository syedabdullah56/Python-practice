dic={"Father name":"SYED TARIQ MAHMOOD","Mother name":"ZAIB UN NISA","SON 1":"S.M ABDULLAH MAHMOOD","SON 2":"S.M USMAN MAHMOOD"}
print(dic["Father name"])
print(dic["Mother name"])
print(dic["SON 1"])
print(dic["SON 2"])
print(dic.keys())
print(dic.values())
print(dic.items())
for key in dic.keys():
    print(key)
for value in dic.values():
    print(value)
for item in dic.items():
    print(item)
for keyvalue in dic.items():
    print(f"The value corresponding to the {dic.items()}")

