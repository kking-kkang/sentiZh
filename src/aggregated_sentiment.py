import json
import pandas as pd

# JSON 파일 로드
file_path = "../data/0310/results/2016.json"  # 실제 파일 경로로 변경
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# 데이터 가공
aggregated_data = {}
for article in data:
    base_title = article["title"].rsplit("-", 1)[0]  # "-1", "-2" 같은 숫자 제거한 제목
    avg_sentiment = article.get("avg_sentiment_score")

    if avg_sentiment is not None:
        if base_title not in aggregated_data:
            # 기존 컬럼을 유지한 채 초기화
            aggregated_data[base_title] = {
                "total_sentiment": 0,
                "count": 0,
                "link": article["link"],
                "date": article["date"],
                "source": article["source"],
                "quarter": article["quarter"],
                "cleaned_content": article["cleaned_content"],  # 전체 기사 내용 포함
            }

        aggregated_data[base_title]["total_sentiment"] += avg_sentiment
        aggregated_data[base_title]["count"] += 1

# 평균 감성 점수 계산
final_results = []
for title, values in aggregated_data.items():
    avg_score = values["total_sentiment"] / values["count"]
    final_results.append({
        "title": title,
        "avg_sentiment_score": avg_score,
        "link": values["link"],
        "date": values["date"],
        "source": values["source"],
        "quarter": values["quarter"],
        "cleaned_content": values["cleaned_content"]
    })

# DataFrame 변환 및 저장

with open("../data/0310/results/2016_avg.json", "w", encoding="utf-8") as f:
    json.dump(final_results, f, ensure_ascii=False, indent=4)
