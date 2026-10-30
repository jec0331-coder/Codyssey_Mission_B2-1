import FileIO
import sys
#import main


    
def ActivateCLI():
    strForCLI="$"
    
    try:
        while True:
                # 트라이;
                #try:
                    # 입력 앞뒤 공백 제거;
                    trimmedInput=""
                    #print("a : "+trimmedInput)
                    trimmedInput = input(strForCLI).strip()
                    #print("trimmedInput_a : "+trimmedInput)
                    # 인풋값이 ""면;
                    #if trimmedInput == "":
                    #    print("a")
                    #    # 다시 입력하세요;
                    #    #print(strForCLI)
                    #    pass
                    if trimmedInput.startswith("python -m budget_app") == False:
                        print("python -m budget_app [명령어 입력]")
                    else:
                        trimmedInput = trimmedInput.replace("python -m budget_app", "").strip()
                        #print("trimmedInput_b : "+trimmedInput)
                        SelectActionOfCLI(trimmedInput)
                        break

            # 엑셉트; 밸류 에러; 숫자가 아니면;
            #except ValueError:
            #    # 숫자를 입력하세요;
            #    print("숫자를 입력하세요.")

    #엑셉트; 키보드 인터럽트 에러;
    except KeyboardInterrupt:
        # 키보드 인터럽트 에러 발생! 데이터를 저장후 종료합니다.
        print("키보드 인터럽트 에러 발생! 데이터를 저장후 종료합니다.")
        sys.exit(1)

    #엑셉트; 입력 스트림 종료(EOFError);
    except EOFError:
        # 입력 스트림 종료(EOFError) 발생! 데이터를 저장후 종료합니다.
        print("입력 스트림 종료(EOFError) 발생! 데이터를 저장후 종료합니다.")
        sys.exit(1)






def AskTransactionDate(tmpTransaction):#:main.Transaction):
    import main
    while True:
        dateStr = input("날짜(YYYY-MM-DD): ")
        alarmStr=main.CheckDateStringFormat(dateStr)
        if alarmStr != "정상":
            print(alarmStr)
            #continue
        else:
            tmpTransaction.dateStr = dateStr#TransformDateToStr(date)
            AskTransactionType(tmpTransaction)
            break

def AskTransactionType(tmpTransaction):
    while True:
        type = input("타입(income/expense):")
        if type not in ["income", "expense"]:
            print("유효하지 않은 타입입니다. income 또는 expense로 입력해주세요.")
            #continue
        else:
            tmpTransaction.type = type
            AskTransactionCategory(tmpTransaction)
            break


def AskTransactionCategory(tmpTransaction):
    #import main
    
    while True:
        category = input("카테고리: ")
        
        #print("category : "+category)
        #print("main.categoryList : "+str(FileIO.categoryList))

        if category not in FileIO.categoryList:
            print("존재하지 않는 카테고리입니다.")
            #continue
        else:
            tmpTransaction.category = category
            AskTransactionAmount(tmpTransaction)
            break

def AskTransactionAmount(tmpTransaction):
    while True:
        amount = input("금액(양수): ")
        
        if not amount.isdigit() or int(amount) <= 0:
            print("유효하지 않은 금액입니다. 양수를 입력해주세요.")
            #continue
        else:
            tmpTransaction.amount = amount
            AskTransactionMemo(tmpTransaction)
            break

def AskTransactionMemo(tmpTransaction):
    memo = input("메모(선택): ")
    tmpTransaction.memo = memo
    AskTransactionTags(tmpTransaction)

def AskTransactionTags(tmpTransaction):
    import main
    
    tags = input("태그(쉼표로 구분, 없으면 엔터): ")
    tmpTransaction.tags = tags.split(",") if tags else []
    main.AddTransaction(tmpTransaction)

    #if idOfTmpTransaction < 0:
    #    addTransaction(tmpTransaction)
    #else:
    #    updateTransaction(idOfTmpTransaction, tmpTransaction)




