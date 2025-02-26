import json
import re
import pandas as pd

# 광고 및 출처 정보 제거
AD_PATTERNS = [
    r"责任编辑：.*?", r"（本文来源.*?）", r"点击阅读全文.*?", r"来源：.*?", r"更多精彩内容.*?",
    r"本文转载自.*?", r"欢迎关注我们的.*?", r"广告.*?", r"（.*?记者.*?报道）", r"如需转载请注明.*?",r"查看更多相关信息.*?"
]

def clean_text(text):
    if not isinstance(text, str):
        return ""

    # 광고 및 출처 제거
    for pattern in AD_PATTERNS:
        text = re.sub(pattern, "", text)

    # 특수 문자 및 공백 정리 (단, 구두점 `。！？`는 유지)
    text = re.sub(r'[^\w\s。！？]', '', text)  # 한자, 숫자, 구두점 외 제거
    text = re.sub(r'\s+', ' ', text).strip()  # 공백 정리
    return text

def split_sentences(text):
    if text == "":
        return []

    sentences = re.split(r'([。！？])', text)  # 문장 기호 유지
    sentences = ["".join(sentences[i:i+2]).strip() for i in range(0, len(sentences)-1, 2)]
    return sentences

def process_json(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        input_data = json.load(file)

    df = pd.DataFrame(input_data)
    df = df[['title', 'link', 'date', 'content']]
    df["date"] = pd.to_datetime(df["date"])
    df['quarter'] = df["date"].dt.to_period("Q").astype(str)
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")

    # 데이터 전처리
    df['cleaned_content'] = df['content'].apply(clean_text)
    df['sentences'] = df["cleaned_content"].apply(split_sentences)
    df["sentences"] = df["sentences"].apply(lambda x: x if isinstance(x, list) else [])

    # '한미일'이 포함된 문장 필터링
    df["filtered_sentences"] = df["sentences"].apply(lambda x: [s for s in x if "美日韩" in s])

    df["num_filtered_sentences"] =df["filtered_sentences"].apply(len)
    df["num_sentences"] = df["sentences"].apply(len)
    #한미일 문장 비중
    df["ratio"] = df.apply(lambda row: row["num_filtered_sentences"] / row["num_sentences"] if row["num_sentences"] > 0 else 0, axis=1)

    output_data = df.to_dict(orient="records")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)


input_path="../data/final_raw.json"
output_path="../data/final.json"

process_json(input_path, output_path)