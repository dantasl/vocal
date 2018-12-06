import threading
import voice
from client_socket import ClientSocket


def automaton(clientsocket):
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

    clientsocket.send_command(sentence["transcription"].encode())


def voice_part(clientsocket):
    while True:
        try:
            text = input("\nHit ENTER for a new command.\nCTRL + C to quit.\n")
            if text == "":
                automaton(clientsocket)
        except (KeyboardInterrupt, SystemExit):
            print("\n\nYou've finished this program. Thanks for using it. ;)")
            break


if __name__ == "__main__":
    host = "192.168.0.24"
    port = 6002
    client_socket = ClientSocket(host, port)
    automaton_thread = threading.Thread(target=voice_part, args=(client_socket,))
    checking_thread = threading.Thread(target=client_socket.check_status)
    automaton_thread.start()
    checking_thread.start()
