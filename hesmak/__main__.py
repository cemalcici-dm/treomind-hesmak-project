from typing import Optional
from typing_extensions import Annotated

import typer

from .utils import version_callback
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
    ),
    version: Annotated[
        Optional[bool],
        typer.Option(
            '--version',
            help='Get version info of the application.', 
            callback=version_callback
        )
    ] = None
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
