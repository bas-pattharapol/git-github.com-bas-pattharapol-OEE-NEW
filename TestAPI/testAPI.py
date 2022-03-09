import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_RunTime_DownTime"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok

data = """
{
    "PDOrder": "90060694",
    "RunTime": [{
        "BatchNo": "2101210003",
        "PostDate": "06-10-2021",
        "Shift": "1",
        "StartTime": "14:12:01",
        "EndTime": "15:12:10",
        "Time": "60"
    },{
        "BatchNo": "2101210003",
        "PostDate": "06-10-2021",
        "Shift": "1",
        "StartTime": "15:12:01",
        "EndTime": "16:12:10",
        "Time": "60"
    }],
    "DonwTime": [{
            "BatchNo": "2101210003",
            "PostDate": "06-10-2021",
            "Shift": "1",
            "StartTime": "4:00:00",
            "EndTime": "4:18:00",
            "DownTimeCode": "5",
            "Time": "1080"
        },
        {
            "BatchNo": "2101210003",
            "PostDate": "06-10-2021",
            "Shift": "1",
            "StartTime": "7:00:00",
            "EndTime": "7:15:00",
            "DownTimeCode": "200",
            "Time": "900"
        }, 
        {
            "BatchNo": "2101210003",
            "PostDate": "06-10-2021",
            "Shift": "1",
            "StartTime": "7:30:00",
            "EndTime": "7:40:00",
            "DownTimeCode": "200",
            "Time": "600"
        }, 
        {
            "BatchNo": "2101210003",
            "PostDate": "06-10-2021",
            "Shift": "1",
            "StartTime": "21:00:00",
            "EndTime": "21:12:00",
            "DownTimeCode": "222",
            "Time": "900"
        },
        {
            "BatchNo": "2101210003",
            "PostDate": "06-10-2021",
            "Shift": "1",
            "StartTime": "21:30:00",
            "EndTime": "1:40:00",
            "DownTimeCode": "222",
            "Time": "600"
        }
    ]
}

"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)