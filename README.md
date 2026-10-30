# Codyssey_Mission_B2-1
코디세이 과제B2-1 제출용 저장소


1.실행방법
main.py파일을 실행하여 프로그램 구동.
```python
python3 main.py
```


2.저장 파일 위치/형식

기본 위치 : 파이썬 파일이 위치한 폴더;
./data/ : data --dir 명령어 테스트를 위한 경로


3.주요 명령 예시;
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


