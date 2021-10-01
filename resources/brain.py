from dict import morse_dict
from playsound import playsound


class Brain:
    def __init__(self):
        self.play_sound = None

    def set_sound_option(self, answer):
        """To set the play_sound variable to either True of False depending on the parameter passed."""

        if answer.upper() == "Y":
            self.play_sound = True
        elif answer.upper() == "N":
            self.play_sound = False
        else:
            print("Invalid sound option.")

    def convert_to_morse(self, string):
        """Converts a string to morse code"""

        morse_text = ""
        for letter in string.upper():
            if letter in morse_dict:
                morse_text += morse_dict[letter]
                morse_text += " "
                if self.play_sound:
                    self.play(letter)

            else:
                morse_text += letter
                morse_text += " "

        return morse_text

    def convert_to_english(self, morse_string):
        """Converts morse code back to english"""
        morse_words_to_look_up = morse_string.split(" ")
        translated_answer = ""
        key_values = list(morse_dict.keys())
        dict_values = list(morse_dict.values())

        for word in morse_words_to_look_up:
            try:
                value_to_look_up = dict_values.index(word)
            except ValueError:
                translated_answer += " "
            else:
                translated_answer += key_values[value_to_look_up]

        output_words_array = translated_answer.split(" ")

        english_text = ""
        formatted_words_array = [output_words_array[0].title()]

        for word in output_words_array[1:]:
            formatted_words_array.append(word.lower())

        for word in formatted_words_array:
            english_text += word
            english_text += " "

        return english_text[:-1]

    def play(self, letter):
        """Plays the corresponding morse sound for the letter passed"""

        if letter == ":":
            playsound("./audio/Morse_Code_-_Colon.ogg.mp3")
        elif letter == "?":
            playsound("./audio/Morse_Code_Question_Mark.ogg.mp3")
        elif letter == '"':
            playsound("./audio/Morse_Code_Quotation_Mark.ogg.mp3")
        elif letter == "/":
            playsound("./audio/Morse_Code_-_Slash.ogg.mp3")
        else:
            playsound(f"./audio/{letter}_morse_code.ogg.mp3")