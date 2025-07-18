"""
Simple Hello World Python application
"""


def hello_world():
    """Return a Hello World message"""
    return "Hello World"


def main():
    """Main function to run the application"""
    message = hello_world()
    print(message)
    return message


if __name__ == "__main__":
    main()
