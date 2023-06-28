#include <stdio.h>

int is_digit_or_minus(char c)
{
    return (c >= '0' && c <= '9') || c == '-';
}

const char* get_double_str(const char* line)
{
    while(!is_digit_or_minus(*line) && *line != '\0')
    {
        line++;
    }
    return line;
}

double my_atof(const char *str)
{   
    // First figure out the sign
    int sign = 1;
    if(*str == '-'){
        sign = -1;
        str++;
    }

    // str is now a string that starts with a digit
    double integer_part = 0;
    while(is_digit_or_minus(*str)){
        integer_part = 10*integer_part + (*str - '0');
        str++;
    }

    // Now we potentially have a fractional part
    // Assume there is always a decimal point
    str++; // Skip the decimal point

    double fractional_part = 0;
    double cur_pow10 = 0.1;
    while(*str != '\0' && *str != '\n'){
        fractional_part += (*str - '0') * cur_pow10;
        cur_pow10 *= 0.1;
        str++;
    }

    return sign * (integer_part + fractional_part);
}

void print_sum_of_constants(const char *filename)
{
    FILE *fp = fopen(filename, "r");
    if(fp == NULL){
        printf("Error opening file %s\n", filename);
        return;
    }

    double sum = 0;
    char line[100]; // Assume no line is longer than 100 characters
    while(fgets(line, 100, fp) != NULL){
        const char *double_str = get_double_str(line);
        sum += my_atof(double_str);
    }
    
    printf("Sum of constants in %s is %f\n", filename, sum);
}

int main()
{
    printf("------------------\nTESTING is_digit()\n------------------\n");
    for(int c = '0'; c <= '9'; c++)
    {
        printf("%c is digit: %d. Another way to compute the value: %d\n", c, (int)c, c-'0');
    }
    printf("Is 'a' a digit? %d\n", is_digit_or_minus('a'));
    printf("Is '0' a digit? %d\n", is_digit_or_minus('0'));
    printf("Is '9' a digit? %d\n", is_digit_or_minus('9'));
    printf("Is ' ' a digit? %d\n", is_digit_or_minus(' '));
    printf("Is '4' a digit? %d\n", is_digit_or_minus('4'));
    printf("Is '4' a digit? %d\n", is_digit_or_minus('-'));


    printf("------------------\nTESTING get_double_str()\n------------------\n");
    printf("%s\n", get_double_str("pi = 3.14"));
    printf("%s\n", get_double_str("G = 0.0000000000667"));
    printf("%s\n", get_double_str("e = 2.728"));
    printf("%s\n", get_double_str("a = -3.1"));

    printf("------------------\nTESTING my_atof()\n------------------\n");
    printf("%f\n", my_atof("3.14"));
    printf("%f\n", my_atof("-5."));

    printf("------------------\nTESTING print_sum_of_constants()\n------------------\n");
    print_sum_of_constants("data.txt");
}