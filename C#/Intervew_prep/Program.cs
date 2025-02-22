﻿using Inventory;
using SensorSystem;
using Analyzer;

class Program
{
    static void Main()
    {
        Console.WriteLine("-- DependencyInjection");
        DependencyInjection dependencyInjection = new DependencyInjection();

        Console.WriteLine("\n-- LINQ");
        LinqClass linqClass = new LinqClass();

        Console.WriteLine("\n-- Inventory Management system");
        InventoryManagementSystem inventoryManagementSystem = new InventoryManagementSystem();

        Console.WriteLine("\n-- Sensor Data");
        SensorDataProcessingSystem sensorDataProcessingSystem = new SensorDataProcessingSystem();

        Console.WriteLine("\n-- Delegate and Events");
        EventsAndDelegates eventsAndDelegates = new EventsAndDelegates();

        Console.WriteLine("\n-- Log Analyzer");
        LogAnalyzerEntryPoint logAnalyzerEntryPoint = new LogAnalyzerEntryPoint();
    }
}