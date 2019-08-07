def get_initials(full_name):

    upper_fullname = full_name.upper()

    initial = ''

    name_list = upper_fullname.split(" ")
    for name in name_list:
        initial += name[0]

    return initial


def main():
    print(get_initials("Ozzie Smith"))


if __name__ == '__main__':
    main()
