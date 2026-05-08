# Day 18 - Requests Library

# 📌 Overview

On Day 18, I explored Python’s powerful **requests library**, which is used to send HTTP requests and interact with web APIs.

The requests library is one of the most popular Python libraries because it makes working with web data simple and efficient.

It is widely used in:

* web development
* API integration
* automation
* data collection
* machine learning projects

Using requests, Python programs can:

* fetch data from websites
* communicate with APIs
* send and receive JSON data
* download files
* automate web tasks

---

# 🌐 What is an API?

API stands for:

```text id="fw2m7u"
Application Programming Interface
```

An API allows applications to communicate with each other.

Example:

* weather apps get weather data from APIs
* payment apps use banking APIs
* social media apps use APIs

---

# 📦 Installing Requests

Install using pip:

```bash id="87vjlwm"
pip install requests
```

---

# 🧠 Importing the Library

```python id="xvskn4"
import requests
```

---

# ⚡ Sending a GET Request

The GET request is used to retrieve data from a server.

Example:

```python id="vgnvwy"
response = requests.get(url)
```

---

# 🔍 Understanding the Response Object

After sending a request:

```python id="i2f7u2"
response = requests.get(url)
```

Python receives a response object containing:

* status code
* headers
* response data
* cookies

---

# 📊 Status Codes

Status codes indicate request results.

Common codes:

| Status Code | Meaning      |
| ----------- | ------------ |
| 200         | Success      |
| 404         | Not Found    |
| 500         | Server Error |
| 403         | Forbidden    |

Example:

```python id="k24xrn"
print(response.status_code)
```

---

# 🧾 Working with JSON Data

Many APIs return JSON data.

Convert JSON to Python:

```python id="lzvg26"
data = response.json()
```

Now data becomes:

* dictionary
* list
* nested objects

---

# 💻 Example Program

```python id="m0mjlwm"
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data[0]["name"])
print(data[0]["email"])
```

---

# 🧠 Accessing JSON Values

Example:

```python id="jgtp86"
data[0]["name"]
```

Explanation:

* `data[0]` → first user
* `["name"]` → user's name

---

# 📨 Headers

Headers contain metadata about the response.

Example:

```python id="4gwjlwm"
print(response.headers)
```

Headers include:

* content type
* server details
* encoding

---

# 🚀 Real-World Uses of Requests

---

# 1. Weather Applications

```python id="l0pq2d"
requests.get(weather_api)
```

Used to fetch:

* temperature
* humidity
* forecasts

---

# 2. AI Applications

AI apps use APIs to:

* send prompts
* receive AI responses

---

# 3. Web Scraping

Requests helps fetch webpage content.

---

# 4. Authentication Systems

Applications send:

* login requests
* tokens
* user data

---

# 🔥 Why Requests is Popular

Compared to older methods:

* easier syntax
* cleaner code
* powerful features
* faster development

---

# ⚠️ Important Notes

Some APIs require:

* API keys
* authentication
* rate limits

Always read API documentation.

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how APIs work
* how Python communicates with servers
* how to send HTTP requests
* how to work with JSON data
* basics of web communication

---

# 🚀 Conclusion

The requests library is one of the most important Python libraries for modern development.

It helps Python applications:

* communicate with the web
* fetch online data
* work with APIs
* build automation tools

Learning requests is an important step toward:

* web development
* backend development
* machine learning
* AI projects
* automation engineering
