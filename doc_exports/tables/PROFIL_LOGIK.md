# ⚙️ Metadatenprofil Berlin - Technische Logik & UI-Steuerung

Diese Datei enthält die Steuerungslogik für das UI-Verhalten, Codelisten und die ISO-Exporte.

### Basisangaben (Steuerung & Logik)

| Feldname (`key`) | Rolle | Export zu ISO | Andere Wege | Codelisten & Vorbelegungen | Hilfe | Kopieren | Übernahme | Vorlage | Löschen |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `isoMetadata.title` | DHS<br>Redakteur | ISO 24<br>(360 - title) |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.description` | DHS<br>Redakteur | ISO 25 (abstract) |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.keywords` | DHS<br>Redakteur | ISO 53 | Geoserver | Umthes Thesaurus: https://sns.uba.de<br><br>Vorbelegungen für GDI-BE: Karten, Geodaten, Berlin<br>Zusätzlich für Darstellungsdienste: Karten<br>Zusätzlich für Downloaddienste: Sachdaten<br><br>Vorbelegungen für GDI-DE:<br>Für offene NB: opendata, open data<br>Für INSPIRE Daten: inspireidentifiziert | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.preview` | DHS<br>Redakteur | ISO 31<br>(ISO 48-51) |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.pointsOfContact` | DHS<br>Redakteur | ISO 29<br>ISO 379 - role |  | Vorbelegung für Metadatenkontaktangabe aller Metadaten:<br>https://github.com/gdi-be/mde-deployment/blob/main/codelists/contact.yaml<br><br>Vorbelegung ISO 379: pointOfContact | ✅ | ❌ | ✅ | ✅ | ✅ |
| `isoMetadata.pointsOfContact.name` | DHS<br>Redakteur | ISO 375 |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.pointsOfContact.organisation` | DHS<br>Redakteur | ISO 376 |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.pointsOfContact.phone` | DHS<br>Redakteur | ISO 388 |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.pointsOfContact.email` | DHS<br>Redakteur | ISO 386 |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |

### Einordnung (Steuerung & Logik)

| Feldname (`key`) | Rolle | Export zu ISO | Andere Wege | Codelisten & Vorbelegungen | Hilfe | Kopieren | Übernahme | Vorlage | Löschen |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `isoMetadata.metadataProfile` | DHS<br>Redakteur | - |  | Codeliste:<br>- ISO<br>- INSPIRE identifiziert<br>- INSPIRE harmonisiert | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.inspireTheme` | DHS<br>Redakteur | ISO 53 | Geoserver | https://inspire.ec.europa.eu/theme/theme.de.xml | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.inspireFormatName` | Redakteur | ISO 270<br>(ISO 285) |  | https://inspire.ec.europa.eu/applicationschema/applicationschema.de.xml | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.inspireAnnexVersion` | Redakteur | ISO 270<br>(ISO 286) |  | https://inspire.ec.europa.eu/applicationschema/applicationschema.de.xml | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.valid` | Redakteur | ISO 107<br>(ISO 128-132) |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.privacy` | DHS<br>Redakteur | - | Gateway | https://github.com/gdi-be/mde-deployment/blob/main/codelists/privacy.yaml | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.termsOfUseId` | DHS<br>Redakteur | ISO 20<br>(ISO 67-72) |  | https://github.com/gdi-be/mde-deployment/blob/main/codelists/terms_of_use.yaml<br><br>https://github.com/gdi-be/mde-deployment/blob/main/codelists/terms_of_use_on_privacy.yaml | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.termsOfUseSource` | DHS<br>Redakteur | ISO 20<br>(ISO 67-72) |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.highValueDataset` | DHS<br>Redakteur | - |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.highValueDataCategory` | DHS<br>Redakteur | ISO 53 |  | http://data.europa.eu/bna/asd487ae75 | ❌ | ❌ | ❌ | ❌ | ❌ |
| `isoMetadata.topicCategory` | Redakteur | ISO 41 | Geoportal | ISO-Codelist: https://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_KeywordTypeCode<br><br>Zuordnungstabelle zu INSPIRE-Thema: https://www.gdi-de.org/download/AK_Metadaten_Konventionen_zu_Metadaten.pdf#page=85 | ✅ | ✅ | ❌ | ✅ | ❌ |

### Zeitliche und Räumliche Angaben (Steuerung & Logik)

