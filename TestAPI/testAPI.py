import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_RunTime_DownTime"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok

data = """
{
    "Order": "90060694",
    "Operation": "0011",
    "RunTime": [{
        "Post_Date": "06-10-2021",
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
            "Post_Date": "06-10-2021",
            "Start_Downtime": "4:00:00",
            "End_Downtime": "4:18:00",
            "Reason_Var": "5",
            "Total_Downtime": "1080"
        },
        {
            "Post_Date": "06-10-2021",
            "Start_Downtime": "5:00:00",
            "End_Downtime": "5:18:00",
            "Reason_Var": "5",
            "Total_Downtime": "1080"
        },
        {
            "Post_Date": "06-10-2021",
            "Start_Downtime": "7:00:00",
            "End_Downtime": "7:15:00",
            "Reason_Var": "200",
            "Total_Downtime": "900"
        }, 
        {
            "Post_Date": "06-10-2021",
            "Start_Downtime": "7:30:00",
            "End_Downtime": "7:40:00",
            "Reason_Var": "200",
            "Total_Downtime": "600"
        }, 
        {
            "Post_Date": "06-10-2021",
            "Start_Downtime": "21:00:00",
            "End_Downtime": "21:12:00",
            "Reason_Var": "222",
            "Total_Downtime": "900"
        },
        {
            "Post_Date": "06-10-2021",
            "Start_Downtime": "21:30:00",
            "End_Downtime": "21:51:00",
            "Reason_Var": "222",
            "Total_Downtime": "600"
        }
    ]
}

"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)