# 计算属相（切片操作符：[]）
chinese_animal = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

zodiac_name = (u'魔蝎座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座',
               u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
               (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# 属相计数(不够优雅可优化)
ca_num = {}
for i in chinese_animal:
    ca_num[i] = 0
# 星座计数(不够优雅可优化)
zn_num = {}
for i in zodiac_name:
    zn_num[i] = 0

# 无限循环
while True:
    try:

        year = input("请输入您的出生年份:")

        month = int(input('请输入您的出生月份：'))

        day = int(input('请输入您的出生日期：'))

        remainder = (int(year) - 4) % 12

        # 使用while循环
        n = 0
        while zodiac_days[n] < (month, day):
            if month == 12 and day > 23:
                break
            n += 1

        print(
            '您的出生日期为%s年%s月%s日，您的生肖属相是%s，您的星座是%s。' %
            (year, month, day, chinese_animal[int(remainder)], zodiac_name[n]))
        # print(str(year) + "的生肖属相是：" + chinese_animal[int(remainder)])
        # print('您查询的日期的星座是：' + str(zodiac_name[n]))
        ca_num[chinese_animal[int(remainder)]] += 1
        zn_num[zodiac_name[n]] += 1

    except (ValueError, IndexError):
        print('请输入正确的日期格式')

    finally:

        # 输出生肖和星座的统计信息
        for each_key in ca_num.keys():
            print('使用者中生肖为%s，一共有%d 个' % (each_key, ca_num[each_key]))
        for each_key in zn_num.keys():
            print('使用者中星座为%s，一共有%d 个' % (each_key, zn_num[each_key]))
