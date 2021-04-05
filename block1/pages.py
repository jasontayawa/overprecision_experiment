from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Guess1(Page):
    form_model = 'player'
    form_fields = ['guess1']

class Guess2(Page):
    form_model = 'player'
    form_fields = ['guess2']

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
