from Human import Human

class Programer(Human):
    #  コンストラクタ
    def __init__(self, name, age, langages):
        super().__init__(name, age)
        self.langs = langages

    #  lang表示メソッド
    def printLang(self):
        for lang in self.langs:
            print('I use ' + lang + '.')

    def addLang(self, lang):
        self.langs.append(lang)
