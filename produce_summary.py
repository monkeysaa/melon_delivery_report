def print_deliveries(file_list):
    for index, filename in enumerate(file_list):
        print(f"Day {index + 1}")
        the_file = open(filename)
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')
            
            melon = words[0]
            count = words[1]
            amount = words[2]
            
            print(f"Delivered {count} {melon}s for a total of ${amount}")
        the_file.close()
        print("\n")


file_list = ["um-deliveries-20140519.txt", 
            "um-deliveries-20140520.txt", 
            "um-deliveries-20140521.txt"]
            
print_deliveries(file_list)
