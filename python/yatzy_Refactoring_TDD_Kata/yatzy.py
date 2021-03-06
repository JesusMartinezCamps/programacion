class Yatzy:

    @staticmethod
    #Un metodo static no puede recibir un objeto
    def chance(*dice):
        total = 0
        for die in dice:
            total += die

        return total

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) == 5:
            return 50
        return 0
    
    @staticmethod
    def ones(*dice):
        score = 0
        for die in dice:
            if die == 1:
                score += die
        return score

        # ONE = 1
        # return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
         score = 0
         for die in dice:
             if die == 2:
                 score += 2
         return score
    """
        TWO = 2
        return dice.count(TWO) * TWO
    """

    @staticmethod
    def threes(*dice):
        score = 0
        for die in dice:
            if die == 3:
                score += 3
        return score 

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    def fours(self):
        score = 0
        for number in range(5):
            if (self.dice[number] == 4): 
                score += 4
        return score

    def fives(self):
        score = 0
        for number in range(5): 
            if (self.dice[number] == 5):
                score += 5
        return score

    def sixes(self):
        score = 0
        for number in range(5): 
            if (self.dice[number] == 6):
                score += 6
        return score
    
    @staticmethod
    def pair(*dice):
        for number in range(6, 0, -1):
            if dice.count(number) >= 2:
                return number * 2
        return 0
    
    @staticmethod
    def two_pair(*dice):
        score = 0
        number_of_pairs = 0
        for number in range(6, 0, -1):
            if dice.count(number) >= 4:
                score += number * 4
                number_of_pairs += 2
            elif dice.count(number) >= 2:
                score += number * 2
                number_of_pairs += 1
        if number_of_pairs >= 2:
            return score
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        score = 0
        for number in range(1, 7, 1):
            if dice.count(number) >= 3:
                score += number * 3
                return score
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        score = 0
        for number in range(1, 7, 1):
            if dice.count(number) >= 4:
                score += number * 4
                return score
        return 0

    @staticmethod
    def small_straight(*dice):
        straight = 0
        for number in range(1, 6, 1):
            if dice.count(number) == 1:
                straight += 1

        if straight == 5:
            return 15
        else:
            return 0

    @staticmethod
    def large_straight(*dice):
        straight = 0
        for number in range(2, 7, 1):
            if dice.count(number) == 1:
                straight += 1

        if straight == 5:
            return 20
        else:
            return 0

    @staticmethod
    def full_house(*dice):
        score = 0
        for number in range(1, 7, 1):
            if dice.count(number) > 4 or dice.count(number) == 1:
                return 0
            elif dice.count(number) == 3:
                score += number * 3
            elif dice.count(number) == 2:
                score += number * 2
        return score