


SolveTask01();

Console.ReadLine();




void SolveTask01()
{
    string task_definition = @"If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
------------------------------------------------------
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9.
Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.";


    Console.WriteLine( task_definition );


    List<int> target_list = new List<int>();

    int i = 1;
    int target = 1000;

    while (i < target)
    {
        if ( i % 3 == 0 || i % 5 == 0)
        {
            target_list.Add( i );
            
        }
        i++;
    }

    int target_sum = target_list.Sum();

  
    Console.WriteLine($"Answer: { target_sum }" );


}