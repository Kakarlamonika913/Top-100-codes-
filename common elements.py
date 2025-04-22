def common_element(self,v1,v2):
        d= {}
        n = []
        for i in v1:
            if i in d:
                d[i]+= 1
            else:
                d[i] = 1
        for j in v2:
            if j in d and d[j] > 0:
                n.append(j)
                d[j] -= 1
        return sorted(n)
