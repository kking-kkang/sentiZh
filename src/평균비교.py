import json
import pandas as pd

# JSON 파일 로드
file_path_2016 = "../data/0310/results/2016_avg.json"

file_path_2023 = "../data/0310/results/2023_avg.json"

with open(file_path_2016, "r", encoding="utf-8") as file:
    data_2016 = json.load(file)

with open(file_path_2023, "r", encoding="utf-8") as file:
    data_2023 = json.load(file)

# 데이터프레임 변환
df_2016 = pd.DataFrame(data_2016)
df_2023 = pd.DataFrame(data_2023)

# avg_sentiment_score를 숫자로 변환 (NaN 값 제거)
df_2016["avg_sentiment_score"] = pd.to_numeric(df_2016["avg_sentiment_score"], errors="coerce")
df_2023["avg_sentiment_score"] = pd.to_numeric(df_2023["avg_sentiment_score"], errors="coerce")

# 분기별 상세 통계 분석 (count, mean, std, min, 25%, 50%(median), 75%, max)
detailed_stats_2016 = df_2016.groupby("quarter")["avg_sentiment_score"].describe()
detailed_stats_2016["Year"] = 2016

detailed_stats_2023 = df_2023.groupby("quarter")["avg_sentiment_score"].describe()
detailed_stats_2023["Year"] = 2023

# 결과를 하나의 데이터프레임으로 합치기
detailed_comparison = pd.concat([detailed_stats_2016, detailed_stats_2023]).reset_index()
print(detailed_comparison)

