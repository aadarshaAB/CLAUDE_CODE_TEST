ascii_art = """
 _   _      _ _         _____ _            _ _
| | | |    | | |       / ____| |          | | |
| |_| | ___| | | ___  | |    | | __ _ _   _| | | ___
|  _  |/ _ \ | |/ _ \ | |    | |/ _` | | | | | |/ _ \\
| | | |  __/ | | (_) || |____| | (_| | |_| | | |  __/
|_| |_|\___|_|_|\___/  \_____|_|\__,_|\__,_|_|_|\___|

"""

with open('hello_claude.txt', 'w') as f:
    f.write(ascii_art)

print("ASCII art saved to 'hello_claude.txt'")
print("\nPreview:")
print(ascii_art)
