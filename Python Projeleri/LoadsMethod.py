import json

# JSON veri:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# x'i çözmek:
y = json.loads(x)

# Sonuç dict olarak çıkar:
print(y)