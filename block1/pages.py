from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Guess1(Page):
    form_model = 'player'
    form_fields = ['guess1']

    def vars_for_template(self):
        s1 = self.subsession.signal1
        s2 = self.subsession.signal2
        s3 = self.subsession.signal3
        return dict(
            s1=s1,
            s2=s2,
            s3=s3,
        )


class Guess2(Page):
    form_model = 'player'
    form_fields = ['guess2']

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Guess1, Guess2, ResultsWaitPage, Results]
