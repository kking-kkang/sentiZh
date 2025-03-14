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
            aggregated_data[base_title] = {"total_sentiment": 0, "count": 0}

        aggregated_data[base_title]["total_sentiment"] += avg_sentiment
        aggregated_data[base_title]["count"] += 1

# 평균 감성 점수 계산
final_results = []
for title, values in aggregated_data.items():
    avg_score = values["total_sentiment"] / values["count"]
    final_results.append({"title": title, "avg_sentiment_score": avg_score})

# DataFrame 변환 및 저장
df_results = pd.DataFrame(final_results)
df_results.to_csv("aggregated_sentiment_scores.csv", index=False, encoding="utf-8")

# 출력
print(df_results)
