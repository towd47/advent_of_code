from collections import Counter

x_dict = []
y_dict = []

def x_vel_in_range(start_vel, min_val, max_val, max_steps):
	vel = start_vel
	pos = 0
	steps = 0
	working_steps = []
	while pos <= max_val and vel > 0:
		pos = pos + vel
		vel = vel - 1
		steps += 1
		if pos >= min_val and pos <= max_val:
			working_steps.append(steps)
			x_dict.append((start_vel, steps))

	if vel == 0 and pos >= min_val and pos <= max_val:
		steps += 1
		while steps < max_steps:
			working_steps.append(steps)
			x_dict.append((start_vel, steps))
			steps += 1
	return working_steps

def y_vel_in_range(start_vel, min_val, max_val):
	vel = start_vel
	pos = 0
	steps = 0
	working_steps = []
	if vel > 0:
		steps = vel + vel + 1
		vel = (vel * -1) - 1

	while pos > min_val:
		pos = pos + vel
		vel = vel - 1
		steps += 1
		if pos >= min_val and pos <= max_val:
			working_steps.append(steps)
			y_dict.append((start_vel, steps))
	return working_steps

# target area: x=241..275, y=-75..-49
target_x_min = 241
target_x_max = 275
target_y_min = -75
target_y_max = -49

x_steps = []
y_steps = []

max_y_start_velocity = abs(target_y_min) - 1
max_y_pos = int((max_y_start_velocity * (max_y_start_velocity + 1)) / 2)
print(max_y_pos)

for x in range(target_x_max + 1):
	steps = x_vel_in_range(x, target_x_min, target_x_max, abs(target_y_min) * 2 + 2)

for y in range(max_y_start_velocity, target_y_min - 1, -1):
	steps = y_vel_in_range(y, target_y_min, target_y_max)


vels = set()
for x in x_dict:
	for y in y_dict:
		if x[1] == y[1]:
			vels.add((x[0], y[0]))

print(len(vels))
