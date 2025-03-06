import json

def load_json(file_path):
    """JSON 파일을 불러와 리스트로 반환"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def remove_duplicates_by_title(data):
    """제목(title) 기준으로 중복 제거"""
    seen_titles = set()  # 중복 확인용 집합
    unique_data = []  # 중복 제거된 결과 리스트

    for item in data:
        title = item.get('link', '')  # 제목 가져오기
        if title not in seen_titles:
            seen_titles.add(title)  # 중복 체크
            unique_data.append(item)  # 결과 리스트에 추가

    return unique_data

def input_json(file_path, data):
    """결과 JSON을 저장"""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 파일 경로 설정
input_file = "0227_marged1.json"


# JSON 데이터 불러오기
data = load_json(input_file)

# 중복 제거
deduplicated_data = remove_duplicates_by_title(data)

# 결과 저장
input_json(input_file, deduplicated_data)

print(f"중복 제거 완료! 결과가 {input_file} 파일에 저장되었습니다.")
