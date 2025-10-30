import re
from operator import itemgetter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    result = text
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        result = result.casefold()

    result = re.sub(r'\s+', ' ', result)

    return result.strip()


def tokenize(text: str) -> list[str]:
    pattern = r'\b[\w]+(?:-[\w]+)*\b'
    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:

    freq = {}

    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items.sort(key=itemgetter(0))
    items.sort(key=itemgetter(1), reverse=True)
    return items[:n]
