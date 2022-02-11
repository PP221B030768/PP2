anum, anum2 = input().split('+')
di_num = {
  'ONE': '1',
  'TWO': '2',
  'THR': '3',
  'FOU': '4',
  'FIV': '5',
  'SIX': '6',
  'SEV': '7',
  'EIG': '8',
  'NIN': '9',
  'ZER': '0'
}
di_alp = {
  '1': 'ONE',
  '2': 'TWO',
  '3': 'THR',
  '4': 'FOU',
  '5': 'FIV',
  '6': 'SIX',
  '7': 'SEV',
  '8': 'EIG',
  '9': 'NIN',
  '0': 'ZER'
}
fi = []
se = []
for i in range(0, len(anum), 3):
  ss = anum[i:i+3]
  fi.append(di_num[ss])
for i in range(0, len(anum2), 3):
  ss = anum2[i:i+3]
  se.append(di_num[ss])
num = ''.join(fi)
numm = ''.join(se)
num = int(num)
numm = int(numm)

summ = num + numm
summ = list(str(summ))
res = []
for i in summ:
    res.append(di_alp[i])
print(''.join(res))