BEGIN {
    FS="[ ,:-]"
}
NR == 1 {printf("%s,%s,%s,%s,%s,%s,hour,day,second\n", $1, $2, $3, $4, $5, $6)}
NR != 1 {
    printf("%d,%d,%d,%d,%d,%d,%d,%d,%d\n", $1, $2, $3, $4, $5, $6, $10, $9, 86400*$9+3600*$10+60*$11+$12)
}
