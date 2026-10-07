r"""Polars io-plugin backed by fastavro.

This plugin allows reading, writing, and scanning avro files into polars
DataFrames using the fastavro library.

Usage
-----

 .. code-block:: python

    from polars_fastavro import scan_avro, read_avro, write_avro

    frame = scan_avro(...).collect()  # or `read_avro(...)`
    write_avro(frame, dest)

Limitations
-----------

1. Because it uses python types as an intermediary, it's slow, (30x read to 80x
   write).
2. Since this is ultimately converting between avro and arrow, it has no support
   for avro maps or unions (other than null).
3. Every type is treated as nullable.
4. Additionally, some types could in theory be supported but aren't for technical
   reasons. These include uuid and duration.
5. Timestamp support is limited. local-timestamp-\*s are treated as Datetime
   without tz info, while timestamp-\*s are treated as UTC Datetime. Writing
   Datetimes with nano-precision or other time zones is also not supported.
6. This can't read cloud files, as that functionality isn't exposed in python to
   my knowledge.
"""

from ._scan import read_avro, scan_avro
from ._sink import write_avro

__all__ = ("read_avro", "scan_avro", "write_avro")
