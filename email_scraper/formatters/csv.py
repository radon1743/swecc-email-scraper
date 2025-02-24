import json
from typing import Any, Dict

from . import OutputFormatter


class CsvFormatter(OutputFormatter):
    """Formats results as CSV."""

    name = "csv"
    description = "Format results as CSV"
    file_extension = "csv"

    def format(self, results: Dict[str, Any]) -> str:
        """Format results as a CSV file.

        Args:
            results: Dictionary of results to format

        Returns:
            JSON-formatted string
        """
        return json.dumps(results, indent=2)
