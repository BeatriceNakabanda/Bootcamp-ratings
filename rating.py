ratings = {
    '-2':'Very un satisfied',
    '-1': 'Un satisfied',
    '0': 'Neutral',
    '1':  'Satisfied',
    '2': 'Very Satisfied'
}
scores = []
users = []
class Ratings:
    def __init__(self, lfa, candidate, rating_value):
        self.lfa = lfa
        self.candidate = candidate
        self.rating_value = rating_value

    def perform_rating(self, lfa, candidate, value):
        
        rating = dict(
            lfa=self.lfa,
            candidate=self.candidate
            value=ratings.get(value)
        )

        if users:
            for user in users:
                if user.get('role') == 'lfa' and value == rating[value]:
                    scores.append(rating)
                    message = "Successfully rated"
                else:
                    message = "Cannot rate the candidate"
        return message

rating = Ratings('tom', 'armstrong', '-2' )



