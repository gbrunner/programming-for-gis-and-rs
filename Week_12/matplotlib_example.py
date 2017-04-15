import xlrd

file_and_path = r"C:\Users\greg6750\Documents\IPython Notebooks\Python_for_GIS_and_RS\Week_12\SENZA_0_SUNAA_0_CORN.xlsx"

print("Reading Workbook")
workbook = xlrd.open_workbook(file_and_path)
worksheet = workbook.sheet_by_index(0)

freq = []
g = []
t = []
print("Creating Arrays")
for row in range(worksheet.nrows):
    if row>0:
        #Frequency
        freq_cell = worksheet.cell(row,0)
        freq.append(freq_cell.value)

        GRR_cell = worksheet.cell(row,8)
        g.append(GRR_cell.value)

        TOA_cell = worksheet.cell(row,14)
        t.append(TOA_cell.value)


#For plotting, import matplotlib
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt


##Basic single plot
#plt.plot(freq, g)
#plt.show()


####Multiple plots
##plt.subplot(211)
###plt.figure(1)
##plt.plot(freq, g, 'b-o')
##plt.subplot(2, 1, 2)
##plt.plot(freq, t, 'r-o')
##plt.show()

##Typing numpy and matplotlib together
import numpy as np
gaussian = np.random.normal(0, 1, 100000)
plt.hist(gaussian, bins=100)
#print "Mean: %f Standard Deviation: %f" % (gaussian.mean(), gaussian.std())
plt.show()