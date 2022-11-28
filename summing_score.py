
def summing_scores(scores):
    win_score = 0
    total_score = 0
    for score in scores:
        if score == 3:
            win_score += 1
        total_score += score
        
    print(total_score,  win_score)


summing_scores([3,0, 1, 3, 1, 0, 0 , 1, 3, 3, 1, 1])