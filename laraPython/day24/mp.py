import time
from multiprocessing import Pool


def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s


def sum_square_with_mp(numbers):

	start_time = time.time()
	p = Pool()
	result = p.map(sum_square, numbers)
	print("mp:", result);
	p.close()
	p.join()
	end_time = time.time() - start_time
	print("time with multiprocessing.", end_time)


def sum_square_no_mp(numbers):
	start_time = time.time()
	result = []
	for i in numbers:
		result.append(sum_square(i))
	print("wmp:", result);
	end_time = time.time() - start_time
	print("time without multiprocessing.", end_time)


if __name__ == '__main__':
    numbers = range(10)
    sum_square_with_mp(numbers)
    sum_square_no_mp(numbers)