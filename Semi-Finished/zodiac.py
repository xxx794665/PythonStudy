zodiac_name = (u'魔蝎座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座',
               u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
               (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# input_days = map(int, (input('请输入要查询的日期(使用,分隔开):').split(',')))

# zodiac_day = filter(lambda x: x <= tuple(input_days), zodiac_days)

month = int(input('请输入要查询的月份：'))

day = int(input('请输入要查询的日期：'))

# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)

# zodiac_len = len(list(zodiac_day)) % 12

# 使用for循环：
# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (month, day):
#         print('您查询的日期的星座是：' + str(zodiac_name[zd_num]))
#         break
#     elif month == 12 and day > 23:
#         print('您查询的日期的星座是：' + str(zodiac_name[0]))
#         break

# 使用while循环
n = 0
while zodiac_days[n] < (month, day):
    if month == 12 and day > 23:
        break
    n += 1
print('您查询的日期的星座是：' + str(zodiac_name[n]))
