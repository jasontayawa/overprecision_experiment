from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import pandas as pd
import random

class Guess1(Page):
    form_model = 'player'
    form_fields = ['guess1',
                   'check_slider_one']

    def error_message(self, values):
        if values['check_slider_one'] == None:
            return 'Please use the slider to make a decision.'

    def vars_for_template(self):
        #table 1 reverse variables
        s1 = self.player.signal1
        s2 = self.player.signal2
        s3 = self.player.signal3
        s4 = self.player.signal4

        Rrr = self.subsession.Rrr
        Rrb = self.subsession.Rrb
        Rbr = self.subsession.Rbr
        Rbb = self.subsession.Rbb

        Brr = self.subsession.Brr
        Brb = self.subsession.Brb
        Bbr = self.subsession.Bbr
        Bbb = self.subsession.Bbb

        #table 1 reverse variables totals
        rr = Rrr + Brr
        rb = Rrb + Brb
        br = Rbr + Bbr
        bb = Rbb + Bbb

        return dict(
            s1=s1,
            s2=s2,
            s3=s3,
            s4=s4,
            Rrr=Rrr,
            Rrb=Rrb,
            Rbr=Rbr,
            Rbb=Rbb,
            Brr=Brr,
            Brb=Brb,
            Bbr=Bbr,
            Bbb=Bbb,
            rr=rr,
            rb=rb,
            br=br,
            bb=bb,
        )

class Guess2(Page):
    form_model = 'player'
    form_fields = ['guess2', 'check_slider_two']

    def error_message(self, values):
        if values['check_slider_two'] == None:
            return 'Please use the slider to make a decision.'

    def vars_for_template(self):
        # table 1 reverse variables
        s1 = self.player.signal1
        s2 = self.player.signal2
        s3 = self.player.signal3
        s4 = self.player.signal4

        Rrr = self.subsession.Rrr
        Rrb = self.subsession.Rrb
        Rbr = self.subsession.Rbr
        Rbb = self.subsession.Rbb

        Brr = self.subsession.Brr
        Brb = self.subsession.Brb
        Bbr = self.subsession.Bbr
        Bbb = self.subsession.Bbb

        # table 1 reverse variables totals
        rr = Rrr + Brr
        rb = Rrb + Brb
        br = Rbr + Bbr
        bb = Rbb + Bbb

        # table 2 reverse variables when s4, s4=r
        Rrrrr = self.subsession.Rrrrr
        Rbrrr = self.subsession.Rbrrr
        Rrrrb = self.subsession.Rrrrb
        Rrrbr = self.subsession.Rrrbr
        Rbrrb = self.subsession.Rbrrb
        Rbrbr = self.subsession.Rbrbr
        Rrrbb = self.subsession.Rrrbb
        Rbrbb = self.subsession.Rbrbb

        Brrrr = self.subsession.Brrrr
        Bbrrr = self.subsession.Bbrrr
        Brrrb = self.subsession.Brrrb
        Brrbr = self.subsession.Brrbr
        Bbrrb = self.subsession.Bbrrb
        Bbrbr = self.subsession.Bbrbr
        Brrbb = self.subsession.Brrbb
        Bbrbb = self.subsession.Bbrbb

        # reverse total signal combos for s1 s2 s3 and s4=r
        rrrr = Rrrrr + Brrrr
        brrr = Rbrrr + Bbrrr
        rrrb = Rrrrb + Brrrb
        rrbr = Rrrbr + Brrbr
        brrb = Rbrrb + Bbrrb
        brbr = Rbrbr + Bbrbr
        rrbb = Rrrbb + Brrbb
        brbb = Rbrbb + Bbrbb

        # table 2 reverse variables when s4, s4=b
        Rrbrr = self.subsession.Rrbrr
        Rbbrr = self.subsession.Rbbrr
        Rrbrb = self.subsession.Rrbrb
        Rrbbr = self.subsession.Rrbbr
        Rbbrb = self.subsession.Rbbrb
        Rbbbr = self.subsession.Rbbbr
        Rrbbb = self.subsession.Rrbbb
        Rbbbb = self.subsession.Rbbbb

        Brbrr = self.subsession.Brbrr
        Bbbrr = self.subsession.Bbbrr
        Brbrb = self.subsession.Brbrb
        Brbbr = self.subsession.Brbbr
        Bbbrb = self.subsession.Bbbrb
        Bbbbr = self.subsession.Bbbbr
        Brbbb = self.subsession.Brbbb
        Bbbbb = self.subsession.Bbbbb

        # reverse total signal combos for s1 s2 s3 and s4=b
        rbrr = Rrbrr + Brbrr
        bbrr = Rbbrr + Bbbrr
        rbrb = Rrbrb + Brbrb
        rbbr = Rrbbr + Brbbr
        bbrb = Rbbrb + Bbbrb
        bbbr = Rbbbr + Bbbbr
        rbbb = Rrbbb + Brbbb
        bbbb = Rbbbb + Bbbbb


        return dict(
            s1=s1,
            s2=s2,
            s3=s3,
            s4=s4,
            Rrr=Rrr,
            Rrb=Rrb,
            Rbr=Rbr,
            Rbb=Rbb,
            Brr=Brr,
            Brb=Brb,
            Bbr=Bbr,
            Bbb=Bbb,
            rr=rr,
            rb=rb,
            br=br,
            bb=bb,
            Rrrrr=Rrrrr,
            Rrrbr=Rrrbr,
            Rrbrr=Rrbrr,
            Rbrrr=Rbrrr,
            Rrbbr=Rrbbr,
            Rbrbr=Rbrbr,
            Rbbrr=Rbbrr,
            Rbbbr=Rbbbr,
            Brrrr=Brrrr,
            Brrbr=Brrbr,
            Brbrr=Brbrr,
            Bbrrr=Bbrrr,
            Brbbr=Brbbr,
            Bbrbr=Bbrbr,
            Bbbrr=Bbbrr,
            Bbbbr=Bbbbr,
            rrrr=rrrr,
            rrbr=rrbr,
            rbrr=rbrr,
            brrr=brrr,
            rbbr=rbbr,
            brbr=brbr,
            bbrr=bbrr,
            bbbr=bbbr,
            Rrrrb=Rrrrb,
            Rrrbb=Rrrbb,
            Rrbrb=Rrbrb,
            Rbrrb=Rbrrb,
            Rrbbb=Rrbbb,
            Rbrbb=Rbrbb,
            Rbbrb=Rbbrb,
            Rbbbb=Rbbbb,
            Brrrb=Brrrb,
            Brrbb=Brrbb,
            Brbrb=Brbrb,
            Bbrrb=Bbrrb,
            Brbbb=Brbbb,
            Bbrbb=Bbrbb,
            Bbbrb=Bbbrb,
            Bbbbb=Bbbbb,
            rrrb=rrrb,
            rrbb=rrbb,
            rbrb=rbrb,
            brrb=brrb,
            rbbb=rbbb,
            brbb=brbb,
            bbrb=bbrb,
            bbbb=bbbb,
        )

