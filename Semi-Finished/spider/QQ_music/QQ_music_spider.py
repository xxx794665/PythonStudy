# __author__: xxeNt
import requests
from mytools.UserAgent import makeAgent

searchUrl = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"

searchData = {
    'is_xml': '0',
    'key': '周杰伦',  # 搜索关键词
    'g_tk': '2120285735',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0'
}

searchRequest = requests.get(
    searchUrl,
    params=searchData,
    headers=makeAgent(Referer='https://y.qq.com/portal/search.html'))

print(searchRequest.text)
