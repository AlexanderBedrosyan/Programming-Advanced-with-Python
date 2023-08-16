text = [ch for ch in input()]
new_text = ""

while len(text) > 0:
    ch = text.pop()
    new_text += ch

print(new_text)
