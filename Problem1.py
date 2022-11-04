def f(stri):
  mystr = str(stri)
  prev = ""
  for i in range(len(stri)):
    cur = mystr[i]
    if cur >= 'a' or cur <='z' and cur >= 'A' or cur <='Z' and cur >= "0" and cur <= "9" or cur == " ":
      if prev in " " and cur in {'a','e','i','o','u','A','E','I','O','U'}:
        mystr = mystr[:i] + "$" + mystr[i+1:]
      if prev == "0" and cur in {0,1,2,3,4,5,6,7,8,9}:
        mystr = mystr[:i] + "1" + mystr[i+1:]
      if prev== cur in {0,1,2,3,4,5,6,7,8,9} :
        mystr = mystr[:i] + "0" +mystr[i+1:]

    else:
      return "Not an Alphanumeric statement"
    prev = cur
  return mystr
stri = input()
print(f(stri))
