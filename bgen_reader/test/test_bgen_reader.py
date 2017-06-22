from __future__ import unicode_literals

import os

import pytest
from numpy.testing import assert_equal

from bgen_reader import read_bgen


# TODO: test not found file


def test_bgen_reader():
    folder = os.path.dirname(os.path.abspath(__file__)).encode()
    filepath = os.path.join(folder, b"example.32bits.bgen")
    (variants, samples, genotype) = read_bgen(filepath)

    assert_equal(variants.loc[0, 'chrom'], '01')
    assert_equal(variants.loc[0, 'id'], 'SNPID_2')
    assert_equal(variants.loc[0, 'nalleles'], 2)
    assert_equal(variants.loc[0, 'pos'], 2000)
    assert_equal(variants.loc[0, 'rsid'], 'RSID_2')

    assert_equal(variants.loc[7, 'chrom'], '01')
    assert_equal(variants.loc[7, 'id'], 'SNPID_9')
    assert_equal(variants.loc[7, 'nalleles'], 2)
    assert_equal(variants.loc[7, 'pos'], 9000)
    assert_equal(variants.loc[7, 'rsid'], 'RSID_9')

    n = variants.shape[0]
    assert_equal(variants.loc[n - 1, 'chrom'], '01')
    assert_equal(variants.loc[n - 1, 'id'], 'SNPID_200')
    assert_equal(variants.loc[n - 1, 'nalleles'], 2)
    assert_equal(variants.loc[n - 1, 'pos'], 100001)
    assert_equal(variants.loc[n - 1, 'rsid'], 'RSID_200')

    assert_equal(samples.loc[0, 'id'], 'sample_001')
    assert_equal(samples.loc[7, 'id'], 'sample_008')

    n = samples.shape[0]
    assert_equal(samples.loc[n - 1, 'id'], 'sample_500')


def test_bgen_reader_file_notfound():
    folder = os.path.dirname(os.path.abspath(__file__)).encode()
    filepath = os.path.join(folder, b"example.33bits.bgen")
    with pytest.raises(FileNotFoundError):
        (variants, samples, genotype) = read_bgen(filepath)
