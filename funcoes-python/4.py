def calcula_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6:
        return f'Você foi aprovado (média {media})'
    else:
        return f'Você foi reaprovado (média {media})'

print(calcula_media(5, 7))