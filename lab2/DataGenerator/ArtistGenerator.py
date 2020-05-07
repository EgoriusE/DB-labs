from BaseGenerator import BaseGenerator
import random
from Utils import open_connection, close_connection


class ArtistGenerator(BaseGenerator):

    def get_params(self):
        artist = {
            'country': self.address.calling_code(),
            'icon_path': self.generic.path.project_dir(),
            'desc': self.text.sentence()
        }
        # if bool(random.getrandbits(1)):
        #     cursor, conn = open_connection()
        #     cursor.execute('SELECT name FROM "group" ORDER BY RANDOM() LIMIT 1;')
        #     group_name = cursor.fetchone()
        #     close_connection(cursor, conn)
        #     artist.update({'group': group_name[0]})
        # else:
        #     artist.update({'group': None})
        print(artist)
        return artist

    def get_primary_key_data(self, num):
        self.clear_data()
        while num != 0:
            name = self.generic.numbers.float_number()
            if not (name in self.data):
                self.data.add(name)
                num = num - 1
