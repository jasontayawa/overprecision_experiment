from os import environ

#add 'consent' app in the app sequence for the real experiment
SESSION_CONFIGS = [
    dict(
       name='p55l50',
       display_name="Belief updating 1",
       num_demo_participants=1,
       app_sequence=['consent',
                     'instructions_p55l50',
                     'p55l50',
                     'questionnaire_p55l50',
                     'payment',]
    ),
    dict(
       name='p70l50',
       display_name="Belief updating 2",
       num_demo_participants=1,
       app_sequence=['consent',
                     'instructions_p70l50',
                     'p70l50',
                     'questionnaire_p70l50',
                     'payment',]
    ),
    dict(
       name='p55l50_reverse',
       display_name="Belief updating 3",
       num_demo_participants=1,
       app_sequence=['consent',
                     'instructions_p55l50_reverse',
                     'p55l50_reverse',
                     'questionnaire_p55l50_reverse',
                     'payment',]
    ),
    # dict(
    #    name='rounds',
    #    display_name="rounds",
    #    num_demo_participants=1,
    #    app_sequence=['p55l50',]
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=2.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ_lab',
        display_name='OSU Experimental Economics Lab',
        #participant_label_file='_rooms/econ_lab.txt',
        #use_secure_urls=True
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '(=kono+@!(=o#+hsyf$*+!fp=%)s55nz)lm#ty@=-_vrw1+560'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
