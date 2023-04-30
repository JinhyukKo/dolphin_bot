import requests
import json

print(
    """*********** Welcome to ALA **********
    (1) proxyempire.io
    (2) x
    (3) x
    (4) x
"""
)

proxysite_num = input("프록시사이트번호를 입력해라 : ")
proxysite = int(proxysite_num)
if 0 < proxysite < 5:
    print(proxysite)
else:
    print("번호똑바로입력하시오 휴먼")
    raise

token = "zfvLnWqQB2H9o2Wk2stZ8NmTUXCJ3C1uMPctfpq9"


url = "https://panel.proxyempire.io/api/regions/us/wifi"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}
files = []
response = requests.request("GET", url, headers=headers, files=files)
print(response.text)
cities = json.loads(response.text)  # list
i = -1
for city in cities:
    i = i + 1
    print(f"""({i}) {city.upper()}""")

cityIndex = int(input("주를 고르시오 : "))
choosen_city = cities[cityIndex]
if 0 <= cityIndex < 50:
    print(f"""{choosen_city}주로 접속을 시도합니다""")

proxyip = f"rotating.proxyempire.io:9000:zUzdZbdi3gtuDvOZ:wifi;us;;{choosen_city};"

list_proxyip = proxyip.split(":")
print(list_proxyip[0])
# print(proxyip)
