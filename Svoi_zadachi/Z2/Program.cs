//C1.17. Вывести «столбиком» значения sin(0,1),  sin(0,2) , …,  sin(1,6).

double x, y;

for (x = 0.1; x < 1.7; x += 0.1)
{
y = Math.Sin(x);

Console.WriteLine(Math.Round(y, 3));
}
Console.ReadKey();
