def input_date():
    year = int(input("년도를 입력하세요: "))
    month = int(input("월을 입력하세요: "))
    day = int(input("일을 입력하세요: "))
    return year, month, day


def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True 
    else:
        return False


def calculate_day_name(total_days):
    day_names = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
    return day_names[total_days % 7]


def calculate_total_days(year, month, day):
    date = {'year': year, 'month': month, 'day': day}
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
    total_days = 0

        # 직전년도까지의 총 일 수 계산
    for i in range(1, date["year"]):
        if is_leap(i):
            total_days = total_days + 366
        else:
            total_days = total_days + 365

    for i in range(1, date["month"]):
        total_days = total_days + month_days[i]

    if is_leap(date["year"]) and date["month"] >= 3:
        total_days = total_days + 1

    total_days = total_days + day
    return total_days