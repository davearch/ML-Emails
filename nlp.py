from afinn import Afinn
from collections import Counter
import os

afinn = Afinn()

textfiles = [file for file in os.listdir(".") if file.endswith(".txt")] # get text for each email

def print_sorted_score(sorted_scores):
    for f,v in sorted_scores.items():
        print(f"{f}: {v}")

def sort_dict_by_value(d):
    sorted_dict = {}
    for key, val in sorted(d.items(), key=lambda item: item[1], reverse=True):
        sorted_dict[key] = val
    return sorted_dict

def print_dictionary(d):
    for k,v in d.items():
        print(f"{k}: {v}")

scores = {}
for textfile in textfiles:
    f = open(textfile, 'r', encoding='utf8')
    file_contents = f.read()
    scores[textfile] = afinn.score(file_contents)
    f.close()

counts = {}
for textfile in textfiles:
    f = open(textfile, 'r', encoding='utf8')
    data = f.read()
    words = data.split()
    counts[textfile] = len(words)
    f.close()

#sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}

sorted_counts = sort_dict_by_value(counts)
print_dictionary(sorted_counts)