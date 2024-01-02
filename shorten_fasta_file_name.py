import argparse

def shorten_fasta_headers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                # Extract the contig ID (everything after ">" until the first space)
                contig_id = line.split()[0][1:]
                outfile.write(f'>{contig_id}\n')
            else:
                outfile.write(line)

def main():
    parser = argparse.ArgumentParser(description='Shorten headers in a FASTA file.')
    parser.add_argument('--input', required=True, help='Input FASTA file')
    parser.add_argument('--output', required=True, help='Output FASTA file')

    args = parser.parse_args()

    shorten_fasta_headers(args.input, args.output)

if __name__ == "__main__":
    main()

