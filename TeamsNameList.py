import re;

def letterToNumber(letter):
  return ord(letter) - 97; # 97 being "a"

f = open('message.txt', "r").read().split("\n");

f = [x for x in f if "Member" not in x]
f = [x for x in f if "Profile picture" not in x]

f = list(map(lambda s: s.rsplit(" ", 1)[0],f))

for i, x in enumerate(f):
  x = x.split();
  x.insert(0, x[-1]);
  x.pop();
  x[0] += ",";
  x = " ".join(x)
  f[i] = x;

f = sorted(f);

for i, x in enumerate(f):
  print(i+1, x);