**C++学习笔记**

C面向过程

C++面向对象

一.入门

1.封装

封装意味着把对象的属性和方法结合成一个独立的系统单位，并尽可能隐藏对象的内部细节。

2.抽象

抽象的过程是对具体问题进行概况的过程，是对一类公共问题进行统一描述的过程。

3.继承

子类对象拥有与其基类相同的全部属性和方法，成为继承。

4.多态

多态是指在基类中定义的属性和行为被子类继承后，可以具有不同的数据类型或者表现行为等特性。

二.程序（1）：对一个整型数组求和。

C语言

```c
#include<stdio.h>
int addArray(int array[],int n);
int main()
{
    int data[]={0,1,2,3,4,5,6,7,8,9};
    int size = sizeof(data)/sizeof(data[0]);//sizeof是计算某个对象的占的内存（多少字节）
    printf("结果是：%d\n",addArray(data,size));
    return 0;
}
int addArray(int array[],int n)
{
    int sum = 0;
    int i;
   	for(i=0;i<n;i++)
    {
        sum+=array[i];
    }
    return sum;
}
```

C++

```c++
#include<iostream>//ostream
using namespace std;
int addArray(int *array,int n);
int main()
{
    int data[]={0,1,2,3,4,5,6,7,8,9};
    int size = sizeof(data)/sizeof(data[0]);
    cout<<"结果是："<<addArray(data,size)<<endl;
    return 0;
}
int addArray(int *array,int n)
{
    int sum=0;
    int i;
    for (i=0;i<n;i++)
    {
        sum+=*array++;
    }
    return sum;
}
```

cout是输出流对象，它是“console out (控制台输出)的缩写。是属于basic_ostream类的对象。ostream类在iostream头文件中定义。

输出流：时时刻刻接收，时时刻刻输出

using namesapce std;命名空间

C++标准库所使用的所有标识符（即类、函数、对象等的名称）都是在同一个特殊的名字空间（std）中来定义的。

支持重载

重载事实上就是允许我们按照不同的方式使用同一个操作符。

三.程序（2）：相加任意整数和空格

C语言

```c
#include<stdio.h>
#include<stdlib.h>
int main() 
{
	int i;
	int sum = 0;
	char ch;
	printf("请输入一串整数和任意数目的空格：");
	while (scanf("%d", &i) == 1) 
	{
		sum += i;
		while ((ch = getchar()) == ' ');//屏蔽空格
			if (ch == '\n') 
			{
				break;
			}
			ungetc(ch, stdin);//将变量ch中存放的字符退回给stdin输入流
		
	}
	printf("结果是：%d", sum);
	printf("\n");
    system("pause");
	return 0;
}
```

C++

```c++
#include<iostream>
using namespace std;
int main()
{
    int sum = 0;
    cout << "请输入一串整数和任意数目的空格：";
    int i;
    while(cin>>i)
    {
        sum+=i;
        while(cin.peek()==' ')
        {
            cin.get();
        }
        if (cin.peek()=='\n')
        {
            break;
        }
    }
    cout <<"结果是："<<sum<<endl;
    return 0;
}
```

输入流对象cin：对象的类型是istream从终端读取数据

cin>>i；cin输入操作符又称提取操作符，它一次从输入流对象cin提取一个整数。

cin对象

cin.ignore()&cin.getline()

cin.get()&cin.peek()

cin.gcount()&cin.read()

cout对象

cout.precision()

cout.width()

四.程序（3）：文件I/O

C语言

```c
#include<stdio.h>
#include<stdlib.h>
int main(int argc,char* argv[])//程序参数，包含本身
    //argv[]的每个指针指向命令行的一个字符串
{
    FILE *in,*out;
    int ch;
    if (argc != 3)
    {
        fprintf(stderr,"输入形式：copyFile 源文件名 目标文件名 \n");
        exit(EXIT_FAILURE);
    }
    if ((in = fopen(argv[1],"rb"))==NULL)
    {
        fprintf(stderr,"打不开文件：%s\n",argv[1]);
        exit(EXIT_FAILURE);
    }
    if ((out=fopen(argv[2],"wb"))==NULL)
    {
        fprintf(stderr,"打不开文件：%s\n",argv[2]);
        fclose(in);
        exit(EXIT_FAILURE);
    }
    while((ch=getc(in)) != EOF)
    {
        if(putc(ch,out)==EOF)
        {
            break;
        }
   	if(ferror(in))
    {
        printf("读取文件%s失败!\n",argv[1]);
    }
    if(ferror(out))
    {
        printf("写入文件%s失败!\n",argv[2]);
    }
   	printf("成功复制1个文件!\n");
    }
}//getc()的返回值是int类型，所以我们声明时应该是int ch。而不是char ch.
```

C++

```c++
#include<fstream>
#include<iostream>
using namespace std;
int main()
{
    ifstream in;
    in.open("test.txt");
    if (!in)
    {
        cerr<<"打开文件失败"<<endl;
        return 0;
    }
    char x;
    while(in>>x)
    {
        cout << x;
	}
    cout << x;
    cout << endl;
    in.close();
    return 0;
}
```

ifstream in(char* filename,int open_mode)

outstream out(char*filename,int open_mode)

ios::in --打开一个可读取文件

ios::out --打开一个可写入文件

ios::binary--以二进制的形式打开一个文件

ios::app--写入的所有数据将被追加到文件的末尾

ios::trunk--删除文件原来已存在的内容

ios::nocreate--如果要打开的文件并不存在，那么以此参数调用open函数将无法进行

ios::noreplece--如果要打开的文件已存在，试图用open函数打开时将返回一个错误

ios::beg使得文件指针指向文件头

ios::end则是文件尾

五.输入和输出小结

```c++
#include<iostream>
int main()
{
    char answer;
    std::cout<<"请问可以格式化您的硬盘吗？【Y/N】"<<"\n";
    std::cin >> answer;
    switch(answer)
    {
       	case'Y':
       	case'y':
            std::cout <<"随便格式化硬盘是不好的"<<"\n";
        	break;
       	case'N':
       	case'n':
            std::cout<<"您的选择是明智的";
            break;
        default:
            std::cout<<"您的输入不符合要求"<<"\n";
    }
    std::cin.ignore(100,'\n')
    std::cout<<"输入任何字符结束程序"<<"\n"
    stc::cin.get();
	return 0;
}
```

