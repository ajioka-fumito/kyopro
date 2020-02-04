def main():
	H = int(input())
	cnt = 0
	if H==1:
		print(1)
		exit()
	while 1:
		if H==1:
			break
		else:
			H = H//2
			cnt += 1
	ans = 0
	for i in range(cnt):
		ans += 2**i
	ans += 2**(i+1)
	print(ans)

if __name__ == '__main__':
	main()