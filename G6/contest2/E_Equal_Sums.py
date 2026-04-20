def find_sequences(k, sequences):
    sum_dict = {}  # Dictionary to store sum differences
    
    for idx in range(k):
        sequence = sequences[idx]
        total_sum = sum(sequence)
        
        for element_index, element in enumerate(sequence):
            new_sum = total_sum - element
            
            if new_sum in sum_dict:
                other_sequence_idx, other_element_index = sum_dict[new_sum]
                
                # Ensure different sequences are used
                if other_sequence_idx != idx:
                    print("YES")
                    print(other_sequence_idx + 1, other_element_index + 1)
                    print(idx + 1, element_index + 1)
                    return
                
            # Store the sum and indices
            sum_dict[new_sum] = (idx, element_index)
    
    print("NO")

# Read input
k = int(input())
sequences = []
for _ in range(k):
    length = int(input())
    arr = list(map(int, input().split()))
    sequences.append(arr)

find_sequences(k, sequences)
