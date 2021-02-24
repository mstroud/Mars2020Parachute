from codebook import code
cb = code['NASA10bits']

def get_nibble_slice_ciphertext(fc, reverse=False):
    ct = []
    for j in range(len(fc[0])-1):
        cw = ''
        for i in range(len(fc)):
            if reverse:
                cw = cw + fc[i][j]
            else:
                cw = fc[i][j] + cw
        ct.append(cw)
    return ct

def get_ring_ciphertext(fc, reverse=False, codewidth=10):
    ct = []
    for i in range(len(fc)):
        cw = ''
        for j in range(len(fc[i])):
            if reverse:
                cw = cw + fc[i][j]
            else:
                cw = fc[i][j] + cw

            if (j % codewidth) == codewidth-1:
                ct.append(cw)
                cw = ''
    return ct


# Ciphertext from file
f = open("parachute.txt","r")
fc = []
for l in f:
    fc.append([c for c in l])
#print(fc)    
f.close()    

#ct = [ w[1:5] for w in sorted(cb.keys(), key=cb.get) ]
#ct = get_nibble_slice_ciphertext(fc)
ct = get_ring_ciphertext(fc,True)

[ print(c) for c in ct ]
print("--")
[ print(c[::-1]) for c in ct ]
print("--")

# Codeword histogram
cwh = dict()
for c in range(len(ct)):
    if ct[c] in cwh.keys():
        cwh[ct[c]] = cwh[ct[c]] + 1
    else:
        cwh[ct[c]] = 1
[ print("{:s}: {:d}".format(k,cwh[k])) for k in sorted(cwh.keys(), key=cwh.get, reverse=True) ]
print(len(cwh))

# Compute plaintext guesses
pt = []
for msb in range(2):
    pt.append([])
    for i in range(len(ct)):
        cw = "{:1d}{:s}".format(msb,ct[i])
        #print(cw)
        if cw in cb.keys():
            pt[msb].append(cb[cw])
        else:
            pt[msb].append(' ')

print("".join(pt[0]))
print("".join(pt[1]))

pt = []
for i in range(len(ct)):
    cw = ct[i]
    if cw in cb.keys():
        pt.append(cb[cw])
        print("{:s}: {:s}".format(cw,cb[cw]))
    else:
        pt.append(' ')

print("".join(pt))
