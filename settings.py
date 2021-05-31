from os import environ

#add 'consent' app in the app sequence for the real experiment
SESSION_CONFIGS = [
    dict(
       name='overprecision',
       display_name="Belief updating",
       num_demo_participants=1,
       app_sequence=['consent',
                     'instructions',
                     'block1',
                     'questionnaire',
                     'payment',]
    # ),
    # dict(
    #    name='questionnaire',
    #    display_name="questionnaire",
    #    num_demo_participants=1,
    #    app_sequence=['questionnaire',]
    # ),
    # dict(
    #    name='rounds',
    #    display_name="rounds",
    #    num_demo_participants=1,
    #    app_sequence=['block1',]
    ),
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
