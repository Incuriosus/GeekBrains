duration = int(input('Введите кол-во секунд: '))
s_in_m = 60
s_in_h = s_in_m*60
s_in_d = s_in_h*24
s_in_y = s_in_d*365
s_in_mon = s_in_y // 12
years = duration // s_in_y
months = duration % s_in_y // s_in_mon
days = duration % s_in_y % s_in_mon // s_in_d
hours = duration % s_in_y % s_in_mon % s_in_d // s_in_h
minutes = duration % s_in_y % s_in_mon % s_in_d % s_in_h // s_in_m
seconds = duration % s_in_m
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
