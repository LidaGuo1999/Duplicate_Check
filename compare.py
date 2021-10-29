from difflib import SequenceMatcher
from load import load_file
from scraper import scraper

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

file_path = "D:\计算机导论助教\个人作业3（人工智能）\陈彦凯(21182640)\提交作业的附件\人工智能.docx"
sentences = load_file(file_path)[0:10]

flag = 0
for s in sentences:
    print(s)
    search = scraper(s)
    print(search)
    sim = similarity(s, search)
    print(similarity(s, search))
    if sim > 0.6:
        print(sim)
        print(s+'\n-------------------------------------------------\n'+search)
        print('\n')
    if sim > 0.6 and len(search) > 30:
        flag += 1

print('flag: '+ str(flag))