import pyfiglet


class Alerts:
    def title(self, msg):
        text = msg
        ascii_art = pyfiglet.figlet_format(text, font="standard")
        return print(ascii_art)
    