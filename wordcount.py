import collections
import re


def word_count(words):
    words = words.decode('utf-8', 'ignore')
    words = words.split()
    io = collections.defaultdict(int)
    exp = ' '
    for word in words:
        word = word.replace(u'\U0001f596', ' ')
        word = word.lower()
        exp += " " + word
    words = re.sub(r'[!&@$%^&:,_.]+', ' ', exp)
    words = words.split()
    for word in words:
        io[word] += 1
    return io
