# coding=utf-8

from urllib import request
import json
import time
from datetime import datetime
from datetime import timedelta
import os
from pymongo import MongoClient


# 获取数据，根据url获取
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    if response.getcode() == 200:
        return response.read()
    return None


# 处理数据
def parse_data(html):
    data = json.loads(html)['cmts']  # 将str转换为json
    comments = []
    for item in data:
        comment = {
            'id': item['id'],
            'nickName': item['nickName'],
            'userLevel': item['userLevel'],
            'gender': item['gender'] if 'gender' in item else '',
            'cityName': item['cityName'] if 'cityName' in item else '',  # 处理cityName不存在的情况
            'content': item['content'].replace('\n', ' ', 10),  # 处理评论内容换行的情况
            'score': item['score'],
            'upCount': item['approve'],
            'startTime': item['startTime'],
            'replyCount': item['reply']
        }
        comments.append(comment)
    return comments


# 存储数据，存储到文本文件
def save_data():
    # # 从固定时间开始爬取
    # start_time = '2019-08-21 09:24:58'
    # start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(seconds=-1)  # 转换为datetime类型，减1秒，避免获取到重复数据
    # start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间，从当前时间向前获取
    end_time = '2019-07-26 00:00:00'  
    # 配置mongodb数据库
    host = os.environ.get('MONGODB_HOST', '127.0.0.1')  # 本地数据库
    port = os.environ.get('MONGODB_PORT', '27017')  # 数据库端口
    mongo_url = 'mongodb://{}:{}'.format(host, port)
    mongo_db = os.environ.get('MONGODB_DATABASE', 'Maoyan')
    client = MongoClient(mongo_url)
    db = client[mongo_db]
    collection = db['Nezha_Comment']
    collection.create_index('id', unique=True)  # 以评论的id为主键进行去重   
    while start_time > end_time:
        url = 'http://m.maoyan.com/mmdb/comments/movie/1211270.json?_v_=yes&offset=0&startTime=' + start_time.replace(
            ' ', '%20')
        html = None
        '''
            问题：当请求过于频繁时，服务器会拒绝连接，实际上是服务器的反爬虫策略
            解决：1.在每个请求间增加延时0.5秒，尽量减少请求被拒绝
                 2.如果被拒绝，则1秒后重试
        '''
        try:
            html = get_data(url)
        except Exception as e:
            print(e)
            time.sleep(1)
            html = get_data(url)
        else:
            time.sleep(0.5)

        comments = parse_data(html)
        # # 存入txt中
        # for item in comments:
        #     with open('comments.txt', 'a', encoding='utf-8') as f:
        #         f.write(str(item['id']) + ',' + item['nickName'] + ',' + item['cityName'] + ',' + item[
        #             'content'] + ',' + str(item['score']) + ',' + item['startTime'] + '\n')

        # 将爬取的评论存入mongodb中
        for item in comments:
            collection.update_one({'id': item['id']}, {'$set': item},
        upsert=True)
        print(start_time)
        start_time = comments[14]['startTime']  # 获得末尾评论的时间
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(
            seconds=-1)  # 转换为datetime类型，减1秒，避免获取到重复数据
        start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')  # 转换为str


    print(start_time)
    print("爬取完成！")


if __name__ == '__main__':
    save_data()
