# square is of 17 digits so number must be greater than 3e8
# square is starting from 1, so number must be below 5e8 as it square is 2.5*10^17
# square ending in 9, so number must be ending in 3, or 7
prime_form = "1_2_3_4_5_6_7_8_9"

for i in range(100000000, 150000000):
    if i % 10 == 3 or i % 10 == 7:
        square = str(i*i)
        # print(i, square)
        if square[0] == '1' and square[2] == '2' and square[4] == '3' and square[6] == '4' and square[8] == '5' and square[10] == '6'  and square[12] == '7' and square[14] == '8' and square[16] == '9':
            print(i)            




