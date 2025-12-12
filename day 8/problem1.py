import math
def print_calu(height, width , cover):
    total_cans = math.ceil((height * width) / 5)
    print(f"You'll neet {total_cans} of paint")




test_h = int(input('Enter the height of the wall : '))
test_w = int(input("Entet rhe width of the wall : "))
coverage = 5
print_calu(height=test_h, width = test_w, cover = coverage)