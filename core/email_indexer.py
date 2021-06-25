import glob
import re
from trie import *
import pickle


def create_word_map(dir_path: str) -> dict:
    # create a mapping of words to email paths
    file_paths = glob.glob(f"{dir_path}/*")

    word_map = {}
    for file_path in file_paths:
        with open(file_path, encoding="utf8", errors="ignore") as f:
            lines = f.readlines()

        words = set()
        for line in lines:
            for word in line.split():
                # if we chose to strip all special characters
                # word = word
                # word = re.sub("[^A-Za-z0-9]+", "", word)
                words.add(word)

        for i in words:
            if i in word_map:
                word_map[i].append(file_path)
            else:
                word_map.update({i: [file_path]})

    return word_map


def index_emails(dir_path: str, target_dir: str) -> Trie:
    word_map = create_word_map(dir_path)

    t = Trie(word_map)
    for word in word_map:
        t.insert(word)

    pickle.dump(t, open(f"{target_dir}temp_trie.p", "wb"))
    # return t


def search_word(word, trie_pickle):
    trie = pickle.load(open(trie_pickle, "rb"))
    solution = {}
    for item in trie.search(word):
        solution.update({item[0]: item[1]})

    return solution[word]
