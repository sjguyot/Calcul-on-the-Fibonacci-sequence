Fibonaccisequence = [0, 1, 1, 2, 3, 5]
currentnumber = 0
when i is True:
    nbinFibo_deg1 = Fibonaccisequence[currentnumber]
    nbinFibo_deg2 = Fibonaccisequence[nbinFibo_deg1]
    nbinFibo_deg3 = Fibonaccisequence[nbinFibo_deg2]
    if currentnumber <= len(Fibonaccisequence):
        if nbinFibo_deg1 <= max(Fibonaccisequence):
            if nbinFibo_deg2 <= max(Fibonaccisequence):
                if nbinFibo_deg3 <= max(Fibonaccisequence):
                    if nbinFibo_deg1 = nbinFibo_deg2:
                        if nbinFibo_deg2 = nbinFibo_deg3:
                            print(nbinFibo_deg1)
                        else:
                            return()
                    else:
                        return()
                elif:
                    while max(Fibonaccisequence) <= nbinFibo_deg3:
                        Fibonaccisequence.addend(Fibonaccisequence[len(Fibonaccisequence)- 1] + Fibonaccisequence[len(Fibonaccisequence)- 2])
            elif:
                while max(Fibonaccisequence) <= nbinFibo_deg2:
                    Fibonaccisequence.addend(Fibonaccisequence[len(Fibonaccisequence)- 1] + Fibonaccisequence[len(Fibonaccisequence)- 2])
        elif:
            while max(Fibonaccisequence) <= nbinFibo_deg1:
                Fibonaccisequence.addend(Fibonaccisequence[len(Fibonaccisequence)- 1] + Fibonaccisequence[len(Fibonaccisequence)- 2])