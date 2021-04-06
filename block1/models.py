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
    def creating_session(self):
        for p in self.get_players():
            if self.round_number == 1:
                p.partition = random.randint(1, 100)
            else:
                p.partition = p.in_round(1).partition

            states = pd.read_csv('block1/Block1rounds.csv')
            p.color = states['Color'][(20*(p.partition - 1)) + self.round_number-1]
            p.signal1 = states['Signal1'][(20*(p.partition - 1)) + self.round_number-1]
            p.signal2 = states['Signal2'][(20*(p.partition - 1)) + self.round_number-1]
            p.signal3 = states['Signal3'][(20*(p.partition - 1)) + self.round_number-1]
            p.signal4 = states['Signal4'][(20*(p.partition - 1)) + self.round_number-1]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess1 = models.IntegerField(initial=50,
                               min=0,
                               max=100,
                               label="What do you this is the chance that the assign color for the round is Red",
                               widget=widgets.Slider)
    guess2 = models.IntegerField(initial=50,
                               min=0,
                               max=100,
                               label="What do you this is the chance that the assign color for the round is Red",
                               widget=widgets.Slider)

    color = models.IntegerField()
    signal1 = models.IntegerField()
    signal2 = models.IntegerField()
    signal3 = models.IntegerField()
    signal4 = models.IntegerField()
    partition = models.IntegerField()