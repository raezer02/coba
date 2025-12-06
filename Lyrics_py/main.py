import time
import os

lyrics = [

    ("Well this",0),
    ("December",1.05),
    ("I'll remember",2.25),
    ("Want you to see it when I do",3.25),
    ("ooh-ooh-ooh",5.6),
    ("God knows I do", 7.8),

    # ("Well, I'm alright if you're alright", 2.6),
    # ("And I'm okay if you're okay", 2.5),
    # ("It's this state, in this state I'm living in", 3.1),
    # ("It's just a little bit, it's just a little bit", 3.2),
    # ("Lonely in this home", 2.3),
    # ("It's always colder on your own", 2.7),
    # ("My darlin', I", 1.8),
    # ("I let the season change my mind", 2.8),

    # ("I'm alright if you're alright", 2.6),
    # ("I'm okay if you're okay", 2.5),
    # ("It's this state, in this state I'm living in", 3.0),
    # ("It's just a little bit, it's just a bit", 3.0),

    # ("Maybe, this December, I'll remember", 3.0),
    # ("Want you to see it when I do, ooh-ooh-ooh", 3.2),
    # ("God knows I do", 3.2),
]

os.system("clear||cls")

def type_effect(text, speed=0.08):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(speed)
    print()

start_time = time.time()
for line, lyrics_time in lyrics:
    while time.time() - start_time < lyrics_time:
        time.sleep(0.1)
    type_effect(line, speed=0.06)