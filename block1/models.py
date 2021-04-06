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
    num_rounds = 2000


class Subsession(BaseSubsession):
    color = models.IntegerField()
    signal1 = models.IntegerField()
    signal2 = models.IntegerField()
    signal3 = models.IntegerField()
    signal4 = models.IntegerField()

    def creating_session(self):
        states = pd.read_csv('block1/Block1rounds.csv')
        self.color = states['Color'][self.round_number-1]
        self.signal1 = states['Signal1'][self.round_number-1]
        self.signal2 = states['Signal2'][self.round_number-1]
        self.signal3 = states['Signal3'][self.round_number-1]
        self.signal4 = states['Signal4'][self.round_number-1]


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

