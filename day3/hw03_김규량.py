import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

plt.figure(figsize=(10,10))
with open('gender.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    population = []
    city_list = ['대구광역시', '대구광역시 중구', '대구광역시 동구',
                '대구광역시 서구', '대구광역시 남구', '대구광역시 북구',
                '대구광역시 수성구', '대구광역시 달서구', '대구광역시 달성군']
    j = 0
    list1=[]
    for city in city_list:
        male_count = 0
        female_count = 0
        j += 1
        for row in data:
            if city in row[0]:
                for i in range(106, 207):
                    male_count += int(row[i].replace(',', ''))
                    female_count += int(row[i+103].replace(',', ''))
                list1.append([male_count,female_count])
                break
        plt.subplot(3,3,j)
        plt.pie(list1[j-1], labels=['남', '여'], autopct='%.1f%%', startangle=90)
        plt.suptitle("대구광역시 구별 남녀 인구 비율", size=25)
        plt.title(city)
    plt.show()