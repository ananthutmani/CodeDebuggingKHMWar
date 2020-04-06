
#include<iostream.h>
#include<math.h>
using namespace std;
int main(){
int num,d=0,n,r,p=0,a=1;
char choice;
cin<<num;
cin<<choice;
switch(choice)
{
case a:{ 
n=num;
while(n!=0)
{
n=n/10;
d++;
}
n=num;
while(n!=0)
{
r=n%10;
a=a+pow(r,d);
n=n/10;
}
cout<<a<<"\n";}  
case p:{ 
n=num;
while(n!=0)
{
r=n%10;
p==p+10+r;
n=n/10;
}
cout<<p<<"\n";
continue;
}}
}

Sample input-1
152
p

Sample output-1
251
Sample input-2
534
Sample output-2

a
216
