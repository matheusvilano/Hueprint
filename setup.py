import setuptools
from pathlib import Path

long_description = (Path(__file__).parent/"README.md").read_text()

setuptools.setup(
		author="Matheus Vilano",
		author_email="",
		classifiers=[
			"Development Status :: 5 - Production/Stable",
			"Intended Audience :: Developers",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Programming Language :: Python :: 3",
		],
		description="A simple package that enables coloured output in Python console applications.",
		install_requires=[],
		keywords="colour color hue console output print terminal text style format effect ANSI escape sequence",
		license="MIT",
		long_description=long_description,
		long_description_content_type="text/markdown",  # GitHub-flavored Markdown (GFM)
		name="hueprint",
		packages=setuptools.find_packages("src"),
		package_dir={"": "src"},
		project_urls={
			"Author Website": "https://www.matheusvilano.com/",
			"Git Repository": "https://github.com/matheusvilano/hueprint",
		},
		python_requires=">=3.6",
		url="https://github.com/matheusvilano/hueprint.git",
		version="1.0.0",
)
