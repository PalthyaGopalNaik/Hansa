def f(arr,start,end):
  if start < len(arr):
    big = arr[start-1]
  else :
    return []
  for i in arr[start-1:end]:
    if i > big :
      big = i
  return big
arr = [int(x) for x in input().split()]
start = int(input("Start Index :"))
end = int(input("End Index :"))
print(f(arr,start,end))
