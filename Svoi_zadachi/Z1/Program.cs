//I1.1. Рассчитать значение у при заданном значении х:
//y=sin(x) при x>0 или y=cos(x) в противном случае.

Console.Write("Введите x: ");
double x = Convert.ToDouble (Console.ReadLine());
double y;

if (x > 0)
{
    y = Math.Sin(x);
    y = Math.Round(y, 2);
    Console.Write ("y= " + y);
}
else
{
    y = Math.Cos(x);
    y = Math.Round(y, 2);
    Console.Write ("y= " + y);
   
}
Console.ReadKey();