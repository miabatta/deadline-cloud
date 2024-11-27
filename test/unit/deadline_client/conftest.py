# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

"""
Common fixtures for Deadline Client Library tests.
"""

import tempfile
import pytest


@pytest.fixture(scope="function")
def temp_job_bundle_dir():
    """
    Fixture to provide a temporary job bundle directory.
    """

    with tempfile.TemporaryDirectory() as job_bundle_dir:
        yield job_bundle_dir


@pytest.fixture(scope="function")
def temp_assets_dir():
    """
    Fixture to provide a temporary directory for asset files.
    """

    with tempfile.TemporaryDirectory() as assets_dir:
        yield assets_dir


@pytest.fixture(
    scope="function",
    params=[
        pytest.param("abcd", id="ASCII"),
        pytest.param("ñ", id="N with tilde"),
        pytest.param("😀", id="Emoji"),
        pytest.param("דּ", id="Dalet with dagesh"),
        pytest.param("ö", id="O with diaeresis"),
        pytest.param("€", id="Euro symbol"),
    ],
)
def special_char_string(request):
    yield f"test_{request.param}"


@pytest.fixture(
    scope="function",
    params=[
        pytest.param({"input": "\u00c3\u00b1", "expected": "ñ"}, id="N tilde"),
        pytest.param({"input": "\ud83d\ude0a", "expected": "😊"}, id="Smile emoji"),
    ],
)
def unicode_string(request):
    yield request.param
