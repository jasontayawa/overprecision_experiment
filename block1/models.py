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

    #table 1 variables
    Rrrr = models.IntegerField()
    Rrrb = models.IntegerField()
    Rrbr = models.IntegerField()
    Rbrr = models.IntegerField()
    Rrbb = models.IntegerField()
    Rbrb = models.IntegerField()
    Rbbr = models.IntegerField()
    Rbbb = models.IntegerField()

    Brrr = models.IntegerField()
    Brrb = models.IntegerField()
    Brbr = models.IntegerField()
    Bbrr = models.IntegerField()
    Brbb = models.IntegerField()
    Bbrb = models.IntegerField()
    Bbbr = models.IntegerField()
    Bbbb = models.IntegerField()

    #table 2 variables given s1,s2 = rr

    Rrr_rr = models.IntegerField()
    Rrb_rr = models.IntegerField()
    Rbr_rr = models.IntegerField()
    Rbb_rr = models.IntegerField()

    Brr_rr = models.IntegerField()
    Brb_rr = models.IntegerField()
    Bbr_rr = models.IntegerField()
    Bbb_rr = models.IntegerField()

    # table 2 variables given s1,s2 = rb

    Rrr_rb = models.IntegerField()
    Rrb_rb = models.IntegerField()
    Rbr_rb = models.IntegerField()
    Rbb_rb = models.IntegerField()

    Brr_rb = models.IntegerField()
    Brb_rb = models.IntegerField()
    Bbr_rb = models.IntegerField()
    Bbb_rb = models.IntegerField()

    # table 2 variables given s1,s2 = br

    Rrr_br = models.IntegerField()
    Rrb_br = models.IntegerField()
    Rbr_br = models.IntegerField()
    Rbb_br = models.IntegerField()

    Brr_br = models.IntegerField()
    Brb_br = models.IntegerField()
    Bbr_br = models.IntegerField()
    Bbb_br = models.IntegerField()

    # table 2 variables given s1,s2 = bb

    Rrr_bb = models.IntegerField()
    Rrb_bb = models.IntegerField()
    Rbr_bb = models.IntegerField()
    Rbb_bb = models.IntegerField()

    Brr_bb = models.IntegerField()
    Brb_bb = models.IntegerField()
    Bbr_bb = models.IntegerField()
    Bbb_bb = models.IntegerField()

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

        #Table 1 showing Signals 1,2, and 3

        self.Rrrr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1)].count()['Color']

        self.Rrrb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0)].count()['Color']

        self.Rrbr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1)].count()['Color']

        self.Rbrr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1)].count()['Color']

        self.Rrbb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0)].count()['Color']

        self.Rbrb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0)].count()['Color']

        self.Rbbr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1)].count()['Color']

        self.Rbbb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0)].count()['Color']

        self.Brrr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1)].count()['Color']

        self.Brrb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0)].count()['Color']

        self.Brbr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1)].count()['Color']

        self.Bbrr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1)].count()['Color']

        self.Brbb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0)].count()['Color']

        self.Bbrb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0)].count()['Color']

        self.Bbbr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1)].count()['Color']

        self.Bbbb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0)].count()['Color']

        # Table 2 showing Signals 3 & 4 given s1,s2 = rr

        self.Rrr_rr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rrb_rr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rbr_rr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Rbb_rr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Brr_rr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Brb_rr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Bbr_rr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Bbb_rr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        # Table 2 showing Signals 3 & 4 given s1,s2 = rb

        self.Rrr_rb = \
        df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
            'Color']

        self.Rrb_rb = \
        df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
            'Color']

        self.Rbr_rb = \
        df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
            'Color']

        self.Rbb_rb = \
        df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
            'Color']

        self.Brr_rb = \
        df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
            'Color']

        self.Brb_rb = \
        df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
            'Color']

        self.Bbr_rb = \
        df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
            'Color']

        self.Bbb_rb = \
        df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
            'Color']

        # Table 2 showing Signals 3 & 4 given s1,s2 = br

        self.Rrr_br = \
        df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
            'Color']

        self.Rrb_br = \
        df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
            'Color']

        self.Rbr_br = \
        df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
            'Color']

        self.Rbb_br = \
        df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
            'Color']

        self.Brr_br = \
        df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
            'Color']

        self.Brb_br = \
        df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
            'Color']

        self.Bbr_br = \
        df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
            'Color']

        self.Bbb_br = \
        df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
            'Color']

        # Table 2 showing Signals 3 & 4 given s1,s2 = bb

        self.Rrr_bb = \
        df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
            'Color']

        self.Rrb_bb = \
        df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
            'Color']

        self.Rbr_bb = \
        df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
            'Color']

        self.Rbb_bb = \
        df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
            'Color']

        self.Brr_bb = \
        df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
            'Color']

        self.Brb_bb = \
        df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
            'Color']

        self.Bbr_bb = \
        df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
            'Color']

        self.Bbb_bb = \
        df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
            'Color']

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
                               label="Guess 1: What do you this is the chance that the assign color for the round is Red?",
                               widget=widgets.Slider)
    guess2 = models.IntegerField(initial=50,
                               min=0,
                               max=100,
                               label="Guess 2: What do you this is the chance that the assign color for the round is Red?",
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







