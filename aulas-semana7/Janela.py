from Imc import Imc
import PySimpleGUI as sg


class Janela:
    def __init__(self):
        linha0 = [
            sg.Text("Qual seu peso?"),
            sg.InputText("", key="peso"),
            sg.Text("Kg"),
        ]
        linha1 = [
            sg.Text("Qual sua altura?"),
            sg.InputText("", key="altura"),
            sg.Text("metros"),
        ]
        linha2 = [
            sg.Text("Seu IMC é"), 
            sg.Text("", key="imc", size=(30, 1))
        ]
        linha3 = [
            sg.Text("", size=(25, 1)), 
            sg.Button("Calcular IMC")
        ]
        container = [linha0, linha1, linha2, linha3]

        self.__window = sg.Window("Calculadora de IMC", container, font=("Arial", 14))
        self.__mainLoop()

    def __mainLoop(self):
        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == "Calcular IMC":
                try:
                    peso = float(values["peso"])
                    altura = float(values["altura"])
                    imc = Imc(peso, altura)

                    valor_imc = imc.calcularIMC()
                    classificacao = imc.classificarIMC(valor_imc)
                    nova_string = str(valor_imc) + classificacao

                    self.atualizarValor("imc", nova_string)
                except:
                    self.atualizarValor("imc", "Valores inválidos")

        self.__window.close()

    def atualizarValor(self, id, valor):
        self.__window[id].Update(valor)
