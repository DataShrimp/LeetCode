#include<stdio.h>

char* reverse(char* str) {
	int i = 0;
	for (; str[i]!='\0'; i++)
		;
	char* nstr = new char[i];
	int j=0;
	printf("%d", i);
	i--;
	for (; i>=0; i--, j++)
		nstr[j] = str[i];
	nstr[j] = '\0';
	return nstr;
}

int main(int argc, char** argv) {
	char* s = "abc\0";
	char* r = reverse(s);
	printf("Hello: %s\n", r);
}