user_input = input("input any string: ")

def title(input: str) -> str:
    input = input.strip()
    if not input:
        return input
    char_list = [char for char in input]
    for char in range(len(char_list)):
        if char_list[char] == ' ':
            char_list[char + 1] = char_list[char + 1].upper()
    char_list[0] = char_list[0].upper()
    fin_str = ''.join(char_list)
    return fin_str

print(title(user_input))