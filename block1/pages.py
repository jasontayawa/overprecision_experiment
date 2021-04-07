from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import pandas as pd


class Guess1(Page):
    form_model = 'player'
    form_fields = ['guess1']

    def vars_for_template(self):
        s1 = self.player.signal1
        s2 = self.player.signal2
        s3 = self.player.signal3
        s4 = self.player.signal4

        Rrrr = self.subsession.Rrrr
        Rrrb = self.subsession.Rrrb
        Rrbr = self.subsession.Rrbr
        Rbrr = self.subsession.Rbrr
        Rrbb = self.subsession.Rrbb
        Rbrb = self.subsession.Rbrb
        Rbbr = self.subsession.Rbbr
        Rbbb = self.subsession.Rbbb

        Brrr = self.subsession.Brrr
        Brrb = self.subsession.Brrb
        Brbr = self.subsession.Brbr
        Bbrr = self.subsession.Bbrr
        Brbb = self.subsession.Brbb
        Bbrb = self.subsession.Bbrb
        Bbbr = self.subsession.Bbbr
        Bbbb = self.subsession.Bbbb
        return dict(
            s1=s1,
            s2=s2,
            s3=s3,
            s4=s4,
            Rrrr=Rrrr,
            Rrrb=Rrrb,
            Rrbr=Rrbr,
            Rbrr=Rbrr,
            Rrbb=Rrbb,
            Rbrb=Rbrb,
            Rbbr=Rbbr,
            Rbbb=Rbbb,
            Brrr=Brrr,
            Brrb=Brrb,
            Brbr=Brbr,
            Bbrr=Bbrr,
            Brbb=Brbb,
            Bbrb=Bbrb,
            Bbbr=Bbbr,
            Bbbb=Bbbb,
        )

class Guess2(Page):
    form_model = 'player'
    form_fields = ['guess2']

    def vars_for_template(self):
        s1 = self.player.signal1
        s2 = self.player.signal2
        s3 = self.player.signal3
        s4 = self.player.signal4

        Rrrr = self.subsession.Rrrr
        Rrrb = self.subsession.Rrrb
        Rrbr = self.subsession.Rrbr
        Rbrr = self.subsession.Rbrr
        Rrbb = self.subsession.Rrbb
        Rbrb = self.subsession.Rbrb
        Rbbr = self.subsession.Rbbr
        Rbbb = self.subsession.Rbbb

        Brrr = self.subsession.Brrr
        Brrb = self.subsession.Brrb
        Brbr = self.subsession.Brbr
        Bbrr = self.subsession.Bbrr
        Brbb = self.subsession.Brbb
        Bbrb = self.subsession.Bbrb
        Bbbr = self.subsession.Bbbr
        Bbbb = self.subsession.Bbbb
        return dict(
            s1=s1,
            s2=s2,
            s3=s3,
            s4=s4,
            Rrrr=Rrrr,
            Rrrb=Rrrb,
            Rrbr=Rrbr,
            Rbrr=Rbrr,
            Rrbb=Rrbb,
            Rbrb=Rbrb,
            Rbbr=Rbbr,
            Rbbb=Rbbb,
            Brrr=Brrr,
            Brrb=Brrb,
            Brbr=Brbr,
            Bbrr=Bbrr,
            Brbb=Brbb,
            Bbrb=Bbrb,
            Bbbr=Bbbr,
            Bbbb=Bbbb,
        )

class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        self.round_number == Constants.num_rounds

    after_all_players_arrive = 'profit_calculation'


class Results(Page):
    def is_displayed(self):
        self.round_number == Constants.num_rounds




page_sequence = [Guess1, Guess2, ResultsWaitPage, Results]
