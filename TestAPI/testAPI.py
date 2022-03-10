import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_INF_OEE03"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok

data2 = """
{
    "Order": "90060694",
    "Operation": "0012",
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
            "End_Downtime": "21:40:00",
            "Reason_Var": "222",
            "Total_Downtime": "600"
        }
    ]
}

"""

data3 = """
{
    "Result":
    [
        {
            "PDOrder": "90060694",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "19:34:24"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "20:10:59"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "20:44:32"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "21:22:08"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "21:39:31"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "2136",
                            "Date": "2021-10-06",
                            "Time": "23:50:57"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-05",
                            "Time": "23:50:58"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "0:24:20"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "0:57:54"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "1:37:43"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "2:06:32"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "2:44:48"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "4:06:43"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "4:46:05"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "5:22:55"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "6:04:39"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "6:25:25"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "8:10:52"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "8:47:55"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "9:06:27"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "9:38:50"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "11:00:37"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "11:33:50"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "3264",
                            "Date": "2021-10-06",
                            "Time": "12:49:40"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "600",
                            "Date": "2021-10-06",
                            "Time": "17:15:19"
                        }
                    ]
                }
            ]
        }
    ]
}
"""


resp = requests.post(url, headers=headers, data=data3)

print(resp.status_code)