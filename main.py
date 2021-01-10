import json
import tkinter as tk

from PresenceWrapper import PresenceWrapper

CLIENT_ID = '592453503377604610'
GAMES_DATABASE = []

def load_database():
    with open('database.json') as json_file:
        data = json.load(json_file)
    return data["games"]


def load_title_list_from_database():
    title_list = []
    for game in GAMES_DATABASE:
        title_list.append(GAMES_DATABASE[game]['title'])
    return title_list


class AGSRPCApplication(tk.Frame):
    def __init__(self, master=None, title_list=None, presence=None):
        super().__init__(master)
        self.master = master
        self.title_list = title_list
        self.presence = presence
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("ActuallyGoodSwitchRPC")
        self.game_option_string = tk.StringVar(self.master)
        self.game_option_string.set(self.title_list[0])  # default value
        self.game_option_menu = tk.OptionMenu(self.master, self.game_option_string, *self.title_list)
        self.game_option_menu.pack()
        self.set_game_btn = tk.Button(self)
        self.set_game_btn["text"] = "Set Game"
        self.set_game_btn["command"] = self.set_game_callback
        self.set_game_btn.pack()

    def set_game_callback(self):
        selected_game = self.game_option_string.get()
        self.presence.set_game(game_id=selected_game)


if __name__ == '__main__':
    GAMES_DATABASE = load_database()
    title_list = load_title_list_from_database()
    presence = PresenceWrapper(client_id=CLIENT_ID, game_database=GAMES_DATABASE)
    root_gui = tk.Tk()
    root_gui.geometry('600x200')
    root_app = AGSRPCApplication(master=root_gui, title_list=title_list, presence=presence)
    root_app.mainloop()
