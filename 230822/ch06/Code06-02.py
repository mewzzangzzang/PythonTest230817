# 파일, 입력 또는 출력을 위한 인스턴스를 사용 후, 반납(메모리)
# with ~ as 구문은, 자동으로 해당 인슨턴스를 반납.
with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :

    inStr = inFp.readline()
    print(inStr, end = "")

    inStr = inFp.readline()
    print(inStr, end = "")
