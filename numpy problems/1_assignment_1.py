import numpy as np

sales = np.array([
    [12, 15, 11, 18, 14], 
    [9,  10, 13, 12, 16],  
    [20, 18, 22, 19, 21],  
    [7,  8,  6,  10, 9]    
])

print("Shape:", sales.shape)
print("Number of dimensions:", sales.ndim)
print("Total number of elements:", sales.size)
print("Product 3 sales:", sales[2])
print("Week 4 sales:", sales[:, 3])
greater_than_15 = sales[sales > 15]
print("Sales greater than 15:", greater_than_15)
total_sales = np.sum(sales)
average_sales = np.mean(sales)
print("Total sales:", total_sales)
print("Average sales:", average_sales)