```c++
#include<iostream>
int main()
{
    const unsigned short ADD_SUBTRACT =32;
    const double RATID =9.0/5.0;
    double tempIn,tempOut;
    char typeIn ,typeOut;
    std::cout << "请亲们以【xx.x C】或者【xx.c F】格式输入一个温度:"；
   	std::cin >>tempIn>>typeIn;
    std::cin.ignore(100,'\n');
    std::cout << "\n";
    switch(typeIn)
    {
      	case'C':
        case'c':
            tempOut=tempIn*RATIO+ADD_SUBTRACT;
            TypeOut='F';
            typeIn ='C';
            break;
      	case'F':
       	case'f':
            tempOut=(tempIn-ADD_SUBTRACT)/RATIO;
            TypeOut='C';
            TypeIn='F';
        default:
            typeOut='E';
            break;
    }
    if(typeOut !='E')
    {
        std::cout << tempIn <<typeIn
            << "="<<tempOut 
            <<typeOut <<"\n\n";
    }
    else
    {
        std::cout <<"输入错误！"<<"\n\n";
    }
    std::cout <<"请输入任何字符结束程序"<<"\n\n"
    return 0;
}
```

cin对象有几个专门用来报告其互作情况的成员函数，他们将返回一个真/假值来表明cin的状态。

-eof()：如果到达文件(或输入)末尾返回true；

-fail():如果cin无法互作，返回true；

-bad()：如果cin因为比较严重的原因（例如内存不足而无法互作,返回ture；

-good()：如果以上情况都没发生,返回ture；

六.函数的重载

```c++
#include<iostream>
void convertTemperature(double tempIn,char typeIn);
int main()
{
    const unsigned short ADD_SUBTRACT =32;
    const double RATID =9.0/5.0;
    double tempIn;
    char typeIn;
    std::cout << "请亲们以【xx.x C】或者【xx.c F】格式输入一个温度:"；
   	std::cin >>tempIn>>typeIn;
    std::cin.ignore(100,'\n');
    std::cout << "\n";
    convertTemperature(tempIn,typeIn);
    return 0;
}
void convertTemperature(double tempIn,char typeIn)
{
	const unsigned short ADD_SUBTRACT =32;
    const double RATID =9.0/5.0;
    float tempOut;
    char typeOut;
	switch(typeIn)
    {
      	case'C':
        case'c':
            tempOut=tempIn*RATIO+ADD_SUBTRACT;
            TypeOut='F';
            typeIn ='C';
            break;
      	case'F':
       	case'f':
            tempOut=(tempIn-ADD_SUBTRACT)/RATIO;
            TypeOut='C';
            TypeIn='F';
        default:
            typeOut='E';
            break;
    }
    if(typeOut !='E')
    {
        std::cout << tempIn <<typeIn
            << "="<<tempOut 
            <<typeOut <<"\n\n";
    }
    else
    {
        std::cout <<"输入错误！"<<"\n\n";
    }
    std::cout <<"请输入任何字符结束程序"<<"\n\n"
}
```

重载

```c++
#include<iostream>
void convertTemperature(int tempIn,char typeIn);
int main()
{
    const unsigned short ADD_SUBTRACT =32;
    const double RATID =9.0/5.0;
    double tempIn;
    char typeIn;
    std::cout << "请亲们以【xx.x C】或者【xx.c F】格式输入一个温度:"；
   	std::cin >>tempInInt>>typeIn;
    std::cin.ignore(100,'\n');
    std::cout << "\n";
    convertTemperature(tempInInt,typeIn);
    return 0;
}
void convertTemperature(double tempInInt,char typeIn)
{
	const unsigned short ADD_SUBTRACT =32;
    const double RATID =9.0/5.0;
    int tempOut;
    char typeOut;
	switch(typeIn)
    {
      	case'C':
        case'c':
            tempOut=tempIn*RATIO+ADD_SUBTRACT;
            TypeOut='F';
            typeIn ='C';
            break;
      	case'F':
       	case'f':
            tempOut=(tempIn-ADD_SUBTRACT)/RATIO;
            TypeOut='C';
            TypeIn='F';
        default:
            typeOut='E';
            break;
    }
    if(typeOut !='E')
    {
        std::cout << tempIn <<typeIn
            << "="<<tempOut 
            <<typeOut <<"\n\n";
    }
    else
    {
        std::cout <<"输入错误！"<<"\n\n";
    }
    std::cout <<"请输入任何字符结束程序"<<"\n\n"
}
```

七.复杂的数据类型1数组

数组

优点在于，一个数组可以把许多个同类型的值存储载同一个变量名下。

回顾一下，数组仍需要被声明为某一种特定的类型float,char,int

type name[x];

```c++
#include<iostream>
#define ITEM 10
int main()
{	
    int num[ITEM];
    std::cout << "请输入<<ITEM<<个整型数据\n\n";
    for (int i=0;i<ITEM;i++)
    {
        std::cout << "请输入第"<<i+1<< "个数据:";
        while(!(std::cin >> num[i];))
        {	
            std::cin.clear();
            std::cin.ignore(100,'\n');
            std::count << "请输入一个合法的值";
        }
    }
    int total = 0;
    for (int j=0;j<10;j++)
    {
        total+=num[j];
    }
    std::cout << "总和是:"<<total;
    std::cout <<"平均值是"<<(float)total/ITEM;
    std::cout <<'\n';
    return 0;
}
```

```c++
#include<iostream>
#include<string>
int main()
{
    std::string str;
    std::cout << "请随便输入一个字符串：";
    std::getline(std::cin,str)
    std::cout<<str;
    return 0;
}
```

C++的std::string类型其实是在C++标准库定义的一个对象，其内建功能非常之多

-提取子字符串

-比较字符串

-添加字符串

-搜索字符串

八.复杂数据类型2指针

指针

指针可以让我们完成一些其他办法无法完成的任务

程序在硬盘上以文件的形式存在，但他们的运行却是在内存中运行

