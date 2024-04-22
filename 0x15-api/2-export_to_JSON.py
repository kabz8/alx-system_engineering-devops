import urllib.request
import json
import sys

def export_to_json(employee_id, data):
    employee_name = data[0]['name']
    tasks = [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in data]
    json_data = {str(employee_id): tasks}
    filename = f"{employee_id}.json"
    
    with open(filename, 'w') as file:
        json.dump(json_data, file)

def get_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    export_to_json(employee_id, data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
