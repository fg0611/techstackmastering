from collections import deque, defaultdict

def find_word(rules):
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    # Build graph and in-degree count
    for rule in rules:
        from_char, to_char = rule.split('>')
        graph[from_char].add(to_char)
        
        if from_char not in in_degree:
            in_degree[from_char] = 0
        if to_char not in in_degree:
            in_degree[to_char] = 0
            
        in_degree[to_char] += 1  # Increase dependency count for `to_char`

    # Find starting points (nodes with in-degree 0)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []

    # Process nodes in topological order
    while queue:
        char = queue.popleft()
        result.append(char)
        
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return "".join(result)

# Test cases
print(find_word(["P>E", "E>R", "R>U"]))  # Output: PERU
print(find_word(["I>N", "A>I", "P>A", "S>P"]))  # Output: SPAIN
print(find_word(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]))  # Output: HUNGARY
print(find_word(["I>F", "W>I", "S>W", "F>T"]))  # Output: SWIFT
print(find_word(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]))  # Output: PORTUGAL
print(find_word(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]))  # Output: SWITZERLAND
