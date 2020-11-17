
a = 1
while a < 9:
    print(f"{'0' * a:^9}")
    a += 2
b = 9
while b > 1:
     print(f"{'0' * a:^9}")
     a -= 2
     if a < 1:
         break