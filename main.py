"""Colour cell asigner"""

import random
from datetime import datetime

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
    print(f'<p class="text-monospace"><b>Last Run: </b>{datetime.today().strftime("%H:%M")}</p>')

def starting_player():
    print(f'<b>Starting Player: </b>{p1_token}')



def code_generator():
    cards = ['<td class=\"table-danger\">'+ '<p class="text-center">' + p1_token +'</p>'] * p1 + ['<td class=\"table-primary\">' + '<p class="text-center">' + p2_token+ '</p>'] * p2 + ['<td class=\"table-dark\">' + '<p class="text-center">' + '<b>O</b>' + '</p>'] * omicorn + ['<td class=\"table-info\">' + '<p class="text-center">' + '\N{Face with Medical Mask}'+'</p>'] * null
    random.shuffle(cards)
    output = "<table class=\"table\">\n" + "<tbody>\n"
    for i in range(0, len(cards), width):
        output += "<tr>\n"
        for j in range(width):
            output += f"{cards[i + j]}"
            output += "</td>\n"
        output += "</tr>\n"
    output += "</tbody>\n" + "</table>\n"
    print(output)
    # print('<br/>')
    starting_player()
    compile_time()
