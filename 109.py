
single_shot_scores = [25, 50]
doubles = [50]
for i in range(1, 21):
    single_shot_scores.extend([i, 2*i, 3*i])
    doubles.append(2*i)

single_shot_scores.sort()
single_shot_scores_len = len(single_shot_scores)
doubles.sort()

max_score = 180
ways = [[[0 for shots_count in range(5)] for total_score in range(max_score)] for single_shot_score in range(single_shot_scores_len+1)]
ways[0][0][0] = 1
for i in range(1, single_shot_scores_len+1):
    ways[i][0][0] = 1

for i in range(1, single_shot_scores_len+1):
    for j in range(1, max_score):
        for shots in range(1, 4):
            ways[i][j][shots] = ways[i-1][j][shots]
            if j >= single_shot_scores[i-1]:
                ways[i][j][shots] += ways[i][j-single_shot_scores[i-1]][shots-1]

answer = 0
for final_score in range(1, 100):     # If you put in range as (1, 171), you will get 42336 i.e. all possible checkouts. For (6, 7), you will get 11
    for final_shot in doubles:
        for shots in range(0, 3):
            answer += ways[single_shot_scores_len][final_score - final_shot][shots]

print(answer)
