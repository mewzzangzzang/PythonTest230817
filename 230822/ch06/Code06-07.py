import csv
# csv 콤마 기준으로 값을 나열하는 구조
# 값의 타입이 문자열 안에 콤마 형식을 처리하는 부분
with open("C:/CookAnalysis/CSV/singer2.csv", "r") as inFp :
    csvReader = csv.reader(inFp)
    header_list = next(csvReader)
    print(header_list[1],header_list[6])
    for row_list in csvReader:
        youtube = int(row_list[6].replace(',',''))
        youtube = int(youtube/10000)
        print(row_list[1], str(youtube)+"만")