from pypresence import Presence

DEBUG = False


class PresenceWrapper:
    def __init__(self, client_id=None, game_database=None):
        self.client_id = client_id
        if client_id is None:
            print('[!] Invalid Client ID.')
            return
        self.client_instance = Presence(self.client_id)
        self.client_instance.connect()
        self.games_database = game_database
        if DEBUG:
            print(f'[DEBUG] {self.games_database}')

    def set_game(self, game_id=None):
        if game_id is None or game_id not in self.games_database:
            print('[!] Invalid Game ID.')
            return
        game = self.games_database[game_id]
        self.client_instance.update(details=game['title'], state=game['description'], small_image=game['image_code'],
                                    large_image=game['image_code'])
        if DEBUG:
            print(
                f'[DEBUG] Setting RPC to values: GAME/DETAILS -> {game["title"]} | STATE/DESCRIPTION -> {game["description"]} | IMAGES -> {game["image_code"]} ')
