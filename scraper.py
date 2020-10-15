import os, re

#rawtext
script_dir = os.path.dirname(__file__)
rel_path = "raw.html"
abs_file_path = str(os.path.join(script_dir, rel_path))
with open(abs_file_path, "r", encoding='utf-8') as f:
    text = f.read()

#alllink
urls = re.findall(r'<a href="http://typeracerdata.com/text?[\'"]?([^\'" >]+)', text)
ids = []
for smol in urls:
    ids.append(smol[4:])

import urllib3
i = 0

allquotes = []
for idd in ids:
    http = str(urllib3.PoolManager().request("get", "http://typeracerdata.com/text?id={}".format(str(idd))).data)
    raw = re.findall(r'<p>(.*?)</p>', http)
    if not "This is a placeholder text. You are seeing it because there are no other texts available for your skill level. Please tell your system administrator to add some texts!" in raw[0]:
        i += 1
        print("\n{0} done. [Out of {1}]\n".format(i, len(ids)))

        quoted = str(raw[0]).strip('\n').strip('\t').replace('\n', '').replace('\t', '').replace('\\', '')[2:]
        print(quoted)
        allquotes.append(quoted)
        

with open("quotes.txt", "w") as file:
    file.write("\n".join(allquotes))
print("Done!")
 # TODO: replace &quot with ""