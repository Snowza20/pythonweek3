
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount, or the original price if discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
    else:
        final_price = price
    
    return final_price


original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))


final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after applying the discount is: ${final_price:.2f}")
