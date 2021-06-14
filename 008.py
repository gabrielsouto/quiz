apostadas = {4, 8, 15, 17, 24, 43}
sorteadas = {4, 23, 16, 8, 15, 42}
acertadas = 0
for apostada in apostadas:
    for sorteada in sorteadas:
        if apostada == sorteada:
            acertadas++
            break
print(acertadas)