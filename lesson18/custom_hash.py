from random import choice, choices
from string import ascii_letters


class CustomHash:
    """
    The hash methods of a class fulfill the following conditions:
    - the same text leads to the same hash value;
    - the same hash value returns the same text;
    - the length of the hash value is always the same.
    """

    def __init__(self):
        self.hash_data = dict()
        self.key_len = 120

    def encoding_text(self, text):
        """
        Creates a hash for a string.
        """

        if type(text) != str:
            print('The method only accepts a string!')
            return

        encoding_text = ''

        for ch in text:

            ord_ch = str(ord(ch))
            letter = choice(ascii_letters)
            encoding_text += ord_ch + letter
            self.hash_data[encoding_text] = text

        if len(encoding_text) < self.key_len:
            letters = choices(ascii_letters, k=self.key_len-len(encoding_text))
            encoding_text += ''.join(letters)

        return encoding_text

    @staticmethod
    def decoding_text(some_hash):
        """
        Decodes the hash and gets the string.
        """
        text = ''
        ord_ch = ''
        digit_flag = False

        for ch in some_hash:
            if ch.isdigit():
                ord_ch += ch
                digit_flag = True
                continue

            elif digit_flag:
                text += chr(int(ord_ch))
                ord_ch = ''
                digit_flag = False

        return text


if __name__ == '__main__':

    custom_hash = CustomHash()

    text_1 = 'Process'
    text_2 = 'lenovo'
    text_3 = 'scratches'

    hash_1 = custom_hash.encoding_text(text=text_1)
    un_hash_1 = custom_hash.decoding_text(some_hash=hash_1)

    print(f'hash_1 = {hash_1}')
    print(f'un_hash_1 = {un_hash_1}')
    print(f'text_1 == un_hash_1  {text_1 == un_hash_1}')

    print('\n-----------------------\n')

    hash_2 = custom_hash.encoding_text(text=text_2)
    un_hash_2 = custom_hash.decoding_text(some_hash=hash_2)

    print(f'hash_2 = {hash_2}')
    print(f'un_hash_2 = {un_hash_2}')
    print(f'text_2 == un_hash_2  {text_2 == un_hash_2}')

    print('\n-----------------------\n')

    hash_3 = custom_hash.encoding_text(text=text_3)
    un_hash_3 = custom_hash.decoding_text(some_hash=hash_3)

    print(f'hash_3 = {hash_3}')
    print(f'un_hash_3 = {un_hash_3}')
    print(f'text_3 == un_hash_3  {text_3 == un_hash_3}')
