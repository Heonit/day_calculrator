year = int(input("년도를 입력하세요: "))
month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))

date = {'year': year, 'month': month, 'day': day}

total_days = 0

for i in range(1, date["year"]):
    if i % 4 == 0: 
        if i % 100 == 0:
            if i % 400 == 0:
                total_days = total_days + 366
            else:
                total_days = total_days + 365
        else: 
            total_days = total_days + 366
    else:
        total_days = total_days + 365

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, date["month"]):
    total_days = total_days + month_days[i]

if date["year"] % 4 == 0: 
    if date["year"] % 100 == 0:
        if date["year"] % 400 == 0:
            if date["month"] >= 3:
                total_days = total_days + 1
        else:
            total_days = total_days + 0
    else: 
        if date["month"] >= 3:
            total_days = total_days + 1
else:
    total_days = total_days + 0

total_days = total_days + day

#print(total_days)
print(total_days%7)
