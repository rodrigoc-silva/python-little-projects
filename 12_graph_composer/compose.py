
import os
import re
import string
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as file:
        text = file.read()

        # remove [text in here]
        # if you are using song list
        # text = re.sub(r'\[(.+)\]', ' ', text) 

        text = ' '.join(text.split()) # turn whitespace into space
        text = text.lower() # making words in lowercase
        text = text.translate(str.maketrans('', '', string.punctuation)) # remove punctuation

    words = text.split() # split on spaces
    words = words[:1000]
    return words


def make_graph(words):
    g = Graph()
    previous_word = None

    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex

    g.generate_probability_mappings()
    return g


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # pick a random word to start
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main():
    # 1: get words from text
    words = get_words_from_text('texts\hp_sorcerer_stone.txt')

    # for songs
    # for song in os.listdir('songs/{}'.format(artist)):
    #     if song == '.DS_Store':
    #         continue
    #     words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))

    # 2: make a graph using the words
    g = make_graph(words)

    # 3: get the next word for x number of words
    # 4: show the user 
    composition = compose(g, words, 100)
    print(' '.join(composition)) # return a string with all the words separeted by space


if __name__ == '__main__':
    main()
