import morph_kgc
import rdflib

graph = morph_kgc.materialize('config.ini')

graph.serialize(destination='eCommerce_1982.nt', format='ntriples', encoding="utf-8")


