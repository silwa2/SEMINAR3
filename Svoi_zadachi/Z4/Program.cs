//C2.1. Найти:
//сумму всех целых чисел от a до b (значения a и b вводятся с клавиатуры; b>a).

Program:
int a, b, result = 0, summa = 0;
Console.Write("Введите число a: ");
a = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите число b: ");
b = Convert.ToInt32(Console.ReadLine());

if ( b > a )
{
    while (result <= b)
    {
        summa += result;
        result ++;
    }
    Console.WriteLine (summa);
}
else
{
  Console.WriteLine("Ввели неправильные числа a>b");
     goto Program;  
}


// {
//     for (result = a; result <= b; result++);
//     {
//     summa = summa + result;
//     }
//     Console.WriteLine (summa);
    
// }
// else
// {
//     Console.WriteLine("Ввели неправильные числа a>b");
//     goto Program;
// }


