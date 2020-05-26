def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    year = int(input("년도를 입력하세요: "))
    month = int(input("월을 입력하세요: "))
    day = int(input("일을 입력하세요: "))

    date = {'year': year, 'month': month, 'day': day}
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_names = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
    total_days = 0

    # 직전년도까지의 총 일 수 계산
    for i in range(1, date["year"]):
        if is_leap(i):
            total_days = total_days + 366
        else:
            total_days = total_days + 365

    for i in range(1, date["month"]):
        total_days = total_days + month_days[i]

    if date["year"] % 4 == 0:
        if date["year"] % 100 == 0:
            if date["year"] % 400 == 0:
                if date["month"] >= 3:
                    total_days = total_days + 1
            else:
                pass
        else:
            if date["month"] >= 3:
                total_days = total_days + 1
    else:
        pass

    total_days = total_days + day

    print(
        f"{date['year']}년 {date['month']}월 {date['day']}일은 {day_names[total_days % 7]} 입니다.")


if __name__ == "__main__":
    main()
