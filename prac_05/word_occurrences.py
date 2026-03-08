text = input("Enter text: ")
words = text.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

max_length = max(len(word) for word in count)
for word in sorted(count):
    print(f"{word:<{max_length}} : {count[word]}")