在C++里，变量类型是根据他们的自然边界进行对齐的，不过这个我们只需要知道即可，不需要太关心，因为编译器会自动帮我们处理这类问题

对于变量名可以通过两种方法来对他进行索引

-一种是通过变量名

-另一种是通过地址

&取址操作符-作用就是获得变量的地址

`int var=123;`

`std::cout<<"Address is:"<<&var`

同一个程序不同时间加载到内存中，同一个变量的地址是会改变的

地址是计算机内存中的某个位置，而指针是专门用来存放地址的特殊类型变量

声明指针变量

`type *pointerName;`

`int *p;`

`int pp=123;`

正确：`int *p1,*p2,*p3;`

在创建指针时，空格放在哪里都是没关系的，下边的语句都是可以接受的：

`int *p1;`

`int * p1;`

`int* p1;`

指针前边的类型是用来说明指针指向的数据的类型

另外允许void类型的指针变量：void *p;

九.复杂的数据类型3利用指针改变值

`int a = 456;`

`char b = 'C';`

`int *aPointer = &a;`

`char *bPointer = &b;`

当我们知道了某个变量在内存中的地址（通过指针），就可以利用指针访问位于该地址的数据。

这需要对指针进行"解引用"处理：即在指针名的前面加上一个星号（*）

`std::cout<<*aPointer;`

`*aPointer=123`

指针所保存的是内存中的一个地址。他并不保存指向的数据的值本身，因此务必确保指针对应一个已经存在的变量或者一块已经分配了的内存。

两种用途，时常困惑了初学者：

第一种是用于创建指针

`int *myPointer =&myInt;`

第二种是对指针进行解引用：

`[ex] *myPointer=3998;`

C++允许指针群P，就是多个指针有同样的值：

`int *p1 = &myInt;`

`int *p2 = &myInt;`

C++支持无类型（void）指针，就是没有被声明为某种特定类型的指针，例如：

`void *vPointer;`

注意：对一个无类型指针进行解引用前，必须先把他转换为一种适当的数据类型。

十.复杂的数据类型4指针和数组

计算机把数组是以一组连续的内存块保存的

这就说明了数组有很多地址，每个地址对应着一个元素

数组的名字其实也是一个指针（指向数组的基地址，也就是第一个元素的地址）

`int *ptr1=&myArray[0];`

`int *ptr2=&myArray;`

通过指针访问其他数组元素

`ptr1++;`

指针运算的奇妙之处就在于，以上并不将地址值简单+1处理，它是按照指向的数组的数据类型来递增的也就是+sizeof(int)

`int Array[5]={1,2,3,4,4};`

`int *ptr = Array;`

`*ptr+1;`

`*(ptr+1);`

重载

使用模板进行修改

泛型程序设计

指针运算的重要性在高级和抽象的程序设计互作中体现的更加明显

数组可以是任何一种数据类型，这意味着我们完全可以创建一个以指针为元素的数组

十一.复杂的数据类型5结构

C和C++的程序员完全可以根据具体情况定义一些新的数据类型并创建新类型的变量-结构

结构式由程序员定义的由其他变量类型组合而成的数据类型

定义一个结构的基本语法是：

```c++
struct name
{
    type varName1;
    type varName2;
   	....
};
```

当需要处理一些具体多种属性的数据时，结构往往是很好的选择

C++对于一个结构所能包含的变量的个数是没有限制的，那些变量通常我们成为该结构的成员，他们可以是任何一种合法的数据类型。

1.定义结构

2.用"."对结构成员进行赋值

如果我们在创建一个结构类型变量的时候就已经知道它各个成员相关的值，我们可以在声明新变量的同时进行赋值

`FishOil Jiayu={"小甲鱼"，"fishc_0000",'M'};`

结构与指针

指针无所不能，也可以指向结构，就像指向其他任何变量那样

创建一个指针指向结构的指针：

`FishOil *pJiayu =&Jiayu;`

注意：因为指针的类型必须与指向的地址的变量的类型一致

所以pJiayu指针的类型也是FishOil

一:我们可以通过对指针解引用来访问相应的变量值

`*(pJiayu).namew="黑夜";`

第二种：

`i.e. ...... ......`

`pJiayu->name="黑夜";`

十二.传值、传址和传引用

在编写个人函数的时候，你将受到C++中一条基本原则的限制：在默认的情况下，参数只能以值传递的方式给函数

被传递到函数的只是变量的值，永远不会是变量本身

绕开“值传递”问题的第一种方法是向函数传递变量的地址取代它的值，我们说C语言强大，有很大一部分就是在于它的灵活，他的灵活，有大一部分就是可以利用指针进行委婉地乱改

如果传过去的是地址，在函数中必须要通过“*”对指针进行解引用，除非你有其他用途

```c++
#include<iostream>
void swap(int *x, int *y);
int main()
{
    int x,y;
    std::cout << "请输入两个不同的值：";
    std::cin >>x >>y;
    swap(&x,&y);
    std::cout << "调用后输出："<< x << ' '<< y<<"\n\n";
    return 0;
}
void swap(int *x,int *y)
{
    int temp;
    temp =*x;
    *x=*y;
    *y=temp;
}
void swap(int *x,int *y)
{
    *x ^= *y;
    *y ^= *x;
    *x ^= *y;
}
```

传址在我们看来已经是很不错，不过C++语言的大神们在完善的过程中完善了地址这个概念

以引用传递方式输人方式的概念因此而产生了

其实他跟我们这个传址的目的是一样的，都是把地址传递给函数，但语法不同更加容易使用了

```c++
#include<iostream>
void swap(int &x, int &y);
int main()
{
    int x,y;
    std::cout << "请输入两个不同的值：";
    std::cin >>x >>y;
    swap(x,y);
    std::cout << "调用后输出："<< x << ' '<< y<<"\n\n";
    return 0;
}
void swap(int &x,int &y)
{
    int temp;
    temp =*x;
    *x=*y;
    *y=temp;
}
```

十三.联合、枚举和类型别名

联合

联合与结构有很多相似之处，联合也可以容纳多种不同类型的值，但是他每次只能存储这些之中的某一个。

