
BASE=/home/ubuntu/Mytest/cobeats/scm/v0.2


#head  -10 $BASE/iofiles/resultado1_compare_b.txt
#cat log3.tmp|awk -F"-" '{print $3}'|awk -F" " '{print $1}'|awk 'BEGIN { FS= "[" ; OFS=SUBSEP="|"}{arr[$2]+=1 }END {for (i in arr) print i,arr[i]}' 
#cat log3.tmp|awk 'BEGIN { FS= ":" ; OFS=SUBSEP="|"}{arr[$1,$2,$3]+=$5 }END {for (i in arr) print i,arr[i]}'|sort 
#cat final.txt|awk -F"|" '{print $4" "$4" "$4}'> $BASE/iofiles/system_status_fifa.csv
head -20  $BASE/iofiles/resultado1_compare_b.txt|awk '
BEGIN {var=0; 
       print "INIT"}
       v1=0;
       v2=0;
{
 if (var==10) {
              print var"-----"v1" "v2; 
              var=0;
              v1=0;
              v2=0;
             
}
 else {var++;
       print var">>>> "$0}
       v1=v1+$1
       v2=v2+$2
}
END {print "The end"}
'


