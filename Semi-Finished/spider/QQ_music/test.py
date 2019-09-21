selectSearchType = input("请输入要查询的类型：(0:歌曲、1：歌手、2：专辑、3：mv)")
searchParams = ['song', 'singer', 'album', 'mv']
print(searchParams[int(selectSearchType)])
print(type(searchParams[int(selectSearchType)]))