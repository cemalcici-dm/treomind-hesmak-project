import typer

from .hesapla import hesap_makinesi
from .islemler import topla

app = typer.Typer()


@app.command(name="hesapla")
def hesap_makinesi(
    a: int = typer.Option(
        help="Birinci sayıyı temsil eder."
    ),
    b: int = typer.Option(
        help="İkinci sayıyı temsil eder."
    ),
    secenek: int = typer.Option(
        help="İşlem türünü temsil eder. "
        "1: Toplama "
        "2: Çıkarma "
        "3: Çarpma "
        "4: Bölme"
    )
):
    operator = {
        1: "+",
        2: "-",
        3: "*",
        4: "/"
    }.get(secenek)

    typer.echo(f'{a} {operator} {b} = {hesap_makinesi(a, b, secenek)}')


@app.command()
def toplama(
    a: int = typer.Option(
        help="Birinci sayıyı temsil eder."
    ),
    b: int = typer.Option(
        help="İkinci sayıyı temsil eder."
    )
):
    typer.echo(f'{a} + {b} = {topla(a, b)}')


if __name__ == '__main__':
    app()
