import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_INF_OEE01"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok

data1 = """
{
    "Result":
    [
        {
            "Plant": "1",
            "PDOrder": "000080114862",
            "MachineID": "2288-01",
            "Material": "203.54",
            "Description": "FLD - PLUS - GO",
            "PlanQuantity": "10000.000",
            "Bacth": "____220030",
            "Code": "",
            "PD_order1": "",
            "PD_order2": "",
            "PD_order3": "",
            "PD_order4": "",
            "PD_order5": "",
            "PD_order6": "",
            "PD_order7": "",
            "PD_order8": "",
            "PD_order9": "",
            "PD_order10": ""
        },
        {
            "Plant": "1",
            "PDOrder": "000080114862",
            "MachineID": "3212-01",
            "Material": "203.54",
            "Description": "FLD - PLUS - GO",
            "PlanQuantity": "10000.000",
            "Bacth": "____220030",
            "Code": "",
            "PD_order1": "",
            "PD_order2": "",
            "PD_order3": "",
            "PD_order4": "",
            "PD_order5": "",
            "PD_order6": "",
            "PD_order7": "",
            "PD_order8": "",
            "PD_order9": "",
            "PD_order10": ""
        }
    ]
}

"""

data2 = """
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
        },
        {
            "PDOrder": "90065292",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "11:58:02"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "12:11:01"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "12:36:20"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "13:11:56"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "13:38:56"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "15:07:07"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "16:19:12"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "16:28:07"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "17:05:18"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "17:25:20"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "17:47:22"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "17:51:50"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "18:07:36"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "18:24:45"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "19:23:17"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "19:39:52"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "960",
                            "Date": "2021-10-27",
                            "Time": "19:59:13"
                        }
                    ]
                },
                {
                    "ID": "10001662",
                    "GR_QTY":
                    [
                        {
                            "QTY": "48",
                            "Date": "2021-10-27",
                            "Time": "20:11:23"
                        }
                    ]
                }
            ]
        }
    ]
}
"""

data4 = """
{
    "Result":
    [
        {
            "PDOrder": "90060694",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "1",
                            "Dep": "Other GI",
                            "Date": "2021-10-06",
                            "Time": "19:34:24"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90065292",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "2",
                            "Dep": "Other GI",
                            "Date": "2021-10-27",
                            "Time": "11:58:02"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90065293",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "3",
                            "Dep": "Other GI",
                            "Date": "2021-10-28",
                            "Time": "9:49:11"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90065227",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "4",
                            "Dep": "Other GI",
                            "Date": "2021-11-15",
                            "Time": "3:04:27"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90065217",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "10",
                            "Dep": "Other GI",
                            "Date": "2021-11-14",
                            "Time": "19:57:58"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90066867",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "5",
                            "Dep": "Other GI",
                            "Date": "2021-11-9",
                            "Time": "0:46:29"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90066817",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "6",
                            "Dep": "Other GI",
                            "Date": "2021-11-4",
                            "Time": "8:58:38"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90068859",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "7",
                            "Dep": "Other GI",
                            "Date": "2021-11-18",
                            "Time": "23:38:18"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90068871",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "8",
                            "Dep": "Other GI",
                            "Date": "2021-11-20",
                            "Time": "9:11:52"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90068882",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "9",
                            "Dep": "Other GI",
                            "Date": "2021-11-30",
                            "Time": "11:42:45"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "90068895",
            "Machine":
            [
                {
                    "ID": "10001662",
                    "GI":
                    [
                        {
                            "QTY": "10",
                            "Dep": "Other GI",
                            "Date": "2021-11-18",
                            "Time": "4:51:47"
                        }
                    ]
                }
            ]
        }
    ]
}
                
"""
resp = requests.post(url, headers=headers, data=data1)

print(resp.status_code)