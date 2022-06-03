function solution(participant, completion) {
    p_map = new Map();
    c_map = new Map();
    for (let p of participant) {
        if (p_map.has(p)) {
            p_map.set(p, p_map.get(p) + 1)
        }
        else {
            p_map.set(p, 1)
        }
    }
    
    for (let c of completion) {
        if (c_map.has(c)) {
            c_map.set(c, c_map.get(c) + 1)
        }
        else {
            c_map.set(c, 1)
        }
    }
    
    for (let pkey of p_map.keys()) {
        if (!c_map.has(pkey)) return pkey;
        if (c_map.get(pkey) !== p_map.get(pkey)) return pkey;
    }
}