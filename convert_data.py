import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

CSV_PATH = 'data/clientes.csv'
NEW_CSV_PATH = 'data/novos_clientes.csv'
PARQUET_PATH = 'data/clientes.parquet'
NEW_PARQUET_PATH = 'data/novos_clientes.parquet'

# Convert csv to parquet (lighter on github)
df = pd.read_csv(CSV_PATH)
table = pa.Table.from_pandas(df)
pq.write_table(table, PARQUET_PATH)

new_df = pd.read_csv(NEW_CSV_PATH)
table = pa.Table.from_pandas(df)
pq.write_table(table, NEW_PARQUET_PATH)

# # Convert parquet back to csv, or refactor analysis.ipynb to use parquet instead
# df = pd.read_parquet(PARQUET_PATH, engine='pyarrow')
# df.to_csv(CSV_PATH, index=False)

# new_df = pd.read_parquet(NEW_PARQUET_PATH, engine='pyarrow')
# new_df.to_csv(NEW_CSV_PATH, index=False)