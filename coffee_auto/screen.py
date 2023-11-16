import coffee_auto.coffee_maker


class Screen:

    def __init__(self, cof_nam):
        spis_coff = [('Мокка', 100), ('Капучино', 110), ('Эспрессо', 50), ('Американо', 80), ('Латте', 100)]

    def coffee_choice(self, cof):
        cofe = coffee_auto.coffee_maker.Maker()
        if cof == 'Мокка':
            cofe.makemokka()
        elif cof == 'Капучино':
            cofe.makecapuchino()
        elif cof == 'Эспрессо':
            cofe.makecespresso()
        elif cof == 'Американо':
            cofe.makeamericano()
        elif cof == 'Латте':
            cofe.makelatte()


    def coffee_give(self):
        print('Вот ваш кофе')