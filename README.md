# Codyssey_Mission_B2-1
코디세이 과제B2-1 제출용 저장소


1.실행방법
main.py파일을 실행하여 프로그램 구동.
```python
python3 main.py
```


2.저장 파일 위치/형식

기본 위치 : 파이썬 파일이 위치한 폴더.  
./data/ : data --dir 명령어 테스트를 위한 경로.


3.주요 명령 예시  
거래 추가
```bash
python -m budget_app add
```
거래 목록
```bash
python -m budget_app list
```
카테고리 관리
```bash
python -m budget_app category add
python -m budget_app category remove
python -m budget_app category list
```
예산 설정, 월별 요약
```bash
python -m budget_app budget set --month 2024-01 --amount 500000
```
거래 내역 export/import
```bash
python -m budget_app export --out export.csv --month 2024-01
python -m budget_app import --from import.csv
```


4.import/export CSV 스키마

| column | required | 설명 |
| --- | --- | --- |
| date | Y | YYYY-MM-DD |
| type | Y | income / expense |
| category | Y | 등록된 카테고리 |
| amount | Y | 양수 정수 |
| memo | N | 문자열 |
| tags | N | 쉼표(,) 구분 문자열 |
| 공통: UTF-8, 헤더 포함 |   |   |



- 데코레이터를 사용하는 이유  
공통으로 사용하는 코드를 하나로 묶어서 코드 중복을 제거하고, 가동성, 유지보수, 재사용성을 높일수 있음.  



- 타입 힌트의 이점  
실시간 경고를 통해 버그 조기 발견.  
자동생성에 도움.  



- jsonl과 csv의 장단점 비교  
|     | jsonl | csv |
| --- | --- | --- |
| 가독성 | 프로그래밍 언어 친화적 | 사용자,데이터 관련 도구 친화적 |
| 유연성 | 행마다 다른 필드 구성 가능 | 모든 행이 동일한 구조(데이터 오염 위험, 스키마 변화에 취약) |
| 용량 | 상대적으로 큼 | 상대적으로 작음 |




- CSV에 일부 깨진 행이 섞인 경우 신뢰성을 보전하는 방법  
1-1.전체 롤백 : 데이터 무결성이 중요한 경우  
1-2.부분 처리 : 일부 누락되어도 전체 비즈니스에 지장이 없는 경우  
2.상세 리포트  
정확인 위치 좌표를 제공하여 어디가 왜 틀렸는지를 공지.
시스템 에러 로그를 그대로 노출하지 말고, 사용자가 이해할 수 있는 용어로 공지.





