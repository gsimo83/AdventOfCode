import itertools
import hashlib

salt = 'cxdnnyjw'
ans1, ans2 = [], {}
for n in itertools.count():
    seed = '{}{}'.format(salt, n).encode()
    #print(seed)
    digest = hashlib.md5(seed).hexdigest()
    #print(digest)
    if digest.startswith('00000'):
        x, y = digest[5:7]
        if len(ans1) < 8:
            ans1.append(x)
            # print(seed)
            # print(digest)
            # print(ans1)
        if x in '01234567' and x not in ans2:
            ans2[x] = y
            print(ans2)
        if len(ans1) == 8 and len(ans2) == 8: break

print(''.join(ans1)) #f77a0e6e
print(sorted(ans2.items()))
print(''.join(v for k,v in sorted(ans2.items()))) #999828ec