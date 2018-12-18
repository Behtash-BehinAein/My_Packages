class plot_fig():

    from matplotlib import pyplot as plt
    def __init__(self, x, y, labelx, labely):
        self.x = x
        self.y = y
        self.labelx = labelx
        self.labely = labely

    def render(self):
        
        self.plt.figure(figsize =(14,10) )
        self.plt.plot(self.x, self.y , '*--', markersize =16, linewidth =3, color = 'blue' )
        self.plt.xlabel = self.labelx
        self.plt.ylabel = self.labely
        self.plt.grid(True)

        return self.plt.show()


