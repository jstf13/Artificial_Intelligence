import numpy as np
IIIIlllllIlII = 1
IIlIIllIllIllIIIIII = 0
class SpaceGPTAgent:
    def __init__(self, IlllIIllIII, llllIlllllIl):
        self.IlllIIllIII = (IlllIIllIII % 2) + 1
        self.lIlIIIlllII = llllIlllllIl
    def next_action(self, lllIlIlIIIIlIllllIIl):
        lIIllIIllIIIlIIl, llIlIlllIIllIIlllII = self.IIIIIIlllIIlIIII(lllIlIlIIIIlIllllIIl, self.IlllIIllIII, self.lIlIIIlllII)
        return lIIllIIllIIIlIIl
    def IIIlIIlIIlllI(self, llIllllllIl):
        llIIIllIllIIIIIll = self.llllIIllIII(llIllllllIl)
        return 1000 * llIIIllIllIIIIIll[4] +                    3 * llIIIllIllIIIIIll[3] +                    2 * llIIIllIllIIIIIll[2]
    def IIIIIIlllIIlIIII(self, llIllllllIl, IlllIIllIII: int, llllIlllllIl: int = 2):
        if llIllllllIl.is_final() or llllIlllllIl == 0:
            return None, self.IIIlIIlIIlllI(llIllllllIl)
        if IlllIIllIII != self.IlllIIllIII:
            IlllIlIlllIII = llIllllllIl.get_posible_actions()
            IlIllllllllllIIII = np.inf
            for llllIlII in IlllIlIlllIII:
                IIlIlIlIlIIlllIlllI = llIllllllIl.clone()
                lIlIllllIIlIlIIlIl = IIlIlIlIlIIlllIlllI.add_tile(llllIlII, IlllIIllIII)
                if lIlIllllIIlIlIIlIl:
                    llIlIlllIIllIIlllII, lIIIIlllIIlllllIIlll = self.IIIIIIlllIIlIIII(IIlIlIlIlIIlllIlllI, self.IIllIlIIllllIIIlI(IlllIIllIII), llllIlllllIl - 1)
                    if lIIIIlllIIlllllIIlll < IlIllllllllllIIII:
                        IlIllllllllllIIII = lIIIIlllIIlllllIIlll
            return None, IlIllllllllllIIII
        if IlllIIllIII == self.IlllIIllIII:
            lIIllIIllIIIlIIl = None
            lllllIIIlllllII = -np.inf
            IlllIlIlllIII = llIllllllIl.get_posible_actions()
            for llllIlII in IlllIlIlllIII:
                IIlIlIlIlIIlllIlllI = llIllllllIl.clone()
                lIlIllllIIlIlIIlIl = IIlIlIlIlIIlllIlllI.add_tile(llllIlII, IlllIIllIII)
                if lIlIllllIIlIlIIlIl:
                    llIlIlllIIllIIlllII, lIIIIlllIIlllllIIlll = self.IIIIIIlllIIlIIII(IIlIlIlIlIIlllIlllI, self.IIllIlIIllllIIIlI(IlllIIllIII), llllIlllllIl - 1)
                    if lIIIIlllIIlllllIIlll >= lllllIIIlllllII:
                        lllllIIIlllllII = lIIIIlllIIlllllIIlll
                        lIIllIIllIIIlIIl = llllIlII
            return lIIllIIllIIIlIIl, lllllIIIlllllII
    def IIllIlIIllllIIIlI(self, IlllIIllIII):
        return ((IlllIIllIII) % 2) + 1
    def llllIIllIII(self, llIllllllIl):
        IIIIllIlllll = {2:0, 3:0, 4:0}
        IlIIIIllllIIIIlII = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        IIlIlIIll = set()
        for lIlIIIlIlIlIllIIl in range(llIllllllIl.heigth):
            for lIlIIIIlllll in range(llIllllllIl.length):
                IlllIIllIII = llIllllllIl[lIlIIIlIlIlIllIIl][lIlIIIIlllll]
                if IlllIIllIII != IIlIIllIllIllIIIIII and ((lIlIIIlIlIlIllIIl, lIlIIIIlllll) not in IIlIlIIll):
                    for (IIlIlllIIIl, llIlIIllIIIIlIllllI) in IlIIIIllllIIIIlII:
                        lIlllIIIl = {1:True, -1:True}
                        IIIIlllIIIlIIlIlIlll = 1
                        for lIllIIlIllIlIllIIl in range(1, 4):
                            if not (lIlllIIIl[1] or lIlllIIIl[-1]):
                                break
                            for IlllIIllIllIlIllIllI in [1, -1]:
                                lIIlIIIIlIIIllllI = lIlIIIlIlIlIllIIl + (IIlIlllIIIl * lIllIIlIllIlIllIIl * IlllIIllIllIlIllIllI)
                                llIlIIllIllIIlll = lIlIIIIlllll + (llIlIIllIIIIlIllllI * lIllIIlIllIlIllIIl * IlllIIllIllIlIllIllI)
                                if self.lIllllIlIIllIIlIIlII(llIllllllIl, lIIlIIIIlIIIllllI, llIlIIllIllIIlll)                                        and (llIllllllIl[lIIlIIIIlIIIllllI][llIlIIllIllIIlll] == llIllllllIl[lIlIIIlIlIlIllIIl][lIlIIIIlllll]
                                             or llIllllllIl[lIIlIIIIlIIIllllI][llIlIIllIllIIlll] == IIlIIllIllIllIIIIII):
                                    if llIllllllIl[lIIlIIIIlIIIllllI][llIlIIllIllIIlll] != IIlIIllIllIllIIIIII:
                                        IIlIlIIll.add((lIIlIIIIlIIIllllI, llIlIIllIllIIlll))
                                        IIIIlllIIIlIIlIlIlll += 1
                                else:
                                    lIlllIIIl[IlllIIllIllIlIllIllI] = False
                        if (lIlllIIIl[1] or lIlllIIIl[-1])                                and IIIIlllIIIlIIlIlIlll > 1:
                            IllIlIIIlIIlIIII = -1 if IlllIIllIII != self.IlllIIllIII else 1
                            IIIIllIlllll[min(IIIIlllIIIlIIlIlIlll, 4)] += IllIlIIIlIIlIIII
        return IIIIllIlllll
    def lIllllIlIIllIIlIIlII(self, llIllllllIl, lIlIIIlIlIlIllIIl, lIlIIIIlllll):
        lIlllIllllI = lIlIIIlIlIlIllIIl >= 0 and lIlIIIlIlIlIllIIl < llIllllllIl.heigth
        lIlIlIIIlIlIllIlIIIl = lIlIIIIlllll >= 0 and lIlIIIIlllll < llIllllllIl.length
        return lIlllIllllI and lIlIlIIIlIlIllIlIIIl
