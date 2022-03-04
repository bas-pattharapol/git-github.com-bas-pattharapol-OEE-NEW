import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_RunTime_DownTime"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok
data = """
{
    "PDOrder": "90066773",
    "RunTime": [{
        "BatchNo": "2101210003",
        "PostDate": "28-01-2022",
        "Shift": "1",
        "StartTime": "14:12:01",
        "EndTime": "15:12:10",
        "Time": "100"
    }],
    "DonwTime": [{
            "BatchNo": "2101210003",
            "PostDate": "28-01-2022",
            "Shift": "1",
            "StartTime": "15:12:11",
            "EndTime": "15:20:10",
            "DownTimeCode": "200"
        },
        {
            "BatchNo": "2101210003",
            "PostDate": "28-01-2022",
            "Shift": "1",
            "StartTime": "15:21:11",
            "EndTime": "15:22:10",
            "DownTimeCode": "114",
            "Time": "100"
        }
    ]
}

"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)