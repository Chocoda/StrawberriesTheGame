Ala = open('source_file.txt', 'r')
lines = Ala.readlines()

print(int(lines[0]) ** 2)

for line in lines[1:]:
    print(f"* {line}",end="")

    