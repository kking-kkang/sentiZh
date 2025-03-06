import json

# 두 개의 JSON 파일 로드
with open("./0227_xinhuanet.json", "r", encoding="utf-8") as file:
    json_file1 = json.load(file)
with open("./0227_people.json", "r", encoding="utf-8") as file:
    json_file2 = json.load(file)
with open("./0227_huanqiu.json", "r", encoding="utf-8") as file:
    json_file3 = json.load(file)
with open("../data/final_raw.json", "r", encoding="utf-8") as file:
    json_file4 = json.load(file)
# with open("./0218/filtered_81_1.json", "r", encoding="utf-8") as file:
#     json_file5 = json.load(file)
# with open("./0218/filtered_gmw.json", "r", encoding="utf-8") as file:
#     json_file6 = json.load(file)
merged_data = json_file1 + json_file2 + json_file3 + json_file4 #+ json_file5 + json_file6

print(f"json_file1 개수: {len(json_file1)}")
print(f"json_file2 개수: {len(json_file2)}")
print(f"json_file3 개수: {len(json_file3)}")
print(f"json_file4 개수: {len(json_file4)}")
# print(f"json_file5 개수: {len(json_file5)}")
# print(f"json_file6 개수: {len(json_file6)}")
print(f"총 머지된 데이터 개수: {len(merged_data)}")

#합친 데이터를 새로운 JSON 파일로 저장
with open("0227_marged1.json", "w", encoding="utf-8") as file:
    json.dump(merged_data, file, ensure_ascii=False, indent=4)


