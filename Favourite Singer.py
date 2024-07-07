def max_countss(playlist,singers):
    unique_singers=[]
    counts=[]
    for i in singers:
        if i in unique_singers:
            index=unique_singers.index(i)
            counts[index]+=1
        else:
            unique_singers.append(i)
            counts.append(1)
    max_count=max(counts)
    fav_singer=counts.count(max_count)
    return (fav_singer)

playlist = int(input())
singers=list(map(int, input().split()))
out=max_countss(playlist,singers)
print(out)
