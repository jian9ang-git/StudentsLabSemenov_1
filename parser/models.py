class GoalPost:
    def __init__(self, post_id='', post_id_html='', post_url='', username='', user_karma='', user_cake_day='',
                 post_category='', post_karma='', post_date='', num_comments='', num_votes=''):
        self.post_id = post_id
        self.post_id_html = post_id_html
        self.post_url = post_url
        self.username = username
        self.user_karma = user_karma
        self.user_cake_day = user_cake_day
        self.post_category = post_category
        self.post_karma = post_karma
        self.post_date = post_date
        self.num_comments = num_comments
        self.num_votes = num_votes

    def __str__(self):
        return f'{self.post_id};{self.post_url};{self.username};{self.user_karma};{self.user_cake_day};' \
               f'{self.post_category};{self.post_karma};{self.post_date};{self.num_comments};{self.num_votes}'
