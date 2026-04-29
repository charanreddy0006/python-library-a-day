# Day 09 - Regular Expressions (re Module)

## 📌 Overview

On Day 09, I explored Python’s **re module**, which is used for pattern matching in strings.

Regular expressions help in searching, validating, and modifying text efficiently.

---

## 🧠 Topics Covered

* findall() → find all matches
* search() → find first match
* match() → check beginning
* sub() → replace text
* split() → split text
* fullmatch() → validation

---

## 💻 Code Explanation

### 1. Find Numbers

```python
re.findall(r'\d+', text)
```

### 2. Find Email

```python
re.search(r'\S+@\S+', text)
```

### 3. Replace Text

```python
re.sub(pattern, replacement, text)
```

---

## 🔐 Mini Example

Phone number validation using:

```python
re.fullmatch(r'\d{10}', phone)
```

---

## 🎯 Learning Outcome

* Learned pattern matching
* Understood text validation
* Applied regex in real examples

---

## 🚀 Next Plan

Continue learning simple and powerful Python modules daily.
