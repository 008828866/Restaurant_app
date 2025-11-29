import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

# Menu items and prices
MENU_ITEMS = {
    "Tacos al Pastor": 2.50,
    "Quesadillas de Flor de Calabaza": 4.00,
    "Tostada de Tinga": 4.50,
    "Sopes de Chorizo": 3.50,
    "Enchiladas Verdes": 9.00,
    "Tamales Oaxaqueños": 4.00,
    "Pozole": 10.00,
    "Agua de Jamaica": 2.50,
    "Horchata": 2.50,
    "Agua de Tamarindo": 2.50
}

# This list will store what the user orders
order = []

# Function to add a menu item and quantity to the order
def add_item():
    item = item_var.get()
    if not item:
        messagebox.showerror("Error", "Please select an item.")
        return
    # Ask user how many they want
    qty = simpledialog.askinteger("Quantity", f"How many '{item}'?", minvalue=1, maxvalue=99)
    if qty:
        order.append((item, qty))
        messagebox.showinfo("Added", f"Added {qty} x {item}")
    else:
        messagebox.showinfo("No item added", "No item was added.")

# Function to show order, calculate total, and ask if order correct
def show_order():
    # Make sure the user enters name
    if not name_var.get().strip():
        messagebox.showerror("Missing Name", "Enter your name.")
        return
    # Make sure at least one item is ordered
    if not order:
        messagebox.showerror("No items", "No items added.")
        return
    summary = f"Order for {name_var.get()}:\n\n"
    total = 0.0
    # Go through all items in the order and calculate total
    for item, qty in order:
        price = MENU_ITEMS[item] * qty
        summary += f"{qty} x {item} @ ${MENU_ITEMS[item]:.2f} = ${price:.2f}\n"
        total += price
    summary += f"\nTotal: ${total:.2f}\n\nIs this correct?"
    # Ask user to confirm
    confirm = messagebox.askyesno("Confirm Order", summary)
    if confirm:
        messagebox.showinfo("Order Confirmed", f"Thank you, {name_var.get()}! Total: ${total:.2f}")
        main.destroy()  # Close the app

# GUI setup

main = tk.Tk()
main.title("Mexican Food Ordering App")
main.geometry("350x300")

# Welcome message
tk.Label(main, text="Welcome to CDMX Eats!", font=("Arial", 16), fg="green").pack(pady=10)

# Name entry
tk.Label(main, text="Enter your name:", font=("Arial", 12)).pack()
name_var = tk.StringVar()
tk.Entry(main, textvariable=name_var, font=("Arial", 12)).pack(pady=5)

# Menu item selection
tk.Label(main, text="What would you like to eat?:", font=("Arial", 12)).pack()
item_var = tk.StringVar()
item_combo = ttk.Combobox(main, textvariable=item_var, state="readonly", font=("Arial", 12))
item_combo['values'] = list(MENU_ITEMS.keys())
item_combo.pack(pady=5)
item_combo.current(0)

# Buttons to add to order and finish  order
tk.Button(main, text="Add Item", command=add_item, bg="yellow", font=("Arial", 12)).pack(pady=10)
tk.Button(main, text="Finish Order", command=show_order, bg="green", fg="white", font=("Arial", 12)).pack()

main.mainloop()
