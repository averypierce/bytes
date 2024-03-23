import pytest
import math
from lib.bytes import (
    Bytes,
    Kilobytes,
    Megabytes,
    Gigabytes,
    Terabytes,
    count_zeros_after_decimal,
    rounder,
)


def test_count_zeros():
    assert count_zeros_after_decimal(0) == 0
    assert count_zeros_after_decimal(0.1) == 0
    assert count_zeros_after_decimal(0.01) == 1
    assert count_zeros_after_decimal(10) == 0
    assert count_zeros_after_decimal(0.00097) == 3


def test_rounder():
    assert rounder(0.00097) == 0.001
    assert rounder(0.123456) == 0.123
    assert rounder(0.999999) == 1
    assert rounder(1.00001) == 1
    assert rounder(123.456) == 123
    assert rounder(0) == 0
    assert rounder(1) == 1


def test_bytes():
    b = Bytes(500)
    assert str(b) == "500 B"


def test_kilobytes():
    kb = Kilobytes(1)
    assert str(kb) == "1 KB"


def test_megabytes():
    mb = Megabytes(1)
    assert str(mb) == "1 MB"


def test_gigabytes():
    gb = Gigabytes(1)
    assert str(gb) == "1 GB"


def test_terabytes():
    tb = Terabytes(1)
    assert str(tb) == "1 TB"


def test_bytes_converions():
    b = Bytes(1024)
    assert str(b.kb) == "1 KB"
    assert str(b.mb) == "0.001 MB"
    assert str(b.gb) == "0.000001 GB"
    assert str(b.tb) == "0.000000001 TB"


def test_kilobytes_converions():
    kb = Kilobytes(1024)
    assert str(kb.b) == "1048576 B"
    assert str(kb.kb) == "1024 KB"
    assert str(kb.mb) == "1 MB"
    assert str(kb.gb) == "0.001 GB"
    assert str(kb.tb) == "0.000001 TB"


def test_megabytes_converions():
    mb = Megabytes(1024)
    assert str(mb.b) == "1073741824 B"
    assert str(mb.kb) == "1048576 KB"
    assert str(mb.mb) == "1024 MB"
    assert str(mb.gb) == "1 GB"
    assert str(mb.tb) == "0.001 TB"


def test_gigabytes_converions():
    gb = Gigabytes(1024)
    assert str(gb.b) == "1099511627776 B"
    assert str(gb.kb) == "1073741824 KB"
    assert str(gb.mb) == "1048576 MB"
    assert str(gb.gb) == "1024 GB"
    assert str(gb.tb) == "1 TB"


def test_terabytes_converions():
    tb = Terabytes(1)
    assert str(tb.b) == "1099511627776 B"
    assert str(tb.kb) == "1073741824 KB"
    assert str(tb.mb) == "1048576 MB"
    assert str(tb.gb) == "1024 GB"
    assert str(tb.tb) == "1 TB"
