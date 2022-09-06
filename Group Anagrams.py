import collections


def GroupAnagram(strs):
    answer=collections.defaultdict(list)
    for word in strs:
        answer[tuple(sorted(word))].append(word)
    return answer.values()

if __name__ in '__main__':
    sequence=["nat","tea","tan","ate","nat","bat"]
    print(GroupAnagram(sequence))