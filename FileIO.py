from pathlib import Path
import os
import json
import main






# 파일 경로를 저장할 전역 변수 (기본값은 현재 디렉토리)
_file_path = Path(".")
# 설정값을 저장할 jsonl 파일명
CONFIG_FILE = "config.jsonl"




def SetFilePath(path_string: str) -> None:
    """
    사용자로부터 파일 경로를 받아 전역 변수에 저장하고, config.jsonl 파일에 기록합니다.
    """
    global _file_path
    _file_path = Path(path_string)
    
    # JSONL 파일에 저장할 데이터 구성 (경로를 문자열로 변환)
    config_data = {"saved_path": str(_file_path)}
    
    # jsonl 파일로 저장 ('w' 모드로 덮어쓰기하여 항상 최신 경로 1줄만 유지)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(json.dumps(config_data, ensure_ascii=False) + "\n")
        
    print(f"📁 경로가 메모리와 {CONFIG_FILE}에 저장되었습니다: {_file_path.resolve()}")

def LoadFilePath() -> None:
    """
    config.jsonl 파일에서 저장된 경로를 읽어와 전역 변수 _file_path에 반영합니다.
    파일이 없으면 기본값('.')을 유지합니다.
    """
    global _file_path
    config_path = Path(CONFIG_FILE)
    
    # 설정 파일이 존재하는지 먼저 확인
    if not config_path.exists():
        print(f"ℹ️ {CONFIG_FILE} 파일이 없습니다. 기본 경로('.')를 사용합니다.")
        _file_path = Path(".")
        return

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            line = f.readline().strip()
            if line:
                config_data = json.loads(line)
                # 불러온 문자열을 다시 Path 객체로 변환하여 저장
                _file_path = Path(config_data["saved_path"])
                print(f"🔄 {CONFIG_FILE}에서 경로를 불러왔습니다: {_file_path.resolve()}")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"⚠️ 설정 파일을 읽는 중 오류가 발생하여 기본 경로를 사용합니다: {e}")
        _file_path = Path(".")

def GetFullPath(filename: str) -> str:
    """
    저장된 파일 경로와 파일명을 합친 전체 경로를 문자열로 반환합니다.
    """
    global _file_path
    full_path = _file_path / filename
    #print(f"📄 전체 경로: {full_path.resolve()}")
    return str(full_path)


#기본 주소값 붙여서 리턴하는 데코레이터 함수;
def add_base_path(func):
    def wrapper(filename):
        # 전역 변수 _file_path를 사용하여 기본 경로를 가져옴
        global _file_path
        full_path = _file_path / filename
        return func(str(full_path))  # Path 객체를 문자열로 변환하여 전달
    return wrapper

@add_base_path
def transaction_generator(file_path):
    # 1. 파일이 존재하는지, 그리고 크기가 0인지 체크하여 비어있으면 경고
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        #print(f"⚠️ 경고: 파일이 비어있거나 존재하지 않습니다. ({file_path})")
        return  # 혹은 raise ValueError("파일이 비어있습니다.") 로 에러를 던질 수 있습니다.

    try:
        has_data = False  # 실제 데이터가 한 줄이라도 있었는지 체크할 변수
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    has_data = True
                    #print("line : " + line.strip())
                    yield line.strip()
        
        # 파일은 존재하지만 내용이 전부 공백/줄바꿈이라 실행이 안 된 경우
        if not has_data:
            print(f"⚠️ 경고: 파일에 유효한 데이터가 없습니다. ({file_path})")
                    
    except Exception as e:
        print("transaction_generator 오류 : " + str(e))




categoryList = []
def SaveCategoryList():
    #global defaultFolderPath
    #path = defaultFolderPath+ "/categories.jsonl"
    path = GetFullPath("categories.jsonl")
    try:
        with open(path, "w", encoding='utf-8') as file:
            for category in categoryList:
                file.write(f"{category}\n")
        #sys.exit(0)
    except FileNotFoundError as e:
        # 1. 사용자에게 시스템 구조를 숨기고 안전한 메시지만 출력
        print("❌ [오류] 지정된 파일이나 폴더 경로를 찾을 수 없습니다.")        
                
def LoadCategoryList():
    global categoryList
    #global defaultFolderPath
    #path = defaultFolderPath+ "/categories.jsonl"
    #path = "categories.jsonl"
    path = GetFullPath("categories.jsonl")
    #print("LoadCategoryList path : "+path)
    
    try:
        with open(path, "r", encoding='utf-8') as file:
            for line in file:
                category = line.strip()
                if category:
                    categoryList.append(category)
        
        if len(categoryList)==0:
            categoryList.append("food")
            categoryList.append("transport")
            categoryList.append("rent")
            categoryList.append("etc")
            SaveCategoryList()
        #sys.exit(0)
    except FileNotFoundError as e:
        # 1. 사용자에게 시스템 구조를 숨기고 안전한 메시지만 출력
        print("❌ [오류] 지정된 파일이나 폴더 경로를 찾을 수 없습니다.")
        
    #print("categoryList : "+str(categoryList))
    
    
    
    
