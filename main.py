import requests

API_URL = "https://api-inference.huggingface.co/models/CAMeL-Lab/bert-base-arabic-camelbert-msa-ner"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "أقدم عدد من الأشخاض مساء الخميس،على إغلاق طريق شارع الجبل الأبيض في محافظة الزرقاء بالإطارات المشتغلة. وكان أشخاص قد أغلقوا طريق بيرين شفا بدران أيضا مساء الخميس احتجاجا على أسعار المحروقات مطالبين بتخفيضها"
})
print(output)

