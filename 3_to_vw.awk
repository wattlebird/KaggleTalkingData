NR != 1 {
    if($1 == 0) {
        printf("-1 |ip %d |app %d |device %d |os %d |channel %d |hour %d \
|frequency ia:%.4f iao:%.4f iaod:%.4f ic:%.4f ih:%.4f ado:%.4f cdo:%.4f ch:%.4f doh:%.4f do:%.4f \
|uniq i_h:%.4f ido_a:%.4f i_a:%.4f i_c:%.4f i_d:%.4f a_c:%.4f doa_h:%.4f doc_h:%.4f do_h:%.4f doa_i:%.4f do_i:%.4f doc_i:%.4f\
|varh iac:%.4f iao:%.4f idc:%.4f doc:%.4f doa:%.4f do:%.4f \
|meanh iac:%.4f \
|prev i:%.4f ic:%.4f ia:%.4f c:%.4f ac:%.4f overall:%.4f adoc:%.4f ado:%.4f cdo:%.4f do:%.4f \
|next i:%.4f ic:%.4f ia:%.4f c:%.4f ac:%.4f overall:%.4f adoc:%.4f ado:%.4f cdo:%.4f do:%.4f \
|sumcum i_o:%.4f ido_a:%.4f\n",
                   $2, $3, $4, $5, $6, $7,
                   log($9+1), log($10+1), log($11+1), log($12+1), log($13+1), log($24+1), log($25+1), log($26+1), log($27+1), log($28+1),
                   log($14+1), log($15+1), log($16+1), log($17+1), log($18+1), log($19+1), log($29+1), log($30+1), log($31+1), log($32+1), log($33+1), log($34+1),
                   $20, $21, $22, $35, $36, $37,
                   $23,
                   log($38+1), log($39+1), log($40+1), log($41+1), log($43+1), log($44+1), log($45+1), log($46+1), log($47+1), log($48+1), 
                   log($49+1), log($50+1), log($51+1), log($52+1), log($54+1), log($55+1), log($56+1), log($57+1), log($58+1), log($59+1), 
                   log($60+1), log($61+1))
    } else { # or one can repeat positive examples
        printf("1 |ip %d |app %d |device %d |os %d |channel %d |hour %d \
|frequency ia:%.4f iao:%.4f iaod:%.4f ic:%.4f ih:%.4f ado:%.4f cdo:%.4f ch:%.4f doh:%.4f do:%.4f \
|uniq i_h:%.4f ido_a:%.4f i_a:%.4f i_c:%.4f i_d:%.4f a_c:%.4f doa_h:%.4f doc_h:%.4f do_h:%.4f doa_i:%.4f do_i:%.4f doc_i:%.4f\
|varh iac:%.4f iao:%.4f idc:%.4f doc:%.4f doa:%.4f do:%.4f \
|meanh iac:%.4f \
|prev i:%.4f ic:%.4f ia:%.4f c:%.4f ac:%.4f overall:%.4f adoc:%.4f ado:%.4f cdo:%.4f do:%.4f \
|next i:%.4f ic:%.4f ia:%.4f c:%.4f ac:%.4f overall:%.4f adoc:%.4f ado:%.4f cdo:%.4f do:%.4f \
|sumcum i_o:%.4f ido_a:%.4f\n",
                   $2, $3, $4, $5, $6, $7,
                   log($9+1), log($10+1), log($11+1), log($12+1), log($13+1), log($24+1), log($25+1), log($26+1), log($27+1), log($28+1),
                   log($14+1), log($15+1), log($16+1), log($17+1), log($18+1), log($19+1), log($29+1), log($30+1), log($31+1), log($32+1), log($33+1), log($34+1),
                   $20, $21, $22, $35, $36, $37,
                   $23,
                   log($38+1), log($39+1), log($40+1), log($41+1), log($43+1), log($44+1), log($45+1), log($46+1), log($47+1), log($48+1), 
                   log($49+1), log($50+1), log($51+1), log($52+1), log($54+1), log($55+1), log($56+1), log($57+1), log($58+1), log($59+1), 
                   log($60+1), log($61+1))
    }
}