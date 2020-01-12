import itertools
# 順列生成
def permutation(list_):
    return list(itertools.permutations(list_))

# 順列カウント


if __name__ == "__main__":
    a = permutation([str(i) for i in range(4)])
    for i in a:
        print(list(i))
        print("".join(i))