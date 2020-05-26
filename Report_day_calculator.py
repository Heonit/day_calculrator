import Report_day_lib
import Report_day_oop

def main():

    day_calculator = Report_day_oop.daycalculator()                             #총 일수를 계산하는 함수
    year, month, day = Report_day_lib.input_date()                              #날짜를 입력하는 함수
    day_name = day_calculator.ask(year, month, day)                             #요일을 묻는 함수

    print(f"{year}년 {month}월 {day}일은 {day_name} 입니다.")
    
if __name__ == "__main__":
    main()