class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        result = ""
        current_points = 0
        if self.player1_points == self.player2_points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1_points, "Deuce")
        elif self.player1_points >= 4 or self.player2_points >= 4:
            point_difference = self.player1_points - self.player2_points
            if point_difference == 1:
                result = "Advantage player1"
            elif point_difference == -1:
                result = "Advantage player2"
            elif point_difference >= 2:
                result = "Win for player1"
            else:
                result = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    current_points = self.player1_points
                else:
                    result += "-"
                    current_points = self.player2_points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[current_points]
        return result
