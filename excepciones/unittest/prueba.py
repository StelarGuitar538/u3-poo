def verificar_contraseña(contraseña):
    if len(contraseña) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")
    if not any(char.isdigit() for char in contraseña):
        raise ValueError("La contraseña debe contener al menos un número")
    if not any(char.isalpha() for char in contraseña):
        raise ValueError("La contraseña debe contener al menos una letra")
    return True
