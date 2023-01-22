"""
"""

from pathlib import Path


def base_function_1():
    current_file = Path(__file__).resolve()

    print(f'Hello, From Base Process: {current_file.name}')


def main():
    base_function_1()


if __name__ == '__main__':
    main()
