# __author__: xxeNt
import request
from urllib.parse import urlencode
from mytools.UserAgent import makeAgent

searchUrl = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"

searchData = urlencode({
    'is_xml': '0',
    'key': 'Gai见面吧电',  #搜索关键词
    'g_tk': '2120285735',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0'
})

headers =urlencode({
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
})

searchRequest = request.GET(searchUrl, params=searchData, headers=headers)

print(searchRequest.text)