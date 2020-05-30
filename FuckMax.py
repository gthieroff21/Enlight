import numpy as np

x_values = np.array([1,2,3,4,5,6,7,8,9,10])
y_values = np.array([1,4,11,14,21,24,31,34,41,44])

def best_fit_line(x_values,y_values):
	m = (((x_values.mean() * y_values.mean()) - (x_values * y_values).mean()) / ((x_values.mean()) ** 2 - (x_values ** 2).mean()))
	b = y_values.mean() - m * x_values.mean()
	return m, b
m,b = best_fit_line(x_values,y_values)

print(f"regression line: y = {round(m,2)}x + {round(b,2)}")

x_prediction = input(" ")