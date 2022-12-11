import heapq
import sys
 
 
def main():
	N = 30000
	T = 10 * 60
 
	expired_time = [0] * N
	free_blocks = list(range(N))
	consumed_blocks = []
 
	anses = []
 
	for line in sys.stdin:
		splitted = line.split()
		if len(splitted) == 2:
			time = int(splitted[0])
 
			while consumed_blocks and time >= consumed_blocks[0][0]:
				freed_block = heapq.heappop(consumed_blocks)
				if freed_block[0] == expired_time[freed_block[1]]:
					expired_time[freed_block[1]] = 0
					heapq.heappush(free_blocks, freed_block[1])
 
			new_block = heapq.heappop(free_blocks)
 
			heapq.heappush(consumed_blocks, (time + T, new_block))
			expired_time[new_block] = time + T
 
			anses.append(new_block + 1)
		else:
			time, block_num = int(splitted[0]), int(splitted[2])
			block_num -= 1
 
			if expired_time[block_num] > time:
				anses.append("+")
				expired_time[block_num] = time + T
				heapq.heappush(consumed_blocks, (time + T, block_num))
			else:
				anses.append("-")
 
	sys.stdout.write("\n".join(map(str, anses)))
 
 
if __name__ == '__main__':
	main()
