"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

  def quadratic_multiply(x, y):
        # this just converts the result from a BinaryNumber to a regular int
        return _quadratic_multiply(x, y).decimal_val

    def _quadratic_multiply(x, y):
        x_vec, y_vec = pad(x.binary_vec, y.binary_vec)
        x_left, x_right = split_number(x_vec)
        y_left, y_right = split_number(y_vec)

        if (x.decimal_val == 0) or (y.decimal_val == 0):
            return BinaryNumber(0)
        elif (x.decimal_val == 1) and (y.decimal_val == 1):
            return BinaryNumber(1)
        else:
            Product1 = _quadratic_multiply(x_left, y_left)
            Product1 = bit_shift(Product1, len(x_vec))
            Product2 = _quadratic_multiply(x_left, y_right)
            Product2 = bit_shift(Product2, len(x_vec)//2)
            Product3 = _quadratic_multiply(x_right, y_left)
            Product3 = bit_shift(Product3, len(x_vec)//2)
            Product4 = _quadratic_multiply(x_right, y_right)
            return BinaryNumber(Product1.decimal_val + Product2.decimal_val + Product3.decimal_val + Product4.decimal_val)

    print(_quadratic_multiply(BinaryNumber(7), BinaryNumber(3)))







    
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    
    return (time.time() - start)*1000


    
    

