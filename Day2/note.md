# 🐍 Python Virtual Environment Guide (Day 2 - DevOps Learning)

## 📌 Why Do We Need a Virtual Environment?

When you install a library using:

pip install library_name

It installs the library globally on your system.

However, in real-world development, different projects may require different libraries or different versions of the same library.

### Example

- You need `psutil` in Day1  
- But you don’t need `psutil` in Day2  

If installed globally, both projects share the same environment, which can cause:

- Version conflicts  
- Dependency issues  
- Unnecessary installations  
- Messy development setup  

To solve this problem, we use a **Virtual Environment**.

---

## 🔹 What is a Virtual Environment?

A Virtual Environment is an isolated Python environment created specifically for a project.

It allows you to:

- Install project-specific libraries  
- Avoid version conflicts  
- Keep projects isolated  
- Maintain clean dependencies  

Each project can have its own independent environment.

---

## ⚙️ How to Create and Use a Virtual Environment

### 1️⃣ Create Virtual Environment

python -m venv venv

This creates a folder named `venv` containing a separate Python environment.

---

### 2️⃣ Activate Virtual Environment

On Windows:

venv\Scripts\activate

On Mac/Linux:

source venv/bin/activate

After activation, your terminal will show:

(venv)

This means your virtual environment is active.

---

### 3️⃣ Install Required Library

pip install psutil

Now, `psutil` is installed only inside this project.

It will NOT affect other projects.

---

### 4️⃣ Deactivate Virtual Environment

deactivate

This returns you to the global Python environment.

---

## 📦 Generate requirements.txt (Best Practice)

After installing libraries, generate a dependency file:

pip freeze > requirements.txt

Another developer can install the same dependencies using:

pip install -r requirements.txt

---

## 🚀 Why This is Important in DevOps

In DevOps and production environments:

- Clean dependency management is critical  
- Projects must be reproducible  
- Version conflicts must be avoided  
- CI/CD pipelines require consistent environments  

Virtual environments help maintain stability, reliability, and scalability.

---

✅ Best Practice: Always create a Virtual Environment for every Python project.