class Program
{
    static void Main()
    {
        Console.WriteLine("-- DependencyInjection");
        DependencyInjection dependencyInjection = new DependencyInjection();

        Console.WriteLine("\n-- LINQ");
        LinqClass linqClass = new LinqClass();
    }
}