from typing import List

def split_str(string: str, n : int) -> List:

    """
        splits the "string" in "n" sub-strings
        returns a list with the substrings        
    """

    #If the string length is less than n 
    #returns a list with chars splitted
    if(len(string) < n):
        return list(string)
    chunks = []
    remaining = len(string) % n
    chunk_size = len(string) // n
    
    start = 0
    for i in range(n):
        end = start + chunk_size
        if remaining:
            end = end + 1
            remaining -= 1
        
        chunk = string[start: end]
        chunks.append(chunk)
        start = end

    return chunks