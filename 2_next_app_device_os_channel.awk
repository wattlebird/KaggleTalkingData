{
    key=$3"_"$4"_"$5"_"$6;
    if(key in lut) printf("%d\n", lut[key]-$9);
    else printf("705600\n");
    lut[key]=$9;
}
