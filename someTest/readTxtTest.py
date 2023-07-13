import numpy as np

w_list = []
h_list = []
a_list = []

with open('result01.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(': ')
            values = parts[1].split(',')
            w = float(values[0].split('W:')[1].strip())
            h = float(values[1].split('H:')[1].strip())
            a = float(values[2].split('A:')[1].strip())
            w_list.append(w)
            h_list.append(h)
            a_list.append(a)

w_np=np.array(w_list)
print(f"W_MEAN:{w_np.mean():.2f}, W_STD:{w_np.std():.2f}, W_MAX:{w_np.max()}, W_MIN:{w_np.min()}")
h_np=np.array(h_list)
print(f"H_MEAN:{h_np.mean():.2f}, H_STD:{h_np.std():.2f}, H_MAX:{h_np.max()}, H_MIN:{h_np.min()}")
a_np=np.array(a_list)
print(f"A_MEAN:{a_np.mean():.2f}, A_STD:{a_np.std():.2f}, A_MAX:{a_np.max()}, A_MIN:{a_np.min()}")
