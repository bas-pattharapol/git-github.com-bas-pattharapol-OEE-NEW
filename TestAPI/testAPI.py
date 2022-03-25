import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_INF_OEE04"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok

data1 = """
{
    "Result":
    [
        {
            "PDOrder": "000090073296",
            "Machine":
            [
                {
                    "ID": "2271-01",
                    "GI":
                    [
                        {
                            "QTY": "9900.000",
                            "Dep": "GI for Order",
                            "Date": "2022-03-21",
                            "Time": "14:52:52"
                        },
                        {
                            "QTY": "9898.000",
                            "Dep": "GI for Order",
                            "Date": "2022-03-21",
                            "Time": "14:54:54"
                        },
                        {
                            "QTY": "12.000",
                            "Dep": "GI for Order",
                            "Date": "2022-03-21",
                            "Time": "15:17:17"
                        }
                    ]
                }
            ]
        },
        {
            "PDOrder": "",
            "Machine":
            []
        }
    ]
}
"""

resp = requests.post(url, headers=headers, data=data1)

print(resp.status_code)