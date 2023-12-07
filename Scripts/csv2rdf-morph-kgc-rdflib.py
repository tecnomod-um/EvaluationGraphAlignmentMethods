import morph_kgc
import rdflib

graph = morph_kgc.materialize('config.ini')

graph.serialize(destination='../E-CommerceData/Mappings/ecommercedataLLM.nt', format='ntriples', encoding="utf-8")


