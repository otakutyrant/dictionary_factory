#!/usr/bin/env python3

from writemdict.writemdict import MDictWriter

# dictionary = {
#         "doe": "<b>doe</b> <i>n.</i> a deer, a female deer.",
#         "ray": "<b>ray</b> <i>n.</i> a drop of golden sun.",
#         "me": "<b>me</b> <i>pron.</i> a name I call myself.",
#         "far": "<b>far</b> <i>adv.</i> a long, long way to run."}


def handle(filename, number):
    temporary_dictionary = {}
    file_ = open(filename)
    father = ""
    for line in file_:
        line = line.lower()
        if line == "\n":
            pass
        elif line[0] == "\t":
            word = line.split()[0]
            temporary_dictionary[father].append(word)
        else:
            father = line.split()[0]
            temporary_dictionary[father] = [father]
    sub_dictionary = {}
    for father, word_family in temporary_dictionary.items():
        entry_body = "{} <b>{}</b> {}".format(
                number * 1000, father, ", ".join(word_family[1:]))
        for headword in word_family:
            sub_dictionary[headword] = entry_body
    return sub_dictionary


dictionary = {}
for number in range(1, 15):
    filename = "basewrd{}.txt".format(number)
    sub_dictionary = handle(filename, number)
    dictionary = {**dictionary, **sub_dictionary}

# for headword, entry_body in dictionary.items():
    # print("{} {}".format(headword, entry_body))

writer = MDictWriter(
        dictionary,
        title="Word Family",
        description="Show all family words and the corresponding frequent of a keyword.")
file_ = open("wordfamily.mdx", "wb")
writer.write(file_)
file_.close()
