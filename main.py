import Libs.MDPlib as MDPlib

cat = MDPlib.BATSE_catalog("grbfermi.csv")

MDPlib.MDP_from_catalogue(cat)