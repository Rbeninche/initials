name = input("Please enter your full name: ").upper()

name_list = list(name.split())

for full_name in name_list:
    for index in range(len(full_name)):
        if index == 0:
            print(full_name[index], end='')
