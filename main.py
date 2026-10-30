#import json

class Transaction:
    def __init__(self,id, date, type, category, amount, memo, tags):
        self.id = id
        self.dateStr = date
        self.type = type
        self.category = category
        self.amount = amount  # Initialize amount to 0
        self.memo = memo
        self.tags = tags
        
        
#transactionList = []

class BudgetData:
    def __init__(self, yearMonth, amount):
        self.yearMonthStr=yearMonth
        self.amount=amount


#입력받은 문자열을 숫자만 남기기;
def TransformIdStringToNumber(idString):
    #앞에 Tx-제거;
    if idString.startswith("TX-"):
        idString = idString[3:]

    #0이 아닌 숫자 나올때까지 앞에서 부터 제거;
    idString = idString.lstrip("0")

    #남은 문자열 값이 없으면 0;
    if not idString:
        idString = "0"

    #남은 문자열=>인트;
    return int(idString)


#숫자=>문자열;
def TransformIdNumberToString(idNumber):
    #스트링으로 변환;
    idString = str(idNumber)

    #자릿수가 6보다 작으면;
    if len(idString) < 6:
        #앞에 0추가;
        #idString = idString.zfill(6)
        while len(idString) < 6:
            #앞에 0추가;
            idString = "0" + idString

    #앞에 Tx-추가;
    return "TX-" + idString


#아이디 입력 오류 판단();
def CheckIdStringFormat(idString):
    alarmStr="정상"
    #아이디 부분의 문자열을 -로 나눴을때;
    parts = idString.split("-")
    if len(parts) != 2:
        alarmStr="잘못된 아이디 형식입니다."
        return alarmStr

    prefix, number = parts
    #앞이 TX가 아니거나;
    if prefix != "TX":
        alarmStr="잘못된 아이디 형식입니다."
        return alarmStr

    #뒷 부분이 숫자가 아니거나;
    if not number.isdigit():
        alarmStr="잘못된 아이디 형식입니다."
        return alarmStr

    #뒷 부분 자릿수가 6자리보다 작으면;
    if len(number) < 6:
        alarmStr="잘못된 아이디 형식입니다."
        return alarmStr

    return alarmStr



#숫자=>문자열;
#def ConvertIdNumberToString(idNumber):
#    #길이가 6보다 짧으면 차이만큼 앞에 0 추가;
#    id_str = str(idNumber)
#    if len(id_str) < 6:
#        id_str = '0' * (6 - len(id_str)) + id_str
    
#    #앞에 TX-추가;
#    return "TX-" + id_str

##문자열=>숫자;
#def ConvertIdStringToNumber(idString):
#    #앞에 TX-제거;
#    if idString.startswith("TX-"):
#        idString = idString[3:]

#    #앞에서부터 0이면 제거;
#    idString = idString.lstrip("0")

#    #문자열로 저장;
#    idNumber = int(idString) if idString else 0

#    #문자열=>숫자;
#    return idNumber


#from pathlib import Path
## 파일 경로를 저장할 전역 변수 (기본값은 현재 디렉토리)
#_file_path = Path(".")
## 설정값을 저장할 jsonl 파일명
#CONFIG_FILE = "config.jsonl"



# 1. 저장하기
#def saveLastUsedId(last_used_id):
#    with open("last_used_id.jsonl", "w", encoding="utf-8") as file:
#        data = {"last_used_id": last_used_id}
#        file.write(json.dumps(data) + '\n')

## 2. 불러오기
#def loadLastUsedId():
#    try:
#        with open("last_used_id.jsonl", "r", encoding="utf-8") as file:
#            line = file.readline()  # JSONL의 첫 번째 줄(최신 값) 읽기
#            if line:
#                data = json.loads(line)
#                return data.get("last_used_id", 0)
#            return 0
#    except (FileNotFoundError, json.JSONDecodeError):
#        return 0



#def searchByFromTo(start_date, end_date):
#    results = []
#    for transaction in transactionList:
#        if start_date <= transaction.date <= end_date:
#            results.append(transaction)
#    PrintList(results)

#def searchByCategory(category):
#    results = []
#    for transaction in transactionList:
#        if transaction.category == category:
#            results.append(transaction)
#    PrintList(results)

#def searchByType(type):
#    results = []
#    for transaction in transactionList:
#        if transaction.type == type:
#            results.append(transaction)
#    PrintList(results)

#def searchByMemo(memo):
#    results = []
#    for transaction in transactionList:
#        if memo in transaction.memo:
#            results.append(transaction)
#    PrintList(results)

#def searchByTag(tag):
#    results = []
#    for transaction in transactionList:
#        if tag in transaction.tags:
#            results.append(transaction)
#    #return results
#    PrintList(results)


#def PrintList(transactions):
#    for transaction in transactions:
#        print(f"ID: {transaction.id}, Date: {transaction.date}, Category: {transaction.category}, Type: {transaction.type}, Memo: {transaction.memo}, Tags: {', '.join(transaction.tags)}")
#        print("-" * 50)
        


#import json
import os

#날짜값으로 내림차순 삽입;
#새 jsonl 파일에 데이터를 쓰고;
#기존 파일을 지우고, 만들어진 파일 이름을 변경;
#def insert_transaction_by_date(new_tx):
#    filename="transactions.jsonl"
#    # 임시 파일 이름 설정
#    output_filename = filename + ".tmp"
#    inserted = False
    
#    try:
#        with open(filename, 'r', encoding='utf-8') as oldFile, \
#             open(output_filename, 'w', encoding='utf-8') as newFile:
            
#            for oldLine in oldFile:
#                line_str = oldLine.strip()
#                if not line_str:
#                    continue
                    
#                old_data = json.loads(line_str)
                
#                # 새 거래 날짜가 기존 데이터보다 최신이면 먼저 삽입
#                if not inserted and new_tx.date > old_data['date']:
#                    newFile.write(json.dumps(new_tx.__dict__, ensure_ascii=False) + '\n')
#                    inserted = True
                
#                newFile.write(oldLine)
                
#            # 새 거래가 가장 과거 날짜면 맨 마지막에 추가
#            if not inserted:
#                newFile.write(json.dumps(new_tx.__dict__, ensure_ascii=False) + '\n')
                
#        # [핵심] 임시 파일을 원본 파일 이름으로 변경 (기존 원본은 자동으로 제거 및 대체됨)
#        os.replace(output_filename, filename)
        
#    except FileNotFoundError:
#        # 만약 원본 파일이 아예 없던 상태라면, 새 파일로 바로 생성
#        with open(filename, 'w', encoding='utf-8') as newFile:
#            newFile.write(json.dumps(new_tx.__dict__, ensure_ascii=False) + '\n')

def CheckCategoryExistInTransactionList(category):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')

    #거래 리스트 생성;
    FileIO.transactionList=[]
    
    #통합 파일의 데이터를 한줄씩 거래로 변환해서 리스트에 담기;
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            oldTx=TransformLineToTx(txLine)
            
            FileIO.transactionList.append(oldTx)
                            
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break
    
    
    #print("category : " +category)
    categoryBeingUsed=False
    for index in range(len(FileIO.transactionList)):
        #print(FileIO.transactionList[index].category)
        if FileIO.transactionList[index].category == category:
            categoryBeingUsed=True
            break
    
    return categoryBeingUsed


