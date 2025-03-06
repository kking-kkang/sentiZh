import json

def load_json(file_path):
    """JSON 파일을 불러와 리스트로 반환"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_duplicates(json1, json2):
    """두 개의 JSON 데이터를 비교하여 제목(title) 기준으로 중복 확인"""
    set1 = {item.get('title', '') for item in json1}
    set2 = {item.get('title', '') for item in json2}

    return list(set1.intersection(set2))

# JSON 파일 경로 설정
file1 = "../data/final_raw.json"
file2 = "./0227_xinhuanet.json"

# JSON 데이터 불러오기
data1 = load_json(file1)
data2 = load_json(file2)

# 중복 데이터 찾기
duplicates = find_duplicates(data1, data2)

# 결과 출력
if duplicates:
    print("중복된 항목:")
    for title in duplicates:
        print({title})
else:
    print("중복된 항목이 없습니다.")
