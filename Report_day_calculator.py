import Report_day_lib
import Report_day_oop

def main():

    day_calculator = Report_day_oop.DayCalculator()
    year, month, day = Report_day_lib.input_date()
    day_name = day_calculator.ask(year, month, day)


    print(f"{year}년 {month}월 {day}일은 {day_name} 입니다.")