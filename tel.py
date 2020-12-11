nickname = 'pidor'
if len(nickname)<100:
    list2 = []
    for alpha in nickname:
        if alpha not in list2:
            list2.append(alpha)
    if len(list2) % 2 == 0:
        print("chat with here")
    else:
        print('ignore him !')
            