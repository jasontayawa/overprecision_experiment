from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.ConsentForm, dict(name='bot', is_consent=True)
        yield Submission(pages.ConsentWait, check_html=False)
