"""this program multiplies 7 by every number from 0 to 12 inclusive and displays the times table as output."""

j=7
for i in range(0,13):
    product= j*i #calculates the product pf seven with the corresponding number
    print(f"{i} * {j} = {product}")
    i=i+1
