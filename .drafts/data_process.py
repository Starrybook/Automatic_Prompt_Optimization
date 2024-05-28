import json
import random
import datetime
import os
from drafts.parse_feedback import *

"""
Shared functions. 
"""
def gen_samples_from_dataset(data_path: str, sample_num: int, keep_orginal_order: bool):
    with open(data_path, 'r') as f:
        data = json.load(f)
    # samples = random.sample(data, sample_num)
    samples = data[:sample_num] if keep_orginal_order else random.sample(data, sample_num)
    return samples

def write_target_model_responses(response_file_dir: str, model_name: str, dataset: str, responses: list):
    if not os.path.exists(response_file_dir):
        os.makedirs(response_file_dir)
    file_name = response_file_dir + f"res_{model_name}_{datetime.datetime.now().strftime('%m%d_%H%M%S')}.json"
    with open(file_name, 'w') as f:
        json.dump(responses, f, indent=4)
    print(f"Responses saved to {file_name}")
    return file_name