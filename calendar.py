import Report_day_lib
import Report_day_oop

def main():

    year, month, day = Report_day_lib.input_date()                              #날짜를 입력하는 함수
    total_days = Report_day_lib.calculate_total_days(year, month, day)          #총 일 수를 구하는 함수
    day_name = Report_day_lib.calculate_day_name(total_days)                    #요일을 구하는 함수

    print(f"{year}년 {month}월 {day}일은 {day_name} 입니다.")

if __name__ == "__main__":
    main()
