import re

class Binary:
    zero_width_chars = {
      '0': '\u200e',
      '1': '\u200f',
      '\u200e': '0',
      '\u200f': '1',
    }
    
    @classmethod
    def encode(self, string):
        binary = "".join([bin(x)[2:] for x in string.encode()])
        chars = ''.join(self.zero_width_chars[bin] for bin in binary)
        return chars

    @classmethod
    def decode(self, characters):
        chars = list(map(str, characters))
        binary = "".join(self.zero_width_chars[char] for char in chars)
        parts = [binary[x:x+7] for x in range(0, len(binary), 7)]
        return "".join([chr(x) for x in [int(x, 2) for x in parts]]).encode("l1").decode()

class ziro:
    pattern = r"\u200e|\u200f"
    
    @classmethod
    def hide(self, string, hide_str) -> str:
        ret = string[:-int(len(string)/2)] + Binary.encode(hide_str) + string[-int(len(string)/2):]
        return ret

    @classmethod
    def reveal(self, string) -> str:
        chars = ''.join(char for char in re.findall(self.pattern, string))
        revealed = Binary.decode(chars)
        return revealed
