def get_initials(full_name):

    name_list = list(full_name.split())

    for name in name_list:
        for index in range(len(name)):
            if index == 0:
                print(name[index], end='')
def main():
    name = input("Please enter your full name: ").upper()
    get_initials(name)

if __name__ == '__main__':
    main()