from bs4 import BeautifulSoup as bs
from lxml import etree
from readmdict import MDX

mdx = MDX('oald10/oald10.mdx')


def get_culture_section(entry):
    tree = etree.HTML(entry.decode('utf-8'))
    culture_passages = tree.xpath(
            '//*[@unbox=\'cult\']/*[@class=\'body\']/*[@class=\'p\']')
    if len(culture_passages) > 0:
        passges_texts = []
        for passage in culture_passages:
            passage = bs(etree.tostring(passage).decode('utf-8'))
            # passage.prettify()
            passges_texts.append(passage.get_text())
        text = '\n\n'.join(passges_texts)
        return text
    else:
        return None


with open('culture.txt', 'w') as file_:
    for headword, entry in mdx.items():
        text = get_culture_section(entry)
        if text is not None:
            file_.write('### {}'.format(headword.decode('utf-8')))
            file_.write('\n\n')
            file_.write(text)
            file_.write('\n\n')
