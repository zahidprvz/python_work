# Day 04: Chapter 5 (Part 1) - If Statements & Conditional Tests

**Date:** July 8, 2025

---

## Chapter 5 (Part 1): If Statements

Today, I delved into the world of **`if` statements**, the cornerstone of decision-making in programming. This chapter is all about writing code that can respond differently based on various conditions. I covered the first half of the chapter.

### Key Learnings:

* **Understanding Conditional Tests:**
    * Conditional tests evaluate to either `True` or `False`.
    * This boolean result dictates whether an `if` block of code is executed.
    * Example of simple equality check:
        ```python
        user = 'zahid'
        print("Is user == 'zahid' ? I predict True")
        print(user == 'zahid') # Output: True

        print("Is user == 'ali' ? I predict False")
        print(user == 'ali')   # Output: False
        ```
* **Equality and Inequality with Strings:**
    * `==` (equality operator): Checks if two values are the same.
    * `!=` (inequality operator): Checks if two values are different.
    * Demonstrated using a `health` variable:
        ```python
        health = 'good'
        if health == 'good':
            print("You are good to go!")
        else:
            print("You have to take care of yourself!")
        # Output: You are good to go!
        ```
* **Ignoring Case When Checking Equality (`.lower()`):**
    * Learned that string comparisons are case-sensitive by default.
    * The `.lower()` method is crucial for case-insensitive comparisons, converting the string to lowercase before comparison.
        ```python
        name = 'Zahid'
        if name.lower() == 'zahid':
            print(f"Hello, {name}")
        else:
            print("I didn't recognized you!")
        # Output: Hello, Zahid
        ```
* **Numerical Tests:**
    * Using equality (`==`), inequality (`!=`), greater than (`>`), less than (`<`), greater than or equal to (`>=`), and less than or equal to (`<=`) for numbers.
    * These operators allow for powerful comparisons based on quantitative values.
* **Combining Conditions (`and` / `or` keywords):**
    * `and`: Both conditions must be `True` for the overall expression to be `True`.
    * `or`: At least one condition must be `True` for the overall expression to be `True`.
    * Example for checking multiple subject pass marks:
        ```python
        english = 98
        maths = 65
        chemistry = 34

        if english >= 50 and maths >= 50 and chemistry >= 50:
            print("You are pass in all subjects")
        else:
            print("You are fail in one or more subjects")
        # Output: You are fail in one or more subjects (because chemistry is < 50)
        ```
* **Checking if an Item is in a List (`in` keyword):**
    * The `in` keyword checks for the presence of a value within a list.
        ```python
        friends = ['zulfiqar', 'umair', 'wahab', 'shazib']
        if 'jahanzaib' in friends:
            print("Jahanzaib is also a friend")
        else:
            print("Jahanzaib is not a friend")
        # Output: Jahanzaib is not a friend
        ```
* **Checking if an Item is Not in a List (`not in` keyword):**
    * The `not in` keyword checks for the absence of a value within a list.
        ```python
        friends = ['zulfiqar', 'umair', 'wahab', 'shazib']
        if 'zulfiqar' not in friends:
            print("Zulfiqar is not my friend")
        else:
            print("Zulfiqar is my friend")
        # Output: Zulfiqar is my friend
        ```

### Challenges & Reflections:

* The logical flow of `if` statements and how they control program execution is clear. The indentation is a constant reminder of Python's structure.
* The `and` and `or` keywords are intuitive but require careful thought when combining multiple conditions to ensure the logic precisely matches the intended outcome. I can see how complex conditions might become tricky to debug if not structured carefully.
* The `in` and `not in` operators are incredibly convenient for list membership tests, much cleaner than looping manually!

---

## Code Examples for Day 04

You can find the Python script files (`.py`) for the exercises and examples from Chapter 5 (Part 1) in the `day_04_code/` directory within this repository.
