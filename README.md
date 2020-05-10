This program is used for creating, adjusting, and adapting my personal dictionaries for GoldenDict.

## Requirements

* mdict-analysis, used for understanding and extracting the mdx format
* writemdict, used for converting text to a dictioanry of the mdx format

## word-family

Note that an ordinary dictionary can list tense forms or plural forms of word, regarded as inflections. However derived forms are not only these, for example artist corresponding to art, so I would like to find a dictionary, that can list utmost derived forms of a word, to learn more words. Up to now I find Prof Paul Nation offering [headwords of the 25,000 word families](https://www.wgtn.ac.nz/lals/about/staff/paul-nation#vocab-lists), not fully comprehensive actually, but I has not encountered any better data so I decided to write a program to convert them into a dictionary, called word-family.

The word-family directory has contained `main.py` and existed `wordfamily.mdx`. Note that `main`.py handles "basewrd\*.txt" from the first to the fourteen, not containing the subsequent txts because the encoding of the fifteen txt is erroneous and frequencies of the remnant are so low as to be negligible, so `wordfamily.mdx` contains top 14000 word families.
