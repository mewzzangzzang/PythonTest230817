
# csv 파일을 읽어서 , 메모리상 infp라는 인스턴스에 잠시 저장

inFp = open("C:/CookAnalysis/CSV/singer1.csv", "r")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()