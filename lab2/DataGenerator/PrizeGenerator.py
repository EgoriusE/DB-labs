from BaseGenerator import BaseGenerator

class PrizeGenerator(BaseGenerator):

    def get_params(self):
        prize = {
            'name': self.person.last_name(),
            'year': self.generic.datetime.year(),
            'description': self.text.text(quantity=1)
        }
        return prize

    def get_primary_key_data(self, num):
        return range(0, num - 1)
