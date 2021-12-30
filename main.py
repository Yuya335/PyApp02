from Human import Human
from Programer import Programer

def main():
    human = Human('YUYU', 27)
    human.printName()
    human.printAge()

    langs = ['Python', 'JavaScript', 'Java', 'C言語']

    programer = Programer('yu', 27, langs)
    programer.printLang()
    # langの追加
    programer.addLang('C#')
    programer.printLang()

if __name__ == '__main__':
    main()