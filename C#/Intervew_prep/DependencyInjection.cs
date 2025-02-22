// Defining an interface that outline the contract for sending emails
public interface IEmailSender
{
    // In C# all members declared in an interface are implicitly public, and you cannot specify any access modifier on them. 
    // This because an interface is meant to define a public contract that any class must provide. 
    void SendEmail(string to, string subject, string body);
}

// Implement the email sender using an SMTP approach
public class SmtpEmailSender : IEmailSender
{
    // In C# if you don't explicitly define a constructor in a class, the compiler automatically provides a default parameterless constructor. 

    public void SendEmail(string to, string subject, string body)
    {
        // Simulate sending an email (in a real-world scenario, this would use an SMTP client)
        Console.WriteLine($"Sending email from first Smtp to {to}: {subject}\n{body}");
    }
}

// Implementing another email sender 
public class SmtpEmailSender1 : IEmailSender
{
    public void SendEmail(string to, string subject, string body)
    {
        Console.WriteLine($"Sending email from second Smtp to {to}: {subject}\n{body}");
    }
}

// A service responsible for sending notification to user
public class NotificationService
{
    // private -> This field is accessible only within the NotificationServices
    // readonly -> This ensures that the field can only be assigned once, either when declared or inside the constructor. This prevents accidental notification after object creation.
    // IEmailSender -> This is an interface type, allowing the class to work with any implementation of IEmailSender
    // _emailSender -> The naming convention (underscore _) is commonly used for private fields in C#
    private readonly IEmailSender _emailSender;

    // Constructor Injection: The email sender dependency is injected into the service.
    public NotificationService(IEmailSender emailSender)
    {
        _emailSender = emailSender;
    }

    // This method sends a notification email to the specified user
    public void Notify(string userEmail)
    {
        _emailSender.SendEmail(userEmail, "Welcome", "Thank you for signing up.");
    }
}

// Entry point for the Dependency Injection. 
public class DependencyInjection
{
    public DependencyInjection()
    {
        // Create an instance of the email sender (this could be swapped for a different implementation)
        IEmailSender emailSender = new SmtpEmailSender1();

        // Injecting the email sender dependency into the NotificationService
        NotificationService notificationService = new NotificationService(emailSender);

        // Send a welcome email to a sample user
        notificationService.Notify("user@example.com");
    }
}