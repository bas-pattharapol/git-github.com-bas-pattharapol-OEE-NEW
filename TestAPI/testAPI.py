import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_INF_OEE03"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok
data = """
{
    "Result":
    [
    
        {
            "PDOrder": "000090000004",
            "Machine":
            [
                {
                    "ID": "",
                    "GR_QTY":
                    [
                        {
                            "QTY": "       720.000",
                            "Date": "2018-03-01",
                            "Time": "16:13:13"
                        }
                    ]
                },
                {
                    "ID": "",
                    "GR_QTY":
                    [
                        {
                            "QTY": "       720.000",
                            "Date": "2018-03-01",
                            "Time": "16:13:13"
                        }
                    ]
                },
                {
                    "ID": "",
                    "GR_QTY":
                    [
                        {
                            "QTY": "       720.000",
                            "Date": "2018-03-",
                            "Time": "16:13:13"
                        }
                    ]
                }
            ]
        }
    ]
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)