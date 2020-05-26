class DayCalculator(object):
    
    def is_leap(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True 
        else:
            return False

    @classmethod
    def daycalculator(year, month, day):
    
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