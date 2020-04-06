
#include <iostream.h>
#include <string.h>
int main()
{
	char str[100];
	char ch; 
	int Lindex,Findex; 
	cin>>str;
	cin>>ch;
	Lindex = getLIndex(str,ch);
	Findex= getFIndex(str,ch);
	if(Lindex!=(-1))
		cout<<Findex<<endl<<Lindex;
	else
		cout<<"NOT FOUND"<<endl;
	return 0;
}
int getLIndex(char string,char  c)
{
	int size = len(string),i=0;
	while(i<size)
	{
		
		if(string[i]=c){
		    return i;
		   break;
		}	
		i++; 
	}
	
}
int getFindex(string, c)
{
	int size = len(string);
	int i=size; 
	while( i>=0);
{		
		if(string[i]==c){
		    return i;
 break;
		}	
	i--;
}
		
}
SAMPLE INPUT-1
	Kerala
a
SAMPLE OUTPUT:1
3
5
SAMPLE INPUT-2
MALAYALaM
A

SAMPLE OUTPUT:2
1
5  
