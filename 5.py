with open(r'C:\Users\Алема милашка\Documents\ДЗ\data.txt') as file:
 array=[row.strip() for row in file]

result = []
for i in array:
   result.append(int(i))
print(result)


result2 = []
for i in result:
   if i % 2 == 0:
    continue
   result2.append(i)

result2.sort(reverse=True)
print(result2)

# ура













































































































