import random, os
from random import randrange
from datetime import datetime, timedelta

current_dir = os.path.dirname(os.path.abspath(__file__))

class RandomEntityGenerator:
    def __init__(self):
        self.data = []

    def __random_line_from_file(self, afile, default=None):
        line = default
        afile.seek(0)
        for i, aline in enumerate(afile, start=1):
            if randrange(i) == 0:  # random int [0..i)
                line = aline
        return line.rstrip()

    def __random_num_string(self):
        r_num = random.randint(1, 9999)
        return f'{r_num:04}'

    def random_person(self):
        data_path = os.path.join(current_dir, "generators_data/person-names.txt")
        personNames = open(data_path, "r", encoding='utf-8')
        pName = self.__random_line_from_file(personNames).rstrip()
        pPhone = f'{self.__random_num_string()}-{self.__random_num_string()}{self.__random_num_string()}'
        return_val = f'{pName}\n{pPhone}'
        personNames.close()
        return return_val


    def random_address(self):
        data_path = os.path.join(current_dir, "generators_data/country-names.txt")
        country_names = open(data_path, "r", encoding='utf-8')
        data_path = os.path.join(current_dir, "generators_data/city-names.txt")
        city_names = open(data_path, "r", encoding='utf-8')
        data_path = os.path.join(current_dir, "generators_data/street-names.txt")
        street_names = open(data_path, "r", encoding='utf-8')

        addr_num = random.randint(1, 3999)
        addr_country = self.__random_line_from_file(country_names).rstrip()
        addr_city = self.__random_line_from_file(city_names).rstrip()
        addr_street = self.__random_line_from_file(street_names).rstrip()
        addr_phone = f'{self.__random_num_string()}-{self.__random_num_string()}{self.__random_num_string()}'
        random_address = f'{addr_num} {addr_street}\n{addr_city}, {addr_country}\n{addr_phone}'

        country_names.close()
        city_names.close()
        street_names.close()
        return random_address

    def random_datetime(self, start_date, end_date):
        """
        This function will return a random datetime between two datetime 
        objects.
        """
        delta = end_date - start_date
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start_date + timedelta(seconds=random_second)

    def random_business_name(self):
        data_path = os.path.join(current_dir, "generators_data/business-names.txt")
        businessNames = open(data_path, "r", encoding='utf-8')
        return_val = self.__random_line_from_file(businessNames)
        businessNames.close()
        return return_val

    def random_business_industries(self, num_industries):
        data_path = os.path.join(current_dir, "generators_data/business-industry-list.txt")
        business_industries = open(data_path, "r", encoding='utf-8')
        bus_industries = ''
        for x in range(num_industries):
            bus_industries += f'- {self.__random_line_from_file(business_industries).rstrip()}\n'
        return_val = f'{bus_industries}\n'
        business_industries.close()
        return return_val

    def random_music_genres(self, num_genres):
        data_path = os.path.join(current_dir, "generators_data/genre-list.txt")
        genre_list = open(data_path, "r", encoding='utf-8')
        mus_genres = ''
        for x in range(num_genres):
            mus_genres += f'- {self.__random_line_from_file(genre_list).rstrip()}\n'
        return_val = f'{mus_genres}\n'
        genre_list.close()
        return return_val

    def random_music_act(self):
        m_genres = self.random_music_genres(3)

        data_path = os.path.join(current_dir, "generators_data/band-names.txt")
        band_names = open(data_path, "r", encoding='utf-8')

        band_name = self.__random_line_from_file(band_names)
        label_name = self.__random_line_from_file(band_names)

        band_names.close()
        return f'ARTIST(S): {band_name}\nGENRES: {m_genres}\nLABEL: {label_name}'

    def random_music_album(self, num_tracks):
        random_act = self.random_music_act()

        data_path = os.path.join(current_dir, "generators_data/band-names.txt")
        band_names = open(data_path, "r", encoding='utf-8')
        band_name = self.__random_line_from_file(band_names)

        tracklist_str = 'TRACKLIST:\n'
        for x in range(num_tracks):
            track_name = self.__random_line_from_file(band_names)
            track_num = x + 1
            track_minutes = random.randint(0,8)
            track_secs = random.randint(0,59)
            
            tracklist_str += f'{track_num:02} - {track_name} ({track_minutes}:{track_secs:02})\n'

        band_names.close()

        return f'{random_act}\n{tracklist_str}'

    def random_music_tour(self, num_stops):
        # tNames = random_line(bandNames).rstrip()
        # tNames += f' -OR- {random_line(albumNames).rstrip()}'
        # loopStr += f'\nTOUR NAME:\n{tNames}\n'

        # loopStr += '\nTOUR STOPS: \n'
        # numCities = random.randint(6,20)
        # tourStart = datetime.strptime('1/1/2032 1:30 PM', '%m/%d/%Y %I:%M %p')
        # tourEnd = datetime.strptime('12/30/2099 4:50 AM', '%m/%d/%Y %I:%M %p')

        # for x in range(numCities):
        #     cityNames.seek(0)
        #     countryNames.seek(0)
        #     eventDay = random_date(tourStart, tourEnd).strftime("%b %d, %Y")
        #     loopStr += f'{eventDay} - {random_line(cityNames).rstrip()}, {random_line(countryNames).rstrip()}\n'
        return None
