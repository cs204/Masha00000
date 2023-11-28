import sm


def dotProd(a, b):
    """
    скалярное произведение списков a, b.
    """
    if len(a) == 0 or len(b) == 0:
        return 0
    if len(a) != len(b):
        print('dotProd mismatch error ' + str(len(a)) + ' != ' + str(len(b)))
    return sum([ai * bi for (ai, bi) in zip(a, b)])

class LTISM(sm.SM):
    """
    Линейные время-инвариантные системы
    """
    def __init__(self, dCoeffs, cCoeffs, previousInputs = [], previousOutputs = []	):
        j = len(dCoeffs) - 1
        k = len(cCoeffs)
        self.cCoeffs = cCoeffs
        self.dCoeffs = dCoeffs
        # Состояние последние j ввода и последние k вывода
        if len(previousInputs) == 0:
            previousInputs = [0.0] * j
        if len(previousOutputs) == 0:
            preivousOutputs = [0.0] * k
        self.startState = (previousInputs, previousOutputs)

    def getNextValues(self, state, input):
        (inputs, outputs) = state
        inputs = [input] + inputs
        o= dotProd(self.dCoeffs, inputs)+ dotProd(self.cCoeffs, outputs)
        outputs =  [o] + outputs [:-1]
        inputs=inputs[:-1]
        return((inputs, outputs), o)
def test():
    m = LTISM([1, 2], [1], [3], [4])
    o = m.transduce([1, 2, 3, 4, 5])
    print(o)

# Чтобы проверить раскомментируйте ниже

if __name__ == "__main__":
    test()
    pass

