import requests

BASE_URL = "http://127.0.0.1:5000/tables"

response = requests.get(BASE_URL)

if response.status_code == 200:
    tables = response.json().get("tables", [])

    if not tables:
        print("Error: There are no tables in the database.")
    else:
        print(f"Found {len(tables)} tables.")

        for table in tables:
            delete_response = requests.delete(f"{BASE_URL}/{table}")
            if delete_response.status_code == 200:
                print(f"Table '{table}' has been deleted successfully.")
            else:
                print(f"Error deleting table '{table}': {delete_response.json()}")
else:
    print("Read Tables error : ", response.json())
