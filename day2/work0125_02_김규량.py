# 2번 지하철 각 노선별 퇴근 시간대 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력
import matplotlib.pyplot as plt
import csv
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result = []
    total_number = 0
    max_num = -1
    max_station = ''

    for row in data:
        row[5:] = map(int, row[5:])
        row_sum = row[35] + row[37]
        result.append(row_sum)
        if row_sum > max_num:
            max_num = row_sum
            max_station = row[3]
            if max_station == max_station:
                max_num += max_num

    print(f'{max_station}: {max_num:,}')