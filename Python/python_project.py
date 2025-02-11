1️. Password Generator 
CODE:

import random
import string
def generate_password(length=12):
 characters = string.ascii_letters + string.digits + 
string.punctuation
 password = ''.join(random.choice(characters) for _ in 
range(length))
 return password
print("Generated Password:", generate_password(12))


2. To-Do List
CODE:

tasks = []
while True:
 print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
 choice = input("Enter choice: ")
 if choice == "1":
 task = input("Enter task: ")
 tasks.append(task)
 print("Task added!")
 elif choice == "2":
 print("\nTo-Do List:")
 for idx, task in enumerate(tasks, 1):
 print(f"{idx}. {task}")
 elif choice == "3":
 task_num = int(input("Enter task number to remove: "))
 if 0 < task_num <= len(tasks):
 tasks.pop(task_num - 1)
 print("Task removed!")
 elif choice == "4":
 break
 else:
 print("Invalid choice. Try again.")


3. Weather App (API-based)
CODE:

import requests
API_KEY = "8f2d6822fb2e4524adf20f8132e6f463"
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url).json()
if response["cod"] == 200:
    print(f"\nCity: {response['name']}")
    print(f"Temperature: {response['main']['temp']}°C")
    print(f"Weather: {response['weather'][0]['description']}")
else:
    print("\nCity not found!")


4️. Number Guessing Game
CODE:

import random
number = random.randint(1, 100)
while True:
    guess = int(input("Guess the number (1-100): "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        break


5️. QR Code Generator
CODE:

import qrcode
data = input("Enter text or URL: ")
qr = qrcode.make(data)
qr.save("qrcode.png")
print("QR Code generated and saved as 'qrcode.png'!")


















