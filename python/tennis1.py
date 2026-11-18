SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
DEUCE_POINTS = 3
ENDGAME_POINTS = 4
WINNING_MARGIN = 2


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
            return self._tied_score()
        if (
            self.player1_points >= ENDGAME_POINTS
            or self.player2_points >= ENDGAME_POINTS
        ):
            return self._endgame_score()
        return self._running_score()

    def _tied_score(self):
        if self.player1_points < DEUCE_POINTS:
            return SCORE_NAMES[self.player1_points] + "-All"
        return "Deuce"

    def _endgame_score(self):
        point_difference = self.player1_points - self.player2_points
        if point_difference == 1:
            return "Advantage player1"
        if point_difference == -1:
            return "Advantage player2"
        if point_difference >= WINNING_MARGIN:
            return "Win for player1"
        return "Win for player2"

    def _running_score(self):
        return (
            SCORE_NAMES[self.player1_points]
            + "-"
            + SCORE_NAMES[self.player2_points]
        )