def AddTransaction(newTransaction):
    #global largestUsedId
    ##최근 아이디값+1로 할당
    #largestUsedId+=1
    #newTransaction.id = largestUsedId
    #saveLastUsedId(lastUsedIdNumber)  # Save the updated last used ID to

    InsertNewTransaction(newTransaction)
    
    #transactionList.insert(0, newTransaction)
    #saveAllTransactionData()
    print(f"[저장 완료] id={TransformIdNumberToString(newTransaction.id)}")

def InsertNewTransaction(newTx):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')

    #global largestUsedId
    #global transactionList
    
    #거래 리스트 생성;
    #transactionList: list[Transaction]
    FileIO.transactionList=[]
    
    #통합 파일의 데이터를 한줄씩 거래로 변환해서 리스트에 담기;
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            oldTx=TransformLineToTx(txLine)
            
            FileIO.transactionList.append(oldTx)
                            
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break
    
    
    isInserted=False
    index:int
    for index in range(len(FileIO.transactionList)):
        #임포트할 거래값보다 통합 리스트의 날짜값이 과거면;
        if TransformStrToDate(newTx.dateStr) > TransformStrToDate(FileIO.transactionList[index].dateStr):
            
            FileIO.largestUsedId+=1
            newTx.id=FileIO.largestUsedId
            #그 위치에 삽입;
            FileIO.transactionList.insert(index, newTx)
            isInserted=True
            break
    
    if isInserted == False:
        FileIO.largestUsedId+=1
        newTx.id=FileIO.largestUsedId
        FileIO.transactionList.append(newTx)

    #print("transactionList length : "+str(len(transactionList)))

    #통합 리스트=>새 파일; 기존 파일명 사용, 기존 파일 제거;
    FileIO.SaveTxListToJsonFile(FileIO.transactionList)




def UpdateTransaction(tmpTx):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')

    
    #경고문=""
    #noIdStr=""
    #거래 리스트 생성;
    #global transactionList
    FileIO.transactionList=[]
    idExist=False
    txToInsert=None
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            oldTx=TransformLineToTx(txLine)
            #아이디값이 일치하면;
            if oldTx.id == tmpTx.id:
                #PrintTransaction(tx)
                #인풋 거래값을 리스트에 추가;
                if tmpTx.dateStr != "":
                    oldTx.dateStr = tmpTx.dateStr
                if tmpTx.type != "":
                    oldTx.type = tmpTx.type
                if tmpTx.category != "":
                    oldTx.category = tmpTx.category
                if tmpTx.amount != "":
                    oldTx.amount = tmpTx.amount
                if tmpTx.memo != "":
                    oldTx.memo = tmpTx.memo
                #if not tmpTx.tags:
                if tmpTx.tags != []:
                    oldTx.tags = tmpTx.tags

                #FileIO.transactionList.append(oldTx)
                txToInsert=oldTx
                #아이디 존재=트루
                idExist=True
                #루프 종료하면 안됨!;
                #break
            #아이디값이 일치하지 않으면; 
            else:
                #기존파일의 거래값을 리스트에 저장;
                FileIO.transactionList.append(oldTx)
                
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break


    #아이디 존재==트루면;
    if idExist == True:
        isInserted=False
        for index in range(len(FileIO.transactionList)):
            #임포트할 거래값보다 통합 리스트의 날짜값이 과거면;
            if TransformStrToDate(txToInsert.dateStr) > TransformStrToDate(FileIO.transactionList[index].dateStr):
                #그 위치에 삽입;
                FileIO.transactionList.insert(index, txToInsert)
                isInserted=True
                break
        if isInserted == False:
            FileIO.transactionList.append(txToInsert)
        
        
        #리스트=>새 거래파일; 올드 거래파일 이름을 새 파일로, 올드 파일 제거;
        FileIO.SaveTxListToJsonFile(FileIO.transactionList)
        #InsertNewTransaction(txToInsert)
        print(f"[수정 완료] id={TransformIdNumberToString(tmpTx.id)}")

    #아이디 존재==펄스면; 
    #else:
    #경고문="아이디가 존재하지 않습니다"; 리턴;
    return idExist


def DeleteTransaction(tmpTx):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')

    #거래 리스트 생성;
    #global transactionList
    FileIO.transactionList=[]
    idExist=False
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            oldTx=TransformLineToTx(txLine)
            #아이디값이 일치하면;
            if oldTx.id == tmpTx.id:
                #아이디 존재=트루
                idExist=True
                #루프 종료하면 안됨!;
                #break
            #아이디값이 일치하지 않으면; 
            else:
                #기존파일의 거래값을 리스트에 저장;
                FileIO.transactionList.append(oldTx)
                
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break


    #아이디 존재==트루면;
    if idExist == True:
        #리스트=>새 거래파일; 올드 거래파일 이름을 새 파일로, 올드 파일 제거;
        FileIO.SaveTxListToJsonFile(FileIO.transactionList)
        print(f"[삭제 완료] id={TransformIdNumberToString(tmpTx.id)}")

    #아이디 존재==펄스면; 
    #else:
    #경고문="아이디가 존재하지 않습니다"; 리턴;
    return idExist

#largestUsedId=-1
##사용된 최대 아이디값 불러오기();
#def LoadLargestUsedId():
#    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')
#    global largestUsedId
    
#    while True:
#        try:
#            # 다음 거래 정보를 수동으로 1개 가져옴.
#            txLine = next(oldFileTx_stream)
#            #파일에서 읽어온 라인을 거래로 변환;
#            oldTx=TransformLineToTx(txLine)
#            #사용된 최대 아이디값 선별해 놓기;
#            if oldTx.id > largestUsedId:
#                largestUsedId=oldTx.id
                
#        except StopIteration:
#            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
#            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
#            break






def ExportTransactionByFromTo(newFilePath, fromDateStr, toDateStr):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')

    #거래 리스트 생성;
    #global transactionList
    FileIO.transactionList=[]
    count=0
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            oldTx=TransformLineToTx(txLine)
            
            #print(f"oldTx.dateStr : {oldTx.dateStr}, fromDateStr : {fromDateStr}, toDateStr : {toDateStr}")
            #날짜가 범위 내면;
            if TransformStrToDate(fromDateStr) <= TransformStrToDate(oldTx.dateStr) <= TransformStrToDate(toDateStr):
                FileIO.transactionList.append(oldTx)
                count+=1

        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break


    #거래 존재==트루면;
    if count > 0:
        #리스트=>새 거래파일; 올드 거래파일 이름을 새 파일로, 올드 파일 제거;
        FileIO.SaveTxListToJsonFile(FileIO.transactionList, newFilePath)

    #경고문="아이디가 존재하지 않습니다"; 리턴;
    return count

