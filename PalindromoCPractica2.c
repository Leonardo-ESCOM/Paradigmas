#include<stdio.h>
#include<stdlib.h> 

//Escribir una función para detectar si una palabra es un palídormo 
char palabra[30];


int espalindromo(char *palindromo, int contar);

int espalindromo(char *palindromo, int contar){
	//char temp = palindromo;
	int i=0;

	while (palindromo[i] == palindromo[contar - 1 - i] && contar/2 > i){
		i++;
	}
	if (i == contar/2 ){
		return 1;
	}
	else{
		return 0;
	}

}


int main(){

	printf("Introduzca una palabra: ");
	scanf("%s", palabra);
	int contar=0;
	for (int i = 0; palabra[i] != '\0'; i++)
	{
		contar++;
	}
	if(espalindromo(palabra,contar)){
		printf("La palabra ingresada %s es un palíndromo", palabra);
	}
	else{
		printf("La palabra ingresada %s no es un palíndromo", palabra);
	}

	return 0;
}