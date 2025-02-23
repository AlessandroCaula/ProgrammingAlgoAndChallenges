using System.Globalization;
using System.Security.Cryptography.X509Certificates;

namespace Analyzer
{
    // Entry point
    class LogAnalyzerEntryPoint
    {
        public LogAnalyzerEntryPoint()
        {
            // Retrieve the Mock data source. Here you could change the data source, so that different mock data source can be injected into the logAnalyzer.
            ILogDataSource dataSource = new MockLogDataSource();
            // Injecting the data source.
            LogAnalyzer analyzer = new LogAnalyzer(dataSource);

            Console.WriteLine("Error Logs:");
            foreach (var log in analyzer.GetLogsByLevel("ERROR"))
            {
                Console.WriteLine(log);
            }

            Console.WriteLine("\nError Count Per Hour: ");
            foreach (var kvp in analyzer.CountErrorPerHour())
            {
                Console.WriteLine($"Hour {kvp.Key}: {kvp.Value} errors");
            }
        }
    }

    // Single log entry objects
    class LogEntry
    {
        public DateTime TimeStamp { get; }
        public string LogLevel { get; }
        public string Message { get; }

        public LogEntry(DateTime timeStamp, string logLevel, string message)
        {
            TimeStamp = timeStamp;
            LogLevel = logLevel;
            Message = message;
        }

        public override string ToString()
        {
            return $"{TimeStamp:yyyy-MM-dd HH:mm:ss} [{LogLevel}] {Message}";
        }
    }

    class LogParser
    {
        // Method used to parse logLines and create new LogEntry Objects.
        public LogEntry ParseLogLine(string logLine)
        {
            string[] parts = logLine.Split("|");
            if (parts.Length < 3)
                throw new FormatException("Invalid log Format");

            DateTime dateTime = DateTime.ParseExact(parts[0].Trim(), "yyyy-MM-dd HH:mm:ss", CultureInfo.InvariantCulture);
            string level = parts[1].Trim();
            string message = parts[2].Trim();

            return new LogEntry(dateTime, level, message);
        }
    }

    interface ILogDataSource
    {
        // The difference between IEnumerable and List (besides one being an interface and the other being a concrete class) is that IEnumerable is read-only and List is not.
        // So if you need the ability to make permanent changes of any kind to your collection (add & remove), you'll need a List. If you just need to read, sort and/or filter your collection, IEnumberable is sufficient for that purpose.
        IEnumerable<string> GetLogLines();
    }

    // Example of Log Data Source.
    class MockLogDataSource : ILogDataSource
    {
        public IEnumerable<string> GetLogLines()
        {
            return new List<string>
            {
                "2025-02-23 14:30:00 | INFO | System started",
                "2025-02-23 14:45:12 | ERROR | Disk space low",
                "2025-02-23 15:10:30 | WARN | High memory usage",
                "2025-02-23 15:22:45 | ERROR | Connection timeout",
                "2025-02-23 15:45:00 | ERROR | Failed to save file",
                "2025-02-23 16:00:10 | INFO | User logged in"
            };
        }
    }

    class LogAnalyzer
    {
        private readonly ILogDataSource _dataSource;
        private readonly LogParser _parser;

        public LogAnalyzer(ILogDataSource dataSource)
        {
            // Injecting the Mock data source into the analyzer
            _dataSource = dataSource;
            // Instantiating the LogParser
            _parser = new LogParser();
        }

        // Method for filtering and retrieving the log entries by level
        public List<LogEntry> GetLogsByLevel(string level)
        {
            // Collection of LogEntries with the specific level
            List<LogEntry> logEntries = new List<LogEntry>();
            // Retrieve the log lines
            IEnumerable<string> logLines = _dataSource.GetLogLines();
            // Parse the log lines into LogEntries, and return only those which match logLevel
            foreach (string logLine in logLines)
            {
                // Parse the logLine into a new LogEntry object.
                LogEntry logLineEntry = _parser.ParseLogLine(logLine);
                // Check if the logLevel is the same. If it is then add it to the final collection. 
                if (logLineEntry.LogLevel == level)
                    logEntries.Add(logLineEntry);
            }

            return logEntries;
        }

        // Method for retrieving the number of errors per hours
        public Dictionary<int, int> CountErrorPerHour()
        {
            // Retrieve the list of logs with the Error, from the GetLogsByLevel
            List<LogEntry> errorLogs = GetLogsByLevel("ERROR");
            
            // Group them by Hour
            Dictionary<int, int> errorPerHour = errorLogs.GroupBy(entry => entry.TimeStamp.Hour).ToDictionary(group => group.Key, group => group.Count());

            // Group them by Hour
            Dictionary<int, int> errorPerHour1 = new Dictionary<int, int>();
            // Loop through the errorLogs
            foreach (LogEntry errorLog in errorLogs)
            {
                if (!errorPerHour1.Keys.Contains(errorLog.TimeStamp.Hour))
                    errorPerHour1[errorLog.TimeStamp.Hour] = 1;
                else
                    errorPerHour1[errorLog.TimeStamp.Hour] += 1;
            }

            return errorPerHour1;
        }
    }
}