import json

x = """{"Name": "abdullah", 
 "iletişim": 5312267590,
  "email": "abdullah18basaran@gmail.com", 
  "Hobiler": ["Kod Okuma", "Kod yazma"]}"""

y = json.loads(x)

print(y)