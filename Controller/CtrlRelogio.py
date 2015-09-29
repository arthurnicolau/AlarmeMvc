from Model.Alarme import alarme
from Model.Relogio import relogio
from View.Application import view


class controller():

    def __init__(self):
        self.view = view()

    def start(self):
        hora = self.view.start()
        self.aguardaAlarme(hora)

    def mostraHora(self):
        rel = relogio()
        diaAtual = rel.pegaHoraData()
        print(diaAtual.strftime('%H:%M:%S'))

    def mostraData(self):
        rel = relogio()
        diaAtual = rel.pegaHoraData()
        print(diaAtual.strftime('%d/%m/%y'))


    def aguardaAlarme(self,hora):
        alam = alarme()
        rel = relogio()
        horaProgramada = alam.programaAlarme(hora)
        horaAtual = rel.pegaHoraData().strftime('%H:%M:%S')
        while(horaProgramada!=horaAtual):
            horaAtual = rel.pegaHoraData().strftime('%H:%M:%S')
        alam.tocaAlarme()

if __name__ == '__main__':
    main = controller()
    main.start()
