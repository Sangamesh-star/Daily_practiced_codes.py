//Assigning Variables:

/* In C, We want to declare the type of variable before assigning the value to it.
*/

//01.

#include<stdio.h>
int main()

{
    int weight_of_Ram = 50;
    printf("%d\n", weight_of_Ram);
    return 0;
}
  
//O/P: 50

/*  
Explanation: Here, 
• int weight_of_Ram is the variable with its type and 50 is the Value assigned to the variable. 
•int is the type of variable.
•%d is the specifier used to symbolise Int.
•\n is the operator use to get value in the next line
*/

//02.  

#include<stdio.h>
int main()
{
     char name[] = "Sangamesh MK😊";
     printf("%s\n", name);
     return 0;
}
                

//O/P: Sangamesh MK😊

//•%s is the specifier used to symbolise char array(string).

//03. 

//(a):

#include<stdio.h>
int main()
{
    char name[] = "Charles Babbage";
    printf(name);
    return 0;
}
        
//O/P: Charles Babbage


//(b): 

#include<stdio.h>
int main()

{
    char name[] = "Rakesh sharma\n";
    printf(name);
    printf("%s\n", name);
    return 0;
    
}

/*
O/P: Rakesh sharma
         Rakesh sharma
*/    

     

//★. We can reassign the values for the same variable multiple times

#include<stdio.h>
int main()

{
    int x = 25;
    printf("%d\n", x);
    
    x = 50;
    printf("%d\n", x);
    return 0;
}

/*
O/P: 25
         50
*/         
