import math
import string
from typing import Dict, Set
from collections import defaultdict
from dataclasses import dataclass

_DEFAULT_SEPARATOR = " "

@dataclass
class FrequencyTable:
    letters: Set[str]
    separator: str
    frequencies: Dict[str, int]

    @classmethod
    def from_text(cls, text: str, separator: str = _DEFAULT_SEPARATOR) -> 'FrequencyTable':
        letters = set(string.ascii_lowercase)
        frequencies = defaultdict(int)

        for i in range(len(text) - 1):
            a = text[i] if text[i] in letters else separator
            b = text[i + 1] if text[i + 1] in letters else separator
            frequencies[a] += 1
            frequencies[a + b] += 1

        return FrequencyTable(letters, separator, frequencies)
    
    @classmethod
    def from_file(cls, filepath: str, separator: str = _DEFAULT_SEPARATOR) -> 'FrequencyTable':
        with open(filepath, "r") as file:
            return cls.from_text(file.read(), separator)

    def _get_key(self, a: str, b: str) -> str:
        a = a if a in self.letters else self.separator
        b = b if b in self.letters else self.separator
        return a + b

    def score(self, sequence: str) -> float:
        if len(sequence) == 1:
            return self.frequencies[sequence]

        s = 0
        for i in range(len(sequence) - 1):
            f = self.frequencies[self._get_key(sequence[i], sequence[i + 1])]
            if f > 0:
                s += math.log(f)
        return s