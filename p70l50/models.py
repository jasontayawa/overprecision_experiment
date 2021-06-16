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
import numpy
from psycopg2.extensions import register_adapter, AsIs
def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)
def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)
register_adapter(numpy.float64, addapt_numpy_float64)
register_adapter(numpy.int64, addapt_numpy_int64)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'p70l50'
    players_per_group = None
    num_rounds = 60


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

    # table 2 variables when s4=r
    Rrrrr = models.IntegerField()
    Rrrbr = models.IntegerField()
    Rrbrr = models.IntegerField()
    Rbrrr = models.IntegerField()
    Rrbbr = models.IntegerField()
    Rbrbr = models.IntegerField()
    Rbbrr = models.IntegerField()
    Rbbbr = models.IntegerField()

    Brrrr = models.IntegerField()
    Brrbr = models.IntegerField()
    Brbrr = models.IntegerField()
    Bbrrr = models.IntegerField()
    Brbbr = models.IntegerField()
    Bbrbr = models.IntegerField()
    Bbbrr = models.IntegerField()
    Bbbbr = models.IntegerField()

    # table 2 variables when s4=b
    Rrrrb = models.IntegerField()
    Rrrbb = models.IntegerField()
    Rrbrb = models.IntegerField()
    Rbrrb = models.IntegerField()
    Rrbbb = models.IntegerField()
    Rbrbb = models.IntegerField()
    Rbbrb = models.IntegerField()
    Rbbbb = models.IntegerField()

    Brrrb = models.IntegerField()
    Brrbb = models.IntegerField()
    Brbrb = models.IntegerField()
    Bbrrb = models.IntegerField()
    Brbbb = models.IntegerField()
    Bbrbb = models.IntegerField()
    Bbbrb = models.IntegerField()
    Bbbbb = models.IntegerField()

    #table 2 variables given s1,s2 = rr

    # Rrr_rr = models.IntegerField()
    # Rrb_rr = models.IntegerField()
    # Rbr_rr = models.IntegerField()
    # Rbb_rr = models.IntegerField()
    #
    # Brr_rr = models.IntegerField()
    # Brb_rr = models.IntegerField()
    # Bbr_rr = models.IntegerField()
    # Bbb_rr = models.IntegerField()
    #
    # # table 2 variables given s1,s2 = rb
    #
    # Rrr_rb = models.IntegerField()
    # Rrb_rb = models.IntegerField()
    # Rbr_rb = models.IntegerField()
    # Rbb_rb = models.IntegerField()
    #
    # Brr_rb = models.IntegerField()
    # Brb_rb = models.IntegerField()
    # Bbr_rb = models.IntegerField()
    # Bbb_rb = models.IntegerField()
    #
    # # table 2 variables given s1,s2 = br
    #
    # Rrr_br = models.IntegerField()
    # Rrb_br = models.IntegerField()
    # Rbr_br = models.IntegerField()
    # Rbb_br = models.IntegerField()
    #
    # Brr_br = models.IntegerField()
    # Brb_br = models.IntegerField()
    # Bbr_br = models.IntegerField()
    # Bbb_br = models.IntegerField()

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
        df = pd.read_csv('p70l50/rounds_p70l50.csv')

        for p in self.get_players():
            if self.round_number == 1:
                p.partition = random.randint(1, 50)
            else:
                p.partition = p.in_round(1).partition

            p.color = df['Color'][(60 * (p.partition - 1)) + self.round_number - 1]
            p.signal1 = df['Signal1'][(60 * (p.partition - 1)) + self.round_number - 1]
            p.signal2 = df['Signal2'][(60 * (p.partition - 1)) + self.round_number - 1]
            p.signal3 = df['Signal3'][(60 * (p.partition - 1)) + self.round_number - 1]
            p.signal4 = df['Signal4'][(60 * (p.partition - 1)) + self.round_number - 1]

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

        # Table 2 with  s1,s2,s3,s4 = s1,s2,s3,r
        self.Rrrrr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rrrbr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Rrbrr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rbrrr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rrbbr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Rbrbr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Rbbrr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rbbbr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Brrrr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Brrbr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Brbrr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Bbrrr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Brbbr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Bbrbr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Bbbrr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Bbbbr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        # Table 2 with  s1,s2,s3,s4 = s1,s2,s3,b
        self.Rrrrb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rrrbb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Rrbrb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rbrrb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rrbbb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Rbrbb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Rbbrb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rbbbb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Brrrb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Brrbb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Brbrb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Bbrrb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Brbbb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Bbrbb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Bbbrb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Bbbbb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        # Table 2 showing Signals 3 & 4 given s1,s2 = rr

        # self.Rrr_rr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']
        #
        # self.Rrb_rr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']
        #
        # self.Rbr_rr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']
        #
        # self.Rbb_rr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']
        #
        # self.Brr_rr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']
        #
        # self.Brb_rr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']
        #
        # self.Bbr_rr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']
        #
        # self.Bbb_rr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']
        #
        # # Table 2 showing Signals 3 & 4 given s1,s2 = rb
        #
        # self.Rrr_rb = \
        # df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Rrb_rb = \
        # df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # self.Rbr_rb = \
        # df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Rbb_rb = \
        # df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # self.Brr_rb = \
        # df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Brb_rb = \
        # df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # self.Bbr_rb = \
        # df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Bbb_rb = \
        # df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # # Table 2 showing Signals 3 & 4 given s1,s2 = br
        #
        # self.Rrr_br = \
        # df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Rrb_br = \
        # df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # self.Rbr_br = \
        # df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Rbb_br = \
        # df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # self.Brr_br = \
        # df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Brb_br = \
        # df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # self.Bbr_br = \
        # df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Bbb_br = \
        # df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # # Table 2 showing Signals 3 & 4 given s1,s2 = bb
        #
        # self.Rrr_bb = \
        # df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Rrb_bb = \
        # df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # self.Rbr_bb = \
        # df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Rbb_bb = \
        # df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # self.Brr_bb = \
        # df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Brb_bb = \
        # df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()[
        #     'Color']
        #
        # self.Bbr_bb = \
        # df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()[
        #     'Color']
        #
        # self.Bbb_bb = \
        # df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()[
        #     'Color']

