'''
Problem Statement :

Arnab has given me a challenge. I have to calculate the number of numbers which are less than a certain value n, and have exactly k set bits in its binary form. As you are a Prepster like me, help me write a code that will take input for n and k and give the expected output.

Constraints :
1<=n<=10000
1<=k<=10
Input Format :
First line containing n and k space separated
Output Format :
Number of numbers present in a single line

Sample Input:
7 2
Sample Output:
3
Explanation:
11,110,101 -> These three numbers.

ans = 0
n, k = map(int, input().split())
l = len(bin(n)[2:])

def func(i, s, L):
    global ans
    global l

    if L > l:
        return

    if s != "":
        if int(s, 2) >= n:
            return

    if i == 0:
        ans += 1

    func(i-1, s + "1", L + 1)
    func(i, s + "0", L + 1)

    
func(k-1, "1", 1)

print(ans)




'''

'''
What does bin(n) return?

bin(n) converts a number to binary, but with a prefix.

Example:

bin(7)  →  '0b111'
bin(10) →  '0b1010'


👉 Notice the 0b at the beginning

0b just means “this number is in binary”

It is not part of the actual binary digits

Why [2:] is used
bin(n)[2:]


This removes the first two characters ('0b').
'''
'''

                         ("1", i=1)
                          /       \
                         /         \
                 add '1'             add '0'
                       /               \
               ("11", i=0)            ("10", i=1)
                 ✅ ans=1                |
                 /   \                  |
                /     \                 |
        add '1'         add '0'     add '1'
           ❌             ("110",0)     |
       ("111",-1)           ✅ ans=2   |
                              |        |
                              |    ("101",0)
                              |        ✅ ans=3
                              |
                         add '0'
                       ("100",1)
                        ❌ (no space)


'''
'''

Got it 👍
Let’s **only** focus on **how the recursion looks on the CALL STACK**, in the **simplest possible way**.

We’ll again use:

```
n = 7, k = 2
```

Initial call:

```python
func(1, "1", 1)
```

---

## What is the call stack? (1-line)

👉 The call stack is just a **stack of active function calls**.
Every time `func()` calls itself, a **new frame is pushed**.
When a function finishes, its frame is **popped**.

---

## Step-by-step Call Stack Trace

I’ll show:

* **Top of stack at the top**
* What gets **pushed**
* What gets **popped**

---

### 🟢 Step 1: First call

```
STACK
-----
func(1, "1", 1)
```

---

### 🟢 Step 2: Call `func(0, "11", 2)`

(from adding `'1'`)

```
STACK
-----
func(0, "11", 2)
func(1, "1", 1)
```

* `i == 0` → count ✔
* Now it makes further calls

---

### 🟢 Step 3: Call `func(-1, "111", 3)`

```
STACK
-----
func(-1, "111", 3)
func(0, "11", 2)
func(1, "1", 1)
```

* `"111"` → `7 >= 7` ❌
* **Returns immediately**

📤 Pop from stack

```
STACK
-----
func(0, "11", 2)
func(1, "1", 1)
```

---

### 🟢 Step 4: Call `func(0, "110", 3)`

```
STACK
-----
func(0, "110", 3)
func(0, "11", 2)
func(1, "1", 1)
```

* `i == 0` → count ✔
* Tries further calls

---

### 🟢 Step 5: Call `func(-1, "1101", 4)`

```
STACK
-----
func(-1, "1101", 4)
func(0, "110", 3)
func(0, "11", 2)
func(1, "1", 1)
```

* `L > l` ❌
* Return immediately

📤 Pop

---

### 🟢 Step 6: Call `func(0, "1100", 4)`

```
STACK
-----
func(0, "1100", 4)
func(0, "110", 3)
func(0, "11", 2)
func(1, "1", 1)
```

* `L > l` ❌
* Return

📤 Pop → `"110"` done → pop again

---

### 🟢 Step 7: Back to `"1"`, now add `'0'`

Call `func(1, "10", 2)`

```
STACK
-----
func(1, "10", 2)
func(1, "1", 1)
```

---

### 🟢 Step 8: Add `'1'` → `func(0, "101", 3)`

```
STACK
-----
func(0, "101", 3)
func(1, "10", 2)
func(1, "1", 1)
```

* `i == 0` → count ✔
* Further calls exceed limits → return

📤 Pop

---

### 🟢 Step 9: Add `'0'` → `func(1, "100", 3)`

```
STACK
-----
func(1, "100", 3)
func(1, "10", 2)
func(1, "1", 1)
```

* No space left ❌
* Return

📤 Pop all the way back

---

## 🧮 Final Stack State

```
STACK
-----
(empty)
```

All recursive calls are done.

```
ans = 3
```

---

## Mental model to remember 🧠

* Every recursive call → **push**
* Every `return` → **pop**
* Stack grows **downward**
* Only one path runs at a time (DFS)

---

## One-line intuition 💡

> Recursion is just Python stacking function calls on top of each other and removing them when they finish.


'''

ans = 0
n, k = map(int, input().split())
l = len(bin(n)[2:])


def func(i, s, L):
    global l
    global ans
    if L > l:
        return
    
    if s != "":
        if int(s, 2) >= n:       #int(value, base) s is the value 2 is its base so that it is recognized as binary, int() function converts it to decimal
            return
    if i == 0:
        ans += 1
    func(i - 1, s + "1", L + 1)
    func(i, s + "0", L + 1)

func(k - 1, "1", 1)
print(ans)