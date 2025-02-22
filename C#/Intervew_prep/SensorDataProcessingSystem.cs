using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace SensorSystem
{
    public class SensorDataProcessingSystem
    {
        public SensorDataProcessingSystem()
        {
            // Tunning the Running simulation method asynchronously and wait for its completion.
            Task.Run(async () => await RunningSimulation()).Wait();
        }

        public static async Task RunningSimulation()
        {
            // Create a list of sensors
            List<Sensor> sensors = new List<Sensor>
            {
                new Sensor(),
                new Sensor(),
                new Sensor()
            };

            // Define acceptable sensor value range (temperature between 18 and 35 C)
            SensorProcessor processor = new SensorProcessor(15, 35);

            // Run the simulation for 10 seconds
            int simulationDurationMs = 3000;
            int readingIntervalMs = 1000; // Each sensor generates a reading every second

            // Get a cancellation token that cancels after simulationDurationMs
            CancellationTokenSource cts = new CancellationTokenSource(simulationDurationMs);

            Console.WriteLine("Starting sensor data simulation...\n");

            // Task list for running sensor concurrently. Each task represents an asynchronous operation. Each sensor running concurrently.
            List<Task> sensorTasks = new List<Task>();

            // For each sensor, start a task that continuously generates data until cancellation is requested
            foreach (var sensor in sensors)
            {
                sensorTasks.Add(Task.Run(async () =>
                {
                    while (!cts.IsCancellationRequested)
                    {
                        SensorData data = await sensor.GenerateDataAsync(readingIntervalMs);
                        processor.AddData(data);
                        Console.WriteLine(data);
                    }
                }, cts.Token));
            }

            // Wait until the simulation period is over
            await Task.WhenAll(sensorTasks);

            Console.WriteLine("\nSimulation complete.");
            double average = processor.ComputeAverage();
            Console.WriteLine($"Average Sensor Value (filtered): {average:F2}");
        }
    }

    // Class that simulates a sensor that generates random data. 
    // It has a method to generate random sensor data (for example, a temperature or pressure reading)
    // It should simulate data generation at set intervals. 
    public class Sensor
    {
        public Guid Id { get; } = Guid.NewGuid();
        private readonly Random _random = new Random();

        // Generate a sensor reading asynchronously
        public async Task<SensorData> GenerateDataAsync(int delayMilliseconds)
        {
            // Simulate waiting for data generation interval
            await Task.Delay(delayMilliseconds);
            // Generate a random value (e.g. temperature between 15 and 40 C)
            double value = _random.NextDouble() * 25 + 15;
            return new SensorData(Id, value);
        }
    }

    // Class that represents a single sensor reading. 
    // Contains properties such as the value (a numeric type), a TimeStamp and the sensor's ID
    public class SensorData
    {
        public Guid SensorID { get; }
        public double Value { get; }
        public DateTime TimeStamp { get; }

        public SensorData(Guid sensorID, double value)
        {
            SensorID = sensorID;
            Value = value;
            TimeStamp = DateTime.Now;
        }

        // Return the sensorData 
        public override string ToString() => $"Sensor: {SensorID}, value: {Value:F2}, Time:{TimeStamp:HH:mm:ss}";
    }

    // Processes sensor data from multiple sensors. 
    // Collects data from multiple sensors.
    // Filters out anomalies (readings that fall outside a predefined acceptable range)
    // Compute statistics such as the average value from the filtered data.
    public class SensorProcessor
    {
        private readonly List<SensorData> _collectedData = new List<SensorData>();
        private readonly double _minAcceptable;
        private readonly double _maxAcceptable;

        public SensorProcessor(double minAcceptable, double maxAcceptable)
        {
            _minAcceptable = minAcceptable;
            _maxAcceptable = maxAcceptable;
        }

        // Add a sensor reading if it's within the acceptable range
        public void AddData(SensorData data)
        {
            // Filter out anomalies
            if (data.Value >= _minAcceptable & data.Value <= _maxAcceptable)
            {
                _collectedData.Add(data);
            }
            else
            {
                Console.WriteLine($"Anomaly detected: {data}");
            }
        }

        // Computes and returns the average value of the accepted sensor data
        public double ComputeAverage()
        {
            if (_collectedData.Count == 0)
                return 0;
            return _collectedData.Average(d => d.Value);
        }
    }
}


