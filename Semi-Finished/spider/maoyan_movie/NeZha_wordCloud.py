import pandas as pd
import numpy as np
import jieba
import wordcloud
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image

# 新定义分词词典
jieba.load_userdict("dict.txt")
df = pd.read_csv('comments.txt', names=['id', 'nickName', 'cityName', 'content', 'score', 'startTime'])

comments = str()
for comment in df['content']:
    comments = comments + str(comment)

stopwords = {}.fromkeys([line.rstrip() for line in open('chineseStopWords.txt')])
segs = jieba.cut(comments, cut_all=False)

cloud_text = []
for seg in segs:
    if seg not in stopwords:
        cloud_text.append(seg)

fre = Counter(cloud_text)

# 设置词云图背景
mask = np.array(Image.open('NeZha.png'))
wc = wordcloud.WordCloud(
    font_path='PingFang Medium.ttf',  # 设置词云图字体格式
    mask=mask,  # 设置背景图
    max_words=200,  # 最多显示词数
    max_font_size=150)  # 字体最大值

wc.generate_from_frequencies(fre)  # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
plt.imshow(wc)  # 显示此云
plt.axis('off')  # 关闭坐标轴
plt.show()
wc.to_file('NeZha_comment_pic.png')
