from docx import Document
import re

def load_file(path):
    split = r';|；|。|？|！|\?|!'
    sentences = []
    test = Document(path)
    para = [paragraph.text for paragraph in test.paragraphs]
    for p in para:
        sentences += re.split(split, p)
    
    
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip()
        sentences[i] = sentences[i].replace('\n', '')
    
    sentences.sort(key=lambda i: len(i), reverse=True)
    return sentences

sentences = load_file("D:\计算机导论助教\个人作业3（人工智能）\包文兴(21371017)\提交作业的附件\人工智能在医疗方面的作用.docx")