//#include <stdio.h>
//int main()
//{
//	int a,b;
//	a=20;
//	b=5;
//	
//	a+=b;
//	printf("a=%d\n",a);
//	a*=b;
//	printf("a=%d\n",a);
//	a-=b;
//	printf("a=%d\n",a);
//	a/=b;
//	printf("a=%d\n",a);
//	a%=b;
//	printf("a=%d\n",a);
//}

//#include <stdio.h>
//int main()
//{
//	int a=10;
//	
//	a++;
//	a++;
//	printf("a=%d\n",a);
//	++a;
//	++a;
//	printf("a=%d\n",a);
//}

//#include <stdio.h>
//int main()
//{
//	int a=10;
//	int b=2;
//	
//	a-=b;
//	printf("a=%d\n",a);
//	a*=b;
//	printf("a=%d\n",a);
//	a--;
//	printf("a=%d\n",a);
//	a%=b;
//	printf("a=%d\n",a);
//	a+=b;
//	printf("a=%d\n",a);
//	a++;
//	printf("a=%d\n",a);
//	a-=b;
//	printf("a=%d\n",a);
//}

//#include <stdio.h>
//int main()
//{
//	int a,b;
//	a=10;
//	b=a++;
//	printf("a=%d b=%d\n",a,b);
//	b=++a;
//	printf("a=%d b=%d\n",a,b);
//	
//	a=20;
//	b=a--;
//	printf("a=%d b=%d\n",a,b);
//	b=--a;
//	printf("a=%d b=%d\n",a,b);
//}

#include <stdio.h>
int main()
{
	int n=0;
	printf("%d\n",n);
	printf("%d\n",n+=3);
	printf("%d\n",n*=0);
	printf("%d\n",n+=5);
	printf("%d\n",n++);
	printf("%d\n",++n);
	printf("%d\n",n%5);
	printf("%d\n",--n);
	printf("%d\n",n--);
	printf("%d\n",n);
}
