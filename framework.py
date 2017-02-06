import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

mpl.style.use('ggplot')



class framework():


    def __init__(self):
        self.df = pd.DataFrame
        self.verbose = False
        self.debug = True

    def importDataFrame(self, df):
        if self.verbose:
            print('>>>> importDataFrame()')
        self.df = df


    def dataFrame(self):
        return self.df

    def setVerbose(self,v):
        self.verbose = v
    
    def getVerbose(self):
        if self.verbose:
            print('>>>> getVerbose()')
        return self.verbose

    def setDebug(self, db):
        self.debug = db

    def getHistDefinitions(self):

        if self.verbose:
            print('>>>> getHistDefinitions()')

        hist_json = open ('pandasAnalysisFramework/hist_definitions.json').read()

        data = json.loads(hist_json)

        self.hist_def = data



    def produceJsonHists(self):

        if self.verbose:
            print('>>>> produceJsonHists()')

        hist_map = {}

        #print(len(self.hist_def))

        fileName = 'test4.pdf'

        pp = PdfPages( fileName )

        if self.debug:
            print('::DEBUG::')
            print('length:')
            print(len(self.hist_def['hist']))
            print(':::::::::')

        if self.verbose == True:
            print(' >>> Creating Histograms From JSON')

        for i in range(0,len(self.hist_def['hist'])):
            hist_map[self.hist_def['hist'][i]['name']] = i

            dim    = self.hist_def['hist'][i]['dim']
            xvar   = self.hist_def['hist'][i]['xvar']
            
            title  = self.hist_def['hist'][i]['title']
            xlabel = self.hist_def['hist'][i]['xlabel']
            ylabel = self.hist_def['hist'][i]['ylabel']
            kind   = self.hist_def['hist'][i]['kind']

            plt.figure()
            if dim == '2D':
                yvar   = self.hist_def['hist'][i]['yvar']
                plt.scatter( self.df[xvar], self.df[yvar] )
            else:
                self.df[xvar].plot(kind = kind)
            
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.savefig(pp, format='pdf')

        pp.close()

        if self.verbose == True:
            print(' >>> Created File '+fileName)

        if self.debug:
            print('::DEBUG::')
            print(hist_map)
            print(':::::::::')

    def produceHistograms(self, file_name, hist_map):

        pp = PdfPages(file_name+'.pdf')

        for k, v in hist_map.iteritems():
            #print(k)
            plt.figure()
            self.df[v].plot()
            plt.savefig(pp, format='pdf')

        pp.close()
