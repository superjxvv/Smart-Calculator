def end_with_s(word):
    if word[len(word) - 1] == "s":
        return word
    return None


print("_".join(filter(end_with_s, input().split())))
