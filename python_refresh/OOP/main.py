"""
Sera contruido um pequeno jogo no qual podemos criar inimigos que irão brigar

Critérios a serem seguidos:
    - Inimigos tem que brigar
    - Tera inimigos do tipo Zumbi e Ogro
    - Cada inimigo tem poderes diferentes, pontos de cura e dano de ataque

Sera implementado os 4 pilares do OOP
"""

from enemy import Enemy

enemy1 = Enemy()
enemy1.tipo_de_inimigo = 'Zumbi'
print(enemy1.tipo_de_inimigo)