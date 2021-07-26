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
    name_in_url = 'p55l50_reverse'
    players_per_group = None
    num_rounds = 64


class Subsession(BaseSubsession):

    #table 1 variables
    Rrr = models.IntegerField()
    Rrb = models.IntegerField()
    Rbr = models.IntegerField()
    Rbb = models.IntegerField()

    Brr = models.IntegerField()
    Brb = models.IntegerField()
    Bbr = models.IntegerField()
    Bbb = models.IntegerField()

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


    def creating_session(self):
        df = pd.read_csv('p55l50_reverse/rounds_p55l50.csv')

        for p in self.get_players():
            if self.round_number == 1:
                p.partition = random.randint(1, 46)
            else:
                p.partition = p.in_round(1).partition

            p.color = df['Color'][(64 * (p.partition - 1)) + self.round_number - 1]
            p.signal1 = df['Signal1'][(64 * (p.partition - 1)) + self.round_number - 1]
            p.signal2 = df['Signal2'][(64 * (p.partition - 1)) + self.round_number - 1]
            p.signal3 = df['Signal3'][(64 * (p.partition - 1)) + self.round_number - 1]
            p.signal4 = df['Signal4'][(64 * (p.partition - 1)) + self.round_number - 1]

        #Table 1 reverse showing Signals 3 and 4  (in the experiment 3 and 4 are presented first)

        self.Rrr = df[(df.Color == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rrb = df[(df.Color == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rbr = df[(df.Color == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Rbb = df[(df.Color == 1) & (df.Signal3 == 0) & (df.Signal4 == 0) ].count()['Color']

        self.Brr = df[(df.Color == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Brb = df[(df.Color == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Bbr = df[(df.Color == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Bbb = df[(df.Color == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        # Table 2 reverse with  s3,s4,s1,s2 = s3,r,s1,s2
        self.Rrrrr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rbrrr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Rrrrb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rrrbr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rbrrb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Rbrbr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Rrrbb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Rbrbb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Brrrr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Bbrrr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Brrrb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Brrbr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Bbrrb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Bbrbr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        self.Brrbb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 1)].count()['Color']

        self.Bbrbb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 1)].count()['Color']

        # Table 2 reverse with  s3,s4,s1,s2 = s3,b,s1,s2
        self.Rrbrr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rbbrr = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Rrbrb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rrbbr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rbbrb = df[(df.Color == 1) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Rbbbr = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Rrbbb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Rbbbb = df[(df.Color == 1) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Brbrr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Bbbrr = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Brbrb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Brbbr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Bbbrb = df[(df.Color == 0) & (df.Signal1 == 1) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Bbbbr = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 1) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']

        self.Brbbb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 1) & (df.Signal4 == 0)].count()['Color']

        self.Bbbbb = df[(df.Color == 0) & (df.Signal1 == 0) & (df.Signal2 == 0) & (df.Signal3 == 0) & (df.Signal4 == 0)].count()['Color']



class Group(BaseGroup):
    pass


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








