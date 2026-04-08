def solution(citations):
    citations.sort(reverse=True)

    for i, x in enumerate(citations):
        if x < i + 1:
            return i
        
    return len(citations)