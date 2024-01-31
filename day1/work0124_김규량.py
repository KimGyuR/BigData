"""
2. 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 최고 기온 및 최저
기온의 평균값을 구하고 그래프로 표현
"""
"""

"""
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd

def draw_two_plots(title, x_data, max_temp_list1, label_y1, max_temp_list2, label_y2):

    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10,4))
    plt.plot(x_data, max_temp_list1, marker='s', markersize=6, color='b', label=label_y1)
    plt.plot(x_data, max_temp_list2, marker='s', markersize=6, color='r', label=label_y2)
    plt.xticks(x_data)

    plt.title(title)
    plt.legend()
    plt.show()

def main():
    start_year = int(input("시작 연도를 입력하세요: "))
    last_year = int(input("마지막 연도를 입력하세요: "))
    change_month = int(input("기온 변화를 측정한 달을 입력하세요: "))

    weather_df = pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')

    change0_month_min_temp_list = [0] * 10
    change1_month_max_temp_list = [0] * 10

    for year in range(10):
        change0_month_df = weather_df[(weather_df['날짜'].dt.year == start_year + year) &
                                        (weather_df['날짜'].dt.month == change_month)]
        change0_month_min_temp_list[year] = round(change0_month_df['최저기온'].mean(), 1)

        change1_month_df = weather_df[(weather_df['날짜'].dt.year == last_year + year) &
                                        (weather_df['날짜'].dt.month == change_month)]
        change1_month_max_temp_list[year] = round(change1_month_df['최고기온'].mean(), 1)

    print(f'{start_year}년부터 {last_year}년까지 {change_month}월의 기온 변화')
    print(f'{change_month}월 최저기온 평균: {change0_month_min_temp_list}')
    print(f'{change_month}월 최고기온 평균: {change1_month_max_temp_list}')

    start_year_low_temp_mean = round(sum(change0_month_min_temp_list) /
                                        len(change0_month_min_temp_list), 1)
    last_year_high_temp_mean = round(sum(change1_month_max_temp_list) /
                                        len(change1_month_max_temp_list), 1)

    x_data = [i for i in range(start_year, last_year, 1)]
    draw_two_plots(f'{start_year}년부터 {last_year}년까지 {change_month}월의 기온 변화', x_data,
                   change0_month_min_temp_list, str(start_year)+'년대',
                   change1_month_max_temp_list, str(last_year)+'년대')

main()