```c++
union mima
{
    unsigned long birthday;
    unsigned short ssn;
    char* pet;
};
//定义了这个联合类型之后，就可以像下面这样创建一个该类型的变量了：
mima mima_1;
mima_1.birthday=19881301;
mima_1.pet="Chaozai";
//这个联合将把"Chaozai"存入mima_1联合的pet成员，并丢弃birthday成员里的值。
```

枚举

```c++
//枚举(enum)类型用来创建一个可取值列表：
enum weekdays{Monday,Tuesday,Wednesday,Thursday,Friday};
//定义一个枚举类型之后，我们就可以像下面这样创建该类型的变量：
weekdays today;
//然后我们像下边的方式对他进行赋值:
today Thursday;
//注意我们这里不需要使用引号，因为枚举值不是字符串，编译器会按照各个枚举值在定义时出现的先后顺序把他们与0~n-1的整数（n是枚举值的总个数）分别关联起来。
//使用枚举好处：
//1.他们对变量的可取值加以限制；
//2.他们可以用做switch条件语句的case标号。
//因为字符串
```

类型别名

Typedef 保留字，使用他可以为一个类型定义创建一个别名

`typedef int* intPointer;`

十四.给大家介绍对象

使用对象进行编程是C++的核心，也是我们常说的C++比C“高级”的重要根据之一

对象的本质上不过是一种新的数据类型

与结构的过程很相似，但是这更有扩展性和前瞻性

对像的内部可以有变量和函数，而结构通常只由各种变量构成

```c++
class MyFirstClass
{
    
};
```

注意：类名的第一个字母采样大写是一种习惯上的标准，但是不是硬性规定，还有在类声明末尾，必须有一个分号，这一点跟C++结构情况相同。

类由变量和函数组成，对象将使用那些变量来存储信息，调用那些函数来完成操作，所以人们常常会看到一些专门术语，类里边的变量成为属性，函数成为方法，注意，他们的本质没有改变。

```c++
class Car
{
    public:
    	std::string color;
    	std::string engine;
        float gas_tank;
    	unsigned int Wheel;
    void fill_tank(float liter);
    void running(void);
    //方法的定义通常安排在类声明的后面
};
void Car::fill_tank(float liter)
{
    gas_tank+=liter;
}
//在声明变量之前先写出"public:"
int main()
{
    return 0;
}
```

作用域解析操作符(::),作用是告诉编译器这个方法存在于何处，或者说是属于哪一个类

十五.闭门造车

面向对象编程技术可以说是面向过程技术的替代品

面向过程技术关注的是对数据进行处理的过程，OOP技术关注的是对数据进行怎么样的处理

对象与结构有很多相似之处，但前者还可以有它们自己的函数，记住这点区别对掌握OOP技术的要领很有帮助

C++允许在类里面声明常量，但不允许对他进行赋值

```c++
class Car
{
    public:
    const float TANKSIZE=85//出错
};
```

绕开这一限制的方法就是创建一个静态常量

`static const float FULL_GAS =85;`

```c++
Car car1,car2;
car1.setColor("WHITE");
car2=car1;
//把一个对象赋值给另一个同类的对象将会自动使同名的属性有同样的值
```

十六.构造器和析构器

面向对象的编程技术开发程序最基本步骤：

1.定义一个有属性和方法的类（模板）

2.为该类创建一个变量（实现）

构造器

构造器和通常方法的主要区别：

1.构造器的名字必须和它所在的类的名字一样

2.系统在创建某个类的实例时会第一时间自动调用这个类的构造器

3.构造器永远不会返回任何值

创建构造器，需要先把它的声明添加到类里：

```c++
class Car
{
    Car(void);
};
```

注意大小写与类名保持一致。在结束声明之后开始定义构造器本身

```c++
Car::Car(void)//不用写void Car::Car(void)
{
    color="WHITE";
    engine = "V8";
    wheel=4;
    gas_tank =FULL_GAS;
}
```

构造对象数组：之前我们已经说过，数组可以时任何一种数据类型，当然也包括对象

`Car mycar[10];`

调用语法依旧是：`mycar[x].running;`

每个类至少有一个构造器，如果你没有在类里定义一个构造器，编译器就会使用如下语法替你定义一个`ClassName::ClassName(){}`

这是一个没有代码内容的空构造器，除此之外，编译器还会替你创建一个副本构造器（CopyConstructor)

`Car mycar;`

`mycar.setColor("Yellow");`

析构器

一般来说，构造器用来完成事先的初始化和准备工作（申请分配内存），析构器用来完成事后所必须的清理工作（清理内存）

```c++
class Car
{
    Car(void);
    ~Car();
}
```

析构器也永远不返回任何值

另外析构器不带参数，析构器往往至关重要（可能引起内存泄漏）

`~ClassName();`

十七.this指针和类的继承

```c++
class Human

{
	char fishc;
	Human(char fishc);
}
Human::Human(char fishc){
    fishc=fishc;
}
```

-Human()构造器有一个名为fishc的参数

-虽然他与Human类里边的属性同名，但却是不相干的两样东西

但是却是不相干的两样东西，所以并没有错

`this->fishc=fishc`

赋值操作符的左边将被解释为当前对象的fishc属性，右边将被解释为构造器的传来的fishc参数

使用this指针的基本原则是：如果代码不存在二义性隐患，就不必使用this指针

this指针在一些更加高级的方法里也会用到

类的继承

继承是面向对象编程技术的核心，他使传统的软件开发模式发生了革命性的变化

继承机制可以创建一个类的堆叠层次结构，每个子类均将继承在基类里定义的方法和属性

基类和子类

基类：可以派生出其他的类，也是父类或超类

子类：子类是从基类派生出来的类

`class SubClass : public SuperClass{...}`

`class Pig : public Animal{...}`

```c++
#include<iostream>
#include<string>
class Animal
{
    public:
    	std::string mouth;
    	void eat;
    	void sleep();
    	void drool();
};
class Pig : public Animal
{
    public:
    	void climb();
};
class Turtle : public Animal
{
    public:
    void swim();
};
void Animal::eat()
{
    std::cout <<"I am eatting!"<<std::enl;
}
void Animal::sleep()
{
    std::cout << "I'm sleeping!"<<std::endl;
}
void Animal::drool()
{
    std::cout<<"我在流口水"<<std::enddl;
}
void Pig::climb()
{
    std::cout<<"我是小母猪"<<std::endl;
}
void Turtle::swim()
{
    std::cout<<"我是小甲鱼"<<std::endl;
}
int main()
{
    Pig pig;
    Turtle turtle;
    pig.eat();
    turtle.eat();
    pig.climb();
    turtle.swim();
    return 0;
}
```

