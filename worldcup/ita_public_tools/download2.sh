
BASE=/home/ubuntu/Mytest/cobeats/scm/v0.2


head  -10 final.txt
echo "======="
#cat log3.tmp|awk -F"-" '{print $3}'|awk -F" " '{print $1}'|awk 'BEGIN { FS= "[" ; OFS=SUBSEP="|"}{arr[$2]+=1 }END {for (i in arr) print i,arr[i]}' 
#cat log3.tmp|awk 'BEGIN { FS= ":" ; OFS=SUBSEP="|"}{arr[$1,$2,$3]+=$5 }END {for (i in arr) print i,arr[i]}'|sort 
#cat final.txt|awk -F"|" '{print $4" "$4" "$4}'> /home/ubuntu/Mytest/cobeats/scm/v0.2/iofiles/system_status_fifa.csv

#cat final.txt|awk 'BEGIN { FS= "|" ; OFS=SUBSEP="|"}{arr[$1,$2,substr($3,1,1)]+=$4 }END {for (i in arr) print i,arr[i]}'|sort|awk -F"|" '{print $4" "$4" "$4}'> /home/ubuntu/Mytest/cobeats/scm/v0.2/iofiles/system_status_fifa_corto.csv

cat final.txt|sort|awk 'BEGIN { FS= "|" ; OFS=SUBSEP="|"}{arr[$1,$2,substr($3,1,1)]+=$4 }END {for (i in arr) print i,arr[i]}'|sort|awk -F"|" '{print $0}'|sort|awk -F"|"  '{print $4" "$4" "$4}' > $BASE/iofiles/system_status_fifa_corto.csv

head -100  $BASE/iofiles/system_status_fifa_corto.csv
wc -l  $BASE/iofiles/system_status_fifa_corto.csv
