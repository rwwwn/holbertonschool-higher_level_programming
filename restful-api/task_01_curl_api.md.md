# 🛠️ RESTful API - Task 1: Use `curl` to Consume Data

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

