import os, clipboard
script_dir = os.path.dirname(__file__)
rel_path = "quotes.txt"
abs_file_path = str(os.path.join(script_dir, rel_path))
with open(abs_file_path, "r", encoding='utf-8') as f:
    text = f.read().split("\n")
    print(str(text))
    clipboard.copy(str(text))
    os.system("CLS")
with open("quoteslist.txt", "w") as file:
    file.write(text)