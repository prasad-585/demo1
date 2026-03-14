# name = input("Enter something:")
# r =""
# for i in name:
#     if i != "":
#         r=i+r
# print(r)

# largest = 0
# for i in range(3):
#     num = int(input("Enter number : "))

#     if num < 0:
#         print("No less then 0")
#         break
#     else:    
#         if num > largest:
#             largest = num
# print("largest no : ",largest)


# n=int(input())
# for n in range(1,m+1):
#     if n%3==0 and n%5==0:
#         print("fizzbuzz")
#     elif n%3==0 and n%5!=0:
#         print("fizz")
#     elif n%5==0 and n%3!=0:
#         print("buzz")
#     else:
#         print(n)

# a=int(input("enter the number:"))
# print("True" if a==10 else "false")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample dataset
print("my name is siva")
data = {
    'URL_Length': [54, 23, 120, 45, 80, 150, 33, 90],
    'Special_Characters': [2, 0, 10, 1, 6, 15, 0, 7],
    'HTTPS': [1, 1, 0, 1, 0, 0, 1, 0],
    'Label': [0, 0, 1, 0, 1, 1, 0, 1]   # 0 = Safe, 1 = Malicious
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and labels
X = df[['URL_Length', 'Special_Characters', 'HTTPS']]
y = df['Label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Machine Learning Model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, predictions))

# Predict a new website
url_length = int(input("Enter URL length: "))
special_chars = int(input("Enter number of special characters: "))
https = int(input("HTTPS present? (1=yes,0=no): "))

result = model.predict([[url_length, special_chars, https]])

if result[0] == 1:
    print("⚠️ Malicious Website")
else:
    print("✅ Safe Website")
