def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def hamming_distance(s1, s2):
    """Return the Hamming distance between two sequences."""
    return sum(a != b for a, b in zip(s1, s2))

def read_fasta(filename):
    """Read sequences from a FASTA file, ignoring headers."""
    sequences = []
    with open(filename, 'r') as file:
        seq = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if seq:
                    sequences.append(seq)
                    seq = ''
            else:
                seq += line
        if seq:
            sequences.append(seq)
    return sequences

def find_corrections(sequences):
    """Find all corrections for incorrect reads."""
    # Count occurrences of each sequence and its reverse complement
    seq_count = {}
    for seq in sequences:
        seq_count[seq] = seq_count.get(seq, 0) + 1
    
    # Identify correct sequences (appear at least twice, including reverse complement)
    correct = set()
    for seq in seq_count:
        rev_seq = reverse_complement(seq)
        total_count = seq_count.get(seq, 0) + seq_count.get(rev_seq, 0)
        if total_count >= 2:
            correct.add(seq)
            if rev_seq in seq_count:
                correct.add(rev_seq)
    
    # Find incorrect sequences and their corrections
    corrections = []
    for seq in sequences:
        # Incorrect if appears exactly once
        if seq_count.get(seq, 0) == 1 and seq not in correct:
            found = False
            # Check Hamming distance to all correct sequences
            for correct_seq in correct:
                if hamming_distance(seq, correct_seq) == 1:
                    if found:  # If already found a match, this seq matches multiple correct seqs
                        found = False
                        break
                    corrections.append(f"{seq}->{correct_seq}")
                    found = True
            # Also check reverse complements of correct sequences
            if not found:
                for correct_seq in correct:
                    rev_seq = reverse_complement(correct_seq)
                    if hamming_distance(seq, rev_seq) == 1:
                        if found:
                            found = False
                            break
                        corrections.append(f"{seq}->{rev_seq}")
                        found = True
    return corrections

def main():
    filename = 'reads.txt'
    sequences = read_fasta(filename)
    corrections = find_corrections(sequences)
    for correction in corrections:
        print(correction)

if __name__ == '__main__':
    main()
