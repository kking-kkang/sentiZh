import json
import os
from collections import defaultdict
import pandas as pd
from typing import List

def split_json_by_sentence_count(input_path: str, output_path_over: str, output_path_under: str, num: int = 60):
    """
    JSON 파일을 읽고 문장 개수가 60 이상이면 분할하여 저장하는 함수
    """
    # JSON 파일 로드
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 새로운 데이터를 저장할 리스트
    split_data_over_num = []
    split_data_under_num = []

    # 메인작업
    for item in data:
        num_sentences = item.get("num_sentences", 0)
        if num_sentences > num:
            title_base = item["title"]
            sentences = item["sentences"]
            num_parts = (num_sentences // num) + (1 if num_sentences % num > 0 else 0)

            for i in range(num_parts):
                split_item = item.copy()
                split_item["title"] = f"{title_base}-{i+1}"
                split_item["sentences"] = sentences[i*num:(i+1)*num]
                split_item["num_sentences"] = len(split_item["sentences"])
                split_data_over_num.append(split_item)
        else:
            split_data_under_num.append(item)

    # JSON 파일로 저장
    with open(output_path_over, "w", encoding="utf-8") as f:
        json.dump(split_data_over_num, f, ensure_ascii=False, indent=4)

    with open(output_path_under, "w", encoding="utf-8") as f:
        json.dump(split_data_under_num, f, ensure_ascii=False, indent=4)

    print(f" 분할된 JSON 파일이 저장되었습니다: {output_path_over}, {output_path_under}")


def split_json_by_year(input_path: str, output_dir: str) -> List[str]:
    """
    JSON 파일을 읽고 'date' 필드를 기준으로 연도별로 분류하여 저장하는 함수.
    """
    # 저장 폴더 생성
    os.makedirs(output_dir, exist_ok=True)

    # JSON 데이터 로드
    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # 연도별 데이터 저장을 위한 딕셔너리
    yearly_data = defaultdict(list)

    # 연도별로 데이터 분류
    for entry in data:
        if "date" in entry:
            try:
                year = pd.to_datetime(entry["date"]).year  # 날짜에서 연도 추출
                yearly_data[year].append(entry)
            except Exception as e:
                print(f" 날짜 변환 실패: {entry['date']} | 오류: {e}")

    # 분리된 JSON 저장
    saved_files = []
    for year, entries in yearly_data.items():
        output_file = os.path.join(output_dir, f"{year}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(entries, f, ensure_ascii=False, indent=4)
        saved_files.append(output_file)

    print(f"연도별 JSON 파일이 저장되었습니다: {saved_files}")


# 함수 실행 (60개 기준으로 나누고 60 언더 data만 연도별 분리)
input_file = "../data/final_0307.json"
output_file_over10 = "../data/0310/10/split_over10.json"
output_file_under10 = "../data/0310/10/split_under10.json"
output_directory = "../data/0310/10/split_by_year"

split_json_by_sentence_count(input_file, output_file_over10, output_file_under10,10)
split_json_by_year(output_file_over10, output_directory)