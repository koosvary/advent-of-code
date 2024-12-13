col_one = [];
col_two = [];

with open('2024/01/input.txt') as f:
    for line in f:
        row = line.split();
        col_one.append(int(row[0]));
        col_two.append(int(row[1]));

col_one.sort();
col_two.sort();

sum = 0

for i, value in enumerate(col_one):
    sum += abs(value - col_two[i]);

print(sum);
       