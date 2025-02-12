p_values = [0, 0, 1, 1]
q_values = [0, 1, 0, 1]

# (p or not p) and q
for i in range(len(p_values)):
    p = p_values[i]
    q = q_values[i]
    respuesta = p and not q
    print(p, q, respuesta)
