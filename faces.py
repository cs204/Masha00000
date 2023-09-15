def main():
	s = input()
	print(convert(s))

def convert(s):
	c = s.replace(":)","\N{Slightly Smiling Face}").replace(":(","\N{Slightly Frowning Face}")
	return c

main()
