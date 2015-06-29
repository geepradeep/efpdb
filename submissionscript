#!/bin/bash

set INPFILE=$argv[1]

touch /var/www/html/gamess/$INPFILE.script

echo '#~/bin/bash' >> /var/www/html/gamess/$INPFILE.script

echo '#PBS -V'
echo '#PBS -q batch'
echo '#PBS -l nodes=1:ppn=16'
echo '#PBS -l walltime=70:00:00'
echo "#PBS -r n" >> /var/www/html/gamess/$INPFILE.script
echo "#PBS -j oe" >> /var/www/html/gamess/$INPFILE.script
echo "#PBS -o $INPFILE.stdout" >> /var/www/html/gamess/$INPFILE.script
echo "#PBS -q batch" >> /var/www/html/gamess/$INPFILE.script
echo chdir `pwd` >> /var/www/html/gamess/$INPFILE.script

echo "/software/gamess/rungms $INPFILE 00 1 >& $INPFILE.log" >> ~/scr/$JOB.script

echo "Submitting GAMESS job $INPFILE ..."

qsub /var/www/html/gamess/$INPFILE.script
