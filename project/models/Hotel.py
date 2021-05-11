class Hotel(object):

    def __init__(self):
        self.num_of_reviews = 0
        self.avg_rating = {}
        self.name = ''
        self.price = ''
        self.address = ''
        # self.city = ''
        # self.state = ''
        self.us = 0
        self.id = ''
        # self.comment = []
        # self.key_words = {'service':'Service','clean':'Cleanliness','overall':'Overall','value':'Value','sleep quality':'Sleep Quality','room':'Rooms','location':'Location','internet':'Business service (e.g., internet access)','check in':'Check in / front desk'}

    def __str__(self):
        return '{:40s}, Universal Score: {:.2f} '.format(self.name, self.us)

    def __repr__(self):
        return '\n{}'.format(str(self))
