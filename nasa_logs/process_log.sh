
FICH=nasa_log.csv
head -10 nasa_log.tsv
echo "=========="
cat nasa_log.tsv|awk -F" " '{var=int($3/600); print var" "1}'|sort|awk 'BEGIN { FS= " " ; OFS=SUBSEP="|"}{arr[$1]+=$2 }END {for (i in arr) print i,arr[i]}'|sort |awk -F"|" '{print $2" "$2" "$2}'>$FICH
wc -l $FICH
head -10 $FICH

