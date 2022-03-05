def encode(message, user_key):
    for i in range(len(message)):
        translate_message = message[i]
        translate_message = ord(translate_message)
        shift = translate_message + user_key
        final_message = chr(shift)

def encode_better(phrase, key):
    for i in range(len(phrase)):
        character_val = ord(phrase[i]) - 65
        key_val = ord(key[i % len(key)]) - 65
        encode_val = ((character_val + key_val) % 57) + 64
        encode_text = chr(encode_val)
        print(encode_text, end="")


