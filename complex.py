def ComplexAddition(real1, imaginary1, real2, imaginary2): 
    sum_real = real1 + real2 
    sum_imaginary = imaginary1 + imaginary2 
    print(f"Addition: {sum_real} + {sum_imaginary}i")

  

def ComplexSubtraction(real1, imaginary1, real2, imaginary2): 
    sub_real = real1 - real2 
    sub_imaginary = imaginary1 - imaginary2 
    print(f"Subtraction: {sub_real} + {sub_imaginary}i")

  

def ComplexMultiplication(real1, imaginary1, real2, imaginary2): 
    mul_real = real1*real2 - imaginary1*imaginary2 
    mul_imaginary = real1*imaginary2 + imaginary1*real2 
    print(f"Multiplication: {mul_real} + {mul_imaginary}i")


def ComplexDivision(real1, imaginary1, real2, imaginary2): 
    divisor = real2**2 + imaginary2**2 
    div_real = (real1*real2 + imaginary1*imaginary2) / divisor 
    div_imaginary = (imaginary1*real2 - real1*imaginary2) / divisor 
    print(f"Division: {div_real} + {div_imaginary}j")



real1 = float(input("Enter the real part of the first complex number: ")) 
imaginary1 = float(input("Enter the imaginary part of the first complex number: ")) 
print(f"1st Complex Number: {real1} + {imaginary1}i")

  
real2 = float(input("Enter the real part of the second complex number: ")) 
imaginary2 = float(input("Enter the imaginary part of the second complex number: ")) 
print(f"2nd Complex Number: {real2} + {imaginary2}i")


ComplexAddition(real1, imaginary1, real2, imaginary2) 
ComplexSubtraction(real1, imaginary1, real2, imaginary2) 
ComplexMultiplication(real1, imaginary1, real2, imaginary2) 
ComplexDivision(real1, imaginary1, real2, imaginary2) 