十八.继承机制中的构造器和析构器

比如基类有个构造器，如Animal(),它将在创造Pig类型的对象时最先被调用，如果Pig类也有一个构造器，他将排在第二个被调用，因为基类必须在子类之前初始化原则

构造器带着输入参数

```c++
class Animal
{
    public:
    	Animal(std::string theName);
    	std::string name;
};
class Pig:public Animal
{
    public:
    	Pig(std::string theName);
};
```

```C++
Animal::Animal(std::string theName)
{
    name=theName;
}
//在子类的构造器定义里的“:Animal(theName)”语法含义是：当调用Pig()构造器时（以theName作为输入参数），Animal()构造器也将被调用（theName输入参数将传递给它）。
Pig::Pig(std::string theName):Animal(theName)
{
    
}
```

在销毁某个对象时，基类的析构器也将被自动调用

因为析构器不需要输入餐宿，所以根本用不着使用：SuperClassMethod(arguments)语法！

```c++
#include<iostream>
#include<string>
class BaseClass
{
    public:
    Baseclass();
    ~BaseClass();
 	void doSomething();
};
class SubClass:public BaseClass
{
    public:
    SubClass();
    ~SubClass();
};
BaseClass::BaseClass()
{
    std::cout<<"进入基类构造器\n";
}
BaseClass::~BaseClass()
{
    std::cout<<"进入基类析构器";
}
void BaseClass::dosomething()
{
    std::cout<<"我干了某些事";
}
SubClass::SubClass()
{
    std::cout<<"进入子类构造器";
}
SubClass::~SubClass()
{
    std::cout<<"进入子类构造器";
}
int main()
{
    SubClass subclass;
    subclass.doSomething();
    std::cout<<"完事，收工！"
    return 0; 
}
```

十九.访问控制

所谓访问控制就是C++提供了一种用来保护类的方法和属性的手段。

这里所说的保护意思是对谁可以调用某个方法和访问某个属性加上一个限制，如果某个对象试图调用一个它无权访问的函数，编译器将报错。

访问级别

```c++
public		//任何代码
protected	//这个类本身和它的子类
private		//只有这个类本身
```

BUG无法避免的原因正是因为我们无法模拟各种情况的输入和修改带来的影响。

一定要记住使用这些访问级别！即使只有你一个人在开发某个项目全部记住各个类的调用方法也是一件困难的事情。

给每个方法和属性加上protected或private访问级别，就由编译器替你记住哪些禁令并在你违反的时候发出警报。

使用private的好处是今后可以只修改某个类的内部实现，而不必重新修改整个程序，这是因为其他代码根本就访问不到private保护的内容，所以不怕牵一发而动全身的惨剧发生！

在同一个类定义里可以使用多个public:,private:和protected:语句，但最好把你的元素集中到一个地方，这样代码的可读性会好很多。

在编写你的类定义代码时，应该从piblic:开始写起，然后是protected:,最后是private:。

二十.覆盖方法和重载方法

`class Pig : public Animal{...}`

C++不仅允许你对在类里定义的方法和属性实施访问控制，还允许你控制子类可以访问基类里的哪些方法和属性。

public

是在告诉编译器:继承的方法和属性的访问级别不发生任何改变-即public仍可以被所有代码访问，protected只能由基类的子类访问，private则只能由基类本身访问。

protected

把基类的访问级别改为protected,如果原来是pubilc的话，这将使得这个子类外部的代码无法通过子类去访问基类中的public。

private

是在告诉编译器从基类继承来的每一个成员都当成private来对待，这意味着只有这个子类可以使用它从基类继承来的元素。

不过一般都只用public

覆盖方法

C++可以让我们很容易实现这种既有共同特征又需要在不同的类里有不同实现的方法

我们需要做的是在类里面重新声明这个方法，然后再改写一下它的实现代码。

重载方法

简化编程互作和提高代码可读性的另一种方法是对方法进行重载。

重载机制使你可以定义多个同名的方法（函数），只是他们的输入参数必须不同。（因为编译器使依靠不同的输入参数来区分不同的方法）

重载并不是一个真正的面向对象特性，它只是可以简化编程工作的捷径，而简化编程工作正是C++的全部追求！

对方法(函数)进行重载一定要有的放失，重载的方法（函数）越多，程序就越不容易看懂。

在对方法进行覆盖（注意区分覆盖和重载）时一定要看仔细，因为只要声明的输入参数和返回值与原来的不一致，你编写出来的就将是一个重载方法而不是覆盖方法。

对从基类继承来的方法进行重载，程序永远不会想你预期的那样工作

继承之后不能重载

二十一.一种特殊的友情

友元关系

友元关系是类之间的一个钟特殊关系，这种关系不仅允许友元类访问对方的public方法和属性，还允许友元访问对伐的protected和private方法和属性。

声明一个友元关系：`friend class **`

这条语句可以放在任何地方，public，protected，private段落里都可以。

二十二.静态属性和静态方法1

OOP

面向对象编程技术的一个重要特征是用一个对象把数据和对数据处理的方法封装在一起

当我们需要的是一个只在创建或删除对象时候才允许访问的计数器，这个问题必须使用C++的静态属性和静态函数才能完美地得到解决

C++允许我们把一个或多个成员声明为属于某个类而不是仅属于该类的对象

这么做的好处是程序员可以在没有创建任何对象的情况下调用有关的方法

另外一个是能够让有关的数据仍在该类的所有对象间共享

创建一个静态属性和静态方法：

-只需要在他的声明前加上static保留字即可

二十三.静态属性和静态方法2

-静态成员是所有对象共享的，所以不能再静态方法里访问非静态的元素

-非静态方法可以访问类的静态成员，也可以访问类的非静态成员

this指针是类的一个自动生成，自动隐藏的私有成员

