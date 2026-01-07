# Problem 1: Sum of elements in an array
x = [1, 2, 3, 4]

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(sum_array(x))


# Problem 2: Maximum element in an array
x = [3, 7, 2, 9, 4]

def max_array(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

print(max_array(x))


# Problem 3: Count vowels in a sentence
s = "Hello World"

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in sentence:
        if ch in vowels:
            count += 1
    return count

print(count_vowels(s))


# Problem 4: Greeting message
name = "Pankaj"
occupation = "engineer"

def greet(name, occupation):
    article = "an" if occupation[0].lower() in "aeiou" else "a"
    return f"Hi {name}, you are {article} {occupation}"

print(greet(name, occupation))


# Problem 5: Check if a number is prime
n = 17

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(n))


# Problem 6: Palindrome check
s = "madam"

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome(s))
