#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char line[1024] = {0};
    u_int8_t ucLlmnrResponse[1024] = {};
    int size = 0;

    // get a string of hex numbers from stdin, like this "0x1 0x2 0x3"
    // and store it in line
    printf("Enter a string of hex numbers: ");
    fgets(line, 1024, stdin);
    //split the line with spaces
    char *token = strtok(line, ", ");
    //loop through the tokens
    while (token != NULL)
    {
        //convert the token to a number, 0x8c to 140
        u_int8_t ucNumber = (u_int8_t)strtol(token, NULL, 16);
        printf("Number: 0x%x\n", ucNumber);
        //add the number to the array
        // printf("size of ucLlmnrResponse: %ld\n", sizeof(ucLlmnrResponse));
        ucLlmnrResponse[size] = ucNumber;
        size++;
        //get the next token
        token = strtok(NULL, ", ");
    }
    // print the array
    u_int8_t *ucLlmnrResponse_byte;
    ucLlmnrResponse_byte = malloc(size*sizeof(u_int8_t));
    memcpy(ucLlmnrResponse_byte, ucLlmnrResponse, size);
    for (int i = 0; i < size; i++)
    {
        // ucLlmnrResponse_byte[i] = ucLlmnrResponse[i];
        printf("0x%x ", ucLlmnrResponse_byte[i]);
    }

    return 0;
}

/* input data
0x9c, 0x3d, 0x01, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x62, 0x61, 0x69, 0x64, 0x75, 0x61, 0x63, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x00
*/