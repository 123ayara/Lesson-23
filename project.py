tup1=(4,3,2,2,-1,18)
tup2=(2,4,8,8,3,2,9)
def calculate_product(tup):
 product=1
 for num in tup:
  product*=num
 return product
print("product of tuple 1:",calculate_product(tup1))
print("product of tuple 2:",calculate_product(tup2))