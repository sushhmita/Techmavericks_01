import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set TTS engine properties
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to convert text to speech
def live_text_to_speech():
    print("Live Text-to-Speech is active. Type your text and press Enter (type 'exit' to quit).")

    while True:
        # Get user input
        text = input("Enter text: ")
        
        # Check if the user wants to exit
        if text.lower() == 'exit':
            print("Exiting Live Text-to-Speech...")
            break

        # Speak the entered text
        engine.say(text)
        engine.runAndWait()  # Wait until the speech is finished

# Run the live TTS function
live_text_to_speech()

# Initialize the TTS engine
engine = pyttsx3.init()

# Set TTS engine properties
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to convert text to speech
def live_text_to_speech():
    print("Live Text-to-Speech is active. Type your text and press Enter (type 'exit' to quit).")

    while True:
        # Get user input
        text = input("Enter text: ")
        
        # Check if the user wants to exit
        if text.lower() == 'exit':
            print("Exiting Live Text-to-Speech...")
            break

        # Speak the entered text
        engine.say(text)
        engine.runAndWait()  # Wait until the speech is finished

# Run the live TTS function
live_text_to_speech()
