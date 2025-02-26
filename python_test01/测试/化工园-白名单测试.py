import json
import requests
import ujson
from python_test01.utils import hutool_encrypt, hutool_decrypt

seed = '087841ec80ec3fd7029fdcaa7f565eed'
url_white_operation = 'http://localhost:9230/huagongyuan/api/visitor/white/vehicleOperation'
url_white_query = 'http://localhost:9230/huagongyuan/api/visitor/white/query'
def add_white():
    white_data = {"business_type":"white","company":"xinao","operation":"add","pass_type":"temp","plate_color":3,"plate_no":"苏L29993","time_end":"2025-03-05 00:00:00","time_start":"2025-02-26 00:00:00","vehicle_id":"苏L29993-3-xinao","vehicle_type":"2"}
    encrypt_content = hutool_encrypt(ujson.dumps(white_data,ensure_ascii=False), seed)
    param = {
        "param": encrypt_content
    }
    resp = requests.post(url=url_white_operation, json=param)
    print(f"Response Status Code: {resp.status_code}")
    print(f"Response Text: {resp.text}")
    if resp.status_code == 200:
        # try:
        #     response_json = resp.json()
        #     print("Response JSON:", response_json)
        # except json.JSONDecodeError as e:
        #     print(f"Error decoding JSON: {e}")
        encrypted_response = resp.text
        decrypted_response = hutool_decrypt(encrypted_response, seed)
        print("Decrypted Response:", decrypted_response)
        try:
            response_json = json.loads(decrypted_response)
            print("Response JSON:", response_json)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print("Failed to get a successful response")

def delete_white():
    white_data = {
        "vehicle_id": "苏A29873-1-qingtian",
        "operation": "delete",
        "business_type": "white"
    }
    encrypt_content = hutool_encrypt(ujson.dumps(white_data, ensure_ascii=False), seed)
    param = {
        "param": encrypt_content
    }
    resp = requests.post(url=url_white_operation, json=param)
    print(f"Response Status Code: {resp.status_code}")
    print(f"Response Text: {resp.text}")
    if resp.status_code == 200:
        # try:
        #     response_json = resp.json()
        #     print("Response JSON:", response_json)
        # except json.JSONDecodeError as e:
        #     print(f"Error decoding JSON: {e}")
        encrypted_response = resp.text
        decrypted_response = hutool_decrypt(encrypted_response, seed)
        print("Decrypted Response:", decrypted_response)
        try:
            response_json = json.loads(decrypted_response)
            print("Response JSON:", response_json)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print("Failed to get a successful response")

def query_white():
    query_data = {
        "plate_no": "苏A298743",
        "plate_color": "",
        "company": ""
    }
    encrypt_content = hutool_encrypt(ujson.dumps(query_data, ensure_ascii=False), seed)
    param = {
        "param": encrypt_content
    }
    resp = requests.post(url=url_white_query, json=param)
    print(f"Response Status Code: {resp.status_code}")
    print(f"Response Text: {resp.text}")
    if resp.status_code == 200:
        # try:
        #     response_json = resp.json()
        #     print("Response JSON:", response_json)
        # except json.JSONDecodeError as e:
        #     print(f"Error decoding JSON: {e}")
        encrypted_response = resp.text
        decrypted_response = hutool_decrypt(encrypted_response, seed)
        print("Decrypted Response:", decrypted_response)
        try:
            response_json = json.loads(decrypted_response)
            print("Response JSON:", response_json)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print("Failed to get a successful response")

if __name__ == '__main__':
    # query_white()
    add_white()
    # delete_white()
