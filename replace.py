import os
script_dir = os.path.dirname(__file__)
rel_path = "quotes.txt"
abs_file_path = str(os.path.join(script_dir, rel_path))
with open(abs_file_path, "r", encoding='utf-8') as f:
    text = f.read().replace("&quot;", '"')
with open("quotes.txt", "w") as file:
    file.write(text)