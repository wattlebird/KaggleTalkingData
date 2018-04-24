FNR!=1 {
    key=$3"_"$6;
    if(key in lut) printf("%d\n", $9-lut[key]);
    else printf("705600\n");
    lut[key]=$9;
}
