
def prod(n):
    sum_price = 0
    for i in range(n):
        #price = int(input("ราคาสินค้า%d:"%(i+1)))
        price = int(input(f"ราคาสอนค้า{i+1}:"))
        sum_price += price
    return sum_price

def tax(total):
    vat = (7/100)*total
    return vat





num = int(input("จํานวนรายการสินค้า:"))
print(tax(prod(3)))