class Group(BaseGroup):
    pass
    # def profit_calculation(self):
    #     for p in self.get_players():
    #         p.random_round1 = 1#random.randint(1, 30)#random.randint(1, 60)
    #         p.random_round2 = 1#random.randint(1, 30)#random.randint(1, 60)
    #         player_in_round1 = p.in_round(p.random_round1)
    #         player_in_round2 = p.in_round(p.random_round2)
    #
    #         # Logging in the vars for the random rounds
    #         p.color_random_round1 = player_in_round1.color
    #         p.signal1_random_round1 = player_in_round1.signal1
    #         p.signal2_random_round1 = player_in_round1.signal2
    #         p.signal3_random_round1 = player_in_round1.signal3
    #         p.signal4_random_round1 = player_in_round1.signal4
    #         p.guess1_random_round1 = player_in_round1.guess1
    #
    #         p.color_random_round2 = player_in_round2.color
    #         p.signal1_random_round2 = player_in_round2.signal1
    #         p.signal2_random_round2 = player_in_round2.signal2
    #         p.signal3_random_round2 = player_in_round2.signal3
    #         p.signal4_random_round2 = player_in_round2.signal4
    #         p.guess2_random_round2 = player_in_round2.guess2
    #
    #         # random number
    #         p.y1 = random.randint(0, 100)
    #         p.y2 = random.randint(0, 100)
    #
    #         p.x1 = random.randint(0, 100)
    #         p.x2 = random.randint(0, 100)
    #
    #         # BDM payment
    #         if p.guess1_random_round1 >= p.y1:
    #             if p.color_random_round1 == 1:
    #                 p.profit_guess1 = 10
    #             else:
    #                 p.profit_guess1 = 0
    #         else:
    #             if p.x1 <= p.y1:
    #                 p.profit_guess1 = 10
    #             else:
    #                 p.profit_guess1 = 0
    #
    #         if p.guess2_random_round2 >= p.y2:
    #             if p.color_random_round2 == 1:
    #                 p.profit_guess2 = 10
    #             else:
    #                 p.profit_guess2 = 0
    #         else:
    #             if p.x2 <= p.y2:
    #                 p.profit_guess2 = 10
    #             else:
    #                 p.profit_guess2 = 0
    #
    #         p.payoff = p.profit_guess1 + p.profit_guess2


class Player(BasePlayer):
    guess1 = models.IntegerField()
    check_slider_one = models.IntegerField()
    guess2 = models.IntegerField()
    check_slider_two = models.IntegerField()

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
    y1 = models.IntegerField()
    x1 = models.IntegerField()

    random_round2 = models.IntegerField()
    color_random_round2 = models.IntegerField()
    signal1_random_round2 = models.IntegerField()
    signal2_random_round2 = models.IntegerField()
    signal3_random_round2 = models.IntegerField()
    signal4_random_round2 = models.IntegerField()
    guess2_random_round2 = models.IntegerField()
    y2 = models.IntegerField()
    x2 = models.IntegerField()

    # selected_round_guess1 = models.IntegerField()
    # selected_round_guess2 = models.IntegerField()
    # color_guess1 = models.IntegerField()
    # guess1 = models.IntegerField()
    # color_guess2 = models.IntegerField()
    # guess2 = models.IntegerField()







