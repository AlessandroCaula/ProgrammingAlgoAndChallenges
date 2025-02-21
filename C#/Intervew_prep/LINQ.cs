using System.Linq;

public class LinqClass
{
    public LinqClass()
    {
        FilteringAndSorting();
    }

    private void FilteringAndSorting()
    {
        int[] numbers = { 4, 7, 2, 9, 5, 1 };

        var evenNumbers = numbers.Where(n => n % 2 == 0).OrderBy(n => n);

        Console.WriteLine("Even Number in ascending order");
        foreach (var num in evenNumbers)
            Console.WriteLine(num);
    }
}