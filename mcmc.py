import math
import random
from typing import Dict, List
from preprocessing import FrequencyTable

def random_mapping(letters: List[str]) -> Dict[str, str]:
    copy = letters.copy()
    random.shuffle(copy)
    return {k: v for k, v in zip(letters, copy)}

def encrypt(mapping: Dict[str, str], text: str) -> str:
    return " ".join("".join(mapping.get(c, c) for c in w) for w in text.lower().split())

def decrypt(
    table: FrequencyTable,
    secret: str,
    iterations: int = 50000,
    verbose: bool = True
) -> Dict[str, str]:
    letters = list(table.letters)
    mapping = random_mapping(letters)

    best_score = 0
    best_guess = ""

    for i in range(iterations):
        guess_before = encrypt(mapping, secret)
        score_before = table.score(guess_before)

        a, b = random.sample(letters, 2)
        mapping[a], mapping[b] = mapping[b], mapping[a]

        guess_after = encrypt(mapping, secret)
        score_after = table.score(guess_after)

        if score_after > best_score:
            best_score = score_after
            best_guess = guess_after

        if random.random() > math.exp(score_after - score_before):
            mapping[a], mapping[b] = mapping[b], mapping[a]
        
        if verbose and i % 500 == 0:
            print(f"{i} - {best_guess[:100]}")

    return mapping