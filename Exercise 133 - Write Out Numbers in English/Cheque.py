class Cheque:

    min_money = 1
    max_money = 999

    int_to_str_mapper = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eightteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eightty",
        90: "ninety"
    }
    
    def __init__(self, payer: str, payee: str, money: int):
        self.payer = payer
        self.payee = payee
        self.money = money
        self._validate_money_value()

    def __str__(self):
        return f"Cheque: {self.payer} is supposed to pay {str(self.money)} ({self.money_to_words()}) to {self.payee}"

    def _validate_money_value(self):
        if self.money > self.max_money:
            raise ValueError(f"The value passed as money ({self.money}) is  greater than max allowed money ({self.max_money})")
        elif self.money < self.min_money:
            raise ValueError(f"The value passed as money ({self.money}) is  smaller than min allowed money ({self.min_money})")

    def money_to_words(self):
        money_as_str = str(self.money)
        words = ""

        if len(money_as_str) == 3:
            words += self.int_to_str_mapper[int(money_as_str[-3])] + " hundred"

        if len(money_as_str) >= 2:
            words += " " + self.int_to_str_mapper[int(money_as_str[-2]) * 10]
        
        words += " " + self.int_to_str_mapper[int(money_as_str[-1])]

        return words.strip()
        