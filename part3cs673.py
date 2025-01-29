def parse_list(input_str):
    return input_str.strip('[]').split(',')

def main():
    list1_input = input("Enter the first list in the format [a,b,c]: ")
    list2_input = input("Enter the second list in the format [1,2,3]: ")

    list1 = parse_list(list1_input)
    list2 = parse_list(list2_input)

    if len(list1) != len(list2):
        print("Error: The lists are not of equal length.")
    else:
        combined_list = [item for pair in zip(list1, list2) for item in pair]
        print(f"Combined list: {combined_list}")

if __name__ == "__main__":
    main()