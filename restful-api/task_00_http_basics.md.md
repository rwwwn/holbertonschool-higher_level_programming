# 📁 RESTful API - Task 0: Basics of HTTP/HTTPS

## 🔍 HTTP vs HTTPS

| Feature     | HTTP                     | HTTPS                            |
| ----------- | ------------------------ | -------------------------------- |
| Security    | ❌ Not secure             | ✅ Secure via SSL/TLS encryption  |
| Port        | 80                       | 443                              |
| Certificate | Not required             | Requires SSL certificate         |
| Data Safety | Data sent in plain text  | Data is encrypted (confidential) |
| Use Case    | Public blogs, test sites | Banking, login, e-commerce       |

> ✅ **HTTPS** is preferred for any application where data privacy or user authentication is required.

---

## 🔢 HTTP Request and Response Structure

### 📤 HTTP Request Example

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

### 📥 HTTP Response Example

```
HTTP/1.1 200 OK
Date: Sat, 01 Jun 2025 12:00:00 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 305

<html>...</html>
```

Use browser dev tools → Network tab → Reload → Click a request → see request/response headers.

---

## 🔧 Common HTTP Methods

| Method     | Description                | Use Case                      |
| ---------- | -------------------------- | ----------------------------- |
| **GET**    | Retrieves data from server | View a web page or fetch data |
| **POST**   | Sends data to server       | Submit form / create resource |
| **PUT**    | Updates existing resource  | Update profile info           |
| **DELETE** | Removes resource           | Delete a post or item         |

---

## 📊 Common HTTP Status Codes

| Code | Name                  | Description                   | Example Use Case         |
| ---- | --------------------- | ----------------------------- | ------------------------ |
| 200  | OK                    | Request succeeded             | Page loaded correctly    |
| 201  | Created               | Resource successfully created | New user registered      |
| 301  | Moved Permanently     | Resource moved to new URL     | Redirect to updated site |
| 404  | Not Found             | Resource doesn’t exist        | Typo in URL              |
| 500  | Internal Server Error | Server encountered an error   | Code crash on server     |

---

# 🧰 RESTful API - Task 1: Use `curl` to Consume Data

## 🌟 Objective

- Use curl to GET/POST from/to APIs.
- Understand headers and methods.
- Analyze responses.

---

## ✅ Step-by-Step Guide

### 1. Check `curl` installation

```bash
curl --version
```

---

### 2. Fetch HTML content from a webpage

```bash
curl http://example.com
```

---

### 3. Fetch posts from JSONPlaceholder (GET)

```bash
curl https://jsonplaceholder.typicode.com/posts
```

Sample Output:

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere...",
    "body": "quia et suscipit..."
  }
]
```

---

### 4. Fetch only response headers

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

Sample Output:

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Cache-Control: max-age=43200
```

---

### 5. Make a POST request

```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

Simulated Response:

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

---

## 📝 Quick Reference Table

| Action        | Command                                                            |
| ------------- | ------------------------------------------------------------------ |
| Check curl    | `curl --version`                                                   |
| Fetch webpage | `curl http://example.com`                                          |
| GET API data  | `curl https://jsonplaceholder.typicode.com/posts`                  |
| Headers only  | `curl -I https://jsonplaceholder.typicode.com/posts`               |
| POST to API   | `curl -X POST -d "..." https://jsonplaceholder.typicode.com/posts` |

---

📁 *This file is part of the Holberton RESTful API curriculum - June 2025.*

