# the Toki Pona Word Generator

I wrote 2 small python scripts that use iteration to generate all possible toki pona words as a challenge, and I've been asked to release it to the public so here it is!

## How it Works
If you want the details, you're free to look at the code as I have put lots of comments. If you need any help understanding how the code works (or of course ifyou find any issues with it) do open an issue to let me know! But also keep in mind that a Python tutorial will probably help you way more than I can cause this is like my 3rd python project.

## How to Use
Technically you only need to have the `possible words.py` file to generate the word list, but if you want you can generate the syllables yourself with `syllables.py`.
### What Do You Need
- Python
  - I am using Python 3.12.0. Check your version with `py -V` in your terminal. If you don't have python, [Download it here](https://www.python.org/).
- Pip
  - Pip is the package installer for Python, which you will need for the nice prograss bar I struggled oh so much to implement (to remind you, this is like my 3rd time coding in Python). If you've installed Python, you already have it! Make sure it's for the same version of Python yo're using to run the project with `pip --version`.
- tqdm
  - tqdm is a package that uses some unknown magic to generate a progress bar for your loops, which if you don't know is like the entirety of this program. Install it with `pip install tqdm`.

### How to Run
Open your console in the project's folder (either by `cd`ing there or by bringing it up in the folder itself) and run `py '.\fileName.py'`.
- Run `'.\possible words.py'` to generate the word list,
- Run `.\syllables.py` to generate the syllables themselves.