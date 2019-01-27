from tkinter import *
import PlotGraph as pg
import functionValue
from decimal import Decimal
from numpy import round
from HJAlg import hooke


class Window(Frame):



    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()


    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget      
        self.master.title("Hook & Jeeves minimum search by Krakowian J. and Gaciarz M.")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


        functionLabel = Label(self, text="Function")
        functionLabel.place(x=30,y=10)

        functionLabel = Label(self, text="f = ")
        functionLabel.place(x=180,y=10)

        textFunction = Text(self, height=1, width=35)
        textFunction.place(x=210,y=10)

        startingPointLabel = Label(self, text="Starting point")
        startingPointLabel.place(x=30,y=60)

        xPointLabel = Label(self, text="X = ")
        xPointLabel.place(x=180,y=60)

        textX = Text(self, height=1, width=3)
        textX.place(x=210,y=60)

        yPointLabel = Label(self, text="Y = ")
        yPointLabel.place(x=250,y=60)

        textY = Text(self, height=1, width=3)
        textY.place(x=280,y=60)


        orthPointLabel = Label(self, text="Orth. basis vector")
        orthPointLabel.place(x=25,y=90)

        orthXPointLabel = Label(self, text="X = ")
        orthXPointLabel.place(x=180,y=90)

        textOrthXPointA = Text(self, height=1, width=3)
        textOrthXPointA.place(x=210,y=90)

        textOrthXPointB = Text(self, height=1, width=3)
        textOrthXPointB.place(x=280,y=90)

        orthYPointLabel = Label(self, text="Y = ")
        orthYPointLabel.place(x=180,y=120)

        textOrthYPointA = Text(self, height=1, width=3)
        textOrthYPointA.place(x=210,y=120)

        textOrthYPointB = Text(self, height=1, width=3)
        textOrthYPointB.place(x=280,y=120)

        tauLabel = Label(self, text="Tau")
        tauLabel.place(x=25,y=150)

        tauLabel = Label(self, text="T = ")
        tauLabel.place(x=180,y=150)

        textTau= Text(self, height=1, width=12)
        textTau.place(x=210,y=150)

        
        betaLabel = Label(self, text="Beta")
        betaLabel.place(x=25,y=180)

        betaLabel = Label(self, text="B = ")
        betaLabel.place(x=180,y=180)

        textBeta= Text(self, height=1, width=12)
        textBeta.place(x=210,y=180)
        alphaLabel = Label(self, text="Alpha")
        alphaLabel.place(x=25,y=210)

        alphaLabel = Label(self, text="A = ")
        alphaLabel.place(x=180,y=210)

        textAlpha= Text(self, height=1, width=12)
        textAlpha.place(x=210,y=210)

        epsilonLabel = Label(self, text="Epsilon")
        epsilonLabel.place(x=25,y=240)

        epsilonLabel = Label(self, text="E = ")
        epsilonLabel.place(x=180,y=240)

        textEpsilon= Text(self, height=1, width=12)
        textEpsilon.place(x=210,y=240)

        iterationsLabel = Label(self, text="Iterations")
        iterationsLabel.place(x=25,y=310)

        iterationsLabel = Label(self, text="I = ")
        iterationsLabel.place(x=180,y=310)

        iterationsResultLabel = Label(self, text="----")
        iterationsResultLabel.place(x=180,y=310)

        minimumLabel = Label(self, text="Minimum")
        minimumLabel.place(x=25,y=340)

        minimumLabel = Label(self, text="X = ")
        minimumLabel.place(x=180,y=340)

        minimumXLabel = Label(self, text="----")
        minimumXLabel.place(x=210,y=340)

        minimumLabel = Label(self, text="Y = ")
        minimumLabel.place(x=180,y=370)

        minimumYLabel = Label(self, text="----")
        minimumYLabel.place(x=210,y=370)

        runButton = Button(self, text="RUN", width=33, command=self.runButtonHandler)
        runButton.place(x=25, y=270)

        # insert default values
        textFunction.insert(END, "2*x[0]**2 + 2*x[0]*x[1] + 2*x[1]**2 - 6*x[0]")

        textX.insert(END, "2")
        textY.insert(END, "5")

        textOrthXPointA.insert(END, "1")
        textOrthXPointB.insert(END, "0")
        textOrthYPointA.insert(END, "0")
        textOrthYPointB.insert(END, "1")

        textTau.insert(END, "0.5")
        textEpsilon.insert(END, "1.0E-07")
        textBeta.insert(END, "1")
        textAlpha.insert(END, "1")

        # save values so We can access them when grabbing data from them
        self.txtFnc = textFunction
        self.txtX = textX
        self.txtY = textY
        self.OrthXptA = textOrthXPointA
        self.OrthXptB = textOrthXPointB
        self.OrthYptA = textOrthYPointA
        self.OrthYptB = textOrthYPointB
        self.txtTau = textTau
        self.txtEps = textEpsilon
        self.txtBeta = textBeta
        self.txtAlpha = textAlpha
        self.IterLabel = iterationsResultLabel
        self.minXlabel = minimumXLabel
        self.minYlabel = minimumYLabel

    # # OPTIONS
    # nvars = 2  # wymiar
    # startpt = [6, 7]  # punkt startowy
    # itermax = 1500  # maks liczba iteracji
    # steplength = 0.5  # should be set to a value between 0.0 and 1.0. inaczej rho
    # eps = 1.0E-04  # the criterion for halting the search for a minimum.




    def runButtonHandler(self):
        print('works')

        # collect values when we click
        txtFunc = self.txtFnc.get("1.0",'end-1c')
        txtX = float(self.txtX.get("1.0",'end-1c'))
        txtY = float(self.txtY.get("1.0",'end-1c'))
        OrthXptA = float(self.OrthXptA.get("1.0",'end-1c'))
        OrthXptB = float(self.OrthXptB.get("1.0",'end-1c'))
        OrthYptA = float(self.OrthYptA.get("1.0",'end-1c'))
        OrthYptB = float(self.OrthYptB.get("1.0",'end-1c'))
        txtTau = float(self.txtTau.get("1.0",'end-1c'))
        txtEps = Decimal(self.txtEps.get("1.0",'end-1c'))
        txtBeta = float(self.txtBeta.get("1.0",'end-1c'))
        txtAlpha = float(self.txtAlpha.get("1.0",'end-1c'))

        minXlbl = self.minXlabel
        minYlbl = self.minYlabel
        iterlbl = self.IterLabel

        print(txtX, type(txtX))
        print(txtY, type(txtY))
        print(txtEps, type(txtEps))
        print(txtFunc,type(txtFunc))

        #hooke(nvars, startpt, rho, eps, itermax, f):
        # Launch hooke
        it, endpt, points = hooke(2, [txtX, txtY], txtTau, txtEps, 1000, functionValue.functionValue)

        # Plot a graph
        pg.PlotGraph(endpt, points)

        # Save endpt - found minimum
        endpt_rounded = round(endpt, 2)
        print('Iterations = ', it, ' end pt : ', endpt_rounded)

        # Set the results to labels in GUI
        minXlbl['text'] = (endpt_rounded[0])
        minYlbl['text'] = (endpt_rounded[1])
        iterlbl['text'] = it

root = Tk()

#size of the window
root.geometry("500x400")

app = Window(root)

root.mainloop() 