在任何一个方法里都可以使用this指针，从本质上将C++中的对象其实是一种特殊的结构，除了变量，还包含着一些函数的特殊结构。

在程序运行时，对象的属性（变量）和方法（函数）都是保存在内存里，这就意味着他们各自都有与之相关联的地址。

this指针保存着对象本身的地址

每当我们调用一个方法的时候，this指针都会随着你提供的输入参数被秘密的传递给那个方法

正是因为如此，我们才能在方法里像使用一个局部变量那样使用this指针

因为静态方法不是属于某个特定的对象，而是由全体对象共享的这就意味着他们无法访问this指针，所以我们才无法在静态方法里访问非静态的类成员

在使用静态属性的时候，千万不要忘记为他们分配内存，只需要在类声明的外部对静态属性做出声明

坚持使用：`ClassName::methodName();`

不要使用：`objectName.methodName();`

二十四.虚方法

将使用指针代替局部变量来容纳Pet对象

C++保留字new和delete

指针就是一种专门用来保存内存地址的数据类型

完全可以在没有创建变量的情况下为有关数据分配内存，直接创建一个指针并让它指向新分配的内存块：

```c++
int *pointer=new int;
*pointer = 110;
std::cout<<*pointer;
delete pointer;
```

因为程序不会自动释放内存，程序中的每一个new操作都必须有一个与之对应的delete操作

为了让编译器知道它应该根据这两个指针在运行时的类型而有选择地调用正确的方法，我们必须把这些方法声明为虚方法

`virtual void play();`

虚方法是继承的，一旦在基类里把某个方法声明为虚方法，在子类就不可能再把它声明为一个非虚方法了

TIPS

1.如果拿不准要不要把某个方法声明为虚方法，那么就把它声明为虚方法好了

2.在基类里把所有的方法都声明为虚方法会让最终生成的可执行代码的速度变得稍微慢一些，但好处是可以一劳永逸的确保程序的行为符合你的预期

3.在实现一个多层次的类继承关系的时候，最顶级的基类应该只有虚方法

4.析构器都是虚方法，从编译的角度看，他们只是普通的方法，如果他们不是虚方法，编译器就会根据他们在编译时的类型而调用那个基类里的定义的版本（构造器），那样往往会导致内存泄漏

二十五.抽象方法

抽象方法在设计一个多层次的类继承关系时常会用到

把某个方法声明为一个抽象方法等于告诉编译器这个方法必不可少，但我现在在（在这个基类里）还不能为它提供一个实现

在声明一个虚方法的基础上在原型的末尾加上=0

多态性

多态性是面向对象程序设计的重要特征之一

多态性是指用一个名字定义不同的函数，调用同一个名字的函数，却执行不同的操作，从而实现一个接口多种用法

多态是如何实现绑定的

编译的多态：通过重载实现

析构函数

一般下类的析构函数里面都是是释放内存资源的，而析构函数不被调用的话就会造成内存泄漏

所以析构器都是虚方法是为了当一个基类的指针删除一个派生类的对象，派生类的析构函数可以正确调用

另外，当类里面有虚函数的时候，编译器会给类添加一个虚函数表，里边存放着虚函数指针，为了节省资源，只有当一个类被用来作为基类的时候，我们才把析构器函数写成虚函数

二十六.运算符重载

函数重载是对一个已有的函数赋予新的含义，使之实现新功能

重载运算符的函数一般格式如下：

```c++
函数类型 operator 运算符名称（形参表列）

{

对运算符的重载处理

}
```

我们在声明Complex类的时候对运算符进行重载，使得这个类在用户编程的时候可以完全不考虑函数是如何实现的，直接使用+，-，*/。

```c++
Complex Complex::operator+(Complex &c2)

{
	return Complex(real+c2.real,imag+c2.imag);
}
```

除了以下运算符不允许重载外，其他运算符允许重载：

-.（成员访问运算符）

-.*（成员指针访问运算符）

-：：（域运算符）

-sizeof(尺寸运算符)

-？：（条件运算符）

1.重载不能改变运算符运算的对象个数

2.重载不能改变运算符的优先级别

3.重载不能改变运算符的结合性

4.重载运算符的函数不能有默认的参数

5.重载运算符必须和用户定义的自定义类型的对象一起使用，其参数至少应该有一个是类对象或类对象的引用

运算符重载函数作为类友元函数

运算符重载函数除了可以作为类的成员函数外，还可以是非成员函数：放在类外，做Complex类的友元函数存在

为什么把运算符函数作为友元函数？

因为运算符函数要访问Complex类对象的成员，如果运算符函数不是Complex类的友元函数，而是一个普通的函数，它是没有权力访问Complex类的私有成员的。

二十七.重载<<操作符

重载<<操作符来实现print打印的功能

第一次输出值开始，<<操作符就一直被重载

返回类型是ostream流的引用，一般来说，在调用operator<<()重载函数时传递给它的是哪一个流，它返回的就应该是那一个流的引用。

二十八.多继承

同时存在着两个"是一个"的关系

`class TeachingStudent : public Student,public Teacher:`

二十九.虚继承

Teaching类继承自Teacher和Student两个类，因而继承了两组Person类的属性，这在某些时候完全有道理，例如classes属性，但它也有可能引起麻烦，例如发生在name属性身上的情况

class Teacher ：virtual public Person

 三十.错误处理和调试1

编译时错误和运行时错误

编译时错误

建议一：培养并保持一种编程风格

建议二：认真对待编译器给出警告的信息

建议三：三思而后行

建议四：注意检查最基本的语法

建议五：把可能有问题的代码行改为注释

建议六：换一个环境或开发工具试试

建议七：检查自己是否已经把所有的必要的头文件全部include进来

建议八：留意变量的作用域和命名空间

建议九：使用调试工具

建议十：避免错误的另一个好方法就是把调试好的代码另外保存起来

并不再改动它

运行时错误

经验一：还是培养并保持一种良好的编程风格

经验二：多用注释，用好注释

经验三：注意操作符的优先级

经验四：千万不要忘记对用户输入和文件输入进行合法性检查

经验五：不要做任何假设

经验六：把程序划分一些比较小的单元模块来测试

三十一.错误处理和调试2

让函数返回错误代码