| Feldname (`key`) | Rolle | Export zu ISO | Andere Wege | Codelisten & Vorbelegungen | Hilfe | Kopieren | Übernahme | Vorlage | Löschen |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `isoMetadata.created` | DHS<br>Redakteur | ISO 24<br>(394 - date,<br>395 - dateType) |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.published` | DHS<br>Redakteur | ISO 24<br>(394 - date,<br>395 - dateType) |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.maintenanceFrequency` | DHS<br>Redakteur | ISO 143 |  | Codeliste: https://standards.iso.org/iso/19139/resources/gmxCodelists.xml<br><br>Vorbelegung: asNeeded | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.modified` | DHS<br>Redakteur | ISO 24<br>(394 - date,<br>395 - dateType) |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `-` | DHS<br>Redakteur | - |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.validFrom` | DHS<br>Redakteur | ISO 45<br>(ISO 351 - extent) |  |  | ❌ | ❌ | ❌ | ❌ | ❌ |
| `isoMetadata.validTo` | DHS<br>Redakteur | ISO 45<br>(ISO 351 - extent) |  |  | ❌ | ❌ | ❌ | ❌ | ❌ |
| `technicalMetadata.deliveredCrs` | DHS<br>Redakteur | - | intern | Vorbelegung: 25833 | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.crs` | Redakteur | ISO 13<br>(ISO 186 - referenceSystemIdentifier) |  | https://github.com/gdi-be/mde-deployment/blob/main/codelists/crs.yaml<br><br>Vorbelegung: 25833 | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.extent` | Redakteur | - |  | https://github.com/gdi-be/mde-deployment/blob/main/codelists/extents.yaml | ✅ | ❌ | ❌ | ✅ | ❌ |
| `isoMetadata.extent.minx` | Redakteur | ISO 45<br>(ISO 346) |  |  | ❌ | ❌ | ❌ | ❌ | ❌ |
| `isoMetadata.extent.maxx` | Redakteur | ISO 45<br>(ISO 347) |  |  | ❌ | ❌ | ❌ | ❌ | ❌ |
| `isoMetadata.extent.miny` | Redakteur | ISO 45<br>(ISO 344) |  |  | ❌ | ❌ | ❌ | ❌ | ❌ |
| `isoMetadata.extent.maxy` | Redakteur | ISO 45<br>(ISO 345) |  |  | ❌ | ❌ | ❌ | ❌ | ❌ |
| `-` | DHS<br>Redakteur |  |  |  | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.scale` | DHS<br>Redakteur | ISO 38<br>(ISO 57) |  |  | ❌ | ❌ | ❌ | ❌ | ❌ |
| `isoMetadata.resolutions` | DHS<br>Redakteur | ISO 38<br>(ISO 61) |  |  | ❌ | ❌ | ❌ | ❌ | ❌ |
| `isoMetadata.spatialRepresentationTypes` | Redakteur | ISO 37 |  | Codeliste ISO 19115: B.5.26 MD_SpatialRepresentationTypeCode | ✅ | ✅ | ❌ | ✅ | ❌ |

### Weitere Angaben (Steuerung & Logik)

| Feldname (`key`) | Rolle | Export zu ISO | Andere Wege | Codelisten & Vorbelegungen | Hilfe | Kopieren | Übernahme | Vorlage | Löschen |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `isoMetadata.contentDescription` | DHS<br>Redakteur | ISO 283<br>(ISO 396-402) |  | Vorbelegung ISO 401 - description: "Inhaltliche Beschreibung"<br><br>Vorbelegung ISO 402 - function: "information" | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.technicalDescription` | DHS<br>Redakteur | ISO 283<br>(ISO 396-402) |  | Vorbelegung ISO 401 - description: "Technische Beschreibung"<br><br>Vorbelegung ISO 402 - function: "information" | ✅ | ✅ | ❌ | ✅ | ❌ |
| `isoMetadata.lineage` | DHS<br>Redakteur | entweder ISO 83 - statement<br>oder ISO 96 - sourceCitation |  |  | ✅ | ❌ | ❌ | ✅ | ✅ |
| `isoMetadata.lineage.title` | DHS<br>Redakteur | ISO 96<br>360 - title |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.lineage.date` | DHS<br>Redakteur | ISO 96<br>362 - date |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.lineage.identifier` | DHS<br>Redakteur | ISO 96<br>365 - identifier |  | Vorbelegung für Präfix des Identifiers unter "registry": https://github.com/gdi-be/mde-deployment/blob/main/codelists/metadatavariables.yaml | ❌ | ✅ | ❌ | ❌ | ❌ |
| `clientMetadata.relatedTopics` | Redakteur | - | intern |  | ❌ | ❌ | ❌ | ❌ | ❌ |
| `isoMetadata.contentDescriptions` | DHS<br>Redakteur | ISO 283 |  |  | ✅ | ❌ | ❌ | ✅ | ✅ |
| `isoMetadata.contentDescriptions.title` | DHS<br>Redakteur | ISO 401 |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.contentDescriptions.code` | DHS<br>Redakteur | ISO 402 |  | Codeliste ISO 19115: B.5.3 CI_OnLineFunctionCode | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.contentDescriptions.url` | DHS<br>Redakteur | ISO 397 |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |

