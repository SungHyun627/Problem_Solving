def solution(genres, plays):
    genre_play_dict = {}
    answer = []
    for i in range(len(genres)):
        x = genres[i]
        if x in genre_play_dict:
            genre_play_dict[x].append((plays[i], i))
        else:
            genre_play_dict[x] = [(plays[i], i)]
    temp = list(genre_play_dict.values())
    temp.sort(key = (lambda x: sum(map(lambda y: y[0], x))), reverse = True)
    
    for k in temp:
        k.sort(key = lambda x: (-x[0], x[1]))
        answer.append(k[0][1])
        if len(k) != 1:
            answer.append(k[1][1])
    return answer