import Libs.CATlib as CATlib
import Libs.MDPlib as MDPlib
import Libs.STATlib as STATlib
import Libs.DISPlip as DISPlip
import Libs.GRBlib as GRBlib

cat = CATlib.BATSE_catalog("grbfermi.csv")

MDPs = MDPlib.MDP_from_catalogue(cat)

MDP_cum = STATlib.cumulative(MDPs)

DISPlip.simpleplot(MDP_cum)