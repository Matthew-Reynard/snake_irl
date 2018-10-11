import click

# print("Hello World!")

@click.command(options_metavar='<options>')
@click.option("-d", "--difficulty", default="medium", help="Difficulty setting: <easy>, <medium> (default), <hard> or <insane>", metavar='<text>', prompt=True)
def main(difficulty):
	"""This is main function"""

	print("hey %s" %difficulty)


# if __name__ == '__main__':
	# print("main")
