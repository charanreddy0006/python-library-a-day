import typer

app = typer.Typer()

@app.command()
def greet(name: str):
    """
    Greet a user.
    """
    typer.echo(f"Hello, {name}! 👋")

@app.command()
def add(num1: int, num2: int):
    """
    Add two numbers.
    """
    typer.echo(f"Result: {num1 + num2}")

if __name__ == "__main__":
    app()