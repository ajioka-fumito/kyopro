def main():
	N,K = map(int,input().split())
	H = [int(h) for h in input().split()]
	H = sorted(H,reverse=True)
	for i in range(min(K,N)):
		H[i] = 0
	print(sum(H))
if __name__ == '__main__':
	main()