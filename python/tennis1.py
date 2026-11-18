SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]


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
        if self.player1_points == self.player2_points:
            if self.player1_points < 3:
                return SCORE_NAMES[self.player1_points] + "-All"
            return "Deuce"
        elif self.player1_points >= 4 or self.player2_points >= 4:
            point_difference = self.player1_points - self.player2_points
            if point_difference == 1:
                return "Advantage player1"
            elif point_difference == -1:
                return "Advantage player2"
            elif point_difference >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
        else:
            return (
                SCORE_NAMES[self.player1_points]
                + "-"
                + SCORE_NAMES[self.player2_points]
            )
