# 파일 읽고 쓰기
# 파일 읽기
with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    # 파일 쓰기
    with open("C:/CookAnalysis/CSV/new_singer230822.csv", "w") as outFp:
        # infp : csv 파일을 읽은 내용을 담은 임시 인스턴스, 한줄 읽기
        header = inFp.readline()
        # 공백제거
        header = header.strip()
        # split 분리
        header_list = header.split(',')
        # map함수 첫번째 str 함수 : 문자열로 변경하는 함수
        # 두번째 인자 header_list 리스트 요소를 하나씩 꺼내서 문자열화
        # 마지막 join함수를이용해서 콤마로 합치기
        header_str = ','.join(map(str, header_list))
        # print(f"{header_str}")

        # csv에 쓰는 작업, outFp인스턴스
        outFp.write(header_str + '\n')
        # 2번째 행부터는 실제 데이터 값을 쓰는 작업
        # inFp : csv 파일의 내용을 담고 있는 인스턴스
        for inStr in inFp:
            # 한줄씩 읽고, 양쪽 공백 제거
            inStr = inStr.strip()
            row_list = inStr.split(',')
            print(f"row_list 출력 :{row_list}")
            #row_list[-1] 리스트의 마지막 부분 /로 바꾸기
            row_list[-1] = row_list[-1].replace('.', '/')
            # 리스트의 뒤에서 두번째 값을 int로 정수화
            # 실수형으로 소수점 둘째자리 확인 필요
            height_str = "{0:.2f}".format(int(row_list[-2]))
            # 키에 값에 소수점으로 표기한 형식으로 재할당
            row_list[-2] = height_str
            print(f"height_str 출력 :{height_str}")
            # row_list의 요소를 하나씩 꺼내어서, str함수를 이용해 문자열화
            row_str = ','.join(map(str, row_list))
            # 해당 csv파일에 쓰기
            outFp.write(row_str + '\n')

print('Save. OK~')