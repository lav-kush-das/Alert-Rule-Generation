import json
import time
import math
import random
import sys
import os

# Get the parent directory of the current file
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("the parent direcory is: ",parent_directory)
# Add the parent directory to the sys.path list if not already there
if(parent_directory not in sys.path):
    sys.path.insert(0,parent_directory)


from Experiment.random_number import threshold_generator,duration_generator

join_condition=["and","or"]
operator=[">","<"]

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
            "join_condition": random.choice(join_condition),
            "parameter": "pressure",
            "operator": random.choice(operator),
            "class": None,
            "threshold": threshold_generator(),
            "duration": duration_generator(),
            "rule_run_frequency": 1,
            "risk_registers": [
                ""
            ],
            "sensor_type": "pt_gauge",
            "severity": "medium"
        }]
    current_dict["operation"]="create"
    file_name=math.floor(time.time()) # get the floor value of current epoch time
    time.sleep(1)
    seriaized_json=json.dumps(current_dict,indent=4)
    with open(f"Alert_Rules/{file_name}_rule.json","w") as output_file:
        output_file.write(seriaized_json)

# print("the paths are: ")
# for paths in sys.path:
#     print(paths)

# print("end of first iteration")
