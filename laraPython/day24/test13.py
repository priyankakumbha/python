import time
from multiprocessing import Pool

def sum_square(number):
    sum = 0
    for i in range(number):
        sum += i * i
    return sum
'''
1 => 0
2 = > 1
3 = > 5
4 = > 14
5 = > 30
6 = > 55
'''
def sum_square_with_mp(numbers):
	start_time = time.time()
	p = Pool(2)
	result = p.map(sum_square, numbers)  #  [7, 5, 25, 100, 45, 444, 222, 5666];
	#print("mp:", result);
	p.close()
	p.join()
	end_time = time.time();
	total_time_taken = end_time - start_time;
	print("time with multiprocessing.", total_time_taken)
def sum_square_no_mp(numbers):
	start_time = time.time()
	result = []
	for i in numbers:
		result.append(sum_square(i))
	#print("wmp:", result);
	end_time = time.time();
	total_time_taken = end_time - start_time;
	print("time without multiprocessing.", total_time_taken)

if __name__ == '__main__':
	numbers = range(30000);
	print(numbers)
	sum_square_with_mp(numbers)
	sum_square_no_mp(numbers)