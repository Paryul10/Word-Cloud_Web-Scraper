f = open("namo.txt", "r")
content = f.read()
f.close()
content = content.replace('.', ' ').replace(',', ' ').replace('(', ' ').replace(')', ' ').replace('।', ' ')
words = content.split()
final_content = []

for word in words:
    if len(word) > 3:
        final_content.append(word)

g = open("final_content.txt", "w")
for word in final_content:
    g.write("%s " % word)

g.close()