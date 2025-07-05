import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model





    def handleAnalizzaOggetti(self, e):
        grafo = self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.number_nodes()}, Numero di archi: {self._model.get_number_edges()}"))
        self._view.update_page()

    def handleCompConnessa(self,e):
        txtImput = self._view._txtIdOggetto.value
        if txtImput == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("selezionare un nodo di partenza", color="red"))
            self._view.update_page()
            return
        try:
            idImput = int(txtImput)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("L' ID inserito non è un intero",color="red"))
            self._view.update_page()
            return
        if not self._model.hasNode(idImput):
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("L' ID inserito non è presente nel grafo", color="red"))
            self._view.update_page()
            return
        componenti = self._model.calcola_componenti_connesse(idImput)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"numero di componenti connesse: {componenti}"))
        self._view._txtLUN.disabled = False
        self._view._btnCecraOggetti.disabled = False
        self._view.update_page()

    def handleCercaOggetti(self,e):
        lunghezza= self._view._txtLUN.value
        if lunghezza == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire una lunghezza", color="red"))
            self._view.update_page()
            return
        try:
            lunghezzaInt = int(lunghezza)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("la lunghezza inserita non è un intero", color="red"))
            self._view.update_page()
            return
        if lunghezzaInt <2:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("la lunghezza inserita deve essere >= di 2", color="red"))
            self._view.update_page()
            return

        if lunghezzaInt > self._model.getN_connesse():
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"la lunghezza inserita deve essere <= di {self._model.getN_connesse()} ", color="red"))
            self._view.update_page()
            return
        source = self._model.getObjectFromId(int(self._view._txtIdOggetto.value))
        optPath,costo = self._model.get_optimal_path(source, lunghezzaInt)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(
            f"Cammino che parte da {source} trovato con peso totale {costo}."))
        for p in optPath:
            self._view.txt_result.controls.append(ft.Text(p))
        self._view.update_page()













