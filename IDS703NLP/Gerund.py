
import re
import string

import pytest


pattern = r"\b[b-df-hj-np-tv-z]+[aeiou]+[b-df-hj-np-tv-z]*[aeiou]*[b-df-hj-np-tv-z]*ing\b|\b[aeiou]+[b-df-hj-np-tv-z]+[aeiou*][b-df-hj-np-tv-z]*ing\b"
test_cases = [
    ("harry loves to sing while showering", ['showering']),
    ("the king needs to swing", []),
    ("the king loves swinging", ['swinging']),
    ("She loves arguing", ['arguing']),
    ("she loves dancing and singing", ['dancing', 'singing']),
    ("she is gathering some trash", ['gathering']),
    ("Kira talks about running a marathon, reading novels, and studying for six hours.",['running','reading','studying'])
]

print(re.findall(pattern,"she loves dancing and singing"))


@pytest.mark.parametrize("string, matches", test_cases)
def test_name_matching(string, matches: list):
    """Test whether pattern correctly matches or does not match input."""
    returned_list = re.findall(pattern, string)
    assert  returned_list == matches