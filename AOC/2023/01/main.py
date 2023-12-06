import re
file = open('input1.txt')

input = file.read().split('\n')


def main():
  for location in input:
    string_letters_removed = re.sub('[a-z]', '', location)
    #print(len(string_letters_removed))
    if len(string_letters_removed) == 1:
      new_value = f'{string_letters_removed}{string_letters_removed}'
      print(new_value)
    
    # remove extra numbers
    if len(string_letters_removed) >= 1:
      print(string_letters_removed[0])
    # SUM them


if __name__ == '__main__':
  main()
