



def calculate_total (price):
        discount = price * 0.2
        subtotal = price - discount
        gst = subtotal * 0.09
        return subtotal + gst

print(calculate_total(100))