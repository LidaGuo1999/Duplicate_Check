from difflib import SequenceMatcher
from load import load_file
from scraper import scraper

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

file_path = "D:\计算机导论助教\个人作业3（人工智能）\曾通(21373315)\提交作业的附件\人工智能的发展会为健康行业带来怎样的变化（曾通 21373315）.docx"
sentences = load_file(file_path)[0:10]

flag = 0
for s in sentences:
    search = scraper(s)
    sim = similarity(s, search)
    if sim > 0.6:
        print(sim)
        print(s+'\n-------------------------------------------------\n'+search)
        print('\n')
    if sim > 0.6 and len(search) > 30:
        flag += 1

print('flag: '+ str(flag))