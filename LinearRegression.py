# Joshua Arias

# module to visual linear regression

import tkinter

class Graph:
    def __init__(self):
        self._nodes = [] # will store all of the points clicked on the graph
        
        self._root_window = tkinter.Tk()
        
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = "#ffffff")
        
        self._canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        
        self._canvas.bind('<Button-1>', self._on_canvas_clicked) # allows the user to add points to graph
        
    def run(self) -> None:
        self._root_window.mainloop()
        
    def _on_canvas_clicked(self, event: tkinter.Event):
        ''' stores point clicked on graph
            if only point on graph stores it, otherwise calculates linear regression and graphs it'''
        click_point = (event.x, event.y)
        self._nodes.append(click_point)
        if len(self._nodes) > 1: # checks if enough points to calculate linear regression
            self._lin_reg = self._calc_regression()
            self._draw_regression()
        else:
            self._draw_spots()
        
    def _draw_spots(self):
        ''' this function will delete everything and redraw all the spots '''
        self._canvas.delete(tkinter.ALL)
        for coords in self._nodes:
            self._canvas.create_oval(
                coords[0] - 5, coords[1] - 5,
                coords[0] + 5, coords[1] + 5,
                fill = '#000000', outline = '#000000')
        
    def _calc_regression(self):
        x = [coord[0] for coord in self._nodes]
        y = [coord[1] for coord in self._nodes]
        xmean = sum(x) / len(self._nodes) # average value for x coordinate
        ymean = sum(y) / len(self._nodes) # average value for y coordinate
        rise = 0
        run = 0
        
        for node in self._nodes: # for every node stored in self._nodes
            (xnode,ynode) = node
            rise += (xnode-xmean) * (ynode-ymean) 
            # calculates average distance each node is from the mean 
            run += (xnode-xmean)**2
            # calculates the density of the nodes
            
        slope = rise / run
        intercept = ymean - slope * xmean
        
        return (slope,intercept)
    
    def _draw_regression(self):
        self._draw_spots() # this deletes the line so a new linear regression line can be drawn
            
        (slope, intercept) = self._lin_reg
        self._canvas.create_line(0,intercept, 
                                 600, intercept + 600*slope, 
                                 fill = "#000000")
        

if __name__ == "__main__":
    g = Graph()
    g.run()