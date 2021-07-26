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

        rrr = Rrrr + Brrr
        rrb = Rrrb + Brrb
        rbr = Rrbr + Brbr
        brr = Rbrr + Bbrr
        rbb = Rrbb + Brbb
        brb = Rbrb + Bbrb
        bbr = Rbbr + Bbbr
        bbb = Rbbb + Bbbb

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
            rrr=rrr,
            rrb=rrb,
            rbr=rbr,
            brr=brr,
            rbb=rbb,
            brb=brb,
            bbr=bbr,
            bbb=bbb,
        )

class Guess2(Page):
    form_model = 'player'
    form_fields = ['guess2', 'check_slider_two']

    def error_message(self, values):
        if values['check_slider_two'] == None:
            return 'Please use the slider to make a decision.'

    def vars_for_template(self):
        s1 = self.player.signal1
        s2 = self.player.signal2
        s3 = self.player.signal3
        s4 = self.player.signal4

        # table 1 variables

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

        # total signal combos for s1 s2 s3
        rrr = Rrrr + Brrr
        rrb = Rrrb + Brrb
        rbr = Rrbr + Brbr
        brr = Rbrr + Bbrr
        rbb = Rrbb + Brbb
        brb = Rbrb + Bbrb
        bbr = Rbbr + Bbbr
        bbb = Rbbb + Bbbb

        # table 2 variables when s4, s4=r
        Rrrrr = self.subsession.Rrrrr
        Rrrbr = self.subsession.Rrrbr
        Rrbrr = self.subsession.Rrbrr
        Rbrrr = self.subsession.Rbrrr
        Rrbbr = self.subsession.Rrbbr
        Rbrbr = self.subsession.Rbrbr
        Rbbrr = self.subsession.Rbbrr
        Rbbbr = self.subsession.Rbbbr

        Brrrr = self.subsession.Brrrr
        Brrbr = self.subsession.Brrbr
        Brbrr = self.subsession.Brbrr
        Bbrrr = self.subsession.Bbrrr
        Brbbr = self.subsession.Brbbr
        Bbrbr = self.subsession.Bbrbr
        Bbbrr = self.subsession.Bbbrr
        Bbbbr = self.subsession.Bbbbr

        # total signal combos for s1 s2 s3 and s4=r
        rrrr = Rrrrr + Brrrr
        rrbr = Rrrbr + Brrbr
        rbrr = Rrbrr + Brbrr
        brrr = Rbrrr + Bbrrr
        rbbr = Rrbbr + Brbbr
        brbr = Rbrbr + Bbrbr
        bbrr = Rbbrr + Bbbrr
        bbbr = Rbbbr + Bbbbr

        # table 2 variables when s4, s4=b
        Rrrrb = self.subsession.Rrrrb
        Rrrbb = self.subsession.Rrrbb
        Rrbrb = self.subsession.Rrbrb
        Rbrrb = self.subsession.Rbrrb
        Rrbbb = self.subsession.Rrbbb
        Rbrbb = self.subsession.Rbrbb
        Rbbrb = self.subsession.Rbbrb
        Rbbbb = self.subsession.Rbbbb

        Brrrb = self.subsession.Brrrb
        Brrbb = self.subsession.Brrbb
        Brbrb = self.subsession.Brbrb
        Bbrrb = self.subsession.Bbrrb
        Brbbb = self.subsession.Brbbb
        Bbrbb = self.subsession.Bbrbb
        Bbbrb = self.subsession.Bbbrb
        Bbbbb = self.subsession.Bbbbb

        # total signal combos for s1 s2 s3 and s4=b
        rrrb = Rrrrb + Brrrb
        rrbb = Rrrbb + Brrbb
        rbrb = Rrbrb + Brbrb
        brrb = Rbrrb + Bbrrb
        rbbb = Rrbbb + Brbbb
        brbb = Rbrbb + Bbrbb
        bbrb = Rbbrb + Bbbrb
        bbbb = Rbbbb + Bbbbb

        # table 2 variables given s1,s2 = rr

        # Rrrr = self.subsession.Rrrr
        # Rrrb = self.subsession.Rrrb
        # Rrbr = self.subsession.Rrbr
        # Rbrr = self.subsession.Rbrr
        # Rrbb = self.subsession.Rrbb
        # Rbrb = self.subsession.Rbrb
        # Rbbr = self.subsession.Rbbr
        # Rbbb = self.subsession.Rbbb
        #
        # Brrr = self.subsession.Brrr
        # Brrb = self.subsession.Brrb
        # Brbr = self.subsession.Brbr
        # Bbrr = self.subsession.Bbrr
        # Brbb = self.subsession.Brbb
        # Bbrb = self.subsession.Bbrb
        # Bbbr = self.subsession.Bbbr
        # Bbbb = self.subsession.Bbbb
        #
        # rrr = Rrrr + Brrr
        # rrb = Rrrb + Brrb
        # rbr = Rrbr + Brbr
        # brr = Rbrr + Bbrr
        # rbb = Rrbb + Brbb
        # brb = Rbrb + Bbrb
        # bbr = Rbbr + Bbbr
        # bbb = Rbbb + Bbbb

        # table 2 variables given s1,s2 = rr

        # Rrr_rr = self.subsession.Rrr_rr
        # Rrb_rr = self.subsession.Rrb_rr
        # Rbr_rr = self.subsession.Rbr_rr
        # Rbb_rr = self.subsession.Rbb_rr
        #
        # Brr_rr = self.subsession.Brr_rr
        # Brb_rr = self.subsession.Brb_rr
        # Bbr_rr = self.subsession.Bbr_rr
        # Bbb_rr = self.subsession.Bbb_rr
        #
        # # total signal combos for s3 s4 given s1,s2 = rr
        #
        # rr_rr = Rrr_rr + Brr_rr
        # rb_rr = Rrb_rr + Brb_rr
        # br_rr = Rbr_rr + Bbr_rr
        # bb_rr = Rbb_rr + Bbb_rr
        #
        # # table 2 variables given s1,s2 = rb
        #
        # Rrr_rb = self.subsession.Rrr_rb
        # Rrb_rb = self.subsession.Rrb_rb
        # Rbr_rb = self.subsession.Rbr_rb
        # Rbb_rb = self.subsession.Rbb_rb
        #
        # Brr_rb = self.subsession.Brr_rb
        # Brb_rb = self.subsession.Brb_rb
        # Bbr_rb = self.subsession.Bbr_rb
        # Bbb_rb = self.subsession.Bbb_rb
        #
        # # total signal combos for s3 s4 given s1,s2 = rb
        #
        # rr_rb = Rrr_rb + Brr_rb
        # rb_rb = Rrb_rb + Brb_rb
        # br_rb = Rbr_rb + Bbr_rb
        # bb_rb = Rbb_rb + Bbb_rb
        #
        # # table 2 variables given s1,s2 = br
        #
        # Rrr_br = self.subsession.Rrr_br
        # Rrb_br = self.subsession.Rrb_br
        # Rbr_br = self.subsession.Rbr_br
        # Rbb_br = self.subsession.Rbb_br
        #
        # Brr_br = self.subsession.Brr_br
        # Brb_br = self.subsession.Brb_br
        # Bbr_br = self.subsession.Bbr_br
        # Bbb_br = self.subsession.Bbb_br
        #
        # # total signal combos for s3 s4 given s1,s2 = br
        #
        # rr_br = Rrr_br + Brr_br
        # rb_br = Rrb_br + Brb_br
        # br_br = Rbr_br + Bbr_br
        # bb_br = Rbb_br + Bbb_br
        #
        # # table 2 variables given s1,s2 = bb
        #
        # Rrr_bb = self.subsession.Rrr_bb
        # Rrb_bb = self.subsession.Rrb_bb
        # Rbr_bb = self.subsession.Rbr_bb
        # Rbb_bb = self.subsession.Rbb_bb
        #
        # Brr_bb = self.subsession.Brr_bb
        # Brb_bb = self.subsession.Brb_bb
        # Bbr_bb = self.subsession.Bbr_bb
        # Bbb_bb = self.subsession.Bbb_bb
        #
        # # total signal combos for s3 s4 given s1,s2 = bb
        #
        # rr_bb = Rrr_bb + Brr_bb
        # rb_bb = Rrb_bb + Brb_bb
        # br_bb = Rbr_bb + Bbr_bb
        # bb_bb = Rbb_bb + Bbb_bb


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
            rrr=rrr,
            rrb=rrb,
            rbr=rbr,
            brr=brr,
            rbb=rbb,
            brb=brb,
            bbr=bbr,
            bbb=bbb,
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
            # Rrr_rr=Rrr_rr,
            # Rrb_rr=Rrb_rr,
            # Rbr_rr=Rbr_rr,
            # Rbb_rr=Rbb_rr,
            # Brr_rr=Brr_rr,
            # Brb_rr=Brb_rr,
            # Bbr_rr=Bbr_rr,
            # Bbb_rr=Bbb_rr,
            # Rrr_rb=Rrr_rb,
            # Rrb_rb=Rrb_rb,
            # Rbr_rb=Rbr_rb,
            # Rbb_rb=Rbb_rb,
            # Brr_rb=Brr_rb,
            # Brb_rb=Brb_rb,
            # Bbr_rb=Bbr_rb,
            # Bbb_rb=Bbb_rb,
            # Rrr_br=Rrr_br,
            # Rrb_br=Rrb_br,
            # Rbr_br=Rbr_br,
            # Rbb_br=Rbb_br,
            # Brr_br=Brr_br,
            # Brb_br=Brb_br,
            # Bbr_br=Bbr_br,
            # Bbb_br=Bbb_br,
            # Rrr_bb=Rrr_bb,
            # Rrb_bb=Rrb_bb,
            # Rbr_bb=Rbr_bb,
            # Rbb_bb=Rbb_bb,
            # Brr_bb=Brr_bb,
            # Brb_bb=Brb_bb,
            # Bbr_bb=Bbr_bb,
            # Bbb_bb=Bbb_bb,
            # rr_rr = rr_rr,
            # rb_rr = rb_rr,
            # br_rr = br_rr,
            # bb_rr = bb_rr,
            # rr_rb = rr_rb,
            # rb_rb = rb_rb,
            # br_rb = br_rb,
            # bb_rb = bb_rb,
            # rr_br = rr_br,
            # rb_br = rb_br,
            # br_br = br_br,
            # bb_br = bb_br,
            # rr_bb = rr_bb,
            # rb_bb = rb_bb,
            # br_bb = br_bb,
            # bb_bb = bb_bb,
        )

class Payment_Calculation(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.random_round1 = random.randint(1, 60)
        self.player.random_round2 = random.randint(1, 60)
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
