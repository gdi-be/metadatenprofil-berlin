import yaml
import os

def generate_html():
    # 1. YAML Datei einlesen
    yaml_path = 'metadatenprofil.yaml'
    if not os.path.exists(yaml_path):
        print(f"Datei {yaml_path} nicht gefunden.")
        return

    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 2. HTML-Grundgerüst mit Styling und DataTables für Komfort (Suche, Sortierung)
    html_content = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metadatenprofil Dokumentation</title>
    <!-- Tailwind CSS für modernes Design -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- DataTables CSS für Sortierung & Suche -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.css">
    <style>
        .dataTables_wrapper .dataTables_filter input {
            border: 1px solid #e2e8f0;
            padding: 0.375rem 0.75rem;
            border-radius: 0.375rem;
            margin-left: 0.5rem;
        }
        table.dataTable tbody tr { background-color: transparent; }
        .br-pre { white-space: pre-line; }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans p-6">
    <div class="max-w-7xl mx-auto bg-white p-8 rounded-xl shadow-md">
        <h1 class="text-3xl font-bold text-blue-900 mb-2">Metadatenprofil</h1>
        <p class="text-gray-600 mb-6">Automatisch generierte Tabellendokumentation aus der Repository-YAML.</p>
        
        <div class="overflow-x-auto">
            <table id="metadataTable" class="display w-full border-collapse text-sm text-left">
                <thead class="bg-blue-900 text-white text-xs uppercase">
                    <tr>
                        <th class="p-3">Sektion</th>
                        <th class="p-3">ID / Key</th>
                        <th class="p-3">Feldname (Label)</th>
                        <th class="p-3">Kardinalität</th>
                        <th class="p-3">Feldtyp</th>
                        <th class="p-3">Beschreibung</th>
                        <th class="p-3">Codelisten / Standardwerte</th>
                        <th class="p-3">ISO-Export</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
"""

    # 3. Schleife über die Sektionen und Felder
    for section_item in data:
        section_title = section_item.get('section', 'Allgemein')
        fields = section_item.get('fields', [])
        
        for field in fields:
            # Sicheres Auslesen der Werte mit Standardfallbacks
            f_id = field.get('id', '')
            f_key = field.get('key', '')
            label = field.get('label', '')
            mult = field.get('multiplicity', '')
            f_type = field.get('field_type', '')
            desc = field.get('description', '').replace('\n', '<br>')
            codelist = field.get('codelists_defaults', '').replace('\n', '<br>')
            iso = field.get('iso_export', '')

            html_content += f"""
                    <tr class="hover:bg-gray-50 transition-colors">
                        <td class="p-3 font-semibold text-blue-700">{section_title}</td>
                        <td class="p-3"><span class="bg-gray-100 text-gray-700 px-2 py-1 rounded text-xs font-mono">{f_id}</span><br><span class="text-xs text-gray-400 font-mono">{f_key}</span></td>
                        <td class="p-3 font-medium text-gray-900">{label}</td>
                        <td class="p-3 text-center">{mult}</td>
                        <td class="p-3"><span class="text-xs uppercase bg-emerald-50 text-emerald-700 px-2 py-0.5 rounded border border-emerald-200">{f_type}</span></td>
                        <td class="p-3 text-xs text-gray-600 max-w-xs br-pre">{desc}</td>
                        <td class="p-3 text-xs font-mono text-purple-700 max-w-xs br-pre">{codelist}</td>
                        <td class="p-3 text-xs text-gray-500 max-w-xs">{iso}</td>
                    </tr>"""

    # 4. HTML abschließen und DataTables-Skript aktivieren
    html_content += """
                </tbody>
            </table>
        </div>
    </div>

    <!-- jQuery und DataTables JS -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script type="text/javascript" charset="utf-8" src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.js"></script>
    <script>
        $(document).ready( function () {
            $('#metadataTable').DataTable({
                "language": {
                    "url": "https://cdn.datatables.net/plug-ins/1.13.6/i18n/de-DE.json"
                },
                "pageLength": 25,
                "order": [[ 0, "asc" ]]
            });
        });
    </script>
</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("index.html erfolgreich generiert!")

if __name__ == "__main__":
    generate_html()
