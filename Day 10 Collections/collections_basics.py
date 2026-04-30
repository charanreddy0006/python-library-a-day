from collections import Counter, defaultdict, namedtuple, deque

# --- Counter (count elements) ---
data = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = Counter(data)
print("Counter:", count)
print("Most common:", count.most_common(1))

# --- defaultdict (auto default values) ---
d = defaultdict(int)
d["a"] += 1
d["b"] += 2
print("\nDefaultDict:", dict(d))

# --- namedtuple (like lightweight class) ---
Student = namedtuple("Student", ["name", "age"])

s1 = Student("Chakri", 21)
print("\nNamedTuple:", s1.name, s1.age)

# --- deque (fast queue/stack) ---
dq = deque([1, 2, 3])

dq.append(4)
dq.appendleft(0)
print("\nDeque after adding:", dq)

dq.pop()
dq.popleft()
print("Deque after removing:", dq)