让程序能够自行处理潜在错误的办法之一时创建一些测试函数：专门测试某种条件并根据测试结果返回一个代码来表示当前函数的执行状态

```c++
int myFunction()
{
    if(condition)
    {
        return 0;
	}
    else
    {
        return 1;
    }
}
```

运用climits头文件

```c++
#include<iostream>
#include<climits>
class Factorial
{
    public:
    Factorial(unsigned short num);
    unsigned long get Factorial();
   	bool inRange;
    private:
    unsigned short num;
}
Factorial::Factorial(unsigned short num)
{
    this->num=num;
}
unsigned long Factorial::get Factorial()
{
    unsigned long sum=1;
    for(int i=1;i<=num;i++)
    {
        sum*=i;
    }
    return sum;
}
bool Factorial::inRange()
{
    unsigned long max =ULONG_MAX;
    for(int i=num;o=i>=1,--i)
    {
        max/=i;
    }
    if (max<1)
        return false;
    else 
        return true;
}
int main()
{
    unsigned short num=0;
    std::cout <<"请输入一个整数：";
    std::cin>>num;
    Factorial fac(num);
    if(fac.inRange())
    {
        std::cout<<num<<"的阶乘是"<<fac.getFactorial()<<"\n\n";
    }
    else:
    {
        std::cout<<"您所输入的值太大\n\n";
    }
}
```

三十二.assert函数和捕获异常

assert函数-专门为调试而准备的工具函数

`#include<assert.h>`

我们可以利用它在某个程序里的关键假设不成立时，立刻停止该程序的执行并报错，从而避免发生更严重的问题

另外，除了结合assert函数，在程序的开发、测试阶段，我们还可以使用大量的cout语句来报告在程序里正在发生的事情

捕获异常

```c++
try
{
	//Do something
    //Throw an exception on error
}
catch
{
    //Do whatever
}
```

`type functionName(arguments)throw(type);`

应该只用它们来处理确实可能不正常的情况

三十三.动态内存管理

在很多时候，需要寸尺的数据量到底有多大在事先往往是应该未知数，要处理好这类情况，就需要C++程序里使用动态内存

动态内存支持程序员创建和使用种种能够根据具体需要扩大和缩小的数据结构，他们只受限于计算机的硬件内存总量和系统特殊约束

静态内存

变量（指针变量）、固定长度的数组、某给定类的对象

动态内存

动态内存由一些没有名字只有地址的内存块构成，那些内存块是在程序运行期间动态分配的

从内存池申请一些内存需要用new语句，它将根据你提供的数据类型分配一块适当的内存，你不必担心内存块的尺寸问题，编译器能够记住每一种数据类型的单位长度并迅速计算出需要分配多少个字节

如果有足够的可用内存能满足你的申请，new语句将返回新分配地址块的起始地址

如果没有足够的可用内存空间

那么new语句将抛出std::bad_alloc异常

注意在用完内存块之后，应该用delete语句把它还给内存池，另外作为一种附加的保险措施，在释放了内存块之后还应该把与之关联的指针设置为NULL

`int *i=new int;`

`delete i;`

`i=NULL`

NULL指针当把一个指针变量设置为NULL时，它的含义是那个指针将不再指向任何东西：

`int *x;`

`x=NULL;`

为对象分配内存和为各种基本数据（int，char，float...)分配内存在做法上完全一样

在重新使用某个指针之前千万不要忘记调用delete语句如果不这样做，那个指针将得到一个新内存块的地址，而程序将永远也无法释放原先那个内存块，因为它的地址已经被覆盖掉了

delete语句只释放给定指针变量正指向的内村块，不影响这个指针，在执行delete语句之后，那个内存块被释放了，但指针变量还存在

三十四.动态数组

数组名和下标操作符[]的组合可以被替换成一个指向该数组的基地址的指针和对应的指针运算

把一个数组声明传递给new语句将使它返回一个该数组基类型的指针

把一个数组声明传递给new语句将使它返回一个该数组基类型的指针

把数组下标操作符和该指针变量的名字搭配使用就可以像对待一个数组那样使用new语句为这个数组分配的内存块了

删除一个动态数组要比删除其他动态数据类型稍微复杂一点

具体的做法是在delete保留字的后面加上一对方括号：delete[]x;

三十五.从函数或方法返回内存

动态内存的另一个常见用途是让函数申请并返回一个指向内存块的指针

```c++
#include<iostream>
int newInt(int value);
int main()
{
    int *x=newInt(20);
    std::cout <<*x;
    delete x;
    x=NULL;
    return 0;
}
int *newInt(int value)
{
    int *myInt=new int;
    *myInt=value;
    return myInt;
}
```

任何一个函数都不应该把自己的局部变量的指针作为它的返回值因为局部变量在栈里函数结束自动会释放

函数指针：指向函数首地址的指针变量成为函数指针

指针函数：一个函数可以带回一个整型数据的值，字符类型值和实型类型的值，还可以带回指针类型的数据，使其指向某个地址单元

三十六.副本构造器

编译器将生成必要的代码把"源"对象各属性的值分别赋值给"目标"对象的对应成员，这种赋值行为称之为逐位复制

重载赋值操作符

`MyClass &operator=(const MyClass &rhs);`

因为这里使用的参数是一个引用，所以编译器在传递输入参数时，就不会再为它创建另外一个副本

`MyClass(const MyClass &rhs);`

三十七.高级强制类型转换

静态对象强制类型转换

（转换后的类型）对象

我们用传统的强制类型转换实现：把所需要的指针型放在一对圆括号之间，然后写出将被强制转换的地址值

`Company *company =new Company("APPLE",Iphone);`

`TechCompany *tecCompany=company;`

动态对象强制类型转换

三十八.避免内存泄漏

new语句所返回的地址是访问这个内存块的唯一线索，同时也是delete语句用来把这个内存块归还给内存池的唯一线索

```c++
int *x;
x = new int[1000];
delete[] x;
x = NULL;
```

这意味着如果这个地址值（保存在x里）丢失了，就会发生内存泄漏问题

```c++
int *x;
x=new int[3000];
x=new int[4000];
delete[] x;
x= NULL;
```

