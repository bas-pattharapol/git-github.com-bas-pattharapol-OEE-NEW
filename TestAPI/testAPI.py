import requests
from requests.structures import CaseInsensitiveDict

url = "http://192.168.1.38:5001/API_INF_OEE05"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok
data = """
{
    "PDOrder": "90066773",
    "Machine": [
        {
            "ID": "xxxxxxxx2",
            "Return": [{
                "QTY": "4",
                "Text": "-----------",
                "Date": "2021-12-12",
                "Time": "12:12:12"
            }, {
                "QTY": "5",
                "Text": "-----------",
                "Date": "2021-12-12",
                "Time": "12:12:12"
            }, {
                "QTY": "4",
                "Text": "-----------",
                "Date": "2021-12-12",
                "Time": "12:12:12"
            }]
        },{
            "ID": "xxxxxxxx3",
            "Return": [{
                "QTY": "4",
                "Text": "-----------",
                "Date": "2021-12-12",
                "Time": "12:12:12"
            }, {
                "QTY": "5",
                "Text": "-----------",
                "Date": "2021-12-12",
                "Time": "12:12:12"
            }, {
                "QTY": "4",
                "Text": "-----------",
                "Date": "2021-12-12",
                "Time": "12:12:12"
            }]
        }
    ]

}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)