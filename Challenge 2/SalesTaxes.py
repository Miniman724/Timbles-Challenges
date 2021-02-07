# Timbles Challenge 2
# Sales Taxes

# import regex
import re

# Global Variables

# Regex pattern for inputs
input_pattern = "^[0-9]+ [a-zA-Z\s]+ at \d+\.[0-9]{2}\n$"
# Sales tax, in %
sales_tax = 10
# Import tax in %
import_tax = 5
# Excluded items from tax
excluded = ["book", "chocolate bar", "pills", "chocolates"]

# Helper Functions

# custom round function
def custom_round(value):
    temp = int(value * 100)
    ones = (temp % 10)
    if ones < 5 and ones != 0:
        #value = float(value)
        temp = temp + (5 - ones)
        return float(temp / 100)
    else:
        return round(value, 2)

# loads input from filename.txt into the given input_array
def load_input(filename):

    input_array = []
    file = None

    while (True):
        try:
            file = open(f"{filename}.txt", "r")
            break
        except:
            filename = input("Invalid file, please try again")

    print("The following input is invalid and has not been included:")

    for line in file:
        if (re.match(input_pattern, line)):
            input_array.append(line[:-1])
        else:
            print(line)

    file.close()
    return input_array

# gets input through manual input
def get_input():
    input_array = []
    while (True):
        line = input("Give input or exit [E]:")
        if (re.match(input_pattern, line)):
            input_array.append(line[:-1])
        elif (line == "E"):
            break
        else:
            print("The input is invalid and has not been included")
    return input_array

# Cleans the input and calculates the tax, puts it into the input_dictionary array
def clean_input(input_array):
    input_dictionary = {"items": []}
    for i in input_array:
        item_contents = i.split()
        quantity = int(item_contents[0])
        price = float(item_contents[-1])

        imported = None
        name = None

        if "imported" in item_contents:
            imported = True
            item_contents.remove("imported")
        else:
            imported = False

        name = item_contents[1:-2]
        name = " ".join(name)

        tax = 100

        if imported:
            tax += import_tax

        tax += sales_tax

        for excluded_item in excluded:
            if excluded_item in item_contents:
                tax -= sales_tax


        total_price = (quantity * price * (tax / 100))

        total_price = custom_round(total_price)

        new_input = {"name": name, "quantity": quantity, "price": price, "imported": imported, "total": total_price}
        input_dictionary["items"].append(new_input)

    return input_dictionary


# ----------------------------------------------------------------------------------------------------------------------


# Which kind of input?
choice = input("Do you want Text File input [T] or Manual input [M]?")

# Array to store input lines
input_lines = []

while (True):
    # If text file input
    if (choice == "T"):
        # Request file name
        filename = input("What is the name of the .txt file? (Don't include .txt)")
        # load input from file name
        input_lines = load_input(filename)
        break
    # If manual input
    elif (choice == "M"):
        # Get input
        input_lines = get_input()
        break
    # If neither
    else:
        # Get new input and loop again
        choice = input("Invalid choice please try again:")

# Dictionary to hold inputted sales
input_sales = {}

# Cleans the input from the file
input_sales = clean_input(input_lines)

added_taxes = 0
total_sale_price = 0

for item in input_sales["items"]:
    quantity = item["quantity"]
    name = item["name"]
    price = item["price"]
    total = item["total"]
    import_suffix = ""
    if item["imported"]:
        import_suffix = "imported "
    print(f"{quantity} {import_suffix}{name}: {'%.2f' % total}")
    added_taxes += total - price
    total_sale_price += total

print(f"Sales Taxes: {'%.2f' % added_taxes}")
print(f"Total: {'%.2f' % total_sale_price}")


