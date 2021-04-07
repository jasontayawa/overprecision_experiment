from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
import pandas as pd


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'block1'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):

    Rrrr = models.FloatField()
    Rrrb = models.FloatField()
    Rrbr = models.FloatField()
    Rbrr = models.FloatField()
    Rrbb = models.FloatField()
    Rbrb = models.FloatField()
    Rbbr = models.FloatField()
    Rbbb = models.FloatField()

    Brrr = models.FloatField()
    Brrb = models.FloatField()
    Brbr = models.FloatField()
    Bbrr = models.FloatField()
    Brbb = models.FloatField()
    Bbrb = models.FloatField()
    Bbbr = models.FloatField()
    Bbbb = models.FloatField()



    def creating_session(self):
        df = pd.read_csv('block1/Block1rounds.csv')

        for p in self.get_players():
            if self.round_number == 1:
                p.partition = random.randint(1, 100)
            else:
                p.partition = p.in_round(1).partition

            p.color = df['Color'][(20 * (p.partition - 1)) + self.round_number - 1]
            p.signal1 = df['Signal1'][(20 * (p.partition - 1)) + self.round_number - 1]
            p.signal2 = df['Signal2'][(20 * (p.partition - 1)) + self.round_number - 1]
            p.signal3 = df['Signal3'][(20 * (p.partition - 1)) + self.round_number - 1]
            p.signal4 = df['Signal4'][(20 * (p.partition - 1)) + self.round_number - 1]

        Rrrr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1)].count()['Color']

        Rrrb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0)].count()['Color']

        Rrbr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1)].count()['Color']

        Rbrr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1)].count()['Color']

        Rrbb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0)].count()['Color']

        Rbrb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0)].count()['Color']

        Rbbr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1)].count()['Color']

        Rbbr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0)].count()['Color']

        Brrr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1)].count()['Color']

        Brrb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0)].count()['Color']

        Brbr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1)].count()['Color']

        Bbrr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1)].count()['Color']

        Brbb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0)].count()['Color']

        Bbrb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0)].count()['Color']

        Bbbr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1)].count()['Color']

        Bbbb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0)].count()['Color']


class Group(BaseGroup):
    def profit_calculation(self):
        for p in self.get_players():
            p.random_round1 = random.randint(1, 20)
            p.random_round2 = random.randint(1, 20)
            player_in_round1 = p.in_round(p.random_round1)
            player_in_round2 = p.in_round(p.random_round2)

            # Logging in the vars for the random rounds
            p.color_random_round1 = player_in_round1.color
            p.signal1_random_round1 = player_in_round1.signal1
            p.signal2_random_round1 = player_in_round1.signal2
            p.signal3_random_round1 = player_in_round1.signal3
            p.signal4_random_round1 = player_in_round1.signal4
            p.guess1_random_round1 = player_in_round1.guess1

            p.color_random_round2 = player_in_round2.color
            p.signal1_random_round2 = player_in_round2.signal1
            p.signal2_random_round2 = player_in_round2.signal2
            p.signal3_random_round2 = player_in_round2.signal3
            p.signal4_random_round2 = player_in_round2.signal4
            p.guess2_random_round2 = player_in_round2.guess2

            # random number
            y1 = random.randint(0, 100)
            y2 = random.randint(0, 100)

            x1 = random.randint(0, 100)
            x2 = random.randint(0, 100)

            # BDM payment
            if p.guess1_random_round1 >= y1 and p.color_random_round1 == 1:
                p.profit_guess1 = 10
            elif p.guess1_random_round1 < y1:
                if x1 <= y1:
                    p.profit_guess1 = 10
                else:
                    p.profit_guess1 = 0

            if p.guess2_random_round2 >= y2 and p.color_random_round2 == 1:
                p.profit_guess2 = 10
            elif p.guess2_random_round2 < y2:
                if x2 <= y2:
                    p.profit_guess2 = 10
                else:
                    p.profit_guess2 = 0


class Player(BasePlayer):
    guess1 = models.IntegerField(initial=50,
                               min=0,
                               max=100,
                               label="(Guess 1) What do you this is the chance that the assign color for the round is Red",
                               widget=widgets.Slider)
    guess2 = models.IntegerField(initial=50,
                               min=0,
                               max=100,
                               label="(Guess 2) What do you this is the chance that the assign color for the round is Red",
                               widget=widgets.Slider)

    color = models.IntegerField()
    signal1 = models.IntegerField()
    signal2 = models.IntegerField()
    signal3 = models.IntegerField()
    signal4 = models.IntegerField()
    partition = models.IntegerField()

    profit_guess1 = models.FloatField()
    profit_guess2 = models.FloatField()
    profit = models.FloatField()

    # Random Payment Vars
    random_round1 = models.IntegerField()
    color_random_round1 = models.IntegerField()
    signal1_random_round1 = models.IntegerField()
    signal2_random_round1 = models.IntegerField()
    signal3_random_round1 = models.IntegerField()
    signal4_random_round1 = models.IntegerField()
    guess1_random_round1 = models.IntegerField()

    random_round2 = models.IntegerField()
    color_random_round2 = models.IntegerField()
    signal1_random_round2 = models.IntegerField()
    signal2_random_round2 = models.IntegerField()
    signal3_random_round2 = models.IntegerField()
    signal4_random_round2 = models.IntegerField()
    guess2_random_round2 = models.IntegerField()







