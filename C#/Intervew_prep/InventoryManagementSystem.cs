namespace Inventory
{
    public class InventoryManagementSystem
    {
        public InventoryManagementSystem()
        {
            Inventory inventory = new Inventory();
            Product prod1 = new Product("Product 1", 50.77);
            Product prod2 = new Product("Product 2", 10.99);
            Product prod3 = new Product("Product 3", 105.5);

            inventory.AddProduct(prod1);
            inventory.AddProduct(prod2);
            inventory.AddProduct(prod3);

            // Display current inventory
            Console.WriteLine("Inventory: ");
            foreach (Product prod in inventory.GetProducts())
            {
                Console.WriteLine($"Id: {prod.ID} - Name: {prod.Name} - Price: {prod.Price} $");
            }
        }
    }

    /// <summary>
    /// Product class
    /// </summary>
    public class Product
    {
        // GUID (Globally Unique Identifier). It's a 128-bit integer number used to identify resources. 
        public Guid ID { get; } = Guid.NewGuid();
        public string Name { get; set; } = string.Empty;
        public double Price { get; set; }

        // Constructor for creating a new product
        public Product(string name, double price)
        {
            Name = name;
            Price = price;
        }
    }

    /// <summary>
    /// Inventory class
    /// </summary>
    public class Inventory
    {
        // Collection of Products
        private List<Product> productCollection;

        // Constructor
        public Inventory()
        {
            productCollection = new List<Product>();
        }

        /// <summary>
        /// Method to add a new product
        /// </summary>
        public void AddProduct(Product product)
        {
            // // Generate a unique identifier
            // string uniqueIdentifier = string.Empty;
            // while (true)
            // {
            //     // Generate a unique identifier
            //     uniqueIdentifier = RandomIdentifier();
            //     // Check whether the unique identifier does not yet exists. Otherwise generate another identifier.
            //     if (!productCollection.Select(p => p.ID).Contains(uniqueIdentifier))
            //         break;
            // }

            // // Create the new product object and add it to the collection
            // Product newProduct = new Product
            // {
            //     ID = uniqueIdentifier,
            //     Name = productName,
            //     Price = productPrice
            // };

            // Add the new product to the collection of products
            productCollection.Add(product);
        }

        /// <summary>
        /// Method used to remove the product by its ID
        /// </summary>
        public void RemoveProductByIdx(Guid productID)
        {
            var productToRemove = productCollection?.FirstOrDefault(p => p.ID == productID);
            if (productToRemove != null)
                productCollection?.Remove(productToRemove);
        }

        /// <summary>
        /// Method to update the product details
        /// </summary>
        public void UpdateProductDetails(Guid productID, string productNewName, double productNewPrice = double.NaN)
        {
            // Retrieve the product with the specific ID
            var productToUpdate = productCollection?.FirstOrDefault(p => p.ID == productID);

            if (productToUpdate == null)
                return;

            // Rename the product 
            if (productNewName != null)
                productToUpdate.Name = productNewName;
            // Reprice the product
            if (!double.IsNaN(productNewPrice))
                productToUpdate.Price = productNewPrice;
        }

        // Return all the products in the inventory
        public List<Product> GetProducts() => productCollection;

        // /// <summary>
        // /// Method to generate a Random Identifier for the new product
        // /// </summary>
        // /// <returns></returns>
        // private string RandomIdentifier()
        // {
        //     Random random = new Random();
        //     string pool = "abcdefghijklmnopqrstuvwxyz0123456789";
        //     string identifier = "#";
        //     for (int i = 0; i < 5; i++)
        //     {
        //         var c = pool[random.Next(0, pool.Length)];
        //         identifier += c;
        //     }
        //     return identifier;
        // }
    }

    /// <summary>
    /// Order class
    /// </summary>
    public class Order
    {
        public List<Product> OrderedProducts { get; } = new List<Product>();

        // Add a product to the order
        public void AddProduct(Product product)
        {
            OrderedProducts.Add(product);
        }

        // Calculates the total cost of the order
        public double GetTotalCost()
        {
            return OrderedProducts.Sum(p => p.Price);
        }

        // If total cost exceeds $100, apply 10% discount.
        public double GetTotalCostWithDiscount()
        {
            double total = GetTotalCost();
            if (total > 100)
            {
                total = total - (total * 0.1);
            }
            return total;
        }
    }
}