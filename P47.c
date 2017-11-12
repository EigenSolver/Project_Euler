#include <stdio.h>

int eratosthenes(int start=2, int end)
{
    if(end<=2)
    {
        printf('Error!')
        return NULL;
    }
    int primes*;
    primes=malloc(end*sizeof(int));

    primes[0]=0;
    primes[1]=0;
    for(int j=2;j<end;j++)
    {
        primes[j]=1;
    }
    
    for(int i=0;i<end;i++)
    {
        if(!primes[i])
        {
            continue;
        }
        else
        {
            int j=i*i;
            while(j<end)
            {
                primes[j]=0;
                j=j+i;
            }
        }
    }
    for(int i=0;i<end;i++)
    {
        if(primes[i])
        {
            printf("%d",i);
        }
    }
    free(primes);
    return 0;
}

int main()
{
    eratosthenes(2000);
    return 0;
}
