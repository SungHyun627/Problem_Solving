from itertools import product

def solution(user_id, banned_id):
    except_id_set = set()
    except_id_each_ban_id = []
    answer = 0
    
    for b_id in banned_id:
        temp = []
        for u_id in user_id:
            is_terminated = False
            if len(u_id) != len(b_id):
                continue
            for i in range(len(b_id)):
                if not (u_id[i] == b_id[i] or b_id[i] == '*'):
                    is_terminated = True
                    break
            if not is_terminated:
                temp.append(u_id)
        except_id_each_ban_id.append(temp)
    #print(*except_id_each_ban_id)
    for i in product(*except_id_each_ban_id):
        i = list(set(i))
        if len(i) == len(banned_id):
            i.sort()
            except_id_set.add(tuple(i))
    
    answer = len(except_id_set)        
    return answer