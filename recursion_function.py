def tri_recursion(k):
  if(k>0):
    try_recursion_val = tri_recursion(k-1)
    result = k + try_recursion_val
    print(f"At k = {k}, we have tri_recursion(k-1) = {try_recursion_val}")
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
