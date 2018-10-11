from setuptools import setup

setup(
	name="Snake",
	version="1.0",
	description="Snake game",
	author="Matthew Reynard",
	author_email="matthewreynard24@gmail.com",
	url="www.matthewreynard.com",
	# packages=["snake"],
	py_modules=[
	"snakeAI",
	"foodAI",
	"obstacleAI",
	"SnakeGame",
	"QLearn"
	],
	install_requires=[
	"numpy",
	"pygame",
	"pandas",
	"click"
	],
	entry_points={
		'console_scripts': ['play=play:play', 'replay=replay:watch'],
	},
)