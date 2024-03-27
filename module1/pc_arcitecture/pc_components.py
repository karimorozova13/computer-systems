# CPU - Central Processing Unit, Центральний процесор
# RAM (Random Access Memory-) - Оперативна пам'ять
# I/O - пристрої введення/виведення

# CPU ->
# ALU (Arithmetic Logic Unit) - арифметико-логічний пристрій

# Кодування
ascii_encoded = ord('A')  # 65
print("ascii_encoded: %s" %(ascii_encoded))
# Декодування
ascii_decoded = chr(97)  # 'A'
print("ascii_decoded: %s" %(ascii_decoded))

# Кодування
unicode_encoded = 'Є'.encode('utf-8')  # b'\\xd0\\x84'
print("unicode_encoded: %s" %(unicode_encoded))
# Декодування
unicode_decoded = unicode_encoded.decode('utf-8')  # 'Є'
print("unicode_decoded: %s" %(unicode_decoded))

