from mimesis import Address
from mimesis import Generic
from mimesis import Person
from mimesis import Text


class BaseGenerator(object):
    person = Person('en')
    text = Text('en')
    generic = Generic('en')
    address = Address('en')
    data = set()

    def get_primary_key_data(self, num):
        raise NotImplementedError("Необходимо переопределить метод")

    def get_params(self):
        raise NotImplementedError("Необходимо переопределить метод")

    def clear_data(self):
        if len(self.data) != 0:
            self.data.clear()
