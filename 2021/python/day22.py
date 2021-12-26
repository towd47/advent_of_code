import time
import sys
from dataclasses import dataclass, field

@dataclass
class Area:
	command: str
	x: range
	y: range
	z: range

	def volume(self):
		# print(self.x)
		# print(self.x[-1], self.x[0])
		return (self.x[-1] - self.x[0]) * (self.y[-1] - self.y[0]) * (self.z[-1] - self.z[0])

	def on_lights(self):
		# print(self)
		on_lights = self.volume()
		off_lights = 0
		for i in range(len(self.off)):
			off_lights += self.off[i].volume()
			for j in range(i + 1, len(self.off)):
				ol = overlap(self.off[i], self.off[j])
				if ol:
					off_lights -= ol.volume()
		return on_lights

	def subtract(self, a_overlap):
		areas = []
		# sx:ax axend:sxend - sy sz
		# sy:ay ayend:syend - ax:axend sz
		# sz:az azend:szend - ax:axend ay:ayend
		
		x1 = range(self.x[0], a_overlap.x[0])
		x2 = range(a_overlap.x[-1], self.x[-1])
		y1 = range(self.y[0], a_overlap.y[0])
		y2 = range(a_overlap.y[-1], self.y[-1])
		z1 = range(self.z[0], a_overlap.z[0])
		z2 = range(a_overlap.z[-1], self.z[-1])

		if x1:
			a = Area(self.command, x1, self.y, self.z)
			areas.append(a)
		if x2:
			a = Area(self.command, x2, self.y, self.z)
			areas.append(a)
		if y1:
			a = Area(self.command, a_overlap.x, y1, self.z)
			areas.append(a)
		if y2:
			a = Area(self.command, a_overlap.x, y2, self.z)
			areas.append(a)
		if z1:
			a = Area(self.command, a_overlap.x, a_overlap.y, z1)
			areas.append(a)
		if z2:
			a = Area(self.command, a_overlap.x, a_overlap.y, z2)
			areas.append(a)

		if not areas:
			areas = [self]
		return areas

def overlap(a1, a2):
	x_overlap, y_overlap, z_overlap, a = None, None, None, None
	if a1.x[0] in a2.x or a1.x[-1] in a2.x:
		x_overlap = range(max(a1.x[0], a2.x[0]), min(a1.x[-1], a2.x[-1])+1)
	if a1.y[0] in a2.y or a1.y[-1] in a2.y:
		y_overlap = range(max(a1.y[0], a2.y[0]), min(a1.y[-1], a2.y[-1])+1)
	if a1.z[0] in a2.z or a1.z[-1] in a2.z:
		z_overlap = range(max(a1.z[0], a2.z[0]), min(a1.z[-1], a2.z[-1])+1)
	
	if x_overlap and y_overlap and z_overlap:
		a = Area(a2.command, x_overlap, y_overlap, z_overlap)
	return a

def equals(self, a):
	return self.x == a.x and self.y == a.y and self.z == a.z

lines = sys.stdin.readlines()

areas = []
for line in lines:
	line = line.strip()
	command, area = line.split()
	x, y, z = area.split(',')
	x1, x2 = x[2:].split('..')
	y1, y2 = y[2:].split('..')
	z1, z2 = z[2:].split('..')
	a = Area(command, range(int(x1), int(x2) + 1), range(int(y1), int(y2) + 1), range(int(z1), int(z2) + 1))
	areas.append(a)

a1 = areas[1]
a2 = areas[2]
ol = overlap(a1, a2)

ars = a1.subtract(ol)
print(a1)
print(a2)
print(ol)
print(ars)
# vs = []
# for ar in ars:
# 	vs.append(ar.volume())


on_areas = []
off_areas = []



while areas:
	print(on_areas)
	time.sleep(1)
	last = areas.pop()
	print()
	if last.command == 'off':
		overlapped = False
		for a in off_areas:
			ol = overlap(last, a)
			print(ol)
			if ol:
				areas.extend(last.subtract(ol))
				overlapped = True
		if not overlapped:
			off_areas.append(last)

	else:
		overlapped = False
		for a in off_areas:
			ol = overlap(last, a)
			print(ol)
			if ol:
				ars = last.subtract(ol)
				areas.extend(ars)
				overlapped = True

		if not overlapped:
			for a in on_areas:
				ol = overlap(last, a)
				print("ON OL")
				print(last)
				print(a)
				print(ol)
				if ol:
					ars = last.subtract(ol)
					areas.extend(ars)
					overlapped = True

		print("TEST", overlapped)
		if not overlapped:
			on_areas.append(last)
			print("TEST2", on_areas)

total_on = 0

for x in on_areas:
	total_on += x.volume()

print(total_on)
