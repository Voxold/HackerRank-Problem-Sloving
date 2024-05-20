if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique = list(set(arr))
    unique.sort(reverse=True)
    runner_up = unique[1]
    print(runner_up)