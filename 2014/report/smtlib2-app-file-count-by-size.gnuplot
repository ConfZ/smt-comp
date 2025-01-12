# metrics on SMT-LIB2 2014-06-03
# file size in bytes
# geq-lt quantity
set terminal pngcairo size 800, 600 enhanced font 'Verdana,16'
set output 'smtlib2-app-file-count-by-size.png'
set termoption enhanced
set title "Number of benchmarks by file size (in bytes)."
set xrange [1:10]
set xtics ("" 1, "[10^2,10^3[" 2, "[10^3,10^4[" 3, "[10^4,10^5[" 4, "[10^5,10^6[" 5, "[10^6,10^7[" 6, "[10^7,10^8[" 7, "[10^8,10^9[" 8, "[10^9,10^{10}[" 9, "" 10) rotate by 45 right
set yrange [0.1:100000]
set logscale y
set ytics ("1" 1, "10" 10, "100" 100, "1000" 1000, "10000" 10000, "100000" 100000)
set boxwidth 0.25
set style fill solid 1.00 noborder
set xlabel "File size (in bytes)."
plot "smtlib2-app-file-count-by-size.dat" w boxes lc rgb "#CCCCCC" t 'Number of benchmarks'
