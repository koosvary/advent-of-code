left_dict = {};
right_dict = {};

sum = 0;

def getUniqueCountsOfKeys(list, dict):
    for key in list:
        if key in dict.keys():
            dict[key] = dict[key] + 1;
        else:
            dict[key] = 1;

def getSimilarityScores(list):
    for key in list:
        if key in right_dict.keys():
            global sum;
            sum += int(key) * right_dict[key];

col_one = [];
col_two = [];

with open('2024/01/input.txt') as f:
    for line in f:
        row = line.split();
        col_one.append(row[0]);
        col_two.append(row[1]);
        
getUniqueCountsOfKeys(col_one, left_dict);
getUniqueCountsOfKeys(col_two, right_dict);

getSimilarityScores(col_one);

print(sum);