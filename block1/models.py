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
    color = models.FloatField()
    signal1 = models.FloatField()
    signal2 = models.FloatField()
    signal3 = models.FloatField()
    signal4 = models.FloatField()

    def creating_session(subsession):
        states = pd.read_csv('block1/Block1rounds.csv')
        subsession.color = states['Color'][subsession.round_number-1]
        subsession.signal1 = states['Signal1'][subsession.round_number-1]
        subsession.signal2 = states['Signal2'][subsession.round_number-1]
        subsession.signal3 = states['Signal3'][subsession.round_number-1]
        subsession.signal4 = states['Signal4'][subsession.round_number-1]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess1 = models.IntegerField(initial=random.randint(0,100),
                               min=0,
                               max=100,
                               label="What do you this is the chance that the assign color for the round is Red",
                               widget=widgets.Slider)
    guess2 = models.IntegerField(initial=random.randint(0,100),
                               min=0,
                               max=100,
                               label="What do you this is the chance that the assign color for the round is Red",
                               widget=widgets.Slider)

