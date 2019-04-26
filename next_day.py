'''

该程序有三个输入变量month、day、year（month 、 day 和year均为整数值，
并且满足：1≤month≤12，1≤day≤31和1900≤year≤2050），分别作为输入日期
的月份、日、年份，通过程序可以输出该输入日期在日历上隔一天的日期。例如输
入为 2004 年11 月29 日，则该程序的输出为2004 年12 月1 日。
'''
encoding = 'gbk'
date = []
def input_date():
    for i in range(3):
        data = int(input())
        date.append(data)
    if date[0]>=1900 and date[0]<=2050 and date[1]>=1 and date[1]<=12 and date[2]>=1 and date[2]<=31:
        #print(date)
        next_day(date)
    elif date[0]=='' or date[1]=='' or date[2]=='' :
        print("请重新输入")


    else:
        print("请重新输入：")
        del date[-3:]

def next_day(date):
    print ("in  "+str(date[0]) + "年" + str(date[1]) + "月" + str(date[2]) + "日")                                                                               #两天后········
    if date[2] ==31 and date[1]==12:
        print(str(date[0]+1) + "年" + '1' + "月" + '2' + "日")                      #跨年

    elif date[1] in [1,3,5,7,8,10,12] :
        if date[2] < 30 and date[1] < 12:
            print(str(date[0]) + "年" + str(date[1]) + "月" + str(date[2]+2) + "日")    #30日月内
        elif  date[2] == 30 and date[1] < 12:
            print(str(date[0]) + "年" + str(date[1]+1) + "月" + '1' + "日")             #30日跨月
        elif  date[2] == 31 and date[1]   < 12:
            print(str(date[0]) + "年" + str(date[1] + 1) + "月" + '2' + "日")          # 31日跨月

    elif date[1] in [4,6,9,11] :
        if date[2] < 29 and date[1] < 12:
            print(str(date[0]) + "年" + str(date[1]) + "月" + str(date[2] + 2) + "日")  #29日月内
        elif  date[2] == 29 and date[1] < 12:
            print(str(date[0]) + "年" + str(date[1]+1) + "月" + '1' + "日")             #29日跨月
        elif  date[2] == 30 and date[1] < 12:
            print(str(date[0]) + "年" + str(date[1] + 1) + "月" + '2' + "日")           #30日跨月
        elif  date[2] >30  :
            print("请重新输入：")


                                              # 平年、28天
    elif date[0] % 100 == 0 and date[0] % 400 != 0 or date[0] % 4 != 0 :
        if date[1] ==2 and date[2] < 27 :     #27日月内
            print(str(date[0]) + "年" + str(date[1]) + "月" + str(date[2] + 2) + "日")
        elif date[1] == 2 and date[2] == 27:  # 27日跨月
            print(str(date[0]) + "年" + '3' + "月" + '1' + "日")
        elif date[1] == 2 and date[2] == 28:  # 28日跨月
            print(str(date[0]) + "年" + '3' + "月" + '2' + "日")
        elif date[1] == 2 and date[2] > 28:  # 28日跨月
            print('请重新输入')


                                               #闰年、29天
    elif date[0] % 400 == 0 or date[0] % 4 == 0:
        if date[1] ==2 and date[2] < 28:         #28日月内
            print(str(date[0]) + "年" + '2' + "月" + str(date[2] + 2) + "日")
        elif date[1] ==2 and date[2] == 28  :    #28日跨月
            print(str(date[0]) + "年" + '3' + "月" + '1' + "日")
        elif date[1] == 2 and date[2] == 29:     #29日跨月
            print(str(date[0]) + "年" + '3' + "月" + '2' + "日")
        elif date[1] == 2 and date[2] > 29:  # 错误
            print('请重新输入')

    elif date[0]=='' or date[1]=='' or date[2]=='' :
        print("请重新输入")
    del date[-3:]
if __name__ == '__main__':
    print("请输入按照年月日顺序输入日期(仅数字），回车结束：")
    input_date()
    while(True):
        input_date()
