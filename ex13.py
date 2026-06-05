def para_segundos(h, m, s):
    return h * 3600 + m * 60 + s


def para_horario(seg):
    h = seg // 3600
    seg = seg % 3600

    m = seg // 60
    s = seg % 60

    return h, m, s


hora = int(input("Hora atual: "))
minuto = int(input("Minuto atual: "))
segundo = int(input("Segundo atual: "))

add_hora = int(input("Horas para adiantar: "))
add_minuto = int(input("Minutos para adiantar: "))
add_segundo = int(input("Segundos para adiantar: "))

tempo_atual = para_segundos(hora, minuto, segundo)
tempo_adicional = para_segundos(add_hora, add_minuto, add_segundo)

total = tempo_atual + tempo_adicional

# Mantém dentro de 24 horas
total = total % (24 * 3600)

h, m, s = para_horario(total)

print(f"Novo horário: {h:02d}:{m:02d}:{s:02d}")