def find_max(numbers):
    if not numbers:  # empty list case
        return None
    
    
    max_num = numbers[0]
    
   
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num

def main():
    numbers = [3, 5, 2, 8, 1, 10]
    
    max_number = find_max(numbers)
    
    if max_number is not None:
        print(f"Maximum number: {max_number}")
    else:
        print("The list is empty.")


if __name__ == "__main__":
    main()
