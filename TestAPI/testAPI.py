import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_RunTime_DownTime"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok

data1 = """
{
    "Order": "90065293",
    "Operation": "0012",
    "RunTime": [{
        "Post_Date": "27-10-2021",
        "Start_Runtime": "14:12:01",
        "End_Runtime": "15:12:10",
        "Total_Runtime": "60"
    },{
        "Post_Date": "06-10-2021",
        "Start_Runtime": "15:12:01",
        "End_Runtime": "16:12:10",
        "Total_Runtime": "60"
    }],
    "DonwTime": [{
            "Post_Date": "28-10-2021",
            "Start_Downtime": "5:00:00",
            "End_Downtime": "7:15:00",
            "Reason_Var": "224",
            "Total_Downtime": "8100"
        }
    ]
}
"""

resp = requests.post(url, headers=headers, data=data1)

print(resp.status_code)