class Payment_Calculation(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.random_round1 = random.randint(1, 21)  # random.randint(1, 60)
        self.player.random_round2 = random.randint(1, 21)  # random.randint(1, 60)
        player_in_round1 = self.player.in_round(self.player.random_round1)
        player_in_round2 = self.player.in_round(self.player.random_round2)

        # Logging in the vars for the random rounds
        self.player.color_random_round1 = player_in_round1.color
        self.player.guess1_random_round1 = player_in_round1.guess1

        self.player.color_random_round2 = player_in_round2.color
        self.player.guess2_random_round2 = player_in_round2.guess2

        selected_round_guess1 = self.player.random_round1
        color_guess1 = self.player.color_random_round1
        guess1 = self.player.guess1_random_round1

        selected_round_guess2 = self.player.random_round2
        color_guess2 = self.player.color_random_round2
        guess2 = self.player.guess2_random_round2

        # random number
        self.player.y1 = random.randint(0, 100)
        self.player.y2 = random.randint(0, 100)

        self.player.x1 = random.randint(0, 100)
        self.player.x2 = random.randint(0, 100)

        # BDM payment
        if self.player.guess1_random_round1 >= self.player.y1:
            if self.player.color_random_round1 == 1:
                self.player.profit_guess1 = 10
            else:
                self.player.profit_guess1 = 0
        else:
            if self.player.x1 <= self.player.y1:
                self.player.profit_guess1 = 10
            else:
                self.player.profit_guess1 = 0

        if self.player.guess2_random_round2 >= self.player.y2:
            if self.player.color_random_round2 == 1:
                self.player.profit_guess2 = 10
            else:
                self.player.profit_guess2 = 0
        else:
            if self.player.x2 <= self.player.y2:
                self.player.profit_guess2 = 10
            else:
                self.player.profit_guess2 = 0

        self.player.payoff = self.player.profit_guess1 + self.player.profit_guess2

        payment = self.participant.payoff

        return dict(
            random_round1= self.player.random_round1,
            random_round2 = self.player.random_round2,
            selected_round_guess1=selected_round_guess1,
            color_guess1=color_guess1,
            guess1=guess1,
            selected_round_guess2=selected_round_guess2,
            color_guess2=color_guess2,
            guess2=guess2,
            payment=payment,
            y1=self.player.y1,
            y2=self.player.y2,
            x1=self.player.x1,
            x2=self.player.x2,

        )



class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        selected_round_guess1 = self.player.random_round1
        color_guess1 = self.player.color_random_round1
        guess1 = self.player.guess1_random_round1

        selected_round_guess2 = self.player.random_round2
        color_guess2 = self.player.color_random_round2
        guess2 = self.player.guess2_random_round2

        payment = self.participant.payoff

        y1 = self.player.y1
        y2 = self.player.y2
        x1 = self.player.x1
        x2 = self.player.x2

        return dict(
            selected_round_guess1=selected_round_guess1,
            color_guess1=color_guess1,
            guess1=guess1,
            selected_round_guess2=selected_round_guess2,
            color_guess2=color_guess2,
            guess2=guess2,
            payment=payment,
            y1=y1,
            y2=y2,
            x1=x1,
            x2=x2,

        )
class Block2(Page):
    def is_displayed(self):
        return self.round_number == 21

class Block3(Page):
    def is_displayed(self):
        return self.round_number == 41



page_sequence = [Block2, Block3, Guess1, Guess2, Payment_Calculation, Results]
