# Zadanie 15. Nieskończony iloczyn sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗
# sqrt(0.5))) ∗ ... ma wartość 2/π. Napisz program korzystający z tej
# zależności i wyznaczający wartość π.

def cw15():
    return_value = (0.5)**(0.5)
    value_of_ret_val_bef = 2
    value_before = (0.5)**(0.5)
    e = 0.00000000001
    while abs(value_of_ret_val_bef-return_value) >= e:
        temp = ((0.5) + ((.5)*value_before))**(.5)
        value_of_ret_val_bef = return_value
        return_value *= temp
        value_before = temp
    pi_value = 2.0/return_value
    return pi_value
