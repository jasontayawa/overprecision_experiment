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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'block1'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):
    pass


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

