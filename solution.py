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
    "\"": ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    "!": "-.-.--",
    " ": "/"
}

def get_morse_char(on, duration):
    if on:
        if duration > 1000:
            return "-"
        else:
            return "."
    else:
        if duration > 2000:
            return " / "
        elif duration > 1000:
            return " "
    return ""


def count_consecutive(values):
    result = []
    count = 0
    value = values[0]
    for v in values:
        if v == value:
            count += 1
        else:
            if count > 1:
                result.append((value, count))
                count = 1
                value = v
    result.append((value, count))
    return result

def get_morse_string(filename):
    with wave.open(filename, "rb") as f:
        frames = f.readframes(f.getnframes())
        print("frames count", frames.count(128))
        most_common = max(set(reversed(frames)), key=frames.count)
        print("MOST", most_common)
        values = [most_common != frame for frame in frames]

        out = ""
        for on, dur in count_consecutive(values):
            out += get_morse_char(on, dur)

        return out


def morse_to_text(morse):
    return "".join([k for k, v in morse_code.items() if v == morse])

def decode(filename):
    morse = get_morse_string(filename).split(" ")
    return''.join(morse_to_text(m) for m in morse)


print(decode("morse.wav"))
