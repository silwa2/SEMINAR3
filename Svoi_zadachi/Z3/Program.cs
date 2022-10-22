// C2.1. Найти:
// а) сумму всех целых чисел от 100 до 500;

int number, result = 0;

for (number = 100; number < 1500; number++)
{
result += number;
}
Console.WriteLine (result);