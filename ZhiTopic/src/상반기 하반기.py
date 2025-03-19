import pandas as pd
import json

file_path = "../data/tokenized_data_제거3.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# 'date' 컬럼이 날짜 형식인지 확인 후 변환
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 'YYYYH1' 또는 'YYYYH2' 형식으로 변환
df['input_half'] = df['date'].dt.year.astype(str) + df['date'].dt.month.apply(lambda x: 'H1' if x <= 6 else 'H2')

# Timestamp → 문자열(ISO 8601 형식)로 변환하여 JSON 저장 오류 방지
df['date'] = df['date'].dt.strftime('%Y-%m-%dT%H:%M:%S')

# JSON 파일로 저장
output_file = "../data/tokenized_data_제거3-1.json"
json_data = df.to_dict(orient="records")  # DataFrame → JSON 리스트 변환
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)

print(f"JSON 파일 저장 완료: {output_file}")
