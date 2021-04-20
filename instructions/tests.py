from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Instructions1
        yield pages.Instructions2
        yield pages.Instructions3
        yield pages.Instructions4
        yield pages.Instructions5
        yield pages.Instructions6
        yield pages.Instructions7
        yield pages.Instructions8
        yield pages.Block1
