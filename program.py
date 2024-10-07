

def duck_sort(n):

    def minimum(n):
        minnimum_number = n[0]
        for i in n:
            if i > minnimum_number:
                minnimum_number = i
        return minnimum_number
    sorted_list = []
    for i in range(len(n)):
        a = minimum(n)
        sorted_list.append(a)
        n.remove(a)
    return sorted_list



