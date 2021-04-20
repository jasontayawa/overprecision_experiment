from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['name', 'is_consent']

    def before_next_page(self):
        if self.player.is_consent:
            self.player.consent = "I consent"
        else:
            self.player.consent = "I do not consent"


class ConsentWait(Page):
    def app_after_this_page(self, upcoming_apps):
        if not self.player.is_consent:
            return upcoming_apps[-1]


page_sequence = [ConsentForm, ConsentWait]
