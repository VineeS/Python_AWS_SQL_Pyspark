def two_list(user_ids, tips):
    max = 0
    for i in range(0,len(tips)):
        if max <= tips[i]:
            max = tips[i]
            user_id_with_max_tip = user_ids[i]
    return user_id_with_max_tip



user_ids = ["user1", "user2", "user3", "user4"]
tips = [10.5, 20.0, 15.75, 25.3]
print(two_list(user_ids, tips))