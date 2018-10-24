%{
int num_letter=0,num_digit=0,num_chars=0;
%}
digit    [0-9]
number    {digit}+
letter    [A-Za-z]
%%
"201692126" {printf("%s","徐诗瑶");num_digit+=9;++num_chars;}
{number} {++num_digit;++num_chars;printf("%s",yytext);}
{letter} {printf("%s",yytext);++num_letter;++num_chars;}
. {++num_chars;printf("%s",yytext);}
%%
int yywrap(){
        return 1;
}
void main(){
        yylex();
        printf("# of letters: %d, # of digits: %d, # of chars: %d",num_letter,num_digit,num_chars);
}