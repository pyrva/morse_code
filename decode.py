import wave

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    "!": "-.-.--",
    " ": "/",
}

# Decode the morse code to text

with wave.open("morse.wav", "rb") as f:
    frames = f.readframes(f.getnframes())
    # what is frames?

    values = [bool(f - 128) for f in frames]

    signals = []
    current = values[0]
    count = 0

    for v in values:
        if v == current:
            count += 1
        else:
            if count > 5:
                signals.append((current, count))
            count = 0
            current = v

    print(signals)

    def get_char(on, duration):
        if duration > 1600:
            return " / "
        elif duration > 500:
            if on:
                return "-"
            else:
                return " "
        elif on:
            return "."

    morse = [get_char(*s) for s in signals]


    morse_characters = "".join(morse).split()

    reversed_dict = {v: k for k, v in morse_code.items()}

    print(''.join(reversed_dict.get(char) for char in morse_characters))
