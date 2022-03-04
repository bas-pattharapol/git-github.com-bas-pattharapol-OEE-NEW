import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.30.1.2:5001/API_INF_OEE01"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
#ok
data = """
{
  "Result":  [
        {
            "Plant": "TLT",
            "PDOrder": "90066773",
            "MachineID": "xxxxxxxx",
            "Material": "031-1111",
            "Description": "BES-........",
            "PlanQuantity": "4000",
            "Bacth": "xxxxx",
            "Code": "4",
            "PD_order1": "800000000",
            "PD_order2": "800000000",
            "PD_order3": "800000000",
            "PD_order4": "800000000",
            "PD_order5": "800000000",
            "PD_order6": "800000000",
            "PD_order7": "800000000",
            "PD_order8": "800000000",
            "PD_order9": "800000000",
            "PD_order10": "800000000"
        },
        {
            "Plant": "TLT",
            "PDOrder": "90066772",
            "MachineID": "xxxxxxxx",
            "Material": "031-1111",
            "Description": "BES-........",
            "PlanQuantity": "4000",
            "Bacth": "xxxxx",
            "Code": "4",
            "PD_order1": "800000000",
            "PD_order2": "800000000",
            "PD_order3": "800000000",
            "PD_order4": "800000000",
            "PD_order5": "800000000",
            "PD_order6": "800000000",
            "PD_order7": "800000000",
            "PD_order8": "800000000",
            "PD_order9": "800000000",
            "PD_order10": "800000000"
        }
    ]
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)