# Bài 2:
input_str = input("Nhập danh sách các chuỗi cách nhau bởi dấu cách: ")

words = input_str.split()

unique_chars = set()

for word in words:
    for char in word:
        unique_chars.add(char)

result = list(unique_chars)

print(result)

