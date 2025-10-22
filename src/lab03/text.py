import sys
from lib import normalize, tokenize, count_freq, top_n



text = sys.stdin.read()
normalized_text = normalize(text)
tokens = tokenize(normalized_text)
top_words = top_n(count_freq(tokens), 5)
print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(count_freq(tokens))}")
print("Топ-5:")

for word, count in top_words:
    print(f"{word}:{count}")