def SelectActionOfCLI(trimmedInput):
    #print("asdf")
    import main
    #global defaultFolderPath
    #idOfTmpTransaction=-1
    
    optionStrList=trimmedInput.split(" --")
    #print("optionStrList : "+str(optionStrList))
    
    if optionStrList[0].strip().lower() == "add":
        if len(optionStrList) <= 1:
            tmpTransaction=main.Transaction(None,None,None,None,None,None,None)
            #tmpTransaction.id=transactionList[0].id + 1 if transactionList else 0
            AskTransactionDate(tmpTransaction)
        elif optionStrList[1].strip().lower() == "help":
            print("거래 추가 : add")

    #인풋에서 경로값 걸러내서; 파일경로 저장 호출하는 코드;
    elif optionStrList[0].strip().lower() == "data":
        if len(optionStrList) == 1:
            print("data --dir <새 경로>")
        elif len(optionStrList) == 2 and optionStrList[1].strip().lower()=="help":
            print("데이터 저장 경로 변경 : data --dir <새 경로>")
        elif len(optionStrList) == 2:
            if optionStrList[1].split(" ")[0].strip().lower()=="dir":
                #덩어리[1].split(" ")[1]=="./~/~"면;
                if optionStrList[1].split(" ")[1].split("/")[0].strip().lower()==".":
                    #폴더 경로값 새걸로 할당;
                    defaultFolderPath=optionStrList[1].split(" ")[1].strip();
                    #폴더 경로값 파일에 저장;
                    FileIO.SetFilePath(defaultFolderPath)
                else:
                    print("경로값은 ./~/~ 형식으로 입력해주세요.")
            else:
                print("data --dir <새 경로>")

    elif optionStrList[0].strip().lower() == "list":
        if len(optionStrList) == 1:
            #print(0)
            main.ListTransactions(10)
        elif len(optionStrList) == 2 and optionStrList[1].strip().lower()=="help":
            #print(1)
            print("거래들 출력 : list --limit <n>")
            print("--limit <n> 설정 없으면 10개까지 출력")
        elif len(optionStrList) == 2:
            #print(2)
            if optionStrList[1].split(" ")[0].strip().lower()=="limit":
                if optionStrList[1].split(" ")[1].strip().isdigit() == True:
                    main.ListTransactions(int(optionStrList[1].split(" ")[1].strip()))
                else:
                    print("--limit <정수>")
        else:
            #print(3)
            pass
            
    #덩어리 2개; 덩어리[0]=="data";
    #elif len(optionStrList) == 2 and optionStrList[0].strip().lower() == "data":
    #    if optionStrList[1].strip().lower == "help":
    #        print("데이터 저장 경로 변경 : data --dir <새 경로>")
    #    #덩어리[1].split(" ")[0]=="dir";
    #    elif optionStrList[1].split(" ")[0].strip().lower() == "dir":
    #        #덩어리[1].split(" ")[1]=="./~/~"면;
    #        if optionStrList[1].split(" ")[1].split("/")[0].strip().lower()==".":
    #            #폴더 경로값 새걸로 할당;
    #            defaultFolderPath=optionStrList[1].split(" ")[1].strip();
    #            #폴더 경로값 파일에 저장;
    #            SaveDefaultFolderPath()

    
    elif len(optionStrList) == 2 and optionStrList[0].strip().lower() == "delete":
        #" "로 나눴을때; 
        idStrList=optionStrList[1].split(" ")
        #[0]=="id", [1]==디지털;
        if len(idStrList) == 2 and idStrList[0].strip().lower()=="id": #and idStrList[1].strip().isdigit() == True:
            alarmStr=main.CheckIdStringFormat(idStrList[1].strip())
            
            if alarmStr != "정상":
                print(alarmStr,"아이디 형식 : TX-000001")
            else:
                tmpTx=main.Transaction(None,None,None,None,None,None,None)
                tmpTx.id=int(main.TransformIdStringToNumber(idStrList[1].strip()))
                idExist=main.DeleteTransaction(tmpTx)

                #호출후; 아이디 없으면 경고문 출력;
                if idExist == False:
                    print("id가 존재하지 않음!")
        elif optionStrList[1].strip().lower()=="help":
            print("거래 삭제 : delete --id <거래 아이디>")
            
    elif len(optionStrList) != 2 and optionStrList[0].strip().lower() == "delete":            
        print("형식이 잘못되었습니다. delete --id <거래 아이디> 형식으로 입력해주세요.")

    #elif len(wordList) > 1 and wordList[0].lower() == "update":
    #    if wordList[1] == "help":
    #        print("update 명령어 설명")
    #    else:
    #        if wordList[1] :
    #        #command="update"
    #            tmpTransaction=transactionList[]
    #            idOfTmpTransaction=
    #            AskTransactionDate()
    #        else:
    #            ActivateCLI()
    elif optionStrList[0].strip().lower() == "category":
        if len(optionStrList) == 2 and optionStrList[1].strip().lower() == "help":
            print("카테고리 추가 : category add")
            print("카테고리 삭제 : category remove")
            print("카테고리들 출력 : category list")
        else:
            print("카테고리 추가 : category add")
            print("카테고리 삭제 : category remove")
            print("카테고리들 출력 : category list")
            
            

    elif len(optionStrList) == 1 and optionStrList[0].lower().startswith("category add"):
        #name=wordList[0].split(" ")[2]
        categoryName=input("카테고리명: ").strip()
        main.addCategory(categoryName)
    elif len(optionStrList) == 1 and optionStrList[0].lower().startswith("category remove"):
        #name=wordList[0].split(" ")[2]
        categoryName=input("카테고리명: ").strip()
        if main.CheckCategoryExistInTransactionList(categoryName) == True:
            print("사용중인 카테고리 입니다.")
        else:
            main.deleteCategory(categoryName)
    elif len(optionStrList) == 1 and optionStrList[0].lower() == "category list":
        main.printCategoryList()


    elif optionStrList[0].lower().strip() == "budget":
        print("예산 설정 : budget set --month <YYYY-MM> --amount <금액>")
    elif optionStrList[0].lower() == "budget set":
        if len(optionStrList)==2 and optionStrList[1].strip().lower()=="help":
            #if optionStrList[1].strip().lower()=="help":
            print("예산 설정 : budget set --month <YYYY-MM> --amount <금액>")
        elif len(optionStrList) == 3:
            #print(optionStrList[1].split(" ")[0].strip().lower(), optionStrList[2].split(" ")[0].strip().lower(), optionStrList[2].split(" ")[1].strip())
            
            if optionStrList[1].split(" ")[0].strip().lower()=="month" and optionStrList[2].split(" ")[0].strip().lower()=="amount":
                if optionStrList[2].split(" ")[1].strip().isdigit() == True and int(optionStrList[2].split(" ")[1].strip()) > 0:
                    
                    #print(optionStrList[1].split(" "), optionStrList[2].split(" "))

                    if len(optionStrList[1].split(" ")) == 2 and len(optionStrList[2].split(" ")) == 2:
                        #"-"로 나눴을때; 덩어리가 2개고;
                        yearMonthStr = optionStrList[1].split(" ")[1]
                        amount = int(optionStrList[2].split(" ")[1])
                        y_mStrList=yearMonthStr.split("-")

                        #[0],[1]이 둘다 디지털;
                        #[1]를 숫자로 변환시; 1~12 범위 내일때;
                        if len(y_mStrList) == 2 and y_mStrList[0].isdigit() == True and y_mStrList[1].isdigit() == True and (1 <= int(y_mStrList[1]) <= 12):
                            main.SetBudget(yearMonthStr, amount)
                        else:
                            print("<YYYY-MM> 형식, 숫자, 월은 12이하.")
                    else:
                        print("예산 설정 : budget set --month <YYYY-MM> --amount <금액>")
                else:
                    print("금액은 양수로 입력해주세요.")
                
                
            else:
                print("예산 설정 : budget set --month <YYYY-MM> --amount <금액>")
        else:
            print("예산 설정 : budget set --month <YYYY-MM> --amount <금액>")



    elif optionStrList[0].lower() == "summary":
        if len(optionStrList) <= 1:
            print("형식이 잘못되었습니다. summary --month YYYY-MM --top <n> 형식으로 입력해주세요.")
        elif len(optionStrList) == 2 and optionStrList[1].strip().lower()=="help":
            print("월별 요약 : summary --month <YYYY-MM> --top <n>")
            print("--top <n> 설정 없으면 지출높은 카테고리 5개까지 출력")

        elif len(optionStrList) == 2 and optionStrList[1].split(" ")[0].lower()=="month":
            monthStr = optionStrList[1].split(" ")[1]
            #PrintSummary(month, 5)
            txExist = main.SummaryMonth(monthStr, 5)
            if txExist == False:
                print("데이터 없음.")
        elif len(optionStrList) == 3 and optionStrList[1].split(" ")[0].lower()=="month" and optionStrList[2].split(" ")[0].lower()=="top":
            monthStr = optionStrList[1].split(" ")[1].strip()
            top_n = int(optionStrList[2].split(" ")[1].strip())
            if top_n <= 0:
                top_n = 5
            #PrintSummary(monthStr, top_n)
            txExist = main.SummaryMonth(monthStr, top_n)
            if txExist == False:
                print("데이터 없음.")


    elif optionStrList[0].lower() == "search":
        if len(optionStrList) <= 1:
            print("형식이 잘못되었습니다. search --type <type> --category <category> --memo <memo> --tag <tag> --from <YYYY-MM-DD> --to <YYYY-MM-DD> 형식으로 입력해주세요.")
            #pass
        elif len(optionStrList) == 2:
            if optionStrList[1].split(" ")[0].strip().lower()=="type":
                type = optionStrList[1].split(" ")[1]
                main.SearchTransactionsWithType(type)
            elif optionStrList[1].split(" ")[0].strip().lower()=="category":
                category = optionStrList[1].split(" ")[1]
                main.SearchTransactionsWithCatagory(category)
            elif optionStrList[1].split(" ")[0].strip().lower()=="q":
                memo = optionStrList[1].split(" ")[1]
                print("q : " + memo)
                main.SearchTransactionsWithMemo(memo)
            elif optionStrList[1].split(" ")[0].strip().lower()=="tag":
                tag = optionStrList[1].split(" ")[1]
                main.SearchTransactionsWithTag(tag)
            elif optionStrList[1].split(" ")[0].strip().lower()=="help":
                print("거래 타입으로 검색 : search --type <income/expense>")
                print("카테고리로 검색 : search --category <카테고리명>")
                print("메모로 검색 : search --q <메모 내용>")
                print("태그로 검색 : search --tag <태그>")
                print("날짜 범위로 검색 : search --from <YYYY-MM-DD> --to <YYYY-MM-DD>")
                
            
        elif len(optionStrList) == 3:
            #print("a")
            if optionStrList[1].split(" ")[0].strip().lower()=="from" and optionStrList[2].split(" ")[0].strip().lower()=="to":
                #print("b")
                start_dateStr = optionStrList[1].split(" ")[1].strip().lower()
                end_dateStr = optionStrList[2].split(" ")[1].strip().lower()

                alarmStr1=main.CheckDateStringFormat(start_dateStr)
                alarmStr2=main.CheckDateStringFormat(end_dateStr)
                
                if alarmStr1 != "정상": 
                    print(alarmStr1)
                elif alarmStr2 != "정상":
                    print(alarmStr2)
                else:
                    main.SearchTransactionsWithFromTo(start_dateStr, end_dateStr)

    elif optionStrList[0].strip().lower() == "update":
        if len(optionStrList) <= 1:
            print("형식이 잘못되었습니다. update --id <id> --date <YYYY-MM-DD> --type <income/expense> --amount <amount> --category <category> --q <memo> --tag <tag> 형식으로 입력해주세요.")
        else:
            if len(optionStrList) == 2 and optionStrList[1].lower()=="help":
                print("거래 수정 : update --id <id> --date <YYYY-MM-DD> --type <income/expense> --amount <amount> --category <category> --q <memo> --tag <tag>")
                
            else:
                if optionStrList[1].split(" ")[0].strip().lower() != "id":
                    print("id를 먼저 입력해주세요. : update --id <id> --date <YYYY-MM-DD> --type <income/expense> --amount <amount> --category <category> --q <memo> --tag <tag> 형식으로 입력해주세요.")
                    #ActivateCLI()
                    #return
                else:
                    
                    #id = int(optionStrList[1].split(" ")[1])
                    
                    if main.CheckIdStringFormat(optionStrList[1].split(" ")[1]) != "정상":
                        print("id 형식이 잘못되었습니다. TX-000001 형식으로 입력해주세요.")
                        #ActivateCLI()
                        #return
                    else:
                        id = int(main.TransformIdStringToNumber(optionStrList[1].split(" ")[1].strip()))
                    
                        #[1]번째 값부터 나머지 값들을 옵션스트링리스트에 담고;
                        #업데이트 입력오류 판정() 호출;
                        alarmString, tmpTx=main.DetermineInputErrorOfUpdateCommand(optionStrList[2:])
                        #반환된 문자열=="정상"이면;
                        if alarmString == "정상":
                            tmpTx.id=id
                            #업데이트(tmpTx) 호출;
                            idExist=main.UpdateTransaction(tmpTx)
                            if idExist == False:
                                print("id가 존재하지 않음!")
                        #"정상"이 아니면; 
                        else:
                            #경고문 출력;
                            print(alarmString)

            #id = int(wordList[1].split(" ")[1])
            #foundId = False
            
            #for transaction in transactionList:
            #    if transaction.id == id:
            #        if
            #        foundId = True
            #        break
                
            #if not foundId:
            #    print(f"Transaction with ID {id} not found.")

    elif optionStrList[0].strip().lower() == "export":
        if len(optionStrList) == 2 and optionStrList[1].strip().lower()=="help":
            print("해당하는 범위의 거래들을 외부 파일로 저장")
            print("export --out <파일 이름> --month <YYYY-MM>")
            print("export --out <파일 이름> --from <YYYY-MM--DD> --to <YYYY-MM-DD>")
        else:
            #[1]번째 값부터 나머지 값들을 옵션스트링리스트에 담고;
            #업데이트 입력오류 판정() 호출;
            alarmString,pathStr,monthStr,fromStr,toStr =main.DetermineInputErrorOfExportCommand(optionStrList[1:])
            #반환된 문자열=="정상"이면;
            if alarmString == "정상":
                if monthStr != "":
                    count=main.ExportTransactionsByMonth(pathStr,monthStr)
                    if count == 0:#txExist == False:
                        print("범위 내의 거래가 존재하지 않음.")
                    else:
                        print(f"[완료] {pathStr} ({count} record)")
                else:
                    count = main.ExportTransactionByFromTo(pathStr,fromStr,toStr)
                    
                    if count == 0:#txExist == False:
                        print("범위 내의 거래가 존재하지 않음.")
                    else:
                        print(f"[완료] {pathStr} ({count} record)")



            #"정상"이 아니면; 
            else:
                #경고문 출력;
                print(alarmString)
            
            
    elif optionStrList[0].strip().lower() == "import":
        if len(optionStrList) == 2 and optionStrList[1].strip().lower()=="help":
            print("외부의 파일을 통합 : import --from <파일 이름>")
        else:
            #[1]번째 값부터 나머지 값들을 옵션스트링리스트에 담고;
            #업데이트 입력오류 판정() 호출;
            alarmString,pathStr =main.DetermineInputErrorOfCommandOfImport(optionStrList[1:])
            #반환된 문자열=="정상"이면;
            if alarmString == "정상":
                main.ImportTransactions(pathStr)

            #"정상"이 아니면; 
            else:
                #경고문 출력;
                print(alarmString)



    elif optionStrList[0].lower() == "exit":
        sys.exit(0)
    
    #
    ActivateCLI()

