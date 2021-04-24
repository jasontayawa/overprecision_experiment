from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import pandas as pd


class Guess1(Page):
    form_model = 'player'
    form_fields = ['guess1',
                   'check_slider_one']

    def error_message(self, values):
        print('values is', values)
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
        print('values is', values)
        if values['check_slider_two'] == None:
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

        # total signal combos for s1 s2 s3
        rrr = Rrrr + Brrr
        rrb = Rrrb + Brrb
        rbr = Rrbr + Brbr
        brr = Rbrr + Bbrr
        rbb = Rrbb + Brbb
        brb = Rbrb + Bbrb
        bbr = Rbbr + Bbbr
        bbb = Rbbb + Bbbb

        # table 2 variables given s1,s2 = rr

        Rrr_rr = self.subsession.Rrr_rr
        Rrb_rr = self.subsession.Rrb_rr
        Rbr_rr = self.subsession.Rbr_rr
        Rbb_rr = self.subsession.Rbb_rr

        Brr_rr = self.subsession.Brr_rr
        Brb_rr = self.subsession.Brb_rr
        Bbr_rr = self.subsession.Bbr_rr
        Bbb_rr = self.subsession.Bbb_rr

        # total signal combos for s3 s4 given s1,s2 = rr

        rr_rr = Rrr_rr + Brr_rr
        rb_rr = Rrb_rr + Brb_rr
        br_rr = Rbr_rr + Bbr_rr
        bb_rr = Rbb_rr + Bbb_rr

        # table 2 variables given s1,s2 = rb

        Rrr_rb = self.subsession.Rrr_rb
        Rrb_rb = self.subsession.Rrb_rb
        Rbr_rb = self.subsession.Rbr_rb
        Rbb_rb = self.subsession.Rbb_rb

        Brr_rb = self.subsession.Brr_rb
        Brb_rb = self.subsession.Brb_rb
        Bbr_rb = self.subsession.Bbr_rb
        Bbb_rb = self.subsession.Bbb_rb

        # total signal combos for s3 s4 given s1,s2 = rb

        rr_rb = Rrr_rb + Brr_rb
        rb_rb = Rrb_rb + Brb_rb
        br_rb = Rbr_rb + Bbr_rb
        bb_rb = Rbb_rb + Bbb_rb

        # table 2 variables given s1,s2 = br

        Rrr_br = self.subsession.Rrr_br
        Rrb_br = self.subsession.Rrb_br
        Rbr_br = self.subsession.Rbr_br
        Rbb_br = self.subsession.Rbb_br

        Brr_br = self.subsession.Brr_br
        Brb_br = self.subsession.Brb_br
        Bbr_br = self.subsession.Bbr_br
        Bbb_br = self.subsession.Bbb_br

        # total signal combos for s3 s4 given s1,s2 = br

        rr_br = Rrr_br + Brr_br
        rb_br = Rrb_br + Brb_br
        br_br = Rbr_br + Bbr_br
        bb_br = Rbb_br + Bbb_br

        # table 2 variables given s1,s2 = bb

        Rrr_bb = self.subsession.Rrr_bb
        Rrb_bb = self.subsession.Rrb_bb
        Rbr_bb = self.subsession.Rbr_bb
        Rbb_bb = self.subsession.Rbb_bb

        Brr_bb = self.subsession.Brr_bb
        Brb_bb = self.subsession.Brb_bb
        Bbr_bb = self.subsession.Bbr_bb
        Bbb_bb = self.subsession.Bbb_bb

        # total signal combos for s3 s4 given s1,s2 = bb

        rr_bb = Rrr_bb + Brr_bb
        rb_bb = Rrb_bb + Brb_bb
        br_bb = Rbr_bb + Bbr_bb
        bb_bb = Rbb_bb + Bbb_bb


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
            Rrr_rr=Rrr_rr,
            Rrb_rr=Rrb_rr,
            Rbr_rr=Rbr_rr,
            Rbb_rr=Rbb_rr,
            Brr_rr=Brr_rr,
            Brb_rr=Brb_rr,
            Bbr_rr=Bbr_rr,
            Bbb_rr=Bbb_rr,
            Rrr_rb=Rrr_rb,
            Rrb_rb=Rrb_rb,
            Rbr_rb=Rbr_rb,
            Rbb_rb=Rbb_rb,
            Brr_rb=Brr_rb,
            Brb_rb=Brb_rb,
            Bbr_rb=Bbr_rb,
            Bbb_rb=Bbb_rb,
            Rrr_br=Rrr_br,
            Rrb_br=Rrb_br,
            Rbr_br=Rbr_br,
            Rbb_br=Rbb_br,
            Brr_br=Brr_br,
            Brb_br=Brb_br,
            Bbr_br=Bbr_br,
            Bbb_br=Bbb_br,
            Rrr_bb=Rrr_bb,
            Rrb_bb=Rrb_bb,
            Rbr_bb=Rbr_bb,
            Rbb_bb=Rbb_bb,
            Brr_bb=Brr_bb,
            Brb_bb=Brb_bb,
            Bbr_bb=Bbr_bb,
            Bbb_bb=Bbb_bb,
            rr_rr = rr_rr,
            rb_rr = rb_rr,
            br_rr = br_rr,
            bb_rr = bb_rr,
            rr_rb = rr_rb,
            rb_rb = rb_rb,
            br_rb = br_rb,
            bb_rb = bb_rb,
            rr_br = rr_br,
            rb_br = rb_br,
            br_br = br_br,
            bb_br = bb_br,
            rr_bb = rr_bb,
            rb_bb = rb_bb,
            br_bb = br_bb,
            bb_bb = bb_bb,
        )

class ResultsWaitPage(WaitPage):

    body_text = 'Please wait while we determine your final payoff.'
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    after_all_players_arrive = 'profit_calculation'


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        guess1_random_y = self.player.y1
        guess1_random_x = self.player.x1
        guess2_random_y = self.player.y2
        guess2_random_x = self.player.x2

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
            guess1_random_y=guess1_random_y,
            guess1_random_x=guess1_random_x,
            selected_round_guess1=selected_round_guess1,
            color_guess1=color_guess1,
            guess1=guess1,
            guess2_random_y=guess2_random_y,
            guess2_random_x=guess2_random_x,
            selected_round_guess2=selected_round_guess2,
            color_guess2=color_guess2,
            guess2=guess2,
            payment=payment,
            y1=y1,
            y2=y2,
            x1=x1,
            x2=x2,

        )



page_sequence = [Guess1, Guess2, ResultsWaitPage, Results]
