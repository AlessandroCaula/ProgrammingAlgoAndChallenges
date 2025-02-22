// DELEGATES
// - A type that holds a reference to a method(s)
// - Enables function pointers, allowing methods to be called dynamically.
// - Can be invoked directly like a method
// - Less restricted. Any class can call it
// 
// EVENTS
// - A wrapper around a delegate that restricts direct access.
// - Used for publisher-subscriber patterns where one object notifies others.
// - Can only be invoked within the declaring class.
// - More restricted. Only the class declaring it can raise it.

public class EventsAndDelegates
{
    public EventsAndDelegates()
    {
        // Delegate examples
        DelegateExample delegateExample = new DelegateExample();

        // Events examples
        Subscriber subscriber = new Subscriber();
    }
}

public class DelegateExample
{
    // Delegate declaration
    delegate void PrintDelegate(string message);

    // Method that matches delegate signature
    static void PrintMessage(string msg)
    {
        Console.WriteLine(msg);
    }

    // Delegate declaration
    delegate void MathOperation(int a, int b);

    // Methods that matches delegate signature
    static void Add(int a, int b)
    {
        Console.WriteLine($"Sum: {a + b}");
    }
    static void Multiply(int a, int b)
    {
        Console.WriteLine($"Product: {a * b}");
    }

    public DelegateExample()
    {
        // Assign method to the delegate
        PrintDelegate del = PrintMessage;
        del("Hello from delegate"); // Invokes method

        // Instantiate the delegate 
        MathOperation operation;
        // Assign methods to the delegate
        operation = Add;
        operation += Multiply; // Multicast delegate (calls both methods)
        // Invoke the delegate
        operation(5, 3);
    }
}

class Publisher 
{
    // Declare an event using a delegate 
    public event Action<string>? OnMessageReceived;

    public void SenMessage(string msg)
    {
        OnMessageReceived?.Invoke(msg); // Only this class can invoke it
    }

    // Declare an event using a delegate
    public event Action<string>? OnDataProcessed;

    public void ProcessData(string data)
    {
        Console.WriteLine("Processing data: " + data);

        // Raise event if there are subscribers
        OnDataProcessed?.Invoke(data);
    }
}

class Subscriber
{
    public Subscriber()
    {
        // 1) Example
        // 
        Publisher publisher = new Publisher();

        // Subscribe to event 
        publisher.OnMessageReceived += msg => Console.WriteLine("Received: " + msg);

        publisher.SenMessage("Hello from event!");

        // 2) Example
        // 
        publisher.OnDataProcessed += HandleEvent;
        // Trigger event
        publisher.ProcessData("Import Data");
    }

    static void HandleEvent(string message)
    {
        Console.WriteLine("Subscriber received: " + message);
    }
}