letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Jarvis").replace("<|Date|>", "24th september 2050")) # chaining of .replace function