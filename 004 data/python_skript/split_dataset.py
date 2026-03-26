import pandas as pd
import os

# Filstier
input_file = "004 data/vasket data/master_data_vasket.csv"
train_output = "004 data/splittet_data/train/train_data.csv"
test_output = "004 data/splittet_data/test/test_data.csv"

# Last inn data
df = pd.read_csv(input_file)

# Sørg for at Dato_Sortering er i datoformat og sorter
df['Dato_Sortering'] = pd.to_datetime(df['Dato_Sortering'])
df = df.sort_values('Dato_Sortering').reset_index(drop=True)

# Beregn splittpunkt (80% trening, 20% test)
split_idx = int(len(df) * 0.8)

train_df = df.iloc[:split_idx]
test_df = df.iloc[split_idx:]

# Lagre filene (konverterer dato tilbake til strengformatet for konsistens)
train_df.to_csv(train_output, index=False)
test_df.to_csv(test_output, index=False)

print(f"Split fullført:")
print(f"- Treningsdata: {len(train_df)} rader -> {train_output}")
print(f"- Testdata: {len(test_df)} rader -> {test_output}")