def SaveBudgetDataListToFile():
    import main
    #global defaultFolderPath
    #tmpFilePath=defaultFolderPath+ "/tmpBudget.jsonl"
    #oldFilePath=defaultFolderPath+ "/budgets.jsonl"
    tmpFilePath=GetFullPath("tmpBudget.jsonl")
    oldFilePath=GetFullPath("budgets.jsonl")
    
    try:
        # 1. 임시 파일에 데이터 쓰기 (파일이 없으면 w 모드로 자동 생성됨)
        with open(tmpFilePath, 'w', encoding='utf-8', newline='') as f_out:
            for budgetData in budgetDataList:
                # 클래스 인스턴스의 데이터를 콤마 구분 문자열로 가공
                line = main.TransformBudgetDataToLine(budgetData)
                # JSONL 형식으로 쓰기
                #f_out.write(json.dumps(line, ensure_ascii=False) + '\n')
                f_out.write(line + '\n')
        #sys.exit(0)
        
        # 2. 파일 교체 작업 (기존 원본을 지우고 임시 파일의 이름을 원본명으로 변경)
        # os.replace는 원본 파일이 없으면 그냥 생성하고, 있으면 기존 원본을 '제거'하면서 강제 덮어씁니다.
        os.replace(tmpFilePath, oldFilePath)

    except Exception as e:
        # 도중에 에러가 나면 쓰다 만 임시 파일을 지워 정돈합니다.
        if os.path.exists(tmpFilePath):
            os.remove(tmpFilePath)
        #sys.exit(1)
    except FileNotFoundError as e:
        # 1. 사용자에게 시스템 구조를 숨기고 안전한 메시지만 출력
        print("❌ [오류] 지정된 파일이나 폴더 경로를 찾을 수 없습니다.")
    
        
budgetDataList = []
def LoadBudgetDataListFromFile():
    import main
    #with open("budget.jsonl", "r") as file:
    #global defaultFolderPath
    #filePath=defaultFolderPath+"/budgets.jsonl"
    #filePath="budgets.jsonl"
    filePath=GetFullPath("budgets.jsonl")

    global budgetDataList
    budgetDataList=[]
    
    try:
        # 1. 임시 파일에 데이터 쓰기 (파일이 없으면 w 모드로 자동 생성됨)
        with open(filePath, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    # 클래스 인스턴스의 데이터를 콤마 구분 문자열로 가공
                    budgetData = main.TransformLineToBudgetData(line)
                    budgetDataList.append(budgetData)
        #sys.exit(0)

    except FileNotFoundError as e:
        # 1. 사용자에게 시스템 구조를 숨기고 안전한 메시지만 출력
        print("❌ [오류] 지정된 파일이나 폴더 경로를 찾을 수 없습니다.")



largestUsedId=-1
#사용된 최대 아이디값 불러오기();
def LoadLargestUsedId():
    import main
    oldFileTx_stream = transaction_generator('transactions.jsonl')
    global largestUsedId
    
    while True:
        try:
            # 다음 거래 정보를 수동으로 1개 가져옴.
            txLine = next(oldFileTx_stream)
            #파일에서 읽어온 라인을 거래로 변환;
            oldTx=main.TransformLineToTx(txLine)
            #사용된 최대 아이디값 선별해 놓기;
            if oldTx.id > largestUsedId:
                largestUsedId=oldTx.id
                
        except StopIteration:
            # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
            #print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
            break


transactionList = []
def SaveTxListToJsonFile(txList, newFilePath:str=None):
    #print("transactionList length : "+str(len(txList)))
    #global defaultFolderPath
    #tmpFilePath=defaultFolderPath+ "/tmpTx.jsonl"
    #oldFilePath=defaultFolderPath+ "/transactions.jsonl"
    #tmpFilePath="tmpTx.jsonl"
    #oldFilePath="transactions.jsonl"
    #tmpFilePath=FileIO.add_base_path("tmpTx.jsonl")
    #oldFilePath=FileIO.add_base_path("transactions.jsonl")
    tmpFilePath=GetFullPath("tmpTx.jsonl")
    oldFilePath=GetFullPath("transactions.jsonl")


    
    try:
        # 1. 임시 파일에 데이터 쓰기 (파일이 없으면 w 모드로 자동 생성됨)
        with open(tmpFilePath, 'w', encoding='utf-8') as f_out:
            for tx in txList:
                # 클래스 인스턴스의 데이터를 콤마 구분 문자열로 가공
                line = main.TransformTxToLine(tx)
                #print("line : "+line)
                # JSONL 형식으로 쓰기
                #f_out.write(json.dumps(line, ensure_ascii=False) + '\n')
                f_out.write(line + '\n')
        
        # 2. 파일 교체 작업 (기존 원본을 지우고 임시 파일의 이름을 원본명으로 변경)
        # os.replace는 원본 파일이 없으면 그냥 생성하고, 있으면 기존 원본을 '제거'하면서 강제 덮어씁니다.
        if newFilePath is None:
            os.replace(tmpFilePath, oldFilePath)
        else:
            os.replace(tmpFilePath, GetFullPath(newFilePath))
        #print(f"✅ 파일 쓰기 완료: '{file_path}'로 안전하게 교체되었습니다.")
        #sys.exit(0)

    except Exception as e:
        # 도중에 에러가 나면 쓰다 만 임시 파일을 지워 정돈합니다.
        if os.path.exists(tmpFilePath):
            os.remove(tmpFilePath)
        print(f"❌ 파일 작업 중 오류 발생: {e}")
        #sys.exit(1)
    except FileNotFoundError as e:
        # 1. 사용자에게 시스템 구조를 숨기고 안전한 메시지만 출력
        print("❌ [오류] 지정된 파일이나 폴더 경로를 찾을 수 없습니다.")
        
