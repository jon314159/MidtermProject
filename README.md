# Command-Line Calculator

A fully interactive command-line calculator built in Python. This tool uses design patterns (Factory, Observer, Memento) and features a Read-Eval-Print Loop (REPL) interface with undo/redo, history persistence, and configurable settings via environment variables.

---

## 📦 Features

- Supports basic and advanced arithmetic operations  
- Maintains command and calculation history  
- Undo and Redo functionality using the Memento Design Pattern  
- Auto-saving history to CSV via Observer Design Pattern  
- Help, clear, save, and load commands  
- Input validation with custom exceptions  
- Modular and extensible design  

---

## 🔧 Installation Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/jon314159/MidtermProject
   cd your-repo

    Set up a virtual environment

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

Install dependencies

    pip install -r requirements.txt

⚙️ Configuration Setup

    Create a .env file in your project root with the following:

    CALCULATOR_LOG_DIR=logs
    CALCULATOR_HISTORY_DIR=history
    CALCULATOR_MAX_HISTORY_SIZE=100
    CALCULATOR_AUTO_SAVE=true
    CALCULATOR_PRECISION=2
    CALCULATOR_MAX_INPUT_VALUE=1000000
    CALCULATOR_DEFAULT_ENCODING=utf-8

    These values control limits, storage directories, and output precision.

🚀 Usage Guide

Start the calculator by running:

python -m app.calculator

Supported Commands:
Command	Description
add a b	Add two numbers
subtract a b	Subtract b from a
multiply a b	Multiply two numbers
divide a b	Divide a by b
power a b	Raise a to the power of b
root a b	Compute the b-th root of a
modulus a b	a modulo b
int_divide a b	Integer division of a by b
percent a b	b percent of a
abs_diff a b	Absolute difference between a and b
undo	Undo the last calculation
redo	Redo the previously undone calculation
history	Show command history
clear	Clear history
save	Save current history to file
load	Load saved history from file
help	Show help message
exit	Exit the calculator
✅ Testing Instructions

    Run unit tests

pytest

Show detailed output

pytest -v

Measure test coverage

    pytest --cov=app --cov-report=term-missing

🔄 CI/CD with GitHub Actions

A basic workflow is included in .github/workflows/python-app.yml:

    Automatically runs tests on push and pull requests

    Ensures code integrity across Python versions

📝 Code Style

    All modules use type hints and docstrings

    Exceptions are meaningful and user-guiding

    Observer and Memento patterns are used for history and state management

    Environment-driven configuration (app/config.py)

📂 Logging

Ensure the logs folder exists or set CALCULATOR_LOG_DIR=logs in your .env.
You may configure logging in logger.py for info/warning/error levels.

📄 License

MIT License

Copyright (c) 2025 [Jonathan Capalbo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      
copies of the Software, and to permit persons to whom the Software is          
furnished to do so, subject to the following conditions:                       

The above copyright notice and this permission notice shall be included in     
all copies or substantial portions of the Software.                            

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN      
THE SOFTWARE.