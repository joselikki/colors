def spl_str(word, n):
    if(len(word) < n):
        return list(word)

    remaining = len(word) % n
    chunk_size = len(word) // n

    chunks = []
    start = 0
    for i in range(n):
        end = start + chunk_size
        if remaining:
            end = end + 1
            remaining -= 1
        
        chunk = word[start: end]
        chunks.append(chunk)
        start = end
    return chunks