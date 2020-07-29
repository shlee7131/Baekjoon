import sys
# 좌표 도달 가능 방법 (n,m) = (n,m-1) + (n-1,m)
n,m,k = map(int,sys.stdin.readline().split())

array = [[1 for i in range(m)] for _ in range(n)]

def path(x,y):
  for i in range(1,x):
    for h in range(1,y):
      array[i][h] = array[i-1][h] + array[i][h-1]
  return array[x-1][y-1]

if (k == 0):
  print(path(n,m))
else:
  #원이 있는 좌표의 위치는 열의 나머지 계산에 따라 다르다
  if(k % m == 0):
    kY = k // m - 1
    kX = m-1
  else:
    kY = k // m
    kX = k % m - 1
  print(path(kY+1,kX+1) * path(n-kY,m-kX))
