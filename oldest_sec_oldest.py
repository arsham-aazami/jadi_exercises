def old_sec_old(candidate_age):
    
    max_age = max(candidate_age)
    candidate_age.remove(max_age)
    sec_max_age = max(candidate_age)
    print(max_age, sec_max_age)

    
old_sec_old([23, 12, 43, 54])