```c++
void foo()
{
    My Class *x;
    x = new MyClass();
}
//当foo()函数结束时，指针变量x将超出它的作用域，这意味着它将不复存在，它的值当然就会丢失
```

```c++
void foo()
{
    MyClass *x;
    x= new MyClass();
    delete x;
    x= NULL;
    return;
}
```

```c++
MyClass *foo()
{
    MyClass *x;
    x=new MyClass();
    return x;
}
```

内存作用域

变量都有一个作用域：规定了他们可以在程序的哪些部分使用

这个作用域通常就是对它们做出声明和定义的函数体，如main函数或某个子函数

如果被定义在任何一个函数的外部，变量将拥有全局作用域，这意味着它们可以在整个程序中所有函数里使用

不过，应该尽量避免使用全局变量，因为它们往往会让代码变得难以调试和容易出错

三十九.命名空间和模块化编程1

模块化

把程序化分多个组成部分

这是通过程序代码分散到多个文件里，等编译程序时再把那些文件重新组合在一起实现的

命名空间

头文件

头文件的基本用途是提供必要的函数声明和类声明

头文件可以细分为系统头文件和自定义头文件

在#include指令里，自定义头文件的文件名要放在双引号里给出:`#include"fishc.h"`

绝大多数头文件是通用型的，不隶属于任何特定的程序

创建日期，文件用途创建者姓名，最后一次修改日期，有什么限制

四十.命名空间和模块化编程2

使用头文件

在创建了头文件之后，只要把它的文件名用双引号括起来，

`#include"fishc.h"`

如果没有给出路径名，编译器将到当前子目录以及当前开发环境中的其他逻辑子目录里取寻找头文件

为了消除这种猜测，在导入自己的头文件时可以使用相对路径，如果头文件与主程序头文件在同一个子目录里，则可以这么写：

`#include"./fishc.h"`

如果头文件位于某个下级子目录里，那么以下级子目录的名字开头：

#include"includes/fishc.h"

最后如果头文件位于某个与当前子目录平行的"兄弟"子目录里，则需要这么写：

`#include"../includes/fishc.h"`

作为一个通用原则，应该把声明放在一个头文件里，把实现代码放在一个.cpp文件里

C预处理器

利用C++预处理器可以让头文件只在这个类还没有被声明过的情况下才声明它。

```c++
#if //如果表达式为真，执行代码、
#else //如果前面的#if表达式为假，执行代码
#elif //相当于elseif
#endif //用来标志一个条件指令的结束
#ifdef //如果本指令所引用的定义已存在，执行代码
#ifndef //如果本指令所引用的定义不存在，执行代码
```

四十一.命名空间和模块化编程3

命名空间

命名空间其实就是由用户定义的范围，同一个命名空间里的东西只要在这个命名空间有独一无二的名字就行了

```c++
namespace myNamespace
{
	//全部东西
}
```

建议使用`std::cout<<"I love fishc.com"`

`using std::cout`

四十二.链接和作用域1

在一个任何函数之前定义的变量可以在任何一个函数里使用（这是一个全局变量），而在某个函数里定义的变量只能在那一个函数里使用（这是一个局部变量）

当一个项目由多个文件构成，变量的作用域也会受到一定的影响

存储类

每个变量都有一个存储类，它决定着程序将把变量的值存储在计算机上的地方，如何存储，以及变量应该有着怎么样的作用域

与auto不同的是static，static变量在程序的生命期内将一直保有它的值，而不会消亡

编译器不会为extern变量分配内存，因为在其其他地方已经为它分配过内存

1.执行预处理指令

2.把.cpp文件编译成.o文件

3.把.o文件链接成一个可执行文件

当你同时编译多个源文件来生成一个可执行文件的时候，在编译好的每一个组件之后，编译器还需要把它们链接在一起才能生成最终的可执行文件

外链接，内链接和无链接

外链接的意思是每个翻译单元都可以访问这个东西

static

在函数定义的变量只存在于该函数内部，根本没有任何链接

四十三.函数模板

泛型编程

STL库

STL库是泛型编程技术

```c++
template <class T>
void fool(T param)
{
    //do something
}
```

```c++
#include<iostream>
#include<string>
template<class T>
void swap(T &a, T &b)
{
    T temp=a;
    a=b;
    b=temp;
}
```

四十四.类模板

如果某个函数对所有数据类型都将进行同样的处理，就应该把它编写为一个模板

如果某个函数对不同的数据类型将进行不同的处理，就应该对它进行重载

```c++
MyClass<T>::MyClass()
{
    //初始化操作
}
//因为MyClass是一个类模板，所以不能只写MyClass::MyClass(),编译器需要你在这里给出一种与MyClass()配合使用的数据类型，必须在尖括号里提供它，因为没有确定的数据类型可以提供，所以使用T作为占位符即可
```

```c++
#include<iostream>
#include<string>
template<class T>
class Stack
{
    public:
    Stack(unsigned int size=100);
    ~Stack();
    void push(T value);
    T pop();
    private:
	unsigned int size;
    unsigned int sp;
    T *data;
}
template<class T>
Stack<T>::Stack(unsigned int size)
{
    this ->size=size;
    data = new T[size];
    sp=0;
}
template<class T>
Stack<T>::~Stack()
{
    delete []data;
}
```

四十五.内联模板

内联函数

引入内联函数的目的是为了解决程序中函数调用的效率问题

```c++
inline int add(int x,int y,int z)
{
    return x+y+z;
}
```

除了可以更好的帮助编译器处理类模板之外，使用内联方法还有一个很好的作用：可以让你少打些字并让源代码的可读性变得更好

```c++
template <class T,class U>
class MyClass
{
    //......
}
```

实例化：`Myclass<int,float>myClass;`

四十六.容器与算法1

容器

能容纳两个或更多个值的数据结构通常成为容器

找到最合适的容器只是编程工作的一部分

数组这种数据结构最大的先天不足就是它受限于一个固定的长度

`std::vector<type>vectorName;`

四十七.容器与算法2

迭代器

C++标准器提供的各种迭代器

通过使用迭代器，当在程序里改用另一种容器的时候就用不着修改那么多的代码了

每一种容器都必须提供自己的迭代器，事实上每种容器都将其迭代器以嵌套的方式定义于内部

算法

