#!/bin/bash

data=$1
start=$2
end=$3
bodies=$4

[ -z "$start" ] && start=0
[ -z "$end" ] && end=0
[ -z "$bodies" ] && bodies=`head -n 1000 $data | awk '{ print $2 }' | sort -u`

rm -f plot-out.*

awk -v st=$start -v et=$end '{ if (et == 0 || ($1 > st && $1 < et)) {print >> ("plot-out."$2); close("plot-out."$2) } }' $data

cat << 'EOF' > orb.gpl
set term pdf
set output 'orbits.pdf'

set linetype  1 lc rgb "#F0A3FF" lw 1
set linetype  2 lc rgb "#0075DC" lw 1
set linetype  3 lc rgb "#993F00" lw 1
set linetype  4 lc rgb "#4C005C" lw 1
set linetype  5 lc rgb "#191919" lw 1
set linetype  6 lc rgb "#005C31" lw 1
set linetype  7 lc rgb "#2BCE48" lw 1
set linetype  8 lc rgb "#FFCC99"   lw 1
set linetype  9 lc rgb "#808080"  lw 1
set linetype  10 lc rgb "#94FFB5"  lw 1
set linetype  11 lc rgb "#8F7C00"  lw 1
set linetype  12 lc rgb "#9DCC00"  lw 1
set linetype  13 lc rgb "#C20088"  lw 1
set linetype  14 lc rgb "#003380"  lw 1
set linetype  15 lc rgb "#FFA405"  lw 1
set linetype  16 lc rgb "#FFA8BB"  lw 1
set linetype  17 lc rgb "#426600"  lw 1
set linetype  18 lc rgb "#FF0010"  lw 1
set linetype  19 lc rgb "#5EF1F2"  lw 1
set linetype  20 lc rgb "#00998F"  lw 1
set linetype  21 lc rgb "#E0FF66"  lw 1
set linetype  22 lc rgb "#740AFF"  lw 1
set linetype  23 lc rgb "#990000"  lw 1
set linetype  24 lc rgb "#FFFF80"  lw 1
set linetype  25 lc rgb "#FF5005"  lw 1
set linetype cycle  25
	
splot \
EOF

for b in `echo $bodies`; do
	echo '"plot-out.'$b'" u 3:4:5 with lines title "'$b'",\' >> orb.gpl
done

gnuplot orb.gpl
rm -f plot-out.*
rm -f orb.gpl
