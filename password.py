from random import shuffle, choice, randint


class Password:
    def __init__(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        lett = [choice(letters) for _ in range(randint(8, 10))]
        sym = [choice(symbols) for _ in range(randint(2, 4))]
        num = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = lett + sym + num
        shuffle(password_list)

        self.password = "".join(password_list)

    def generate(self):
        return self.password
