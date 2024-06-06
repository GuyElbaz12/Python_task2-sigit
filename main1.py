#1
def find_longest_name(file_path):
    with open('names.txt', 'r') as file:
        names = file.readlines()
        names = [name.strip() for name in names]  # Remove any trailing newlines or spaces
        if not names:
            print("The file is empty.")
            return
        longest_name = max(names, key=len)  # Find the longest name based on length
        print("The longest name is:")
        print(longest_name)


if __name__ == '__main__':
    file_path = 'names.txt'  # Ensure this file is in the same directory as the script
    find_longest_name(file_path)

#2
def sum_of_name_lengths(file_path):
  with open('names.txt', 'r') as file:
    names = file.readlines()
    names = [name.strip() for name in names]  # Remove any trailing newlines or spaces
    total_length = sum(len(name) for name in names)  # Calculate the sum of lengths of all names
    print("The sum of the lengths of the names is:")
    print(total_length)


if __name__ == '__main__':
  file_path = 'names.txt'  # Ensure this file is in the same directory as the script
  sum_of_name_lengths(file_path)

#3
  def find_shortest_names(file_path):
    with open('names.txt', 'r') as file:
      names = file.readlines()
      names = [name.strip() for name in names]  # Remove any trailing newlines or spaces
      if not names:
        print("The file is empty.")
        return
      min_length = min(len(name) for name in names)  # Find the shortest length
      shortest_names = [name for name in names if len(name) == min_length]  # Collect all shortest names
      print("The shortest names are:")
      for name in shortest_names:
        print(name)

if __name__ == '__main__':
  file_path = 'names.txt'  # Ensure this file is in the same directory as the script
  find_shortest_names(file_path)

#4
  def write_name_lengths(input_file, output_file):
      with open('names.txt', 'r') as file:
          names = file.readlines()  # Read all lines from the input file

      # Open the output file in write mode
      with open('name_length.txt', 'w') as output:
          # Write the length of each name to the output file, one per line
          for name in names:
              output.write(f"{len(name.strip())}\n")


  if __name__ == '__main__':
      input_file = 'names.txt'  # Input file containing names
      output_file = 'name_length.txt'  # Output file to write the lengths
      write_name_lengths(input_file, output_file)
#5
def find_names_by_length(filename, length):

  with open('names.txt', 'r') as file:
    for line in file:
      name = line.strip()  # Remove trailing newline character
      if len(name) == length:
        print(name)
desired_length = int(input("Enter the desired name length: "))
find_names_by_length("names.txt", desired_length)