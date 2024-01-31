# 1번 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력

import matplotlib.pyplot as plt
import csv
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result1 = []
    total_number = 0
    max_num=-1
    max_station = ''

    for row in data:
        if row[1] == '1호선':
            row[5:] = map(int, row[5:])
            row_sum1 = row[11] + row[13]
            result1.append(row_sum1)
            if row_sum1 > max_num:
                max_num = row_sum1
                name_line = row[1]
                max_station = row[3]
    print(f'출근 시간대 {name_line} 최대 하차역: {max_station}역, 하차인원: {max_num:,}명')


with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result2 = []
    total_number = 0
    max_num=-1
    max_station = ''

    for row in data:
        if row[1] == '2호선':
            row[5:] = map(int, row[5:])
            row_sum2 = row[11] + row[13]
            result2.append(row_sum2)
            if row_sum2 > max_num:
                max_num = row_sum2
                name_line = row[1]
                max_station = row[3]
    print(f'출근 시간대 {name_line} 최대 하차역: {max_station}역, 하차인원: {max_num:,}명')

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result3 = []
    total_number = 0
    max_num=-1
    max_station = ''

    for row in data:
        if row[1] == '3호선':
            row[5:] = map(int, row[5:])
            row_sum3 = row[11] + row[13]
            result3.append(row_sum3)
            if row_sum3 > max_num:
                max_num = row_sum3
                name_line = row[1]
                max_station = row[3]
    print(f'출근 시간대 {name_line} 최대 하차역: {max_station}역, 하차인원: {max_num:,}명')

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result4 = []
    total_number = 0
    max_num=-1
    max_station = ''

    for row in data:
        if row[1] == '4호선':
            row[5:] = map(int, row[5:])
            row_sum4 = row[11] + row[13]
            result4.append(row_sum4)
            if row_sum4 > max_num:
                max_num = row_sum4
                name_line = row[1]
                max_station = row[3]
    print(f'출근 시간대 {name_line} 최대 하차역: {max_station}역, 하차인원: {max_num:,}명')

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result5 = []
    total_number = 0
    max_num=-1
    max_station = ''

    for row in data:
        if row[1] == '5호선':
            row[5:] = map(int, row[5:])
            row_sum5 = row[11] + row[13]
            result5.append(row_sum5)
            if row_sum5 > max_num:
                max_num = row_sum5
                name_line = row[1]
                max_station = row[3]
    print(f'출근 시간대 {name_line} 최대 하차역: {max_station}역, 하차인원: {max_num:,}명')

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result6 = []
    total_number = 0
    max_num=-1
    max_station = ''

    for row in data:
        if row[1] == '6호선':
            row[5:] = map(int, row[5:])
            row_sum6 = row[11] + row[13]
            result6.append(row_sum6)
            if row_sum6 > max_num:
                max_num = row_sum6
                name_line = row[1]
                max_station = row[3]
    print(f'출근 시간대 {name_line} 최대 하차역: {max_station}역, 하차인원: {max_num:,}명')

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result7 = []
    total_number = 0
    max_num=-1
    max_station = ''

    for row in data:
        if row[1] == '7호선':
            row[5:] = map(int, row[5:])
            row_sum7 = row[11] + row[13]
            result7.append(row_sum7)
            if row_sum7 > max_num:
                max_num = row_sum7
                name_line = row[1]
                max_station = row[3]
    print(f'출근 시간대 {name_line} 최대 하차역: {max_station}역, 하차인원: {max_num:,}명')



plt.figure(figsize=(10,4))
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.bar(range(len(result2)), result2)
plt.show()

