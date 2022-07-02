NAMES = ("John", "Jack")


def main():

    print("How many pencils would you like to use:")
    n_pencils = get_pencils()

    print("Who will be the first (John, Jack):")
    name = get_first_player()

    print("|" * n_pencils)

    turn = NAMES.index(name)
    while n_pencils > 0:
        print(f"{NAMES[turn % 2]}'s turn:")
        if NAMES[turn % 2] == "Jack":
            n = take_pencils_bot(n_pencils)
        else:
            n = take_pencils(n_pencils)
        n_pencils -= n
        if n_pencils == 0:
            print(f"{NAMES[(turn + 1) % 2]} won!")
            break

        print("|" * n_pencils)
        turn += 1


def get_pencils():
    while True:
        number = input()

        if not number.isnumeric():
            print("The number of pencils should be numeric")
            continue

        number = int(number)

        if number <= 0:
            print("The number of pencils should be positive")
            continue

        return number


def get_first_player():
    while True:
        name = input()
        if name not in NAMES:
            print("Choose between 'John' and 'Jack'")
            continue

        return name


def take_pencils(max_count):
    while True:
        number = input()

        if not number.isnumeric():
            print("Possible values: '1', '2' or '3'")
            continue

        number = int(number)

        if number not in (1, 2, 3):
            print("Possible values: '1', '2' or '3'")
            continue

        if number > max_count:
            print("Too many pencils were taken")
            continue

        return number


def take_pencils_bot(max_count):
    if max_count % 4 == 1:
        print(1)
        return 1
    elif max_count % 4 == 0 and max_count >= 4:
        print(3)
        return 3
    else:
        print(max_count % 4 - 1)
        return max_count % 4 - 1


if __name__ == "__main__":
    main()
