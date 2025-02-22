using System.Linq;

public class LinqClass
{
    public LinqClass()
    {
        FilteringAndSorting();
        Console.WriteLine("");
        FilteringAndSelecting();
        Console.WriteLine("");
        AggregateFunctions();
        Console.WriteLine("");
        GroupByMethod();
        Console.WriteLine("");
        JoinCollections();
        Console.WriteLine("");
        AllAnyContains();
    }

    /// <summary>
    /// Filtering with Where and sorting with OrderBy
    /// </summary>
    private void FilteringAndSorting()
    {
        int[] numbers = { 4, 7, 2, 9, 5, 1 };

        var evenNumbers = numbers.Where(n => n % 2 == 0).OrderBy(n => n);

        Console.WriteLine("Even Number in ascending order: ");
        foreach (var num in evenNumbers)
            Console.WriteLine(num);
    }

    /// <summary>
    /// Filtering with Where and Selecting with Select
    /// </summary>
    private void FilteringAndSelecting()
    {
        List<Employee> employees = new List<Employee>
        {
            new Employee { Name = "Alice", Age = 30 },
            new Employee { Name = "Bob", Age = 25 },
            new Employee { Name = "Charlie", Age=35 }
        };

        // Filtering out the employees older than 30 and select their name.
        var youngEmployees = employees.Where(e => e.Age < 30)
                                        .Select(e => e.Name);

        Console.WriteLine("Employees younger than 30: ");
        foreach (var name in youngEmployees)
        {
            Console.WriteLine(name);
        }
    }

    /// <summary>
    /// Aggregate functions (Sum, Average, Count, Max, Min)
    /// </summary>
    private void AggregateFunctions()
    {
        int[] numbers = { 3, 7, 2, 9, 5, 1 };

        Console.WriteLine("Aggregate Functions: ");
        Console.WriteLine("Sum: " + numbers.Sum());
        Console.WriteLine("Average: " + numbers.Average());
        Console.WriteLine("Count: " + numbers.Count());
        Console.WriteLine("Max: " + numbers.Max());
        Console.WriteLine("Min: " + numbers.Min());
    }

    /// <summary>
    /// Grouping data with GroupBy
    /// </summary>
    private void GroupByMethod()
    {
        List<Product> products = new List<Product>
        {
            new Product { Name = "Laptop", Category = "Electronics" },
            new Product { Name = "Phone", Category = "Electronics" },
            new Product { Name = "Bread", Category = "Food" },
            new Product { Name = "Milk", Category = "Food" }
        };

        // Grouping products by category
        var groupedProducts = products.GroupBy(p => p.Category);

        // Loop through all the grouped groups by category
        foreach (var group in groupedProducts)
        {
            Console.WriteLine($"Category: {group.Key}");

            // Loop through the products for each product in the grouped category
            foreach (var product in group)
            {
                Console.WriteLine(" " + product.Name);
            }
        }
    }

    /// <summary>
    /// Joining two collections based on matching keys.
    /// </summary>
    private void JoinCollections()
    {
        List<Student> students = new List<Student>
        {
            new Student {Id = 1, Name = "Alice"},
            new Student {Id = 2, Name = "Bob"}
        };

        List<Grade> grades = new List<Grade>
        {
            new Grade {StudentId = 1, GradeLetter = "A"},
            new Grade {StudentId = 2, GradeLetter = "B"}
        };

        // Correlates the elements of two sequences based on matching keys. The default equality comparer is used to compare keys.
        var studentGrades = students.Join(grades,
                                            s => s.Id,
                                            g => g.StudentId,
                                            (s, g) => new { s.Name, g.GradeLetter });

        foreach (var item in studentGrades)
        {
            Console.WriteLine(item.Name + " received " + item.GradeLetter);
        }
    }

    private void AllAnyContains()
    {
        int[] numbers = { 3, 7, 2, 9, 5, 1 };

        // Returns true if all numbers are greater than 0.
        Console.WriteLine("All numbers > 0: " + numbers.All(n => n > 0));
        // Return true if at least one number is greater than 5
        Console.WriteLine("Any number > 5: " + numbers.Any(n => n > 5));
        // Checks if 7 is in the array
        Console.WriteLine("Contains 7: " + numbers.Contains(7));
    }
}

class Employee
{
    // Default string name value = Empty
    public string Name { get; set; } = string.Empty;
    public int Age { get; set; }
}

class Product
{
    public string Name { get; set; } = string.Empty;
    public string Category { get; set; } = string.Empty;
}

class Student
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
}

class Grade
{
    public int StudentId { get; set; }
    public string GradeLetter { get; set; } = string.Empty;
}