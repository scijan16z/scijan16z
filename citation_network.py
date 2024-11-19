import networkx as nx
from typing import Dict, List, Union
import community
import matplotlib.pyplot as plt
import scipy.sparse as sp

class CitationNetwork:
    def __init__(self):
        self.G = nx.DiGraph()
        self.metrics = NetworkMetrics()
        self.community_detector = CommunityDetector()
        
    def build_network(self, papers: List[Dict]) -> nx.DiGraph:
        for paper in papers:
            self.G.add_node(paper['doi'], **paper['metadata'])
            for citation in paper['citations']:
                self.G.add_edge(paper['doi'], citation['doi'], 
                               year=citation['year'],
                               context=citation['context'])
                               
        return self._analyze_network() 