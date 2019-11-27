set -x
for i in *
do
if [ -d $i ]; then
   cd $i
   k=1
   for j in *
   do
        mv -f $j $i$k.jpg
        let k=k+1
   done
cd ..
fi

done
