import pandas as pd
from tabulate import tabulate


def get_words(data_folder: str, class_: int) -> dict:
    df = pd.read_excel(f"{data_folder}/class{class_}.xls", header=0, skiprows=[0])
    df = df[df.Status == 'Active']
    term = df.Term.to_list()
    words_dict = {}
    for t in term:
        words_dict[t] = t.split(" ")
    return words_dict

def count_words(words_dict: dict) -> dict:
    num_of_words = {}
    for term in words_dict:
        for w in words_dict[term]:
            if w not in num_of_words:
                num_of_words[w] = 1
            else:
                num_of_words[w] += 1
    return num_of_words

if __name__ == "__main__":
    words_dict = get_words("/home/nhan/Desktop/other/cipo/data", 36)
    num_of_words = count_words(words_dict)
    print(num_of_words)
    print(len(num_of_words))