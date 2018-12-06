import threading
import voice
from client_socket import ClientSocket
from time import sleep


HOST = "192.168.0.24"
PORT = 6002

def automaton(clientSocket):
    # Showing first instructions
    print(voice.get_options())

    # Listening from microphone
    sentence = voice.listen_sentence_from_mic(voice.recognizer, voice.microphone)

    # Checking for errors
    while sentence["error"]:
        print("ERROR: {}".format(sentence["error"]))
        print("Say something: ")
        sentence = voice.listen_sentence_from_mic(voice.recognizer, voice.microphone)

    # Print sentence
    print("Your command was: {}".format(sentence["transcription"]))

    clientSocket.send_command(sentence["transcription"].encode())


def voice_part(clientSocket):
    while True:
        try:
            text = input("\nHit ENTER for a new command.\nCTRL + C to quit.\n")
            if text == "":
                automaton(clientSocket)
        except (KeyboardInterrupt, SystemExit):
            print("\n\nYou've finished this program. Thanks for using it. ;)")
            break

clientSocket = ClientSocket(HOST, PORT)
automaton_thread = threading.Thread(target=voice_part, args=(clientSocket,))
checking_thread = threading.Thread(target=clientSocket.check_status)
automaton_thread.start()
checking_thread.start()