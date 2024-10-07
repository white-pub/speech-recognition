# Speech Recognition System
# Anna Chen
# 9/16/2024
#
# This is a speech recognition system that utilizes the 
# SpeechRecognition and PyAudiowith library.


# Import needed library
import speech_recognition as sr

# Create a recognizer instance (Initialization)
recognizer = sr.Recognizer()


def capture_voice_input():
    """ Capture voice input from user microphone. """

    # Set microphone as input source
    with sr.Microphone() as source:

        # Prompt to indicate that system is running
        print("Listening...")
        audio = recognizer.listen(source)
    
    return audio



def convert_voice_to_text(audio):
    """ Convert voice to text. """
    
    try:

        # Select Google Web Speech API. Requires internet to run.
        text = recognizer.recognize_google(audio)
        print("You said: " + text)

    # If the recognizer could not understand input
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")

    # Handle request errors
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text


def process_voice_command(text):
    """ Process voice command. """

    if "hello" in text.lower():
        print("Hello! How can I help you?")

    elif "goodbye" in text.lower():
        print("Goodbye! Have a great day!")
        return True

    else:
        print("I didn't understand that command. Please try again.")
    return False



def main():
    """ Run speech recognition system. """

    # Set flag so the system default is keep working
    end_program = False
    
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)


if __name__ == '__main__':
    main()