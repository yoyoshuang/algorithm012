
count = 0

def findMinStep(start, end, bank):
    if end not in bank:
        return -1



    def distance(s1, s2):
        dis = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dis += 1
        return dis

    def dfs(start, end, bank):
        global count
        if start == end:
            return
        for b in bank:
            dis = distance(b, start)
            if dis==1:
                count += 1
                bank.remove(b)
                dfs(b, end, bank)

    dfs(start, end, bank)

    return count

    

if __name__ == "__main__":
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

    count = findMinStep(start, end, bank)
    print(count)