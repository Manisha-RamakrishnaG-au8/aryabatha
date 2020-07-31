import sort
function highFive(items [][]int) [][]int {
    dict := map[int][]int{}
    for _, item := range items {
        sid, score := item[0], item[1]
        scores, ok := dict[sid]
        if !ok {
            scores = make([]int, 5)
            dict[sid] = scores
        }
        // find the min, then decide whether to replace
        k := 0
        for i:=1; i<5; i++ {
            if scores[i] < scores[k] {
                k = i
            }
        }
        if score > scores[k] {
            scores[k] = score
        }
    }

    res := [][]int{}
    keys := []int{}
    for sid, _ := range dict {
        keys = append(keys, sid)  
    }
    sort.Ints(keys)
    for _, sid := range keys {
        sum := 0
        for _, v := range dict[sid] {
            sum += v
        }
        res = append(res, []int{sid, int(sum/5)})
    }
    return res
}