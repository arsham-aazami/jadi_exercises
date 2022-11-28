def oldest_candidate(candidates_ages):
    first_age = candidates_ages[0]
    for age in candidates_ages:
        if age > first_age:
            first_age = age
    #first age is now the maximum age
    print(first_age)


oldest_candidate([17, 15, 39, 51, 14, 32, 28, -1])

# or use the following code:

def oldest_candidate(candidates_ages):
    max_age = max(candidates_ages)
    print(max_age)


oldest_candidate([17, 15, 39, 51, 14, 32, 28, -1])
