#include <stdio.h>

int main() {

    int t;

    scanf("%d",&t);

    for(int i=0;i<t;i++){

        int a,b;

	    scanf("%d %d",&a,&b);

	    if(a+b<3){

	        printf("1\n");

	    }else if(a+b<=10){

	        printf("2\n");

	    }else if(a+b<=60){

	        printf("3\n");

	    }else{

	        printf("4\n");

	    }

    }

	return 0;

}

