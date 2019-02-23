capital = {
    "city": "Moscow",
    "temperature": 20
}
print(capital)
print(capital["city"])
print(capital["temperature"]-5)
capital["temperature"] = capital["temperature"] - 5
print(capital)
print(capital.get("country"))
print(capital.get("country", "Russia"))
capital["data"] = '27.05.2019'
print(len(capital))

eng_dic = {
"dom": "house",
"auto": "car",
"miasto": "city"
}
print(eng_dic)
print(len(eng_dic))
print(eng_dic.get("country"))