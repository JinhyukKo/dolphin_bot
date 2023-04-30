import requests
import json

# platform:linux
# browser_type:anty
# browser_version:112
# type:ingerprint
# screen:2560x1440
url = "https://anty-api.com/fingerprints/fingerprint?platform=windows&browser_type=anty&browser_version=112&type=fingerprint&screen=2560x1440"

payload = {}
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjM0MTMzNCwidXNlcm5hbWUiOiJhbGFnZW5jeXNlcnZpY2VAZ21haWwuY29tIiwicm9sZSI6ImFkbWluIiwidGVhbUlkIjoyMjgzMzk2LCJ0b2tlbkNyZWF0ZWRBdCI6MTY4Mjc4MzAwNH0.YCVpsd_jt0uD5b7sHFadFSVhDomLa4gXjPb0jg-wi04",
}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)
print(data)

# print(len(list(data.keys())))
# print(type(data))
# {
#     "screen": {
#         "availWidth": 1600,
#         "availHeight": 870,
#         "width": 1600,
#         "height": 900,
#         "colorDepth": 24,
#         "pixelDepth": 24,
#     },
#     "connection": {"downlink": 10, "rtt": 50, "effectiveType": "4g", "saveData": 0},
#     "deviceMemory": 8,
#     "hardwareConcurrency": 4,
#     "donottrack": 0,
#     "language": "",
#     "languages": "",
#     "productSub": "20030107",
#     "vendorSub": "",
#     "vendor": "Google Inc.",
#     "appCodeName": "Mozilla",
#     "appVersion": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
#     "platform": "Win32",
#     "product": "Gecko",
#     "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
#     "cpu": {"architecture": "amd64"},
#     "os": {"name": "Windows", "version": "10"},
#     "browser": {"name": "Chrome", "version": "112.0.0.0", "shortVersion": 112},
#     "webgl": {
#         "unmaskedVendor": "Google Inc. (Intel)",
#         "unmaskedRenderer": "ANGLE (Intel, Intel(R) HD Graphics 4400 Direct3D11 vs_5_0 ps_5_0, D3D11)",
#     },
#     "voices": "[]",
#     "fonts": '["Agency FB", "Arial Black", "Arial", "Bauhaus 93", "Bell MT", "Bodoni MT", "Bookman Old Style", "Broadway", "Calibri Light", "Calibri", "Californian FB", "Cambria Math", "Cambria", "Candara", "Castellar", "Centaur", "Century Gothic", "Colonna MT", "Comic Sans MS", "Consolas", "Constantia", "Copperplate Gothic Light", "Corbel", "Courier New", "Ebrima", "Engravers MT", "Forte", "Franklin Gothic Heavy", "Franklin Gothic Medium", "French Script MT", "Gabriola", "Georgia", "Gigi", "Goudy Old Style", "Haettenschweiler", "Harrington", "Impact", "Informal Roman", "Lucida Bright", "Lucida Console", "Lucida Fax", "Lucida Sans Unicode", "MS Gothic", "MS PGothic", "MS Reference Sans Serif", "MS UI Gothic", "MV Boli", "Magneto", "Malgun Gothic", "Marlett", "Matura MT Script Capitals", "Microsoft Himalaya", "Microsoft JhengHei", "Microsoft New Tai Lue", "Microsoft PhagsPa", "Microsoft Sans Serif", "Microsoft Tai Le", "Microsoft YaHei", "Microsoft Yi Baiti", "MingLiU-ExtB", "MingLiU_HKSCS-ExtB", "Mongolian Baiti", "NSimSun", "Niagara Solid", "PMingLiU-ExtB", "Palace Script MT", "Palatino Linotype", "Papyrus", "Perpetua", "Playbill", "Rockwell", "Segoe Print", "Segoe Script", "Segoe UI Light", "Segoe UI Semibold", "Segoe UI Symbol", "Segoe UI", "Showcard Gothic", "SimSun", "SimSun-ExtB", "Snap ITC", "Sylfaen", "Symbol", "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana", "Vladimir Script", "Webdings", "Wide Latin", "Wingdings"]',
#     "browserType": "chrome",
#     "platformVersion": "10.0.0",
#     "uaFullVersion": "112.0.5615.49",
#     "webgl2Maximum": '{"UNIFORM_BUFFER_OFFSET_ALIGNMENT":256,"MAX_TEXTURE_SIZE":16384,"MAX_VIEWPORT_DIMS":[32767,32767],"MAX_VERTEX_ATTRIBS":16,"MAX_VERTEX_UNIFORM_VECTORS":4096,"MAX_VARYING_VECTORS":30,"MAX_COMBINED_TEXTURE_IMAGE_UNITS":32,"MAX_VERTEX_TEXTURE_IMAGE_UNITS":16,"MAX_TEXTURE_IMAGE_UNITS":16,"MAX_FRAGMENT_UNIFORM_VECTORS":1024,"MAX_CUBE_MAP_TEXTURE_SIZE":16384,"MAX_RENDERBUFFER_SIZE":16384,"MAX_3D_TEXTURE_SIZE":2048,"MAX_ELEMENTS_VERTICES":2147483647,"MAX_ELEMENTS_INDICES":2147483647,"MAX_TEXTURE_LOD_BIAS":2,"MAX_DRAW_BUFFERS":8,"MAX_FRAGMENT_UNIFORM_COMPONENTS":4096,"MAX_VERTEX_UNIFORM_COMPONENTS":16384,"MAX_ARRAY_TEXTURE_LAYERS":2048,"MIN_PROGRAM_TEXEL_OFFSET":-8,"MAX_PROGRAM_TEXEL_OFFSET":7,"MAX_VARYING_COMPONENTS":120,"MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS":4,"MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS":120,"MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS":4,"MAX_COLOR_ATTACHMENTS":8,"MAX_SAMPLES":8,"MAX_VERTEX_UNIFORM_BLOCKS":12,"MAX_FRAGMENT_UNIFORM_BLOCKS":12,"MAX_COMBINED_UNIFORM_BLOCKS":24,"MAX_UNIFORM_BUFFER_BINDINGS":24,"MAX_UNIFORM_BLOCK_SIZE":65536,"MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS":212992,"MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS":200704,"MAX_VERTEX_OUTPUT_COMPONENTS":120,"MAX_FRAGMENT_INPUT_COMPONENTS":120,"MAX_ELEMENT_INDEX":4294967294}',
# }
