a = int(input())

group_wrod = 0
for i in range(a):
    word = input()
    worng = 0
    for p in range(len(word)-1):
        if word[p] != word[p+1]:
            new = word[p+1:]
            if new.count(word[p]) > 0:
                worng += 1
    if worng ==0:
        group_wrod += 1
print(group_wrod)

