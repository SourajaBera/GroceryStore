import tkinter as tk
from tkinter import messagebox
from db_operations import add_product, view_products, update_stock, delete_product


class GroceryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Store Management")
        
        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Add Product Section
        self.name_label = tk.Label(self.root, text="Product Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)
        
        self.price_label = tk.Label(self.root, text="Price")
        self.price_label.grid(row=1, column=0)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=1, column=1)
        
        self.stock_label = tk.Label(self.root, text="Stock")
        self.stock_label.grid(row=2, column=0)
        self.stock_entry = tk.Entry(self.root)
        self.stock_entry.grid(row=2, column=1)
        
        self.add_button = tk.Button(self.root, text="Add Product", command=self.add_product)
        self.add_button.grid(row=3, columnspan=2)
        
        # View Products Section
        self.view_button = tk.Button(self.root, text="View Products", command=self.view_products)
        self.view_button.grid(row=4, columnspan=2)

        # Update Stock Section
        self.product_id_label = tk.Label(self.root, text="Product ID")
        self.product_id_label.grid(row=5, column=0)
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.grid(row=5, column=1)
        
        self.new_stock_label = tk.Label(self.root, text="New Stock")
        self.new_stock_label.grid(row=6, column=0)
        self.new_stock_entry = tk.Entry(self.root)
        self.new_stock_entry.grid(row=6, column=1)
        
        self.update_button = tk.Button(self.root, text="Update Stock", command=self.update_stock)
        self.update_button.grid(row=7, columnspan=2)
        
        # Delete Product Section
        self.delete_id_label = tk.Label(self.root, text="Product ID to Delete")
        self.delete_id_label.grid(row=8, column=0)
        self.delete_id_entry = tk.Entry(self.root)
        self.delete_id_entry.grid(row=8, column=1)
        
        self.delete_button = tk.Button(self.root, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=9, columnspan=2)

    def add_product(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        stock = int(self.stock_entry.get())
        add_product(name, price, stock)
        messagebox.showinfo("Success", "Product added successfully!")

    def view_products(self):
        products = view_products()
        products_str = "\n".join([f"ID: {p[0]}, Name: {p[1]}, Price: {p[2]}, Stock: {p[3]}" for p in products])
        messagebox.showinfo("Products", products_str)

    def update_stock(self):
        product_id = int(self.product_id_entry.get())
        new_stock = int(self.new_stock_entry.get())
        update_stock(product_id, new_stock)
        messagebox.showinfo("Success", "Stock updated successfully!")

    def delete_product(self):
        product_id = int(self.delete_id_entry.get())
        delete_product(product_id)
        messagebox.showinfo("Success", "Product deleted successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()
