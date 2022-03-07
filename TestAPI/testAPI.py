import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_RunTime_DownTime"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok
data = """
{
    "PDOrder": "90067862",
    "RunTime": [{
        "BatchNo": "2101210003",
        "PostDate": "2022-01-02",
        "Shift": "1",
        "StartTime": "14:12:01",
        "EndTime": "15:12:10",
        "Time": "60"
    },{
        "BatchNo": "2101210003",
        "PostDate": "2022-01-02",
        "Shift": "1",
        "StartTime": "15:12:01",
        "EndTime": "16:12:10",
        "Time": "60"
    }],
    "DonwTime": [{
            "BatchNo": "2101210003",
            "PostDate": "01-02-2021",
            "Shift": "1",
            "StartTime": "15:12:11",
            "EndTime": "15:20:10",
            "DownTimeCode": "200",
            "Time": "8"
        },
        {
            "BatchNo": "2101210003",
            "PostDate": "2022-01-02",
            "Shift": "1",
            "StartTime": "15:21:11",
            "EndTime": "15:22:10",
            "DownTimeCode": "114",
            "Time": "1"
        }
    ]
}

"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)