# __author__: xxeNt
import requests
from mytools.UserAgent import makeAgent
import time


def get_info(keyword):
    '''
    根据关键词和输入的类型返回相应页面URL
    keyword:搜索关键词
    '''
    searchUrl = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"
    searchParams = {
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
        params=searchParams,
        headers=makeAgent(Referer='https://y.qq.com/portal/search.html'))

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
        url = 'https://y.qq.com/n/yqq/{}/{}.html'.format(
            searchType, selectionMid)
        print('\n链接地址为:' + url)
        return url, selectionId, selectionName, selectionSinger
    else:
        url = 'https://y.qq.com/n/yqq/{}/{}.html'.format(
            searchType, selectionVid)
        print('\n链接地址为:' + url)
        return url, selectionVid, selectionName, selectionSinger


def get_comments(url, selectionId, selectionName, selectionSinger):
    commentUrl = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
    pageNum = 0
    commentParmas = {
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'GB2312',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        'cid': '205360772',
        'reqtype': '2',
        'biztype': '1',
        'topid': selectionId,  # 获取指定歌曲评论
        'cmd': '8',
        'needmusiccrit': '0',
        'pagenum': pageNum,  # 评论页数
        'pagesize': '25',
        'lasthotcommentid': '',  # 上一页最后一条评论ID
        'domain': 'qq.com',
        'ct': '24',
        'cv': '10101010'
    }

    commentRequest = requests.get(
        commentUrl, params=commentParmas, headers=makeAgent(Referer=url))

    # print(commentRequest.json())
    commentDict = commentRequest.json()
    commentTotal = int(commentDict['comment']['commenttotal'])
    commentNum = 1

    for i in range(commentTotal // 25 + 1):
        try:
            commentParmas = {
                'g_tk': '5381',
                'loginUin': '0',
                'hostUin': '0',
                'format': 'json',
                'inCharset': 'utf8',
                'outCharset': 'GB2312',
                'notice': '0',
                'platform': 'yqq.json',
                'needNewCode': '0',
                'cid': '205360772',
                'reqtype': '2',
                'biztype': '1',
                'topid': selectionId,  # 获取指定歌曲评论
                'cmd': '8',
                'needmusiccrit': '0',
                'pagenum': pageNum,  # 评论页数
                'pagesize': '25',
                'lasthotcommentid': '',  # 上一页最后一条评论ID
                'domain': 'qq.com',
                'ct': '24',
                'cv': '10101010'
            }

            commentRequest = requests.get(
                commentUrl,
                params=commentParmas,
                headers=makeAgent(Referer=url))

            commentDict = commentRequest.json()
            commentList = commentDict['comment']['commentlist']
            for j in commentList:
                if j['middlecommentcontent'] is not None:
                    subcommentContent = j['middlecommentcontent']
                    commentResult = j['rootcommentid'], j['nick'], j[
                        'time'], j['praisenum'], j['vipicon'], j[
                            'is_hot_cmt'], subcommentContent[0][
                                'subcommentcontent']
                    print('第{}条评论->{}'.format(commentNum, commentResult))
                    commentNum += 1
                else:
                    commentResult = j['rootcommentid'], j['nick'], j[
                        'time'], j['praisenum'], j['vipicon'], j[
                            'is_hot_cmt'], j['rootcommentcontent']
                    print('第{}条评论->{}'.format(commentNum, commentResult))
                    commentNum += 1
        except Exception as e:
            print('第{}页爬取失败,错误：{}'.format(pageNum, e))
            time.sleep(1)
        else:
            time.sleep(0.5)
            pageNum += 1



if __name__ == '__main__':
    getKeyword = str(input("请输入要查询的关键词:"))
    arg = get_info(getKeyword)
    get_comments(*arg)
