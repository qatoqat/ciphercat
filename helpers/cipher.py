encipher_dict = {
    "J": "🡤-", "D": "🡥-", "B": "∣🡥-",
    "G": "∣🡤", "C": "🡤", "T": "🡥", "P": "∣🡥",
    "H": "\"", "Y": "^", "W": "∣^",
    "X": "∣∣", "N": "=", "M": "∣=",
    "K": "∣🡧", "S": "🡧", "L": "🡦", "F": "∣🡦",
    "Q": "∣🡧-", "Z": "🡧-", "R": "🡦-", "V": "∣🡦-",
    "A": ">", "E": "<", "I": "Ʌ",
    "O": "O", "U": "V",
}

decipher_dict = {
    "🡤-": "J", "🡥-": "D", "∣🡥-": "B",
    "∣🡤": "G", "🡤": "C", "🡥": "T", "∣🡥": "P",
    "\"": "H", "^": "Y", "∣^": "W",
    "∣∣": "X", "=": "N", "∣=": "M",
    "∣🡧": "K", "🡧": "S", "🡦": "L", "∣🡦": "F",
    "∣🡧-": "Q", "🡧-": "Z", "🡦-": "R", "∣🡦-": "V",
    ">": "A", "<": "E", "Ʌ": "I",
    "O": "O", "V": "U",
}

arrows = ["🡤", "🡥", "🡧", "🡦"]


def encipher(plaintext):
    return "".join([encipher_dict[c] if c in encipher_dict else c for c in plaintext.upper()])


def decipher(ciphertext):
    plaintext = ""
    box = [None, None, None]
    for s in ciphertext:
        if s == "∣" and box == [None, None, None]:
            box[0] = s
        elif s in arrows and box[1] is None and box[2] is None:
            box[1] = s
        elif s in ["-"] and box[2] is None:
            box[2] = s
        else:
            if box == ["∣", None, None]:
                plaintext += "X" if s == "∣" else "W" if s == "^" else "M" if s == "=" else "".join(box) + s
                box = [None, None, None]
            else:
                x = "".join([x if x is not None else "" for x in box])
                plaintext += decipher_dict[x] if x in decipher_dict else x
                box = [None, None, None]
                if s in "><ɅOV":
                    plaintext += decipher_dict[s] if s in decipher_dict else s
                elif s == "∣":
                    box[0] = s
                elif s in arrows:
                    box[1] = s
                elif s in ["-", "=", "^", "\""]:
                    box[2] = s
                else:
                    plaintext += s
    if box != [None, None, None]:
        e = "".join([e if e is not None else "" for e in box])
        plaintext += decipher_dict[e] if e in decipher_dict else e
    return plaintext


if __name__ == "__main__":
    c_set = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%&*()_+"

    for a_char in c_set:
        for b_char in c_set:
            for c_char in c_set:
                pl = a_char + b_char + c_char
                ci = encipher(pl)
                de = decipher(ci)
                # print(f"'{pl}' '{de}'")
                if pl != de:
                    raise Exception(f"'{pl}' '{de}'")
