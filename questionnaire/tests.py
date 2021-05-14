from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        yield pages.Experience, dict(
            understanding=random.choice([True, False]),
            confusion="none cause this rocked",
            decision1="Testing",
            decision2="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            decision3="3333333333333333333333333333333333333333333333333333333333333333333333333333333333333",
        )

        yield pages.Demographics, dict(
            age=random.randint(18, 25),
            gender=random.randint(1, 3),
            major='bot',
            educ_year=random.randint(1, 6),
            past_experiments=random.choice([True, False]),
            game_theory=random.choice([True, False]),
            experiment=random.choice([True, False]),
        )
