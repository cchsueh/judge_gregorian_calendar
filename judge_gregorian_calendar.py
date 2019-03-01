def is_leap(year):
    if (year % 4) != 0:
        return False
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 100 == 0) and (year % 400 != 0):
        return False
    elif (year % 400 == 0) and (year % 3200 != 0):
        return True

if __name__ == '__main__':
    year = input('請輸入要查詢的年份： ')
    year = int(year)
    leap = is_leap(year)
    if leap == True:
        print(year, '年為潤年')
    else:
        print(year, '年為平年')