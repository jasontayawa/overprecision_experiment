from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire_p70'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Variables for Experience Questions
    understanding = models.BooleanField(label="Were you able to understand the structure of this Experiment?",
                                        choices=[
                                            [True, 'Yes'], [False, 'No']
                                        ],
                                        widget=widgets.RadioSelect)
    confusion = models.LongStringField(label="Were there any sources of confusion, for you, in this Experiment?")
    decision1 = models.IntegerField(label="If the 1st and 2nd signals are Red while the 3rd and 4th signals are Blue, which color is more likely to be assigned for the round?",
                                 choices=[
                                     [1, 'Red'], [2, 'Blue'], [3, 'Both equally likely']
                                 ],
                                 widget=widgets.RadioSelect)
    decision2 = models.IntegerField(label="If the 1st, 2nd, and 3rd signals are Red while the 4th signal is Blue, which color is more likely to be assigned for the round?",
                                 choices=[
                                     [1, 'Red'], [2, 'Blue'], [3, 'Both equally likely']
                                 ],
                                 widget=widgets.RadioSelect)
    decision3 = models.IntegerField(label="If the 1st and 3rd signals are Red while the and 2nd and 4th signals are Blue, which color is more likely to be assigned for the round?",
                                 choices=[
                                     [1, 'Red'], [2, 'Blue'], [3, 'Both equally likely']
                                 ],
                                 widget=widgets.RadioSelect)



    # Variables for demographics
    age = models.IntegerField(label="What is your age (in years)?")
    gender = models.IntegerField(label="What is your gender?",
                                 choices=[
                                     [1, 'Male'], [2, 'Female'], [3, 'Non-binary']
                                 ],
                                 widget=widgets.RadioSelect)
    major = models.StringField(label='What is your major?')
    educ_year = models.IntegerField(label='What year of college are you in?',
                                    choices=[
                                        [1, 'Freshman'], [2, 'Sophomore'], [3, 'Junior'],
                                        [4, 'Senior'], [5, 'Graduate Student'], [6, 'Not Applicable/Graduated']
                                    ],
                                    widget=widgets.RadioSelect)
    past_experiments = models.BooleanField(label='Have you taken part in previous Economics Experiments?',
                                           choices = [
                                               [False, 'No'], [True, 'Yes']
                                           ],
                                           widget=widgets.RadioSelect)
    game_theory = models.BooleanField(label='Have you taken a course in Statistics?',
                                      choices=[
                                          [False, 'No'], [True, 'Yes']
                                      ],
                                      widget=widgets.RadioSelect)

    experiment = models.BooleanField(label='Have you taken a course in Experimental Economics?',
                                     choices=[
                                         [False, 'No'], [True, 'Yes']
                                     ],
                                     widget=widgets.RadioSelect
                                     )