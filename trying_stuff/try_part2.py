
import numpy  as np
from collections import Counter
import pandas as pd
import random

Level_n = 0

# edulidean_dis = sqrt((feature[i] - predict[i])**2 for i in range(4)) .... FORMULA
# edulidean_dis = np.sqrt(np.sum((np.array(feature)-np.array(predict))**2)) ... simplified
# edulidean_dis = np.linalg.norm(np.array(feature)-np.array(predict)) ... fastest

def k_nearby(data, predict, k=4):
    distances = []
    for team in data:
        for items in data[team]:
            edulidean_dis = np.linalg.norm(np.array(items)-np.array(predict))
            distances.append([edulidean_dis, team])
            
    #distances.sort(reverse=False)
    #print(distances[:k])
    votes = [i[1] for i in sorted(distances)[:k]]
    print(votes)
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result

if Level_n == 10:
    print()
    dataset = {"team_bob":[[1,2], [2, 3], [1, 3], [3, 2]], "team_pil":[[9, 9], [8, 9], [7, 9], [9, 7]]}
    wanna_know = [6, 4]

    knear = k_nearby(dataset, wanna_know, k=4)
    print(knear)
    print()

def kn_base(df):

    test_size = 0.2 # 20%
    train_set, test_set = {0:[], 1:[]}, {0:[], 1:[]}
    train_data = df[:-int(test_size*len(df))]
    test_data = df[-int(test_size*len(df)):]

    #[train_set[i[-1]].append(i[:-1]) for i in train_data]
    for i in train_data:
        train_set[i[1]].append(i[1])
                                                                         
    for i in test_data:
        test_set[i[-1]].append(i[:-1])

    correct, total = 0, 0
    for group in test_set:
        for data in test_set[group]:
            vote = k_nearby(train_set, data, k=5)
            if group == vote:
                correct += 1
            total += 1          
    return "accuracy :", (correct/total)*100

if Level_n == 20:
    data_frame = pd.read_csv("/home/groot/.pylint.d/pokemon_data.csv") 
    data_frame = data_frame.drop(['#', 'Name', "Type 1", "Type 2", 'Generation', 'HP'], axis=1)

    print(data_frame[:5])
    
    full_data = data_frame.astype(float).values.tolist()
    #print(full_data[:5])
    random.shuffle(full_data)
    print(full_data[:5])

    #print(kn_base(data_frame))
    print(kn_base(full_data))
 

l = {3:[4, 5], 6:[5, 6]}
print(l)

recursion_partice = 10

if recursion_partice == 10:
    r, c = 12, 12
    def cum(r, c):
        if r == 1 or c == 1:
            return 1
        else:
            return cum(r-1, c) + cum(r, c-1)
    print(cum(r, c))

if recursion_partice == 20:
    n = 5
    def roll(n):
        if n ==  1:
            return 1
        else:
            return n + roll(n-1)

    print(roll(n))

