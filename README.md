This program is used for creating, adjusting, and adapting personal dictionaries for GoldenDict.

## Requirements

* mdict-analysis, used for understanding and extracting the mdx format
* writemdict, used for converting text to a dictionary of the mdx format

## word-family

An ordinary dictionary can list tense forms or plural forms for words, regarded as inflections. However, derived forms are not included, for example artist derived from art. So I would like to find a dictionary that can list most derived forms of a word, to help me learn more words. Earlily I found Prof Paul Nation offering [headwords of the 25,000 word families](https://www.wgtn.ac.nz/lals/about/staff/paul-nation#vocab-lists). They are not fully comprehensive, but I have not encountered any better data so I decided to write a program to convert them into a dictionary, called word-family.

The word-family directory comprises `main.py` and existed `wordfamily.mdx`. Note that `main.py` handles "basewrd\*.txt" from the first to the fourteenth txt, but does not handle the subsequent txts because the encoding of the fifteen txt is erroneous and frequencies of the remaining words are so low as to be negligible. Consequentely, `wordfamily.mdx` contains the top 14000 word families.
