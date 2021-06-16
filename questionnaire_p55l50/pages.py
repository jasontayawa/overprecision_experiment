from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Experience(Page):
    form_model = 'player'

    form_fields = ['decision1', 'decision2', 'decision3', 'confusion', 'understanding']

    def vars_for_template(self):
        profit_in_dollar = self.participant.payoff.to_real_world_currency(self.session)

        return dict(
            final_dollar=profit_in_dollar
        )


class Demographics(Page):
    form_model = 'player'

    form_fields = ['age',
                   'gender',
                   'major',
                   'educ_year',
                   'past_experiments',
                   'game_theory',
                   'experiment']

    def vars_for_template(self):
        profit_in_dollar = self.participant.payoff.to_real_world_currency(self.session)

        return dict(
            final_dollar=profit_in_dollar
        )


page_sequence = [Experience, Demographics]
