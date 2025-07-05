import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes= DAO.getAllNodes()
        self._idMapObjects = {}
        for node in self._nodes:
            self._idMapObjects[node.object_id] = node
        self._graph= nx.Graph()
        self.buildGraph()
        self._nodo_partenza = ""
        self._best_path = []
        self._best_cost = 0
        self._Nconnesse=0



    def buildGraph(self):
        nodes = DAO.getAllNodes()
        archi = DAO.getAllEdges()
        self._graph.add_nodes_from(nodes)
        for arco in archi:
            self._graph.add_edge(self._idMapObjects[arco[0]], self._idMapObjects[arco[1]], weight=arco[2])
        return self._graph

    def number_nodes(self):
        return len(self._graph.nodes)

    def get_number_edges(self):
        return len(self._graph.edges)

    def calcola_componenti_connesse(self, idImput):
        source= self._idMapObjects[idImput]
        connesse = nx.node_connected_component(self._graph, source)
        self._Nconnesse = len(connesse)
        return len(connesse)

    def getN_connesse(self):
        return self._Nconnesse



    def hasNode(self, idImput):
        return idImput in self._idMapObjects

    def get_optimal_path(self,source, lunghezza):
        self._best_path=[]
        self._best_cost=0

        parziale= [source]

        for nodo in self._graph.neighbors(source):
            if nodo.classification == parziale[-0].classification:
                parziale.append(nodo)
                self.ricorsione(parziale,lunghezza)
                parziale.pop()

        return self._best_path,self._best_cost

    def ricorsione(self,parziale,lunghezza):
        if len(parziale) == lunghezza:
            if self.calcola_costo(parziale) > self._best_cost:
                self._best_cost = self.calcola_costo(parziale)
                self._best_path = copy.deepcopy(parziale)
            return

        for nodo in self._graph.neighbors(parziale[-1]):
            if nodo.classification == parziale[-0].classification and nodo not in parziale:
                parziale.append(nodo)
                self.ricorsione(parziale,lunghezza)
                parziale.pop()


    def calcola_costo(self,parziale):
        costo = 0
        for i in range(len(parziale)-1):
            costo += self._graph[parziale[i]][parziale[i+1]]['weight']
        return costo

    def getObjectFromId(self, id):
        return self._idMapObjects[id]






