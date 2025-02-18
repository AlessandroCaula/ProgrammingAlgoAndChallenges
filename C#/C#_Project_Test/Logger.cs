using System;

public class Logger 
{
    string stringToLog;

    public Logger(string whatToLog)
    {
        this.stringToLog = whatToLog;
    }

    public void PrintToConsole()
    {
        Console.WriteLine(stringToLog);
    }
}