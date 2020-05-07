from BaseGenerator import BaseGenerator


class AlbumGenerator(BaseGenerator):

    def get_params(self):
        album = {
            'name': self.person.last_name(),
            'year': self.generic.datetime.year(),
            'duration': self.generic.datetime.time(),
            'quantity': self.generic.numbers.integer_number(start=0, end=100),
            'icon_path': self.generic.path.project_dir()
        }
        return album

    def get_primary_key_data(self, num):
        return range(0, num - 1)
