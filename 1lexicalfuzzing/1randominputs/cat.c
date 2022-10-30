
#include<stdio.h>
 
int main(void)   //方法一
{
  int c;
  int inspace;	 //设置inspace标志位，检查是否在空格里
 
  inspace = 0;
 
  while((c = getchar()) != EOF)
  {
    if(c == ' ')
    {
      if(inspace == 0)
      {
        inspace = 1;  //下一次继续出现空格时，程序不输出任何值
        putchar(c);
      }
    }
 
    if(c != ' ')    
    {
      inspace = 0;	  //若接收的c不是空格时，将inspace置为0
      putchar(c);
    }
  }
 
  return 0;
}
