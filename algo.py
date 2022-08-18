from words_in_terms import get_words, count_words
from glob import glob
import pandas as pd

REMOVED_WORDS = ['in', 'on', 'at', 'for', 'into', 'upon', 'up', 'from', 'the', 'a', 'an' 'of', 'and', 'or', 'be', 'use', 'let', 'with', 'real']

DATAFOLDER = "data"

def find_overlap(data_folder, class_: list, threshold1:int, threshold2:int):
    rare_words = {i: {} for i in class_}
    num_of_words = {}
    for i in class_:
        num_of_words[i] = count_words(get_words(data_folder, i))
    for i in class_:
        terms = get_words(data_folder, i)
        for t in terms:
            for word in terms[t]:
                if num_of_words[i][word] <= threshold1 and word not in REMOVED_WORDS:
                    rare_words[i][word] = t
    overlap_dict = {}
    for i in class_:
        for word, term in rare_words[i].items():
            overlap_dict[term] = [i]
            for j in class_:
                try:
                    if num_of_words[j][word] >= threshold2 and word not in REMOVED_WORDS:
                        overlap_dict[term].append([j, word])
                except KeyError:
                    pass
    count = 0
    for key, value in overlap_dict.items():
        if len(value) > 1:
            count += 1
            print(f"{count}. '{key}' in class {value[0]} overlaps with classes {value[1:]}")


if __name__ == "__main__":
    find_overlap(data_folder=DATAFOLDER, class_=[9, 36, 1], threshold1=30, threshold2=70)