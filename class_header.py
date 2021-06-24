import random
from for_headers import USER_AGENT, ACCEPT, ACCEPT_ENCODING, CACHE_CONTROL, REFERRER, SCREEN_RES


class Header:
    referrer = REFERRER

    screen_resolution = SCREEN_RES

    def generate_header_list(self, num: int) -> list:
        """generate list of headers"""
        headers = []
        for i in range(0, num):
            header = {
                'accept': random.choice(ACCEPT),
                'accept-encoding': random.choice(ACCEPT_ENCODING),
                'cache-control': random.choice(CACHE_CONTROL),
                'connection': 'keep-alive',
                'referer': f'https://{random.choice(Header.referrer)}/',
                'upgrade-insecure-requests': '1',
                'user-agent': random.choice(USER_AGENT),
            }
            headers.append(header)
        return headers

    def change_referrer(self, new=None, expand=None):
        """URLs separated by comma"""
        if new != None:
            Header.referrer = new.replace(' ', '').split(',')

        if expand != None:
            referrers = expand.replace(' ', '').split(',')
            for ref in referrers:
                Header.referrer.append(ref)

    def show_header_data(self, key: str):
        """referrer, cache_control, accept, accept_encoding, user_agent"""
        files = {
            'user_agent': USER_AGENT,
            'accept': ACCEPT,
            'accept_encoding': ACCEPT_ENCODING,
            'cache_control': CACHE_CONTROL,
            'referrer': Header.referrer
        }

        print(files[key])
