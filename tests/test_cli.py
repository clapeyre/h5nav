import os
import pytest
import numpy as np

from .context import cli, setup_module, teardown_module, interp


# `get_whitespace_name` command
def test_get_whitespace_name(interp):
    name = interp.get_whitespace_name("Group1")
    assert name == "Group1"
    name = interp.get_whitespace_name(" Group2")
    assert name == " Group2"


def test_get_whitespace_fail(interp):
    with pytest.raises(cli.UnknownLabelError):
        interp.get_whitespace_name('zzz')


# `help` functions
def test_helps_work(capsys, interp):
    for cmd in ["help_" + cmd[3:] for cmd in dir(interp)
                if cmd[:3] == "do_"]:
        if cmd == "help_help":
            continue
        assert hasattr(interp, cmd)


# `ls` command
def test_ls_simple(capsys, interp):
    interp.do_ls('')
    out, err = capsys.readouterr()
    assert out == " Group2/ Group1/\n"


def test_ls_star(capsys, interp):
    interp.do_ls('*')
    out, err = capsys.readouterr()
    assert out == """\
 Group2/
     field1
Group1/
     Subgroup1/ field1
./
    \n"""


def test_ls_unknown_label(capsys, interp):
    interp.do_ls('zzz')
    out, err = capsys.readouterr()
    assert out == "*** unknown label\n"
    # with pytest.raises(cli.UnknownLabelError):
    #     interp.do_ls('zzz')


# `cd` command
def test_cd_group(interp):
    assert interp.position == '/'
    interp.do_cd(' Group2')
    assert interp.position == '/ Group2/'


def test_cd_dataset(capsys, interp):
    interp.do_cd('Group1')
    interp.do_cd('field1')
    out, err = capsys.readouterr()
    assert out == "*** can only cd into groups\n"


def test_cd_dotdot(interp):
    interp.do_cd(' Group2')
    interp.do_cd('..')
    assert interp.position == '/'


def test_cd_root(interp):
    interp.do_cd('Group1')
    interp.do_cd('Subgroup1')
    interp.do_cd('')
    assert interp.position == '/'


def test_cd_2args(capsys, interp):
    interp.do_cd('Group1 Group2')
    out, err = capsys.readouterr()
    assert out == "*** invalid number of arguments\n"


def test_cd_unknown_label(capsys, interp):
    interp.do_cd('zzz')
    out, err = capsys.readouterr()
    assert out == "*** unknown label\n"
    # with pytest.raises(cli.UnknownLabelError):
    #     interp.do_cd('zzz')


# `print` command
def test_print(capsys, interp):
    interp.do_cd("Group1")
    interp.do_print("field1")
    out, err = capsys.readouterr()
    assert out == "information\n"

def test_print_star(capsys, interp):
    interp.do_cd("Group1")
    interp.do_cd("Subgroup1")
    interp.do_print("*")
    out, err = capsys.readouterr()
    assert out == """\
 field2 :
     [  0   2   4   6   8  10  12  14  16  18  20  22  24  26  28  30  32  34
  36  38  40  42  44  46  48  50  52  54  56  58  60  62  64  66  68  70
  72  74  76  78  80  82  84  86  88  90  92  94  96  98 100 102 104 106
 108 110 112 114 116 118 120 122 124 126 128 130 132 134 136 138 140 142
 144 146 148 150 152 154 156 158 160 162 164 166 168 170 172 174 176 178
 180 182 184 186 188 190 192 194 196 198]
field1 :
     [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74
 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]
"""


# `stats` command
def test_stats(capsys, interp):
    interp.do_cd("Group1")
    interp.do_cd("Subgroup1")
    interp.do_stats("field1")
    out, err = capsys.readouterr()
    assert out == """\
Shape type min mean max std
(100,) int64 0 49.5 99 28.8660700477
"""


# `pdf` command
def test_pdf(capsys, interp):
    interp.do_cd("Group1")
    interp.do_cd("Subgroup1")
    interp.do_pdf("field1")
    out, err = capsys.readouterr()
    assert out == """\
Min        Max        | Pdf (10 buckets)
0.0000e+00 9.9000e+01 | [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
"""


# `dump` command
def test_dump(interp):
    fname = "field1.npy"
    interp.do_cd(" Group2")
    interp.do_dump("field1")
    data = np.load(fname)
    assert np.allclose(data, np.zeros(10))
    os.remove(fname)


# `txt_dump` command
def test_txt_dump(interp):
    fname = "field1.txt"
    interp.do_cd(" Group2")
    interp.do_txt_dump("field1")
    data = np.loadtxt(fname)
    assert np.allclose(data, np.zeros(10))
    os.remove(fname)

# `rm` command
def test_rm_dataset(capsys, interp):
    interp.do_cd("Group1")
    interp.do_cd("Subgroup1")
    interp.do_rm("field1")
    interp.do_ls('')
    out, err = capsys.readouterr()
    assert out.split("\n")[1] == " field2"

# `rm` command
def test_rm_group(capsys, interp):
    interp.do_rm("Group2")
    interp.do_ls('')
    out, err = capsys.readouterr()
    assert out.split("\n")[1] == "Group1/"

# `exit` command
def test_exit(capsys, interp):
    with pytest.raises(SystemExit):
        interp.do_exit('')
    out, err = capsys.readouterr()
    assert out == "Bye!\n"
