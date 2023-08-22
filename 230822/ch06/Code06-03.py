# 함수, 매개변수(리스트), 반환값은 없는 함수

def printList(pList) :
    for data in pList :
        print(data, end='\t')
    print()

# 자동 닫는 버전으로, 인스턴스 생성(csv 파일 내용을 읽은 임시 저장내용(메모리))
with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    # 첫 행은: 해당 컬럼
    header = inFp.readline()
    # 헤더 부분의 양쪽 공백 제거
    header = header.strip()
    # 헤더의 내용을 split
    header_list = header.split(',')
    printList(header_list)
    # csv 읽은 인스턴스에서 하나씩 가져와서
    # 1번째
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        printList(row_list)