### Dienste (Steuerung & Logik)

| Feldname (`key`) | Rolle | Export zu ISO | Andere Wege | Codelisten & Vorbelegungen | Hilfe | Kopieren | Übernahme | Vorlage | Löschen |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `isoMetadata.services` | DHS<br>Redakteur | - | Geoserver |  | ❌ | ❌ | ❌ | ❌ | ✅ |
| `isoMetadata.services.type` | DHS<br>Redakteur | - | Geoserver | Codeliste: <br>WMS, WMTS, WFS, ATOM | ✅ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.title` | DHS<br>Redakteur | ISO 24<br>(360 - title) | Geoserver - Titel des Dienstes<br>Geoportal - Titel der Karte |  | ✅ | ✅ | ✅ | ❌ | ❌ |
| `isoMetadata.services.shortDescription` | DHS<br>Redakteur | ISO 25<br>(abstract) |  |  | ✅ | ✅ | ✅ | ❌ | ❌ |
| `isoMetadata.services.workspace` | Redakteur | - | Geoserver - Name Arbeitsbereich |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.preview` | DHS<br>Redakteur | ISO 31<br>(ISO 48-51) |  |  | ✅ | ✅ | ✅ | ❌ | ❌ |

### WMS / WMTS (Steuerung & Logik)

| Feldname (`key`) | Rolle | Export zu ISO | Andere Wege | Codelisten & Vorbelegungen | Hilfe | Kopieren | Übernahme | Vorlage | Löschen |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `isoMetadata.services.legendImage` | DHS<br>Redakteur | ISO 31 |  |  | ✅ | ❌ | ❌ | ❌ | ❌ |
| `isoMetadata.services.legendImage.url` | DHS<br>Redakteur | ISO 49 |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.legendImage.format` | DHS<br>Redakteur | ISO 51 |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.legendImage.width` | DHS<br>Redakteur | - |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.legendImage.height` | DHS<br>Redakteur | - |  |  | ❌ | ✅ | ❌ | ❌ | ❌ |
| `clientMetadata.layers` | DHS<br>Redakteur | - | intern<br>Geoserver |  | ✅ | ❌ | ❌ | ❌ | ✅ |
| `clientMetadata.layers.title` | DHS<br>Redakteur | - | Geoserver |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `clientMetadata.layers.name` | Redakteur | - | Geoserver |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `clientMetadata.layers.styleTitle` | Redakteur | - | Geoserver - SLD-userStyle |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `clientMetadata.layers.styleName` | Redakteur | - | Geoserver |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `clientMetadata.layers.legendImage` | DHS<br>Redakteur | - | Geoserver |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `clientMetadata.layers.shortDescription` | DHS<br>Redakteur | - | Geoserver |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `clientMetadata.layers.datasource` | DHS<br>Redakteur | - | intern |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `clientMetadata.layers.secondaryDatasource` | Redakteur | - | DB<br>GeoServer |  | ✅ | ✅ | ❌ | ❌ | ❌ |

### WFS (Steuerung & Logik)

| Feldname (`key`) | Rolle | Export zu ISO | Andere Wege | Codelisten & Vorbelegungen | Hilfe | Kopieren | Übernahme | Vorlage | Löschen |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `isoMetadata.services.featureTypes` | DHS<br>Redakteur | - | Geoserver |  | ✅ | ❌ | ❌ | ❌ | ✅ |
| `isoMetadata.services.featureTypes.title` | DHS<br>Redakteur | - | Geoserver |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.featureTypes.name` | Redakteur | - | Geoserver |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.featureTypes.shortDescription` | DHS<br>Redakteur | - | Geoserver |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.featureTypes.columns` | DHS<br>Redakteur | - | Geoserver |  | ✅ | ❌ | ❌ | ❌ | ✅ |
| `isoMetadata.services.featureTypes.columns.name` | DHS<br>Redakteur | - | Datenbank<br>Geoserver |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.featureTypes.columns.alias` | DHS<br>Redakteur | - | Datenbank<br>Geoserver<br>Geoportal |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.featureTypes.columns.type` | Redakteur | - | Datenbank<br>Geoserver<br>Geoportal |  | ✅ | ✅ | ❌ | ❌ | ❌ |
| `isoMetadata.services.featureTypes.columns.filterType` | Redakteur | - | Geoportal |  | ✅ | ✅ | ❌ | ❌ | ❌ |

### Sonstige (Steuerung & Logik)

| Feldname (`key`) | Rolle | Export zu ISO | Andere Wege | Codelisten & Vorbelegungen | Hilfe | Kopieren | Übernahme | Vorlage | Löschen |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `clientMetadata.comments` | DHS<br>Redakteur | - | intern |  | ✅ | ❌ | ❌ | ❌ | ✅ |