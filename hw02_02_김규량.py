country = {'Seoul': ['South Korea', 'Asia', 9655000],
           'Tokyo': ['Japan', 'Asia', 14110000],
           'Beijing': ['China', 'Asia', 21540000],
           'London': ['United Kingdom', 'Europe', 14800000],
           'Berlin': ['Germany', 'Europe', 3426000],
           'Mexico City': ['Mexico', 'America', 21200000]}
while True:
    print('----------------------------------------------')
    print('1. 전체 데이터 출력')
    print('2. 수도 이름 오름차순 출력')
    print('3. 모든 도시의 인구수 내림차순 출력')
    print('4. 특정 도시의 정보 출력')
    print('5. 대륙별 인구수 계산 및 출력')
    print('6. 프로그램 종료')
    print('----------------------------------------------')

    menu = int(input('메뉴를 입력하세요: '))
    idx = 1
    # 1 전체 데이터 출력
    if menu == 1:
        for k,v in country.items():
            print(f'{[idx]} {k}: {v}')
            idx += 1

    # 2 수도 이름 오름차순 출력
    elif menu == 2:
        for k,v in sorted(country.items()):
            print(f'{[idx]} {k:<10s}: {v[0]:<15s} {v[1]:<12s} {v[2]:,}')
            idx += 1

    # 3 모든 도시의 인구수 내림차순 출력
    elif menu == 3:
        for k,v in sorted(country.items(), reverse=True):
            print(f'{[idx]} {k:<10s}: {v[2]:,}')
            idx += 1

    # 4 특정 도시의 정보 출력
    elif menu == 4:
        city = input('출력할 도시 이름을 입력하세요: ')
        if city == 'Seoul' or city == 'Tokyo' or city == 'Beijing' or city == 'London' or city == 'Berlin' or city == 'Mexico City':
            print(f"도시:{city}\n국가:{country[city][0]} , 대륙: {country[city][1]}, 인구수: {country[city][2]}")
        else:
            print(f'도시이름: 은(는) key에 없습니다.')

    # 5 대륙별 인구수 계산 및 출력
    elif menu == 5:
        total = 0
        earth = input('대륙 이름을 입력하세요(Asia, Europe, America): ')
        if earth == 'Asia' or earth == 'Europe' or earth == 'America':
            for city in country.keys():
                if country[city][1] == earth:
                    print(f'{city}: {country[city][2]:,}')
                    total += country[city][2]
            print(f'{earth} 전체 인구수: {total:,}')
        else:
            print('잘못 입력되었습니다.')

    # 6 프로그램 종료
    elif menu == 6:
        print('프로그램을 종료합니다.')
        break;
    else:
        print('다시 입력해주세요.')