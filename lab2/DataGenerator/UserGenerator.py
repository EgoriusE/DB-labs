from BaseGenerator import BaseGenerator


class UserGenerator(BaseGenerator):

    def get_params(self):
        user = {
            'name': self.person.name(),
            'icon_path': self.person.age(),
            'password': self.person.password()
        }
        return user

    def get_primary_key_data(self, num):
        self.clear_data()
        while num != 0:
            email = self.person.email()

            if not (email in self.data):
                self.data.add(self.person.email())
                num = num - 1
