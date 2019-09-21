# __author__: xxeNt
import requests
from mytools.UserAgent import makeAgent


def get_info(keyword):
    '''
    根据关键词和输入的类型返回相应页面URL
    keyword:搜索关键词
    '''
    searchUrl = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"
    searchData = {
        'is_xml': '0',
        'key': keyword,  # 搜索关键词
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

    # print(searchRequest.text)

    musicInfoDict = searchRequest.json()
    selectSearchType = int(input("\n请输入要查询的类型(0:单曲、1：歌手、2：专辑、3：mv):"))
    searchTypeList = ['song', 'singer', 'album', 'mv']
    searchType = ''.join(list(searchTypeList[int(selectSearchType)]))
    searchResult = musicInfoDict['data']['{}'.format(searchType)]['itemlist']

    for i in range(len(searchResult)):
        print("序号:{}, 名称:{}, 演唱者:{}".format(i + 1, searchResult[i]['name'],
                                            searchResult[i]['singer']))

    confirmSelection = int(input("\n请选择需要查询的歌曲序号:"))
    selectionList = searchResult[confirmSelection - 1]
    selectionName = selectionList['name']
    selectionSinger = selectionList['singer']
    selectionId = selectionList['id']
    selectionMid = selectionList['mid']
    if selectSearchType == 3:
        selectionVid = selectionList['vid']

    print("\n" + selectionName, selectionSinger, selectionId, selectionMid)

    if selectSearchType != 3:
        print('\n链接地址为:' + 'https://y.qq.com/n/yqq/' + searchType + '/' +
              selectionMid + '.html')
    else:
        print('\n链接地址为:' + 'https://y.qq.com/n/yqq/' + searchType + '/v/' +
              selectionVid + '.html')


if __name__ == '__main__':
    getKeyword = str(input("请输入要查询的关键词:"))
    get_info(getKeyword)
