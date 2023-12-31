# csv 2개를 하나의 csv 합치는 예제
import csv

with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA :
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singerSum.csv", "w", newline='') as outFp:
            # csv 모듈의 함수를 이용해서, 읽기 및 쓰기 작업을 함
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)

            # 2개의 csv파일의 구조가 동일해서 
            # 헤더가 동일해, 덮어쓰기
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            # csv 파일을 쓰는 작업
            csvWriter.writerow(header_list)


            # 2행부터 실제 데이터 값
            # csv 첫번째 파일을 쓰기
            # csv 파일 
            for row_list in csvReaderA:
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')