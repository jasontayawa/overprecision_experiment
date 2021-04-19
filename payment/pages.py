from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class PaymentInfo(Page):
    form_model = 'player'
    form_fields = ['name', 'venmo', 'phone']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [PaymentInfo, End]
