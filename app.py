from abc import ABC, abstractmethod
from random import randint
from os import system

class Entidade(ABC):
    def __init__(self,nome):
        self.nome = nome
        self.lv = 1
        self.atributos()

    
    def atributos(self):
        self.hp = self.lv * 15
        self.atk = self.lv * 7
        self.hp_max = self.hp
        self.exp = 0
        self.exp_max = self.lv * 10
    
    @property
    def esta_vivo(self) -> bool:
        return self.hp > 0
    
    @abstractmethod
    def atacar(self,alvo):
        return ...


class inventario:
    def __init__(self):
        self.potion = 5
        self.atk_especial = 3

class Personagem(Entidade):
    def __init__(self, nome):
        super().__init__(nome)
        self.inventario = inventario()
        self.escapar = 2

    def level_up(self):
        print(f'\n✅ {self.nome} subiu de LEVEL! ✅')
        self.lv += 1
        self.atributos()
        self.inventario.potion += 1
        self.exp = 0
        return self.lv
    
    def curar(self):
        if self.inventario.potion > 0:
            print(f'\n💚💚 {self.nome} curou {self.hp_max - self.hp} de HP 💚💚')
            self.hp = self.hp_max
            self.inventario.potion -= 1
            return
        print('\n❌❌ Sem poções sulficientes ❌❌')

    def atacar(self, alvo):
        dano = self.atk
        if randint(1,100) <= 30:
            dano *= 2
            print(f'\n💥💥 {self.nome} causou {dano} de dano critico em {alvo.nome} 💥💥')
        alvo.hp -= dano
        print(f'\n⚔️⚔️ {self.nome} atacou {alvo.nome} causando {dano} de dano! ⚔️⚔️')


    def exibir_atributos(self):
        print(f'\nNome: {self.nome}')
        print(f'HP: {self.hp} | {self.hp_max}')
        print(f'ATK: {self.atk}')
        print(f'Potion: {self.inventario.potion}')
        print(f'Level: {self.lv}')
        print(f'XP: {self.exp} | {self.exp_max}')



class Inimigo(Entidade):
    def __init__(self, nome):
        super().__init__(nome)
        self.drop_xp = self.lv * 6

    def atributos(self):
        self.drop_xp = self.lv * 6
        return super().atributos()
    def atacar(self, alvo):
        dano = self.atk
        alvo.hp -= dano
        print(f'⚔️⚔️ {self.nome} atacou {alvo.nome} causando {dano} de dano! ⚔️⚔️')

    def exibir_atributos(self):
        print(f'\nNome: {self.nome}')
        print(f'HP: {self.hp} | {self.hp_max}')
        print(f'ATK: {self.atk}')
        print(f'Level: {self.lv}')


def chamar_novo_inimigo(personagem):
    novo_inimigo = Inimigo('Goblin')
    novo_inimigo.lv = randint(personagem.lv,personagem.lv +2)
    novo_inimigo.atributos()
    print(f"\n⚠️  Um novo {novo_inimigo.nome} nível {novo_inimigo.lv} apareceu!")
    return novo_inimigo

def limpar_tela():
    system('cls')

def batalhar(personagem,inimigo):
    print('-------------RPG PYTHON-------------')
    while True:
        personagem.exibir_atributos()
        print('------------------------------------')
        inimigo.exibir_atributos()
        print('-------------AÇÃO-------------------')
        print('[A] Atacar [U] Usar Poção [F] Fugir')
        opcao = input('Opção: ').lower()
        limpar_tela()
        if opcao == 'a':
            personagem.atacar(inimigo)
            if inimigo.esta_vivo:
                inimigo.atacar(personagem)
            else:
                personagem.exp += inimigo.drop_xp
                if personagem.exp >= personagem.exp_max:
                    personagem.level_up()
                inimigo = chamar_novo_inimigo(personagem)

            if not personagem.esta_vivo:
                print('\n💀 Você morreu... GAME OVER')
                break
        elif opcao =='u':
            personagem.curar()
        elif opcao =='f':
            if personagem.escapar > 0:
                print(f'\n{personagem.nome} fugiu da batalha')
                inimigo = chamar_novo_inimigo(personagem)
                personagem.escapar  -= 1
                continue
            print('\nVocê não pode mais fugir!')
        else:
            print('\nopção inválida...')
def new_game():
    nome = input('\nDigite o nome do seu personagem: ')
    personagem = Personagem(nome)
    inimigo = Inimigo('Goblin')
    batalhar(personagem,inimigo)


new_game()


