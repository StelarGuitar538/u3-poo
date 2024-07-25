def divide(a, b):
    assert b != 0, "El divisor no puede ser cero killer"
    return a / b

print(divide(10, 2))  # Esto funciona correctamente
print(divide(10, 0))  # Esto generará AssertionError