import json
import time
import math

# create a dict, and then write it
for i in range(5):
    current_dict={}
    current_dict["rule_id"]=i+1
    current_dict["rule_name"]=f"Test Alert {i+1}"
    current_dict["tenant_id"]="fe038303-3c56-4a6a-a251-c26a328d11c6"
    current_dict["conditions"]=[{
            "condition_id": i+1,
            "condition_name": f"condition {i+1}",
            "asset_id": [
                f"PTG_{i+1:03}"
            ],
            "join_condition": "or",
            "parameter": "pressure",
            "operator": ">",
            "class": None,
            "threshold": 2000,
            "duration": 300,
            "rule_run_frequency": 1,
            "risk_registers": [
                ""
            ],
            "sensor_type": "pt_gauge",
            "severity": "medium"
        }]
    current_dict["operation"]="create"
    file_name=math.floor(time.time()) # get the floor value of current epoch time
    # print(file_name)
    time.sleep(1)
    seriaized_json=json.dumps(current_dict,indent=4)
    with open(f"../Alert_Rules/{file_name}_rule.json","w") as output_file:
        output_file.write(seriaized_json)



