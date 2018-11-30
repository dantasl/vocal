import speech_recognition as sr
import assets

if __name__ == "__main__":
    # List of sentences accepted
    SENTENCES = [
        "kitchen on", "kitchen off", "living room on", "living room off",
        "bathroom on", "bathroom off", "all on", "all off"
    ]
    
    # Create Recognizer and Mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Format the available options
    options = (
        "\nHouse Automaton actually supports those sentences:\n"
        "{sentences}\n"
    ).format(sentences=', \n'.join(SENTENCES))
    print(options)

    # Listening from microphone
    sentence = assets.listen_sentence_from_mic(recognizer, microphone)

    # Checking for errors
    while sentence["error"]:
        print("ERROR: {}".format(sentence["error"]))
        sentence = assets.listen_sentence_from_mic(recognizer, microphone)

    # Print sentence
    print("Your command was: {}".format(sentence["transcription"]))