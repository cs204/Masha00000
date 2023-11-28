import signalDefinitions as sign
import poly

def sum1(l):
    if len(l) == 0:
        return 0
    res = l[0]
    for elem in l[1:]:
        res += elem
    return res


def polyR(s, p):
    """
    @param s:  экземпляр класса Signal,
    @param p:  экземпляр класса Polynomial,
    @return: новый экземпляр класса Singal, который получен из сигнала  s, преобразованного  полиномом по R
    """
    #ваш код
    return sum1([p.coeff(i) * sign.Rn(s, i) for i in range (p.order + 1)])


#step1: сигнал равен 3.0 для t >= 0 и 0 для других
step1 = 3 * sign.Rn(sign.StepSignal(), 3 )

#step2: сигнал равен -3.0 для t >= 7 и 0 для других t.
step2 = -3 * sign.Rn(sign.StepSignal(), 7 )


#stepUpDown: сигнал равен 3.0 для 3 <= t <= 6 и 0 для других t
stepUpDown = sign.Rn(sign.StepSignal() * 3 , 3) + sign.Rn(sign.StepSignal() * (-3), 7)

#stepUpDownPoly: используйте polyR, чтобы построить сигнал, который имеет
#значение 1.0 в t = 1, значение 3 в t = 3, 5 для t = 5 и 0 для остальных.
stepUpDownPoly = polyR(sign.UnitSampleSignal(), poly.Polynomial ([5, 0, 3, 0, 1, 0]) )


#Для проверки раскомментируйте строку ниже
def test():
    print("step1:")
    print(list(range(0, 5)))
    print(step1.samplesInRange(0, 5))

    print("step2:")
    print(list(range(0, 9)))
    print(step2.samplesInRange(0, 9))

    print("stepUpDown:")
    print(list(range(0, 9)))
    print(stepUpDown.samplesInRange(0, 9))

    print("stepUpDownPoly:")
    print(list(range(0, 9)))
    print(stepUpDownPoly.samplesInRange(0, 9))




if __name__ == "__main__":
    test()
