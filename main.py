"""Colour cell asigner"""

import random
from datetime import datetime


class OpenElement:
    def __init__(self, top, bot):
        self._top = top
        self._bot = bot

    def __enter__(self):
        print(self._top)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(self._bot)


width = 5
height = 5
dimesions = width, height
p1 = 9
p2 = p1 - 1
omicorn = 1

tokens = ['\N{Microbe}', '\N{Syringe}']
random.shuffle(tokens)
p1_token, p2_token = tokens

null = width * height - p1 - p2 - omicorn

def compile_time():
    print(f'<b>Briefing Compiled: </b>{datetime.today().strftime("%A at %H:%M")}')

def starting_player():
    print(f'<b>Starting Player: </b>{p1_token}')



def code_generator():
    cards = ['<td class=\"table-danger\">'+ '<p class="text-center">' + p1_token +'</p>'] * p1 + ['<td class=\"table-primary\">' + '<p class="text-center">' + p2_token+ '</p>'] * p2 + ['<td class=\"table-dark\">' + '<p class="text-center">' + '<b>O</b>' + '</p>'] * omicorn + ['<td class=\"table-info\">' + '<p class="text-center">' + '\N{Face with Medical Mask}'+'</p>'] * null
    random.shuffle(cards)
    output = "<table id=\"content\" class=\"table\">\n" + "<tbody>\n"
    for i in range(0, len(cards), width):
        output += "<tr>\n"
        for j in range(width):
            output += f"{cards[i + j]}"
            output += "</td>\n"
        output += "</tr>\n"
    output += "</tbody>\n" + "</table>\n"
    with OpenElement('<div id="banner-top">', '</div>'):
        compile_time()
    print(output)
    with OpenElement('<div id="banner-bottom">', '</div>'):
        starting_player()