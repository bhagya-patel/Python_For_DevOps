import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

print(response)
print("Status Code:", response.status_code)
print("Response Body:", response.json())

for key,value in response.json().items():
    if key == "completed":
        if value == False:
            print("Task is Not Completed")
        else:
            print("Task is Completed")