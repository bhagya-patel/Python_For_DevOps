# 🌐 What is an API?  
## API = Application Programming Interface

An **API (Application Programming Interface)** is a set of rules that allows two software systems to communicate with each other.

It defines:
- How requests are sent  
- How responses are received  
- What data format is used (commonly JSON over HTTP)  

👉 **In simple words:**  
An API acts as a **bridge** between two applications.

---

# 🔎 Real-World Example

Imagine:

- You open a food delivery application.  
- You place an order.  
- The application sends your request to the restaurant’s system.  
- The restaurant processes the request and sends back a response.  
- The application displays the confirmation.  

All of this communication happens through an **API**.

---

# 🧠 Technical Explanation

An API defines:

- The **endpoint (URL)** where the request is sent  
- The **HTTP method** used  
- The structure of the request  
- The structure of the response  

Most modern APIs follow the **REST architecture** and exchange data in **JSON format**.

---

# 🔥 Types of APIs

## 1️⃣ Web API
Web APIs are accessed over the internet.

Examples:
- Weather APIs  
- Payment APIs  
- Maps APIs  

---

## 2️⃣ REST API (Most Popular in DevOps & Backend)

REST APIs use standard HTTP methods:

| Method | Purpose |
|--------|----------|
| GET    | Retrieve data |
| POST   | Create data |
| PUT    | Update data |
| DELETE | Remove data |

### Example Request:

```
GET https://api.example.com/users
```

---

# 📦 Example JSON Response

```json
{
  "name": "Bhagya Patel",
  "role": "DevOps Engineer",
  "city": "Ahmedabad"
}
```

---

# 🛠 Python Example – Calling an API

```python
import requests

# Sending a GET request to GitHub API
response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print("Response Data:", response.json())
```

---

# 🚀 Why APIs Are Important (DevOps & Cloud Perspective)

APIs are essential because:

- CI/CD tools communicate through APIs  
- Cloud services (AWS, Azure, GCP) operate using APIs  
- Microservices architecture is API-driven  
- Infrastructure as Code tools (like Terraform) use provider APIs  
- Monitoring and automation systems rely on APIs  

---

# 🔥 Real DevOps Example

When you run:

```
aws ec2 run-instances ...
```

Behind the scenes, AWS CLI makes an API call to AWS services to provision infrastructure.

---

# 🎯 Interview-Ready Definition

> An API is a set of rules that enables communication between two software systems. It defines how requests are made and how responses are structured, typically using JSON over HTTP.

---

# 📌 Conclusion

APIs are the backbone of modern software systems.  
From mobile applications to cloud infrastructure, everything communicates through APIs.

Understanding APIs is fundamental for:

- DevOps Engineers  
- Cloud Engineers  
- Backend Developers  

---

⭐ If you found this useful, consider starring the repository.