def ExportTransactionsByMonth(newFilePath, yearMonthStr):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')

    #거래 리스트 생성;
    #여기 수정;
    #global transactionList
    FileIO.transactionList=[]
    #txExist=False
    count=0
    
    yearStr=yearMonthStr.split("-")[0]
    monthStr=yearMonthStr.split("-")[1]
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            oldTx=TransformLineToTx(txLine)
            
            yearStrOfOldTx=oldTx.dateStr.split("-")[0]
            monthStrOfOldTx=oldTx.dateStr.split("-")[1]
            
            
            #날짜가 범위 내면;
            if yearStr == yearStrOfOldTx and monthStr == monthStrOfOldTx:
                FileIO.transactionList.append(oldTx)
                #txExist=True
                count+=1
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break


    #거래 존재==트루면;
    if count > 0:#txExist == True:
        #리스트=>새 거래파일; 올드 거래파일 이름을 새 파일로, 올드 파일 제거;
        FileIO.SaveTxListToJsonFile(FileIO.transactionList, newFilePath)

    #경고문="아이디가 존재하지 않습니다"; 리턴;
    return count


def ImportTransactions(newFilePath):
    
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')

    #global largestUsedId
    
    #거래 리스트 생성;
    oldTransactionList: list[Transaction]=[]
    newTransactionList: list[Transaction]=[]
    

    #통합 파일의 데이터를 한줄씩 거래로 변환해서 리스트에 담기;
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            oldTx=TransformLineToTx(txLine)
            
            oldTransactionList.append(oldTx)
                            
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break
    

    #newFileTx_stream = transaction_generator(defaultFolderPath+"/"+ newFilePath)
    newFileTx_stream = FileIO.transaction_generator(newFilePath)
    #임포트할 파일의 데이터를; 거래로 변환해서 임포트할 리스트에 담기;
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(newFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            newTx=TransformLineToTx(txLine)
            
            newTransactionList.append(newTx)
                            
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break




    #임포트할 리스트를 돌면서;
    for item in newTransactionList:
        txToImport: Transaction=item
        isTxImported=False
        
        for index in range(len(oldTransactionList)):
            #임포트할 거래값보다 통합 리스트의 날짜값이 과거면;
            if TransformStrToDate(txToImport.dateStr) > TransformStrToDate(oldTransactionList[index].dateStr):
                
                FileIO.largestUsedId+=1
                txToImport.id=FileIO.largestUsedId
                #그 위치에 삽입;
                oldTransactionList.insert(index, txToImport)
                isTxImported=True
                break
        
        if isTxImported == False:
            FileIO.largestUsedId+=1
            txToImport.id=FileIO.largestUsedId
            oldTransactionList.append(txToImport)




    #통합 리스트=>새 파일; 기존 파일명 사용, 기존 파일 제거;
    if len(newTransactionList) > 0:
        FileIO.SaveTxListToJsonFile(oldTransactionList)
        print(f"[완료] imported={len(newTransactionList)}")
    else:
        print("import할 거래가 없습니다.")



def SummaryMonth(yearMonthStr, categoryLimit):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')

    #거래 리스트 생성;
    #여기 수정;
    #global transactionList
    transactionList=[]
    txExist=False
    
    yearStr=yearMonthStr.split("-")[0]
    monthStr=yearMonthStr.split("-")[1]
    #print("yearMonthStr : "+yearMonthStr)
    #print("yearStr : "+yearStr)
    #print("monthStr : "+monthStr)
    
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            oldTx=TransformLineToTx(txLine)
            
            yearStrOfOldTx=oldTx.dateStr.split("-")[0]
            monthStrOfOldTx=oldTx.dateStr.split("-")[1]
            
            
            #날짜가 범위 내면;
            if yearStr == yearStrOfOldTx and monthStr == monthStrOfOldTx:
                transactionList.append(oldTx)
                txExist=True
                
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break


    #거래 존재==트루면;
    if txExist == True:
        accIncome=0
        accExpense=0
        accExpenseListOfCategory:list[int]
        accExpenseListOfCategory=[]
        
        for _ in FileIO.categoryList:
            accExpenseListOfCategory.append(0)
        #print("accExpenseListOfCategory : "+str(accExpenseListOfCategory))
        
        #리스트로;
        for item in transactionList:
            tx: Transaction=item
            #수입 누적;
            if tx.type=="income":
                accIncome+=tx.amount
            #지출 누적;
            elif tx.type == "expense":
                accExpense+=tx.amount
                
                categoryIndex=-1
                #카테고리별 지출액 누적;
                for index in range(len(FileIO.categoryList)):
                    if tx.category == FileIO.categoryList[index]:
                        categoryIndex=index
                        break
                if categoryIndex > -1:
                    accExpenseListOfCategory[categoryIndex]+=tx.amount
                



        print(yearMonthStr)
        #총 수입;
        print("총 수입 : "+str(accIncome))
        #총 지출;
        print("총 지출 : "+str(accExpense))
        #잔액=총 수입-총 지출;
        net=accIncome-accExpense
        print("잔액 : "+str(net))


        
        budgetExist=False
        budgetAmount=0
        #print("budgetDataList : "+str(len(budgetDataList)))
        #예산 설정값 존재하는지 탐색
        for item in FileIO.budgetDataList:
            budgetData: BudgetData=item
            if budgetData.yearMonthStr == yearMonthStr:
                budgetAmount:int= int(budgetData.amount)
                budgetExist=True
                break
        #해당 연월의 예산값 있으면;
        if budgetExist == True:
            print("예산 : "+str(budgetAmount))
            #지출/예산 비율 출력;
            ratio= float(accExpense)/budgetAmount
            value=int(ratio*100)
            print("총 지출/예산 : "+str(value)+"%")
            #초과시; 경고문구 출력;
            if accExpense > budgetAmount:
                print("총 지출이 예산을 초과했습니다!")



        #print("accExpenseListOfCategory : "+str(accExpenseListOfCategory))
        decendingOrderedIndexList=[]
        #카테고리별 누적 지출이 많은 순으로 인덱스 리스트 생성; 
        for i in range(len(accExpenseListOfCategory)):
            if len(decendingOrderedIndexList) == 0:
                decendingOrderedIndexList.append(i)
            else:
                inserted=False
                for j in range(len(decendingOrderedIndexList)):
                    if accExpenseListOfCategory[i] > accExpenseListOfCategory[decendingOrderedIndexList[j]]:
                        decendingOrderedIndexList.insert(j,i)
                        inserted=True
                        break
                if inserted == False:
                    decendingOrderedIndexList.append(i)
            #print(str(i)+" : "+str(decendingOrderedIndexList))
        
        #print(len(decendingOrderedIndexList),len(categoryList), (categoryLimit))
        #카테고리 개수 한도값만큼;
        for index in range(min(categoryLimit, len(FileIO.categoryList))):
            order=index+1
            #카테고리 이름, 총 지출액 출력;
            print(str(order)+"."+FileIO.categoryList[decendingOrderedIndexList[index]]+" : "+str(accExpenseListOfCategory[decendingOrderedIndexList[index]]))




    #경고문="아이디가 존재하지 않습니다"; 리턴;
    return txExist





#defaultFolderPath="./data"
#def SaveDefaultFolderPath():
#    with open("./data/defaultFolderPath.jsonl", 'w', encoding='utf-8') as f_out:
#        f_out.write(defaultFolderPath + '\n')


#from pathlib import Path
#def LoadDefaultFolderPath():
#    global defaultFolderPath
    
#    # 1. 현재 main.py 파일이 있는 폴더 경로를 알아냅니다.
#    BASE_DIR = Path(__file__).resolve().parent
#    # 2. 그 폴더 안의 data/defaultFolderPath.jsonl 절대 경로를 만듭니다.
#    target_file_path = BASE_DIR / "data" / "defaultFolderPath.jsonl"
    
#    #with open("./data/defaultFolderPath.jsonl", 'r', encoding='utf-8') as file:
#    with open(target_file_path, 'r', encoding='utf-8') as file:
#        for line in file:
#            if line.strip():
#                defaultFolderPath=line



    
#def SaveTxListToJsonFile(txList, newFilePath:str=None):
#    #print("transactionList length : "+str(len(txList)))
#    #global defaultFolderPath
#    #tmpFilePath=defaultFolderPath+ "/tmpTx.jsonl"
#    #oldFilePath=defaultFolderPath+ "/transactions.jsonl"
#    #tmpFilePath="tmpTx.jsonl"
#    #oldFilePath="transactions.jsonl"
#    #tmpFilePath=FileIO.add_base_path("tmpTx.jsonl")
#    #oldFilePath=FileIO.add_base_path("transactions.jsonl")
#    tmpFilePath=FileIO.GetFullPath("tmpTx.jsonl")
#    oldFilePath=FileIO.GetFullPath("transactions.jsonl")


    
#    try:
#        # 1. 임시 파일에 데이터 쓰기 (파일이 없으면 w 모드로 자동 생성됨)
#        with open(tmpFilePath, 'w', encoding='utf-8') as f_out:
#            for tx in txList:
#                # 클래스 인스턴스의 데이터를 콤마 구분 문자열로 가공
#                line = TransformTxToLine(tx)
#                #print("line : "+line)
#                # JSONL 형식으로 쓰기
#                #f_out.write(json.dumps(line, ensure_ascii=False) + '\n')
#                f_out.write(line + '\n')
        
#        # 2. 파일 교체 작업 (기존 원본을 지우고 임시 파일의 이름을 원본명으로 변경)
#        # os.replace는 원본 파일이 없으면 그냥 생성하고, 있으면 기존 원본을 '제거'하면서 강제 덮어씁니다.
#        if newFilePath is None:
#            os.replace(tmpFilePath, oldFilePath)
#        else:
#            os.replace(tmpFilePath, FileIO.GetFullPath(newFilePath))
#        #print(f"✅ 파일 쓰기 완료: '{file_path}'로 안전하게 교체되었습니다.")
#        #sys.exit(0)

#    except Exception as e:
#        # 도중에 에러가 나면 쓰다 만 임시 파일을 지워 정돈합니다.
#        if os.path.exists(tmpFilePath):
#            os.remove(tmpFilePath)
#        print(f"❌ 파일 작업 중 오류 발생: {e}")
#        #sys.exit(1)
#    except FileNotFoundError as e:
#        # 1. 사용자에게 시스템 구조를 숨기고 안전한 메시지만 출력
#        print("❌ [오류] 지정된 파일이나 폴더 경로를 찾을 수 없습니다.")
        
    
    #for transaction in transactionList:
    #    if transaction.id == id:
    #        transaction.date = newTransactionData.date
    #        transaction.category = newTransactionData.category
    #        transaction.type = newTransactionData.type
    #        transaction.memo = newTransactionData.memo
    #        transaction.tags = newTransactionData.tags
    #        saveAllTransactionData()
    #        print(f"[수정 완료] id={transaction.id}")
    #        return
    #print(f"Transaction with ID {id} not found.")

#def deleteTransaction(id):
#    for transaction in transactionList:
#        if transaction.id == id:
#            transactionList.remove(transaction)
#            saveAllTransactionData()
#            return
#    print(f"Transaction with ID {id} not found.")
    

#def PrintSummary(month, top_n=3):
#    # 총수입/총지출/잔액 + 카테고리별 지출 TOP N
#    total_income = 0
#    total_expense = 0
#    category_expense = {}
#    for transaction in transactionList:
#        if transaction.date.startswith(month):
#            if transaction.type == "income":
#                total_income += transaction.amount
#            elif transaction.type == "expense":
#                total_expense += transaction.amount
#                if transaction.category in category_expense:
#                    category_expense[transaction.category] += transaction.amount
#                else:
#                    category_expense[transaction.category] = transaction.amount


#    balance = total_income - total_expense
#    print(f"Month: {month}")
#    print(f"Total Income: {total_income}")
#    print(f"Total Expense: {total_expense}")
#    print(f"Balance: {balance}")



#    #카테고리별 지출 TOP N
#    sorted_categories = sorted(category_expense.items(), key=lambda x: x[1], reverse=True)
#    print(f"Top {top_n} Categories by Expense:")
#    for i, (category, amount) in enumerate(sorted_categories[:top_n]):
#        print(f"{i + 1}. {category}: {amount}")




#budgetDataList = []
def SetBudget(yearMonthStr, amount):
    #budgetList[yearMonthStr] = amount
    selectedBudgetData=None
    for item in FileIO.budgetDataList:
        budgetData:BudgetData=item
        if budgetData.yearMonthStr == yearMonthStr:
            selectedBudgetData=budgetData
            break
    if selectedBudgetData != None:
        selectedBudgetData.amount=amount
        
    else:
        newBudgetData=BudgetData(yearMonthStr,amount)
        FileIO.budgetDataList.append(newBudgetData)
        
    FileIO.SaveBudgetDataListToFile()
    print(f"[저장 완료] yearMonth={yearMonthStr}, amount={amount}")

#def SaveBudgetDataListToFile():
#    #global defaultFolderPath
#    #tmpFilePath=defaultFolderPath+ "/tmpBudget.jsonl"
#    #oldFilePath=defaultFolderPath+ "/budgets.jsonl"
#    tmpFilePath="tmpBudget.jsonl"
#    oldFilePath="budgets.jsonl"
    
#    try:
#        # 1. 임시 파일에 데이터 쓰기 (파일이 없으면 w 모드로 자동 생성됨)
#        with open(tmpFilePath, 'w', encoding='utf-8') as f_out:
#            for budgetData in budgetDataList:
#                # 클래스 인스턴스의 데이터를 콤마 구분 문자열로 가공
#                line = TransformBudgetDataToLine(budgetData)
#                # JSONL 형식으로 쓰기
#                #f_out.write(json.dumps(line, ensure_ascii=False) + '\n')
#                f_out.write(line + '\n')
#        #sys.exit(0)
        
#        # 2. 파일 교체 작업 (기존 원본을 지우고 임시 파일의 이름을 원본명으로 변경)
#        # os.replace는 원본 파일이 없으면 그냥 생성하고, 있으면 기존 원본을 '제거'하면서 강제 덮어씁니다.
#        os.replace(tmpFilePath, oldFilePath)

#    except Exception as e:
#        # 도중에 에러가 나면 쓰다 만 임시 파일을 지워 정돈합니다.
#        if os.path.exists(tmpFilePath):
#            os.remove(tmpFilePath)
#        #sys.exit(1)
#    except FileNotFoundError as e:
#        # 1. 사용자에게 시스템 구조를 숨기고 안전한 메시지만 출력
#        print("❌ [오류] 지정된 파일이나 폴더 경로를 찾을 수 없습니다.")
    
        
#def LoadBudgetDataListFromFile():
#    #with open("budget.jsonl", "r") as file:
#    #global defaultFolderPath
#    #filePath=defaultFolderPath+"/budgets.jsonl"
#    #filePath="budgets.jsonl"
#    filePath=FileIO.GetFullPath("budgets.jsonl")

#    global budgetDataList
#    budgetDataList=[]
    
#    try:
#        # 1. 임시 파일에 데이터 쓰기 (파일이 없으면 w 모드로 자동 생성됨)
#        with open(filePath, 'r', encoding='utf-8') as file:
#            for line in file:
#                if line.strip():
#                    # 클래스 인스턴스의 데이터를 콤마 구분 문자열로 가공
#                    budgetData = TransformLineToBudgetData(line)
#                    budgetDataList.append(budgetData)
#        #sys.exit(0)

#    except FileNotFoundError as e:
#        # 1. 사용자에게 시스템 구조를 숨기고 안전한 메시지만 출력
#        print("❌ [오류] 지정된 파일이나 폴더 경로를 찾을 수 없습니다.")


def TransformBudgetDataToLine(budgetData:BudgetData):
    line = ",".join([budgetData.yearMonthStr, str(budgetData.amount)])
    return line;

def TransformLineToBudgetData(line:str):
    values = line.split(',')
    budgetData=BudgetData(values[0],values[1])
    return budgetData


    
        
        
#def LoadAllTransactionData():
#    with open("transactions.txt", "r") as file:
#        for line in file:
#            data = line.strip().split(",")
#            if len(data) == 6:
#                id, date, category, type, memo, tags = data
#                tags = tags.split("|")  # Assuming tags are separated by '|'
#                transactionList.append(transaction(date, category, type, memo, tags))
#                transactionList[-1].id = int(id)
#def saveAllTransactionData():
#    with open("transactions.txt", "w") as file:
#        for transaction in transactionList:
#            file.write(f"{transaction.id},{transaction.date},{transaction.category},{transaction.type},{transaction.memo},{'|'.join(transaction.tags)}\n")






def printCategoryList():
    for category in FileIO.categoryList:
        print("- "+category)
def addCategory(category):
    if category not in FileIO.categoryList:
        FileIO.categoryList.append(category)
        FileIO.SaveCategoryList()
        print(f"[저장 완료 : {category}]")
    else:
        print(f'"{category}" already exists.')
def deleteCategory(category):
    if category in FileIO.categoryList:
        FileIO.categoryList.remove(category)
        FileIO.SaveCategoryList()
        print(f"[삭제 완료 : {category}]")
    else:
        print(f'"{category}" does not exist.')
        
    
    




def CheckDateStringFormat(dateStr: str) -> bool:
    alarmStr:str="정상"
    #
    if dateStr.split("-")[0].isdigit() == False or dateStr.split("-")[1].isdigit() == False or dateStr.split("-")[2].isdigit() == False:
        alarmStr="년,월,일을 -로 구분하여 숫자로 입력해주세요."
    elif int(dateStr.split("-")[1]) < 1 or int(dateStr.split("-")[1]) > 12:
        alarmStr="월은 1에서 12 사이의 숫자를 입력해주세요."
    else:
        year=int(dateStr.split("-")[0])
        month=int(dateStr.split("-")[1])
        day=int(dateStr.split("-")[2])
        
        #월,일; 2자리수일때만 통과시키게;
        if len(dateStr.split("-")[1]) != 2 or len(dateStr.split("-")[2]) != 2:
            alarmStr="월,일은 2자리 숫자로 입력해주세요."

        elif month in [1,3,5,7,8,10,12]:
            if day < 1 or day > 31:
                alarmStr="일은 1에서 31 사이의 숫자를 입력해주세요."
        elif month in [4,6,9,11]:
            if day < 1 or day > 30:
                alarmStr="일은 1에서 30 사이의 숫자를 입력해주세요."
        elif month == 2:
            #윤년 계산;
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                #윤년이면;
                if day < 1 or day > 29:
                    alarmStr="일은 1에서 29 사이의 숫자를 입력해주세요."
            else:
                #평년이면;
                if day < 1 or day > 28:
                    alarmStr="일은 1에서 28 사이의 숫자를 입력해주세요."
    return alarmStr;



    
#command=""
#idOfTmpTransaction=-1
#tmpTransaction=None

#def PrintTransaction(tx:Transaction):
#    print(tx.id+" | "+tx.dateStr+" | "+tx.type+" | "+tx.category+" | "+tx.amount+" | "+tx.memo+" | "+tx.tag)

#def TransformTxToLine(tx:Transaction):
#    line = ",".join([str(tx.id), str(tx.dateStr), tx.type, tx.category, str(tx.amount), tx.memo, tx.tag])
#    return line;

#def TransformLineToTx(line:str):
#    values = line.split(',')
#    tx=Transaction(int(values[0]),values[1],values[2],values[3],int(values[4]),values[5],values[6])
#    return tx

#def ChangeTxDateToString(func):
#    def wrapper(tx: Transaction):
#        return func()  
#    return wrapper

def PrintTransaction(tx: Transaction):
    # 1. 태그 리스트를 출력용 문자열로 예쁘게 합칩니다. (예: "식비, 외식")
    # 태그가 없으면 빈 문자열("")이 됩니다.
    tags_str = ", ".join(tx.tags) if tx.tags else "없음"
    
    # 2. f-string을 사용하여 정수와 문자열을 에러 없이 한 번에 출력합니다.
    #print(f"{tx.id} | {tx.dateStr} | {tx.type} |   {tx.category}   | {tx.amount} | {tx.memo} | {tags_str}")
    print(f"{TransformIdNumberToString(tx.id)} | {tx.dateStr} | {tx.type} |   {tx.category}   | {tx.amount} | {tx.memo} | {tags_str}")

def TransformTxToLine(tx: Transaction):
    # 1. tags 리스트를 공백(' ')으로 먼저 합쳐서 하나의 문자열로 만듭니다.
    # 예: ['식비', '외식'] -> "식비 외식"
    tags_str = " ".join(tx.tags)
    
    # 2. 모든 요소를 하나의 CSV 라인으로 합칩니다.
    line = ",".join([
        str(tx.id), 
        str(tx.dateStr), 
        tx.type, 
        tx.category, 
        str(tx.amount), 
        tx.memo, 
        tags_str  # 변환된 태그 문자열 삽입
    ])
    return line

def TransformLineToTx(line: str):
    # 공백 제거 후 콤마(,) 기준으로 분리
    values = line.strip().split(',')
    
    # 맨 마지막 요소인 태그 문자열을 다시 공백 기준으로 쪼개서 리스트로 복원합니다.
    # 예: "식비 외식" -> ['식비', '외식']
    # 만약 태그가 비어있다면 빈 리스트([])가 됩니다.
    tags_list = values[6].split() if values[6] else []
    #print("tags_list : "+str(tags_list))
    # Transaction 객체 생성 (마지막 인자로 리스트 전달)
    tx = Transaction(
        int(values[0]),  # id
        values[1],       # dateStr
        values[2],       # type
        values[3],       # category
        int(values[4]),  # amount
        values[5],       # memo
        tags_list        # tags (리스트 형태)
    )
    return tx


# 한 줄씩 거래 정보를 양보(yield)하는 제너레이터 함수
#def transaction_generator(file_path):
#    try:
#        with open(file_path, 'r', encoding='utf-8') as f:
#            for line in f:
#                if line.strip():
#                    print("line : "+line.strip())
#                    yield line.strip()#json.loads(line.strip())
#        #sys.exit(0)
                    
#    except Exception as e:
#        #sys.exit(1)
#        print("transaction_generator : "+str(e))
import os

import FileIO


#oldFileTx_stream = transaction_generator(defaultFolderPath+'/transactions.jsonl')
#oldFileTx_stream = transaction_generator('transactions.jsonl')


def ListTransactions(volume):
    #global oldFileTx_stream
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')

    print("id        | date       | type    | category | amount | memo | tag")

    count=0
    
    while count < volume:
        try:
            #print(10)
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #print("txLine : "+txLine)
            tx=TransformLineToTx(txLine)
            #print(12)
            PrintTransaction(tx)
            count+=1
            #print(13)
            ## 특정 조건에 부합하는지 판단. (예: amount >= 50000)
            #if tx.get('amount', 0) >= 50000:
            #    found_transactions.append(tx)
            #    print(f"🎯 조건 만족 거래 발견 ({len(found_transactions)}/{target_count}): {tx}")
            #sys.exit(0)
                
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {count}개뿐입니다.")
            if count == 0:
                print("⚠️ 거래 내역이 없습니다.")
            break



from datetime import datetime, date

# 1. 문자열로 된 날짜값을 파이썬 date 객체로 변환하는 함수
def TransformStrToDate(date_str: str) -> date:
    """
    "YYYY-MM-DD" 형식의 문자열을 파이썬 datetime.date 객체로 변환합니다.
    (예: "2026-09-29" -> date(2026, 9, 29))
    """
    # strptime으로 문자열을 datetime 객체로 만든 뒤, 날짜(.date())만 추출합니다.
    return datetime.strptime(date_str, "%Y-%m-%d").date()


# 2. 파이썬 date 객체를 "YYYY-MM-DD" 형식의 문자열로 변환하는 함수
def TransformDateToStr(date_obj: date) -> str:
    """
    파이썬 datetime.date 객체를 "YYYY-MM-DD" 형식의 문자열로 변환합니다.
    (예: date(2026, 9, 29) -> "2026-09-29")
    """
    # strftime을 사용하여 원하는 포맷의 문자열로 출력합니다.
    return date_obj.strftime("%Y-%m-%d")

def SearchTransactionsWithFromTo(dateStrFrom, dateStrTo):
    print("c")

    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')
    count=0
    print("id        | date       | type    | category | amount | memo | tag")
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            tx=TransformLineToTx(txLine)

            if TransformStrToDate(dateStrFrom) <= TransformStrToDate(tx.dateStr) <= TransformStrToDate(dateStrTo):
                PrintTransaction(tx)
                count+=1
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            if count == 0:
                print("⚠️ 거래 내역이 없습니다.")
                
            break

def SearchTransactionsWithCatagory(categoryName):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')
    count=0
    print("id        | date       | type    | category | amount | memo | tag")
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            tx=TransformLineToTx(txLine)

            if tx.category == categoryName:
                PrintTransaction(tx)
                count+=1
                
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            if count == 0:
                print("⚠️ 거래 내역이 없습니다.")
            break
def SearchTransactionsWithType(type):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')
    
    count=0
    print("id        | date       | type    | category | amount | memo | tag")
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            tx=TransformLineToTx(txLine)

            if tx.type == type:
                PrintTransaction(tx)
                count+=1
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            if count == 0:
                print("⚠️ 거래 내역이 없습니다.")
            break
def SearchTransactionsWithMemo(memo):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')
    
    count=0
    print("id        | date       | type    | category | amount | memo | tag")
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            tx=TransformLineToTx(txLine)
            #print("tx.memo : "+tx.memo)
            if tx.memo == memo:
                PrintTransaction(tx)
                count+=1
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            if count == 0:
                print("⚠️ 거래 내역이 없습니다.")
            break

def SearchTransactionsWithTag(tag):
    oldFileTx_stream = FileIO.transaction_generator('transactions.jsonl')
    count=0
    print("id        | date       | type    | category | amount | memo | tag")
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            tx=TransformLineToTx(txLine)

            if tag in tx.tags:
                PrintTransaction(tx)
                count+=1
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            if count == 0:
                print("⚠️ 거래 내역이 없습니다.")
            break



#업데이트 입력 오류 판정(옵션 문자열[]);
def DetermineInputErrorOfUpdateCommand(optionStringList):
    #경고문="정상";
    alarmStringToReturn="정상"
    tmpTransactionToReturn=Transaction("","","", "", "", "", [])
    
    #print("optionStringListAfterId : "+str(optionStringList))

    for i in range(len(optionStringList)):
        #옵션 문자열[i]를 " "로 분할후
        splitStringList0 = optionStringList[i].split(" ")
        splitStringList0[0]=splitStringList0[0].strip().lower()
        splitStringList0[1]=splitStringList0[1].strip()
        
        #print("splitStringList0 : "+str(splitStringList0))
        
        #" "로 분할된 문자열[0]=="date"일때
        if splitStringList0[0] == "date":
            splitStringList_YMD = splitStringList0[1].split("-")
            #문자열[1]을 "-"로 분할해서 3개가 아니면;
            if len(splitStringList_YMD) != 3:
                #경고문=YYYY-MM-DD형식으로 입력하세요. 반환;
                alarmStringToReturn="YYYY-MM-DD형식으로 입력하세요."
                return alarmStringToReturn,tmpTransactionToReturn
            else:
                #"-"로 분할된 문자열[0]이 숫자로 변환이 안되면;
                if not splitStringList_YMD[0].isdigit():
                    #경고문=연도에 숫자를 입력하세요; 반환;
                    alarmStringToReturn="연도에 숫자를 입력하세요."
                    return alarmStringToReturn,tmpTransactionToReturn
                elif not splitStringList_YMD[1].isdigit():
                    #경고문=월에 숫자를 입력하세요; 반환;
                    alarmStringToReturn="월에 숫자를 입력하세요."
                    return alarmStringToReturn,tmpTransactionToReturn
                #숫자로 변환이 되면;
                else:
                    #1~12범위가 아니면; 
                    if not (1 <= int(splitStringList_YMD[1]) <= 12):
                        alarmStringToReturn="1월~12월만 가능합니다."
                        return alarmStringToReturn,tmpTransactionToReturn
                    else:
                        #[2]값이 숫자로 변환이 안되면;
                        if not splitStringList_YMD[2].isdigit():
                            #경고문=일에 숫자를 입력하세요; 반환;
                            alarmStringToReturn="일에 숫자를 입력하세요."
                            return alarmStringToReturn,tmpTransactionToReturn
                        else:
                            #[1]값이 2일때;
                            if splitStringList_YMD[1] == "2":
                                #윤년인지 평년인지 판별;
                                if int(splitStringList_YMD[0]) % 4 == 0 and (int(splitStringList_YMD[0]) % 100 != 0 or int(splitStringList_YMD[0]) % 400 == 0):
                                    #윤년인데; [2]값이 0~29범위가 아니면;
                                    if not (0 <= int(splitStringList_YMD[2]) <= 29):
                                        alarmStringToReturn="0~29일까지 존재합니다."
                                        return alarmStringToReturn,tmpTransactionToReturn
                                else:
                                    #평년인데; [2]값이 0~28범위가 아니면;
                                    if not (0 <= int(splitStringList_YMD[2]) <= 28):
                                        alarmStringToReturn="0~28일까지 존재합니다."
                                        return alarmStringToReturn,tmpTransactionToReturn


                            #[1]값이 2가 아닐때;
                            else:
                                #[1]값이 1,3,5,7,8,10,12일때;
                                if splitStringList_YMD[1] in ["1", "3", "5", "7", "8", "10", "12"]:
                                    #[2]값이 0~31범위가 아니면;
                                    if not (0 <= int(splitStringList_YMD[2]) <= 31):
                                        alarmStringToReturn="0~31일까지 존재합니다."
                                        return alarmStringToReturn,tmpTransactionToReturn

                                #[1]값이 1,3,5,7,8,10,12가 아닐때;
                                else:
                                    #[2]값이 0~30범위가 아니면;
                                    if not (0 <= int(splitStringList_YMD[2]) <= 30):
                                        alarmStringToReturn="0~30일까지 존재합니다."
                                        return alarmStringToReturn,tmpTransactionToReturn
            #tmpTransactionToReturn.date에 값 할당;
            tmpTransactionToReturn.dateStr=splitStringList0[1]
            #return alarmStringToReturn, tmpTransactionToReturn
            
        #" "로 분할된 문자열[0]=="type"일때;
        elif splitStringList0[0] == "type":
            #문자열[1]이"income" or "expense" 둘다 아니면;
            if splitStringList0[1] not in ["income", "expense"]:
                #경고문=--type <income/expense>; 반환;
                alarmStringToReturn="--type <income/expense> 형식으로 입력하세요."
                return alarmStringToReturn,tmpTransactionToReturn
            else:
                #tmpTransactionToReturn.type에 값 할당;
                tmpTransactionToReturn.type=splitStringList0[1]
                #return alarmStringToReturn, tmpTransactionToReturn

        #" "로 분할된 문자열[0]=="amount"
        elif splitStringList0[0] == "amount":
            #문자열[1]값이 숫자로 변환이 안되면;
            if not splitStringList0[1].isdigit():
                #경고문=금액으로 숫자를 입력하세요;
                alarmStringToReturn="금액으로 숫자를 입력하세요."
                return alarmStringToReturn,tmpTransactionToReturn
            else:
                #tmpTransactionToReturn.amount에 값 할당;
                tmpTransactionToReturn.amount=int(splitStringList0[1])
                #return alarmStringToReturn, tmpTransactionToReturn

        #" "로 분할된 문자열[0]=="category"
        elif splitStringList0[0] == "category":
            #문자열[1]값이 비어있으면;
            if not splitStringList0[1]:
                #경고문=카테고리를 입력하세요; 반환;
                alarmStringToReturn="카테고리를 입력하세요."
                return alarmStringToReturn,tmpTransactionToReturn
            else:
                #tmpTransactionToReturn.category에 값 할당;
                tmpTransactionToReturn.category=splitStringList0[1]
                #return alarmStringToReturn, tmpTransactionToReturn

        #" "로 분할된 문자열[0]=="q"
        elif splitStringList0[0] == "q":
            #문자열[1]값이 비어있으면;
            if not splitStringList0[1]:
                #경고문=메모를 입력하세요; 반환;
                alarmStringToReturn="메모를 입력하세요."
                return alarmStringToReturn,tmpTransactionToReturn
            else:
                #tmpTransactionToReturn.memo에 값 할당;
                tmpTransactionToReturn.memo=splitStringList0[1]
                #return alarmStringToReturn, tmpTransactionToReturn
        #" "로 분할된 문자열[0]=="tag"
        elif splitStringList0[0] == "tag":
            #문자열[1]값이 비어있으면;
            if not splitStringList0[1]:
                #경고문=태그를 입력하세요; 반환;
                alarmStringToReturn="태그를 입력하세요."
                return alarmStringToReturn,tmpTransactionToReturn
            else:
                #tmpTransactionToReturn.tags에 값 할당;
                tmpTransactionToReturn.tags=splitStringList0[1].split(",")
                #return alarmStringToReturn, tmpTransactionToReturn

        #어떤 옵션 이름도 아닌 경우; 
        else:
            #경고문=잘못된 명령어입니다; 반환;
            alarmStringToReturn="잘못된 명령어입니다."
            return alarmStringToReturn,tmpTransactionToReturn

    return alarmStringToReturn, tmpTransactionToReturn




#export입력 오류 판정(옵션 문자열 리스트);
#export --out asdf.csv --month 2024-01
#export --out asdf.csv --from 2024-01-01 --to 2024-01-31
def DetermineInputErrorOfExportCommand(optionCommandStrList):
    #print("optionCommandStrList : "+str(optionCommandStrList))
    #경고문="정상"
    alarmStringToReturn:str="정상"
    pathStringToReturn:str=""
    yearMonthStringToReturn:str=""
    fromDateString:str=""
    toDateString:str=""


    #옵션문자열[0]을 " "로 나누고;
    out_path_ValueList = optionCommandStrList[0].split(" ")#.strip()
    out_path_ValueList[0]=out_path_ValueList[0].strip().lower()
    out_path_ValueList[1]=out_path_ValueList[1].strip()
    #서브문자열[0]=="out"이 아니면; 
    if out_path_ValueList[0] != "out":
        alarmStringToReturn="잘못된 명령어입니다."
        return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
    else:
        #서브문자열[1]을 "."으로 나누고;
        pathValueList = out_path_ValueList[1].split(".")
        
        #서브문자열2[1]이 "csv"나 "jsonl" 둘다 아니면;
        if pathValueList[1] not in ["csv", "jsonl"]:
            #경고문="csv"나 "jsonl"로만 가능합니다; 반환;
            alarmStringToReturn='"csv"나 "jsonl"로만 가능합니다.'
            return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
        else:
            #
            pathStringToReturn=out_path_ValueList[1]
            
            #옵션문자열[1]을 " "로 나누고;
            rangeCommandStrList = optionCommandStrList[1].split(" ")

            #서브문자열[0]=="month"가 아니면; 
            #if year_monthOptionValueList[0] != "month":
            #    alarmStringToReturn="잘못된 명령어입니다."
            #    return alarmStringToReturn
            
            #print("v : ",rangeCommandStrList[0].strip().lower(), str(len(optionCommandStrList)), optionCommandStrList[2].split(" ")[0].strip().lower())

            #서브문자열[0]=="month"일때; 
            if rangeCommandStrList[0].strip().lower() == "month":
                #서브문자열[1]을 "-"로 나누고;
                year_monthValueList = rangeCommandStrList[1].split("-")

                #서브문자열2[0]값이 숫자가 아니면; 
                if not year_monthValueList[0].isdigit():
                    alarmStringToReturn="연도에 숫자를 입력하세요."
                    return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString

                #서브문자열2[1]값이 숫자가 아니면; 
                if not year_monthValueList[1].isdigit():
                    alarmStringToReturn="월에 숫자를 입력하세요."
                    return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString

                #서브문자열2[1]값이 1~12범위가 아니면;
                if not (1 <= int(year_monthValueList[1]) <= 12):
                    alarmStringToReturn="1~12월만 가능합니다."
                    return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString

                #
                yearMonthStringToReturn=rangeCommandStrList[1]
                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
            #from to
            elif rangeCommandStrList[0].strip().lower() =="from" and len(optionCommandStrList)==3 and optionCommandStrList[2].split(" ")[0].strip().lower()=="to":
                #print("a")
                dateValueStrListForFrom=rangeCommandStrList[1].split("-")
                dateValueStrListForTo=optionCommandStrList[2].split(" ")[1].split("-")
                
                if len(dateValueStrListForFrom)!=3 or len(dateValueStrListForTo)!=3:
                    alarmStringToReturn="YYYY-MM-DD형식으로 입력하세요."
                    return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
                if dateValueStrListForFrom[0].isdigit() == False or dateValueStrListForTo[0].isdigit() == False:
                    alarmStringToReturn="연도에 숫자를 입력하세요."
                    return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
                if dateValueStrListForFrom[1].isdigit() == False or dateValueStrListForTo[1].isdigit() == False:
                    alarmStringToReturn="월에 숫자를 입력하세요."
                    return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
                if dateValueStrListForFrom[2].isdigit() == False or dateValueStrListForTo[2].isdigit() == False:
                    alarmStringToReturn="일에 숫자를 입력하세요."
                    return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
                
                if (1 <= int(dateValueStrListForFrom[1]) <= 12) == False or (1 <= int(dateValueStrListForTo[1]) <= 12) == False:
                    alarmStringToReturn="1~12월만 가능합니다."
                    return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString

                else:
                    #[1]값이 2일때;
                    if dateValueStrListForFrom[1] == "2":
                        #윤년인지 평년인지 판별;
                        if int(dateValueStrListForFrom[0]) % 4 == 0 and (int(dateValueStrListForFrom[0]) % 100 != 0 or int(year_monthValueList[0]) % 400 == 0):
                            #윤년인데; [2]값이 0~29범위가 아니면;
                            if not (0 <= int(dateValueStrListForFrom[2]) <= 29):
                                alarmStringToReturn="0~29일까지 존재합니다."
                                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
                        else:
                            #평년인데; [2]값이 0~28범위가 아니면;
                            if not (0 <= int(dateValueStrListForFrom[2]) <= 28):
                                alarmStringToReturn="0~28일까지 존재합니다."
                                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
                    #[1]값이 2가 아닐때;
                    else:
                        #[1]값이 1,3,5,7,8,10,12일때;
                        if dateValueStrListForFrom[1] in ["1", "3", "5", "7", "8", "10", "12"]:
                            #[2]값이 0~31범위가 아니면;
                            if not (0 <= int(dateValueStrListForFrom[2]) <= 31):
                                alarmStringToReturn="0~31일까지 존재합니다."
                                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString

                        #[1]값이 1,3,5,7,8,10,12가 아닐때;
                        else:
                            #[2]값이 0~30범위가 아니면;
                            if not (0 <= int(dateValueStrListForFrom[2]) <= 30):
                                alarmStringToReturn="0~30일까지 존재합니다."
                                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString

                    #[1]값이 2일때;
                    if dateValueStrListForTo[1] == "2":
                        #윤년인지 평년인지 판별;
                        if int(dateValueStrListForTo[0]) % 4 == 0 and (int(dateValueStrListForTo[0]) % 100 != 0 or int(year_monthValueList[0]) % 400 == 0):
                            #윤년인데; [2]값이 0~29범위가 아니면;
                            if not (0 <= int(dateValueStrListForTo[2]) <= 29):
                                alarmStringToReturn="0~29일까지 존재합니다."
                                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
                        else:
                            #평년인데; [2]값이 0~28범위가 아니면;
                            if not (0 <= int(dateValueStrListForTo[2]) <= 28):
                                alarmStringToReturn="0~28일까지 존재합니다."
                                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString
                    #[1]값이 2가 아닐때;
                    else:
                        #[1]값이 1,3,5,7,8,10,12일때;
                        if dateValueStrListForTo[1] in ["1", "3", "5", "7", "8", "10", "12"]:
                            #[2]값이 0~31범위가 아니면;
                            if not (0 <= int(dateValueStrListForTo[2]) <= 31):
                                alarmStringToReturn="0~31일까지 존재합니다."
                                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString

                        #[1]값이 1,3,5,7,8,10,12가 아닐때;
                        else:
                            #[2]값이 0~30범위가 아니면;
                            if not (0 <= int(dateValueStrListForTo[2]) <= 30):
                                alarmStringToReturn="0~30일까지 존재합니다."
                                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString

                #윤년/평년, 일값 1~31 범위 판단 필요;=>기존 코드 함수로 독립시켜서 사용?;
                
                #
                fromDateString=rangeCommandStrList[1]
                toDateString=optionCommandStrList[2].split(" ")[1];
                #print("aaa")
                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString

                
            else:
                #print("b")
                alarmStringToReturn="잘못된 명령어입니다."
                return alarmStringToReturn, pathStringToReturn, yearMonthStringToReturn,fromDateString,toDateString




#입력 오류 판정(옵션문자열 리스트)
def DetermineInputErrorOfCommandOfImport(optionStringList):
    #경고문="정상"
    alarmStringToReturn:str="정상"
    pathString:str=""

    #print("op : ",str(optionStringList))

    if len(optionStringList) != 1:
        alarmStringToReturn="잘못된 명령어입니다."
        return alarmStringToReturn,pathString
        
    #옵션문자열[0]이 from가 아니면; 
    if optionStringList[0].split(" ")[0].strip().lower() != "from":
        alarmStringToReturn="잘못된 명령어입니다."
        return alarmStringToReturn,pathString


    #경로값리스트=옵션문자열[1]을 "."으로 나눈값
    pathValueList = optionStringList[0].split(" ")[1].split(".")
    #경로값리스트[1]이 "csv"나"jsonl" 둘다 아니면; 
    if pathValueList[1].strip() not in ["csv", "jsonl"]:
        #경고문="csv"나"jsonl"만 가능합니다; 반환
        alarmStringToReturn='"csv"나 "jsonl"만 가능합니다.'
        return alarmStringToReturn,pathString


    pathString=optionStringList[0].split(" ")[1].strip()
    return alarmStringToReturn, pathString







def try_except_decorator(func):
    def wrapper():
        #print("--- 함수 시작 ---")
        try:
            func()  # 원본 함수 호출
            #sys.exit(0)
        #print("--- 함수 종료 ---")
        except:
            #sys.exit(1)
            pass
    return wrapper


import my_CLI
import FileIO


if __name__ == "__main__":
    #lastUsedIdNumber = loadLastUsedId()  # Load the last used ID from the file
    #LoadDefaultFolderPath()
    FileIO.LoadFilePath()
    FileIO.LoadLargestUsedId()
    #LoadAllTransactionData()
    FileIO.LoadCategoryList()

    FileIO.LoadBudgetDataListFromFile()

    #print("현재 로드된 my_CLI 경로:", my_CLI.__file__)
    my_CLI.ActivateCLI()

#python -m budget_app


