def subsequence(source, target):
    pointer_s, pointer_t = 0, 0
    count = 0
    while pointer_t < len(target):
        pointer_s = 0
        check = pointer_t
        while pointer_s < len(source) and pointer_t < len(target):
            if source[pointer_s] == target[pointer_t]:
                pointer_t += 1
            pointer_s += 1
        if pointer_t == check:
            return -1
        count += 1
    return count


source = "xyz"
target = "xzyxz"

print(subsequence(source, target))
