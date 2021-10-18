import gerberex

ctx = gerberex.GerberComposition()

metal1 = gerberex.read('board1.gtl')
ctx.merge(metal1)

metal2 = gerberex.read('board2.gtl')
metal2.to_metric()
metal2.rotate(-20)
metal2.offset(30, 0)
ctx.merge(metal2)

ctx.dump('panelized-board.gtl')