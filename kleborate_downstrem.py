import pandas as pd

# Load the provided Excel file
file = 'AMR_Presence_abscence.xlsx'
data = pd.read_excel(file)

# Display the first few rows to understand the structure
data.head()



# Define the genes of interest based on the provided template
genes_of_interest = ['mphA', 'ermB.v1*', 'mphA?', 'CTX-M-15', 'SHV-12']

# Create a dictionary to hold the data
output_dict = {'IDs': data['IDs'].tolist()}
for gene in genes_of_interest:
    output_dict[gene] = []

# Function to check presence of gene
def check_gene_presence(row, gene):
    for column in ['MLS_acquired', 'Bla_ESBL_acquired', 'Bla_Carb_acquired', 'Omp_mutations', 'Flq_mutations']:
        if gene in str(row[column]).split(';'):
            return 1
    return 0

# Populate the dictionary for each gene
for index, row in data.iterrows():
    for gene in genes_of_interest:
        output_dict[gene].append(check_gene_presence(row, gene))

# Create a DataFrame from the dictionary
output_df = pd.DataFrame(output_dict)

# Display the formatted DataFrame
output_df
# Function to extract unique genes from a column
def extract_genes(column):
    gene_list = []
    for item in column:
        if not pd.isna(item):
            gene_list.extend(item.split(';'))
    return set(gene_list)

# Combine and extract unique genes from all relevant columns
all_genes = set()
for column in ['MLS_acquired', 'Bla_ESBL_acquired', 'Bla_Carb_acquired', 'Omp_mutations', 'Flq_mutations']:
    all_genes.update(extract_genes(data[column]))

# Remove any placeholder like "-" indicating no gene
all_genes.discard('-')

all_genes
# Extend the dictionary to include all unique genes
extended_output_dict = {'IDs': data['IDs'].tolist()}
for gene in all_genes:
    extended_output_dict[gene] = [check_gene_presence(row, gene) for index, row in data.iterrows()]

# Create a DataFrame from the extended dictionary
extended_output_df = pd.DataFrame(extended_output_dict)

# Display the extended DataFrame
extended_output_df.head()
