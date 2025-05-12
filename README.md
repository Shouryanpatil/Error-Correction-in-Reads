# Error Correction in Reads

## Problem Statement

The most common type of sequencing error occurs when a single nucleotide from a read is interpreted incorrectly. Given a collection of up to 1000 reads (each at most 50 bp) in FASTA format, the task is to identify and correct these single-nucleotide errors.

### Conditions

* Correct reads appear at least twice (including reverse complements).
* Incorrect reads appear exactly once and have a Hamming distance of 1 to exactly one correct read (or its reverse complement).

### Objective

Return corrections in the format:

```
[old read]->[new read]
```

## Files

* `error_correction.py`: Python script to perform error correction on DNA reads.
* `reads.txt`: Example input file containing DNA reads in FASTA format.

## Usage

### Prerequisites

* Python 3

### Running the script

Ensure both files (`error_correction.py` and `reads.txt`) are in the same directory, then run:

```bash
python error_correction.py
```

### Sample Output

```
TTCAT->TTGAT
GAGGA->GATGA
TTTCC->TTTCA
```

## Features

* Reads sequences in FASTA format.
* Calculates reverse complements.
* Computes Hamming distances.
* Identifies and outputs necessary corrections.

