import emoji

inp_str = input()
out_str = emoji.emojize(inp_str, language='alias')
out_str = out_str.strip()
print(f"{out_str}")
