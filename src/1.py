import json
from collections import defaultdict

def load_json(file_path):
    """JSON 파일을 불러와 리스트로 반환"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_prefix(title, length=5):
    """제목의 앞에서 지정된 글자 수만큼 추출 (기본 5글자)"""
    return title[:length] if len(title) >= length else title

def group_titles_by_prefix(data, prefix_length=5):
    """제목의 앞 글자를 기준으로 유사한 제목 그룹화"""
    title_groups = defaultdict(list)

    for item in data:
        raw_title = item.get('title', '')  # 원본 제목
        prefix = get_prefix(raw_title, prefix_length)  # 앞 5글자 추출
        title_groups[prefix].append(raw_title)  # 같은 접두사끼리 그룹화

    # 중복이 있는 경우만 필터링
    return {key: values for key, values in title_groups.items() if len(values) > 1}

# JSON 파일 경로 설정
file_path = "./cleaned_marged.json"

# JSON 데이터 불러오기
data = load_json(file_path)

# 앞 5글자가 같은 제목 그룹 찾기
similar_titles = group_titles_by_prefix(data)

print(len(similar_titles))

# 결과 출력
if similar_titles:
    for prefix, titles in similar_titles.items():
        print(f"✅ 공통 접두사: {prefix}")
        for title in titles:
            print(f"   - {title}")
else:
    print("유사한 제목이 없습니다.")
