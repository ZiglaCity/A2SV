n = int(input())
a = list(map(int, input().split())) # cost of chocolate bars
m = int(input()) # number of coupons
q = list(map(int, input().split())) # coupons (number of chocolate bars that can be bought with the ith coupon)

#  ith coupon can buy qi chocolate bars and pay the qi - 1 most expensive ones
# use only one coupon
# using i th coupon mean choose qi bars and buy them using the coupon, ad but the remaining n - qi bars without discount


a.sort(reverse=True) 
total = sum(a) # total cost of all chocolate bars
for c in q:
    print(total - a[c - 1])
