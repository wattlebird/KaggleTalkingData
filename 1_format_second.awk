BEGIN {
    FS="[ ,:-]"
}
NR == 1 {printf("%s,%s,%s,%s,%s,%s,%s,%s,second\n", $1, $2, $3, $4, $5, $6, $7, $8)}
NR != 1 {
    printf("%d,%d,%d,%d,%d,%d,%d,%d,%d\n", $1, $2, $3, $4, $5, $6, $7, $8, 86400*$11+3600*$12+60*$13+$14)
}
