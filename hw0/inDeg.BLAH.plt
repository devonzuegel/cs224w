#
# BLAH in degree. G(562, 1616). 100 (0.1779) nodes with in-deg > avg deg (5.8), 24 (0.0427) with >2*avg.deg (Wed Sep 30 14:30:23 2015)
#

set title "BLAH in degree. G(562, 1616). 100 (0.1779) nodes with in-deg > avg deg (5.8), 24 (0.0427) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png size 1000,800
set output 'inDeg.BLAH.png'
plot 	"inDeg.BLAH.tab" using 1:2 title "" with linespoints pt 6
