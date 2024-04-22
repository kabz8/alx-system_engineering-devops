import urllib.request
import json
import csv
import sys

def export_to_csv(employee_id, data):
    employee_name = data[0]['name']
    filename = f"{employee_id}.csv"
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in data:
            completed_status = "True" if task['completed'] else "False"
            writer.writerow([employee_id, employee_name, completed_status, task['title']])

def get_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    export_to_csv(employee_id, data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
