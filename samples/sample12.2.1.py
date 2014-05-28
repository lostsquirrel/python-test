# -*- coding: utf-8 -*-
#随机数
import random

def flip(numberFlip):
	head = 0.0
	for x in xrange(numberFlip):
		if random.random() < 0.5:
			head += 1

	# print head
	return head / numberFlip

def flipSim(numberFlipPerTrail, numberTrails):
	faceHeads = []
	for x in xrange(numberTrails):
		faceHeads.append(flip(numberFlipPerTrail))
	mean = sum(faceHeads) / len(faceHeads)
	return mean

print flipSim(100,1)
print flipSim(100,10)