import json

#cd 1_Season/Mission_2-1; python3 main.py
#python3 main.py
#python -m budget_app
#python -m budget_app category remove
#python -m budget_app search --tag d
#python -m budget_app update --id TX-000011 --date 2026-10-01
#python -m budget_app update --id TX-000011 --date 2026-10-07 --type income --amount 20000 --category food --q m --tag t
#python -m budget_app budget set --month 2026-13 --asdf as
#python -m budget_app budget set --month 2026-13 --amount 50000
#python -m budget_app export --out exTx1.jsonl --from 2026-09-30 --to 2026-10-05

# 1. 한 줄씩 거래 정보를 양보(yield)하는 제너레이터 함수
def transaction_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line.strip())

# -------------------------------------------------------------
# 사용부: 특정 조건(예: 금액이 50000원 이상)을 만족하는 거래 3개 추출
# -------------------------------------------------------------
tx_stream = transaction_generator('transactions.jsonl')

target_count = 3  # 찾고 싶은 거래 개수 (n개)
found_transactions = []

# 파일에 더 이상 데이터가 없을 때 StopIteration 에러가 나는 것을 방지
while len(found_transactions) < target_count:
    try:
        # 2. 다음 거래 정보를 수동으로 1개 가져옵니다.
        tx = next(tx_stream)
        
        # 3. 특정 조건에 부합하는지 판단합니다. (예: amount >= 50000)
        if tx.get('amount', 0) >= 50000:
            found_transactions.append(tx)
            print(f"🎯 조건 만족 거래 발견 ({len(found_transactions)}/{target_count}): {tx}")
            
    except StopIteration:
        # 파일 끝까지 다 읽었는데도 n개를 못 채운 경우 예외 처리
        print(f"⚠️ 파일 끝에 도달했습니다. 조건에 맞는 거래가 {len(found_transactions)}개뿐입니다.")
        break

print("\n최종 결과:", found_transactions)








from datetime import datetime, date

# 1. 문자열로 된 날짜값을 파이썬 date 객체로 변환하는 함수
def str_to_date(date_str: str) -> date:
    """
    "YYYY-MM-DD" 형식의 문자열을 파이썬 datetime.date 객체로 변환합니다.
    (예: "2026-09-29" -> date(2026, 9, 29))
    """
    # strptime으로 문자열을 datetime 객체로 만든 뒤, 날짜(.date())만 추출합니다.
    return datetime.strptime(date_str, "%Y-%m-%d").date()


# 2. 파이썬 date 객체를 "YYYY-MM-DD" 형식의 문자열로 변환하는 함수
def date_to_str(date_obj: date) -> str:
    """
    파이썬 datetime.date 객체를 "YYYY-MM-DD" 형식의 문자열로 변환합니다.
    (예: date(2026, 9, 29) -> "2026-09-29")
    """
    # strftime을 사용하여 원하는 포맷의 문자열로 출력합니다.
    return date_obj.strftime("%Y-%m-%d")


# -------------------------------------------------------------
# 사용 예시
# -------------------------------------------------------------

# 테스트 1: 문자열 -> 데이트 객체
sample_str = "2026-09-29"
converted_date = str_to_date(sample_str)

print(f"1. 변환된 타입: {type(converted_date)}")  # <class 'datetime.date'>
print(f"   변환된 값: {converted_date}")


# 테스트 2: 데이트 객체 -> 문자열
sample_date = date(2026, 12, 25)
converted_str = date_to_str(sample_date)

print(f"2. 변환된 타입: {type(converted_str)}")   # <class 'str'>
print(f"   변환된 값: '{converted_str}'")



#python3 main.py
#python -m budget_app






import json
from pathlib import Path

# 파일 경로를 저장할 전역 변수 (기본값은 현재 디렉토리)
_file_path = Path(".")
# 설정값을 저장할 jsonl 파일명
CONFIG_FILE = "config.jsonl"

def set_file_path(path_string: str) -> None:
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

def load_file_path() -> None:
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

def get_full_path(filename: str) -> str:
    """
    저장된 파일 경로와 파일명을 합친 전체 경로를 문자열로 반환합니다.
    """
    global _file_path
    full_path = _file_path / filename
    return str(full_path)

# [상황 1] 프로그램 처음 실행 시: 기존에 저장된 경로가 있다면 불러오기
load_file_path() 
# 처음 실행해서 config.jsonl이 없다면 -> 기본 경로('.') 사용


# [상황 2] 사용자가 새로운 경로를 지정하고 저장할 때
set_file_path("my_project/data_folder")
# 출력: 📁 경로가 메모리와 config.jsonl에 저장되었습니다.
# 결과: 프로그램 실행 폴더에 config.jsonl 파일이 생기고 그 안에 {"saved_path": "my_project/data_folder"} 가 적힙니다.


# [상황 3] 실제 파일 이름을 합쳐서 가져올 때
final_path = get_full_path("output.txt")
print(final_path)
# 출력: my_project/data_folder/output.txt (윈도우는 역슬래시)
