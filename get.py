import requests

url = "https://anty-api.com/browser_profiles/82183224"

payload = {}
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjM0MTMzNCwidXNlcm5hbWUiOiJhbGFnZW5jeXNlcnZpY2VAZ21haWwuY29tIiwicm9sZSI6ImFkbWluIiwidGVhbUlkIjoyMjgzMzk2LCJ0b2tlbkNyZWF0ZWRBdCI6MTY4Mjc4MzAwNH0.YCVpsd_jt0uD5b7sHFadFSVhDomLa4gXjPb0jg-wi04",
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

{
    "id": 82183224,
    "teamId": 2283396,
    "userId": 2341334,
    "name": "John - Tinder_Kate #03 (North Carolina) 0426",
    "tags": ["John", "Tinder"],
    "platform": "windows",
    "browserType": "anty",
    "mainWebsite": "",
    "useragent": {
        "mode": "manual",
        "value": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36",
    },
    "webrtc": {"mode": "altered", "ipAddress": null},
    "canvas": {"mode": "real"},
    "webgl": {"mode": "real"},
    "webglInfo": {
        "mode": "manual",
        "vendor": "Google Inc.",
        "renderer": "ANGLE (Intel(R) UHD Graphics 600 Direct3D11 vs_5_0 ps_5_0)",
    },
    "clientRect": {"mode": "real"},
    "notes": {
        "content": "<p>ProxyEmire Static Resi\u00a0(SOCKS5)<\/p>",
        "color": "blue",
        "style": "text",
        "icon": "info",
    },
    "timezone": {"mode": "auto", "value": null},
    "locale": {"mode": "auto", "value": null},
    "tabs": [
        "https:\/\/iphey.com\/",
        "https:\/\/mylocation.org\/",
        "https:\/\/iphey.com\/",
        "https:\/\/mylocation.org\/",
    ],
    "ports": {"mode": "protect", "blacklist": "3389,5900,5800,7070,6568,5938"},
    "proxyId": 62605194,
    "proxy": {
        "id": 62605194,
        "name": "socks5:\/\/\tstatic.proxyempire.io:9000:user_185.104.15.103:db2cd51d3c",
        "type": "socks5",
        "host": "static.proxyempire.io",
        "savedByUser": 1,
        "cryptoKeyId": 44,
        "login": "user_185.104.15.103",
        "password": "db2cd51d3c",
        "changeIpUrl": null,
        "port": "9000",
    },
    "access": {"view": 1, "update": 1, "delete": 1, "share": 1, "usage": 1},
    "status": {"id": 5360505, "name": "SHD-BANNED", "color": "orange"},
    "geolocation": {
        "mode": "auto",
        "latitude": null,
        "longitude": null,
        "accuracy": null,
    },
    "cpu": {"mode": "manual", "value": 2},
    "memory": {"mode": "manual", "value": 4},
    "platformName": "Win32",
    "cpuArchitecture": "amd64",
    "osVersion": "10",
    "screen": {"width": null, "height": null, "mode": "real", "resolution": null},
    "connection": {
        "downlink": 10,
        "effectiveType": "4g",
        "rtt": 100,
        "saveData": false,
    },
    "vendorSub": "",
    "productSub": "20030107",
    "vendor": "Google Inc.",
    "product": "Gecko",
    "doNotTrack": false,
    "args": [],
    "appCodeName": "Mozilla",
    "userFields": null,
    "updated_at": "2023-04-29T09:22:52.000000Z",
    "mediaDevices": {
        "mode": "real",
        "audioInputs": null,
        "videoInputs": null,
        "audioOutputs": null,
    },
    "storagePath": "7ff8b539d24bc7abf9b19e4e8cc649e1309c2891f0cf03a1c40512c44b3ca2ad\/90b1d5d0d019c93b41dfafc4c2e086df7a9baf574f319aa173aa855b0fa73858\/90b1d5d0d019c93b41dfafc4c2e086df7a9baf574f319aa173aa855b0fa73858",
    "lastRunningTime": null,
    "lastRunnedByUserId": null,
    "lastRunUuid": null,
    "running": 0,
    "platformVersion": "10.0.0",
    "uaFullVersion": "112.0.5615.48",
    "extensionsNewNaming": true,
    "login": "",
    "password": "",
    "bookmarks": [],
    "extensions": [],
    "homepages": [],
}
