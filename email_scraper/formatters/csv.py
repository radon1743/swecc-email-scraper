import csv
import io
from typing import Any, Dict

import click
from rich.console import Console

from . import OutputFormatter

console = Console(stderr=True)  # use stderr for status messages


class CsvFormatter(OutputFormatter):
    """Formats results as CSV."""

    name = "csv"
    description = "Format results as CSV"
    file_extension = "csv"

    def format(self, results: Dict[str, Any], **kwargs: Dict[str, Any]) -> str:
        """Format results as a CSV string.

        Args:
            results: Dictionary of results to format

        Returns:
            CSV-formatted string
        """
        
        try:
            if (isinstance(kwargs.get("unchecked"),bool)): #Checks for boolean value
                is_unchecked = kwargs.get("unchecked")
            else:
                raise TypeError(
                    f"[red] 'unchecked': not a boolean check -u flag [/red]"
                )
        except Exception as e:
            raise click.Abort() from e
        
        col = list(results.keys())
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=col)

        if not is_unchecked:
            try:
                rows = [
                    j
                    for j in results.values()
                    if type(j) is not int and type(j) is not str
                ]
                for row in rows:
                    if len(row) > 1:
                        raise ValueError(
                            f"\nsssThe value is imcompatible for csv file -> {row}"
                        )
            except Exception as e:
                console.print(
                    f"[red]Data is nested try with -u or --unchecked flag {e}[/red]"
                )
                raise click.Abort() from e
        writer.writeheader()
        writer.writerow(results)
        return output.getvalue()
