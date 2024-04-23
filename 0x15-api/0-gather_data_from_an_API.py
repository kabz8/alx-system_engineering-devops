import urllib.request
import json
import sys

def get_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    total_tasks = len(data)
    done_tasks = [task for task in data if task['completed']]
    num_done_tasks = len(done_tasks)
    
    employee_name = data[0]['name']
    
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
