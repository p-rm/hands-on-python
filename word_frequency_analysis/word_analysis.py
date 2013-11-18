'''****************************************************
 File:     word_analyze.py
 Author:   (c) Paulo Martins (source ThinkPython)
 Date:     20130831
 Desc:     word analyze
 version:  1.0
 Change Log:
****************************************************'''

import string

def histogram(s):
    # count how many times a word appear in a given string
    d = dict()
    for w in s:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    return  d


def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    line = line.replace('-',' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        hist[word]=hist.get(word, 0) + 1


def total_words(hist):
    return sum(hist.values())


def different_words(hist):
    return len(hist)


def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t


def print_most_common(hist, num=30):
    t = most_common(hist)
    print 'The most common are: '
    for freq, word in t[0:num]:
        print word, '\t', freq


hist = process_file('40409-8.txt')

print 'Total number of words: ', total_words(hist)
print 'Total number of different words: ', different_words(hist)
print_most_common(hist)
