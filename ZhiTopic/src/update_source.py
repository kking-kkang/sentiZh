import json

# JSON 파일 경로
file_path = '../data/final_0307.json'

# JSON 파일 열기
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 'source' 필드의 값이 NaN인 경우 '环球网'으로 변경
def update_source(data):
    if isinstance(data, list):
        for item in data:
            update_source(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if key == 'source' and (value != value):  # NaN 값을 체크하는 방법
                data[key] = '环球网'
            else:
                update_source(value)

# 데이터 수정
update_source(data)

# 수정된 데이터 저장
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"{file_path} 파일이 수정되었습니다.")
