import requests
import json
import random

print(
    """*********** Welcome to ALA **********
    (1) proxyempire.io
    (2) x
    (3) x
    (4) x
"""
)
while 1:
    try:
        proxysite = int(input("\nQ. 프록시사이트번호를 입력하시오 : "))
    except:
        print("\n번호똑바로입력하시오 휴먼")
        continue
    if 0 < proxysite < 5:
        print(proxysite)
        break
    else:
        print("\n번호똑바로입력하시오 휴먼")

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

while 1:
    try:
        cityIndex = int(input("Q. 주를 고르시오 : "))
    except:
        print(f"""\n*******************  번호똑바로입력하시오  *******************""")
        continue
    if 0 <= cityIndex < 50:
        choosen_city = cities[cityIndex]
        print(
            f"""\n*******************  {choosen_city}주로 접속을 시도합니다  *******************"""
        )
        break
    else:
        print(f"""\n*******************  번호똑바로입력하시오  *******************""")

random_num = random.randint(9000, 9999)
proxyip = (
    f"rotating.proxyempire.io:{random_num}:zUzdZbdi3gtuDvOZ:wifi;us;;{choosen_city}"
)

list_proxyip = proxyip.split(":")
print(f"\nIP 주소 = {proxyip}")
