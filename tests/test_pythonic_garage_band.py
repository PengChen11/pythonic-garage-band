from pythonic_garage_band import __version__
import pytest
from pythonic_garage_band.pythonic_garage_band import *



def test_version():
    assert __version__ == '0.1.0'

def test_band_name(prep):
    tester=Band('tester')
    assert tester.name == 'tester'

def test_band_members(members):
    tester = Band('Cool Band',members)
    assert len(tester.members) ==3

def test_band_members_2(members_2):
    tester = Band('Another Band',members_2)
    assert len(tester.members) ==5

def test_band_play_solos(members_2):
    tester = Band('tester',members_2)
    assert tester.play_solos()==[
        'The Guitarist is playing solo now, Dang Ding Dang !',
        'The Guitarist is playing solo now, Dang Ding Dang !',
        'The Bassist is playing solo now, Wong Dong Wong !',
        'The Drummer is playing solo now, Dong Si Da Si !',
        'The Drummer is playing solo now, Dong Si Da Si !'
        ]

def test_band_str():
    tester = Band('tester')
    assert tester.__str__()=='This is the band tester'

def test_band_repr():
    tester = Band('tester')
    assert tester.__repr__()=='Band instant. Name: tester'

def test_band_to_list():
    Band('test1')
    Band('test2')
    Band('test3')
    assert len(Band.band_list)==3
    assert Band.band_list[0].name == 'test1'
    assert Band.band_list[2].members == []
    assert Band.band_list[0].__str__()=='This is the band test1'


def test_Musician_str():
    guitarist = Guitarist('Guy One')
    bassist=Bassist('Guy Two')
    drummer=Drummer('Guy Three')
    assert guitarist.__str__()=='Hi, I am Guy One, a Guitarist'
    assert bassist.__str__()=='Hi, I am Guy Two, a Bassist'
    assert drummer.__str__()=='Hi, I am Guy Three, a Drummer'


def test_Musician_repr():
    guitarist = Guitarist('Guy One')
    bassist=Bassist('Guy Two')
    drummer=Drummer('Guy Three')
    assert guitarist.__repr__()=='Guitarist instant. Name: Guy One'
    assert bassist.__repr__()=='Bassist instant. Name: Guy Two'
    assert drummer.__repr__()=='Drummer instant. Name: Guy Three'

def test_Musician_get_instrument():
    guitarist = Guitarist('Guy One')
    bassist=Bassist('Guy Two')
    drummer=Drummer('Guy Three')
    assert guitarist.get_instrument()=='I play guitar'
    assert bassist.get_instrument()=='I play bass guitar'
    assert drummer.get_instrument()=='I play drum set'

def test_Musician_solo():
    guitarist = Guitarist('Guy One')
    bassist=Bassist('Guy Two')
    drummer=Drummer('Guy Three')
    assert guitarist.play_solo()=='The Guitarist is playing solo now, Dang Ding Dang !'
    assert bassist.play_solo()=='The Bassist is playing solo now, Wong Dong Wong !'
    assert drummer.play_solo()=='The Drummer is playing solo now, Dong Si Da Si !'

@pytest.fixture(autouse=True)
def prep():
    Band.band_list=[]

@pytest.fixture
def members():
    members = [
        Guitarist("Guy One"),
        Bassist("Guy Two"),
        Drummer("Guy Three"),
    ]
    return members

@pytest.fixture
def members_2():
    members = [
        Guitarist("Guy One"),
        Guitarist("Another Guy"),
        Bassist("Guy Two"),
        Drummer("Guy Three"),
        Drummer("Another Guy")
    ]
    return members
