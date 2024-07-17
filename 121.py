
import math

turns = 15
probability = 0
pr = 0
for i in range((1<<turns)):
    game = ""
    game_p = 1
    blues = 0
    reds = 0    
    for j in range(0, turns):
        if (i & (1 << j)) != 0:
            game += "B"
            blues += 1
            game_p *= 1/(j+2) 
        else:
            game += "R"
            reds += 1
            game_p *= (j+1)/(j+2)
    pr += game_p
    if blues > reds:
        probability += game_p
        
print(probability)
print(pr)
answer = 1 / probability
print("Final answer: ", math.floor(answer))


