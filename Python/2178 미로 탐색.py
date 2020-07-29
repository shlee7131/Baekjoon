# BFS 활용
n, m = map(int, input().split())
array = []

for i in range(n):
  array.append([int(i) for i in input()])
array2 = array[:] # BFS 시행 횟수 저장을 위한 배열
visit = []
cur = (0,0)
queue = [cur]

while( queue[0] != (n-1,m-1)):
  visit.append(cur)
  
  temp = queue.pop(0)
  # down
  if ((temp[0] + 1 < n) and (array[temp[0]+1][temp[1]] == 1)):
    newCur = (temp[0]+1,temp[1])
    if (newCur not in visit):
      queue.append(newCur)
      visit.append(newCur)
      # BFS 시행된 횟수를 진행되는 칸에 저장
      array2[newCur[0]][newCur[1]] = array2[temp[0]][temp[1]] + 1
  #right
  if ((temp[1] + 1 < m) and (array[temp[0]][temp[1]+1] == 1)):
    newCur = (temp[0],temp[1]+1)
    if (newCur not in visit):
      queue.append(newCur)
      visit.append(newCur)
      # BFS 시행된 횟수를 진행되는 칸에 저장
      array2[newCur[0]][newCur[1]] = array2[temp[0]][temp[1]] + 1
  # up
  if ((temp[0] - 1 > -1) and (array[temp[0]-1][temp[1]] == 1)):
    newCur = (temp[0]-1,temp[1])
    if (newCur not in visit):
      queue.append(newCur)
      visit.append(newCur)
      # BFS 시행된 횟수를 진행되는 칸에 저장
      array2[newCur[0]][newCur[1]] = array2[temp[0]][temp[1]] + 1
  # left
  if ((temp[1] - 1 > -1) and (array[temp[0]][temp[1]-1] == 1)):
    newCur = (temp[0],temp[1]-1)
    if (newCur not in visit):
      queue.append(newCur)
      visit.append(newCur)
      # BFS 시행된 횟수를 진행되는 칸에 저장
      array2[newCur[0]][newCur[1]] = array2[temp[0]][temp[1]] + 1



print(array2[n-1][m-1])
