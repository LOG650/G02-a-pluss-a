import csv
import os

# Definer stier
raw_data_dir = "004 data"
processed_dir = os.path.join(raw_data_dir, "processed")

if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

month_map = {
    'Januar': '01', 'Februar': '02', 'Mars': '03', 'April': '04', 'Mai': '05', 'Juni': '06',
    'Juli': '07', 'August': '08', 'September': '09', 'Oktober': '10', 'November': '11', 'Desember': '12'
}

def read_csv_to_list(file_path):
    with open(file_path, mode='r', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def clean_and_merge():
    print("Fullfører vask og strukturering med ALT relevant data...")
    
    # 1. Last inn alle hjelpefiler
    costs_list = read_csv_to_list(os.path.join(raw_data_dir, "Kostnadsparametere.csv"))
    suppliers_list = read_csv_to_list(os.path.join(raw_data_dir, "Leverandøroversikt.csv"))
    orders_list = read_csv_to_list(os.path.join(raw_data_dir, "Bestillingsdata.csv"))
    
    # Oppslagstabeller
    costs_lookup = {row['Kategori']: row for row in costs_list}
    
    # Leverandøroppslag (Nøkkel: Kategori + Leverandørnavn for nøyaktig matching)
    supp_lookup = {(row['Kategori'], row['Leverandør']): row for row in suppliers_list}
    
    # Bestillingsoppslag (Nøkkel: År + Måned + Kategori)
    orders_lookup = {}
    for row in orders_list:
        key = (row['År'], row['Måned'], row['Kategori'])
        orders_lookup[key] = row
            
    fact_files = [
        ("Faktadata_-_Norsk_Krim.csv", "Norsk krim"),
        ("Faktadata_-_Norske_barnebøker.csv", "Norske barnebøker"),
        ("Faktadata_-_Engelsk_fiksjon.csv", "Engelsk fiksjon")
    ]
    
    master_data = []
    
    for filename, category in fact_files:
        file_path = os.path.join(raw_data_dir, filename)
        if os.path.exists(file_path):
            rows = read_csv_to_list(file_path)
            for row in rows:
                # 1. Kategori og Dato
                row['Kategori'] = category
                m_num = month_map.get(row['Måned'], '00')
                row['Dato_Sortering'] = f"{row['År']}-{m_num}-01"
                
                # 2. Kostnadsparametere
                c_info = costs_lookup.get(category, {})
                for k, v in c_info.items():
                    if k != 'Kategori':
                        row[f"Kostnad_{k}"] = v
                
                # 3. Bestillingsdata
                order_key = (row['År'], row['Måned'], category)
                o_info = orders_lookup.get(order_key, {})
                row['Bestilt_kvantum'] = o_info.get('Bestilt kvantum', '0')
                row['Dato_bestilt'] = o_info.get('Dato bestilt', '')
                row['Dato_mottatt'] = o_info.get('Dato for motatt bestilling', '')
                actual_supplier = o_info.get('Leverandør', '')
                row['Leverandør_navn'] = actual_supplier
                
                # 4. Leverandør-detaljer (Nøyaktig matching på hvem som ble brukt)
                # Hvis ingen bestilling ble gjort, hentes info fra første leverandør for kategorien (som backup)
                s_key = (category, actual_supplier)
                if actual_supplier and s_key in supp_lookup:
                    s_info = supp_lookup[s_key]
                else:
                    # Finn første tilgjengelige leverandør for denne kategorien hvis ingen ble brukt denne måneden
                    s_info = next((v for k, v in supp_lookup.items() if k[0] == category), {})
                
                for k, v in s_info.items():
                    if k not in ['Kategori', 'Leverandør']:
                        row[f"Supp_{k}"] = v
                
                master_data.append(row)
            print(f"Fullført: {filename}")
    
    master_data.sort(key=lambda x: (x['Kategori'], x['Dato_Sortering']))
    
    if master_data:
        keys = master_data[0].keys()
        output_path = os.path.join(processed_dir, "master_data_vasket.csv")
        with open(output_path, mode='w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(master_data)
        
        print(f"FERDIG! Absolutt alt relevant data er nå samlet i: {output_path}")

if __name__ == "__main__":
    clean_and_merge()
