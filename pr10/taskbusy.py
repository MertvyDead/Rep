


 
busy = [
{'start' : '10:30',
'stop' : '10:50'
},
{'start' : '18:40',
'stop' : '18:50'
},
{'start' : '14:40',
'stop' : '15:50'
},
{'start' : '16:40',
'stop' : '17:20'
},
{'start' : '20:05',
'stop' : '20:20'
}
]

# a = sorted(busy, key= lambda x:(x['start']))


# def bs_time(a):
#     return [dt.datetime.strptime(i['start'],'%H:%M').strftime('%H:%M') for i in a]



# print(*bs_time(a), sep='\n')



# # Доктор принимает с 9 до 21 00

# # Найти свободные окна по 30 минут
from datetime import *

busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

busy_times = []
for b in busy:
    start_time = datetime.strptime(b['start'], '%H:%M').strftime('%H:%M')
    stop_time = datetime.strptime(b['stop'], '%H:%M').strftime('%H:%M')
    busy_times.append((start_time, stop_time))

busy_times.sort(key=lambda x: x[0])

# free_windows = []
# start_time = datetime.strptime('09:00', '%H:%M').strftime('%H:%M')
# end_time = datetime.strptime('21:00', '%H:%M').strftime('%H:%M')

# for busy_start, busy_stop in busy_times:
#     if start_time < busy_start:
#         free_windows.append((start_time, busy_start))
#     start_time = busy_stop
    
print(busy_times)

# if start_time < end_time:
#     free_windows.append((start_time, end_time))

# for window in free_windows:
#     if (window[1] - window[0]) >= timedelta(minutes=30):
#         print(f"Free window from {window[0].strftime('%H:%M')} to {window[1].strftime('%H:%M')}")
# print(free_windows)