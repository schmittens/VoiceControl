from src import voice as voice

sample = [
    "turn the light on",
    "turn on the light",
    "switch the light on",
    "switch on the light",
    "put the light on",
    "put on the light",
    "turn the light off",
    "turn off the light",
    "switch the light off",
    "switch off the light",
    "put the light out",
    "put out the light",
    "turn on the lights",
    "turn the lights off",
    "turn off the lights",
    "turn off the light right now",
    "turn off the lamp",
    "turn off the spotlight",
    "turn off the illumination"
]

keyphrase = "Jarvis"
languages = ["en-US"]

#r = voice.callibration()

#voice.backgroundRecognition(keyphrase)

from src.voice.voice import Voice
from src.parse.parse import Parse

#voice = Voice()

#voice.backgroundrecognition()

#callback to activate parsing if voice.query gets updated


for query in sample:
    print("----------------")
    parse = Parse(query)

    # extract verb and particle (action), noun (object)
    #parse.verbphrase()


    print("----------------")
