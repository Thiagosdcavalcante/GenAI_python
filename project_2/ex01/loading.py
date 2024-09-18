import time

percentTotal = 100;

def	ft_progressionbar(iterator, totalItems, prefix="", suffix="", size=10, fill="="):
	percent = ("{0:.1f}").format(percentTotal * (iterator / float(totalItems)))
	filled_length = int((size * iterator) / totalItems)
	bar = ((fill * filled_length + '>') + ((size - filled_length) * ' '))
	return (f'{prefix}{bar}{suffix}')

def	ft_progress(lst):
	count = 0
	start = time.time()
	etaTime = 0
	for _ in lst:
		progression = ((count + 1) / len(lst)) * percentTotal
		elapsedTime = time.time() - start
		if (count > 0):
			etaTime = ((elapsedTime / count) * (len(lst) - count))
		count += 1
		print(f"\033[36m\rETA:\033[0m \033[32m{etaTime:.2f}\033[0m [\033[31m{progression:.0f}%\033[0m] \033[31m[{ft_progressionbar(count, len(lst))}]\033[0m {count}/{len(lst)} | elapsed time \033[33m{elapsedTime:.2f}s\033[0m", end='')
		time.sleep(0.01)
		yield count

for i in ft_progress(range(1000)):
	pass
