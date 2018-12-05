import threading
import voice
import client_socket as csocket
from time import sleep

# Showing first instructions
print(voice.get_options())

# Listening from microphone
sentence = voice.listen_sentence_from_mic(voice.recognizer, voice.microphone)

# Checking for errors
while sentence["error"]:
    sleep(3)
    print("ERROR: {}".format(sentence["error"]))
    print("Say something: ")
    sentence = voice.listen_sentence_from_mic(voice.recognizer, voice.microphone)

# Print sentence
print("Your command was: {}".format(sentence["transcription"]))

csocket.send_command(sentence["transcription"].encode())