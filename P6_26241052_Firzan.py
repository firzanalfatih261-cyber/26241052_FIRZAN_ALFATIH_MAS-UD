print("======Memasukkan Data======")

A = int(input("Digit A :"))
B = int(input("Digit B :"))

kondisi1 = A >= 5
kondisi2 = B >= 5

print("======Hasil Data======")

print("kondisi 1 :", kondisi1)
print("kondisi 2 :", kondisi2)

print("NOT :", not kondisi1)
print("AND :", kondisi1 and kondisi2)
print("OR  :", kondisi1 or kondisi2)
print("XOR :", kondisi1 ^ kondisi2)