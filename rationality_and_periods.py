def calculate_k_array(P_values, q, p_values):
    k_array = []
    for P, p in zip(P_values, p_values):
        if p % q != 0:  # Check if p is not divisible by q
            k_array.append(P * q // p)  # Integer division
    return k_array

# Example usage:
P_values = [2, 3, 4]
q = 5
p_values = [3, 7, 6]

k_array = calculate_k_array(P_values, q, p_values)
print("k array:", k_array)
