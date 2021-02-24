duration = int(input('Введите кол-во секунд: '))
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sec_list = [31536000, 86400, 3600, 60]
time = []
i = 0
while i < 4:
    counter = duration // sec_list[i]
    time.append(counter)
    duration -= counter*sec_list[i]
    if i == 1:
        if counter >= 31:
            days_summ = 0
            for m in range(len(month_list) - 1):
                days_summ += month_list[m]
                if counter == days_summ:
                    time[i] = m + 1
                    time.append(0)
                    break
                elif counter < days_summ:
                    time[i] = m
                    time.append(counter - days_summ + month_list[m])
                    break
        else:
            time.append(counter)
            time[i] = 0
    i += 1
else:
    time.append(duration)

if time[0]:
    print(time[0], 'y, ', time[1], 'm, ', time[2], "d, ", time[3], 'h, ', time[4], 'm, ', time[5], 's')
elif time[1]:
    print(time[1], 'm, ', time[2], "d, ", time[3], 'h, ', time[4], 'm, ', time[5], 's')
elif time[2]:
    print(time[2], "d, ", time[3], 'h, ', time[4], 'm, ', time[5], 's')
elif time[3]:
    print(time[3], 'h, ', time[4], 'm, ', time[5], 's')
elif time[4]:
    print(time[4], 'm, ', time[5], 's')
else:
    print(time[5], 's')


