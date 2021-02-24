duration = int(input('Введите кол-во секунд: '))
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
s_in_m = 60
s_in_h = s_in_m*60
s_in_d = s_in_h*24
s_in_y = s_in_d*365
years = duration // s_in_y
days = duration % s_in_y // s_in_d
hours = duration % s_in_y % s_in_d // s_in_h
minutes = duration % s_in_y % s_in_d % s_in_h // s_in_m
seconds = duration % s_in_m
months = 0
if days >= 31:
    days_summ = 0
    for i in range(len(month_list)-1):
        days_summ += month_list[i]
        if days == days_summ:
            months = i+1
            days = 0
            break
        elif days < days_summ:
            months = i
            days = days - days_summ + month_list[i]
            break
if years:
    print(years, 'y, ', months, 'm, ', days, "d, ", hours, 'h, ', minutes, 'm, ', seconds, 's')
elif months:
    print(months, 'm, ', days, "d, ", hours, 'h, ', minutes, 'm, ', seconds, 's')
elif days:
    print(days, "d, ", hours, 'h, ', minutes, 'm, ', seconds, 's')
elif hours:
    print(hours, 'h, ', minutes, 'm, ', seconds, 's')
elif minutes:
    print(minutes, 'm, ', seconds, 's')
else:
    print(seconds, 's')
