import speech_recognition as sr

def listen_sentence_from_mic(recognizer, microphone):
    # Check if instances are from correct class
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    
    # Record audio from default microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Create response for easy debugging
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # Tries to extract text from audio
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "Could not connect with API."
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Could not understand the instruction."

    return response