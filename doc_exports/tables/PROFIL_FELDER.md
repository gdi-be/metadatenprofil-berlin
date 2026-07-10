# 📋 Metadatenprofil Berlin - Dokumentation der Felder

Diese Datei enthält die fachliche und funktionale Beschreibung aller Felder des Metadatenprofils.

### Basisangaben

| ID | Feldname (`key`) | Anzeige-Titel (`label`) | Multiplizität | Typ | Funktionsweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `isoMetadata.title` | Titel des Datenbestandes | 1..1 | Freitextfeld (maximal 250 Zeichen) | Der Titel des Datenbestandes muss im internen Metadatenkatalog eineindeutig sein. Das Formular verhindert durch Überprüfung eine Fehleingabe.<br>Ab 100 Zeichen wird die Zeichenanzeige rot eingefärbt. |
| 2 | `isoMetadata.description` | Kurzbeschreibung des Datenbestandes | 1..1 | Freitextfeld (maximal 1250 Zeichen) | Erfassen eines unformatierten Textes als Kurzbschreibung. Zeilenumbrüche sind zulässig. |
| 15 | `isoMetadata.keywords` | Schlagwörter | 1..* | Vorbelegungen<br>Thesaurus<br>Freitextfeld | Erfassen von thematischen Schlagwörtern über:<br>Thesaurus Umthes, Einzeleingabe, kommaseparierte Eingabe.<br>Übernahme in Datenbestands- und alle Dienst-Metadaten.<br>Alle bedingten Schlagwörter werden bei der ISO-Erzeugung automatisch gesetzt und werden in der Schlagwortliste ausgegraut angezeigt. |
| 29 | `isoMetadata.preview` | Vorschaubild | 1..1 | URL | Erfassen einer URL auf eine im Internet aufrufbare Vorschaugrafik. |
| 19 | `isoMetadata.pointsOfContact` | Kontaktangaben | 1..* | Inkrement | Ein Kontakt ist mindestens auszufüllen. Die Anzahl kann über den Plus-Button erhöht werden.<br>Beim Erzeugen von ISO-MD wird die Art des Kontaktes automatisiert auf "pointOfContact" in ISO-Feld 379 gesetzt.<br>Kontaktangaben des angemeldeten Nutzenden können per Übernahme-Button aus dem angebundenen AD-Userverzeichnis in eine neue Kontaktangabe übernommen werden und angepasst werden. |
| 20 | `isoMetadata.pointsOfContact.name` | Name | 1..1 | AD-Suchfeld<br>Freitextfeld | Erfassen eines Kontaktnamens. |
| 21 | `isoMetadata.pointsOfContact.organisation` | Organisation | 1..1 | AD-Suchfeld<br>Freitextfeld | Erfassen einer Kontaktorganisation. |
| 22 | `isoMetadata.pointsOfContact.phone` | Telefonnummer | 1..1 | AD-Suchfeld<br>Freitextfeld | Erfassen einer Kontakttelefonnummer. |
| 23 | `isoMetadata.pointsOfContact.email` | E-Mailadresse | 1..1 | AD-Suchfeld<br>Freitextfeld | Erfassen einer gültigen Kontakt-Emailadresse. |

### Einordnung

| ID | Feldname (`key`) | Anzeige-Titel (`label`) | Multiplizität | Typ | Funktionsweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 5 | `isoMetadata.metadataProfile` | Metadaten-Typ | 1..1 | Auswahlliste | Auswahl der entsprechenden INSPIRE Relevanz. Entsprechend werden abhängige Metadatenfelder angezeigt oder nicht. Ebenso werden bei der ISO-Erzeugung entsprechende Templates und Erzegungsregeln angewandt.<br>Beim ändern des INSPIRE-Typs zu ISO sollen die zusätzlichen Felder dennoch gespeichert bleiben, sie tauchen im Formular aber nicht mehr auf und werden bei der ISO-Erzeugung nicht berücksichtigt. |
| 7 | `isoMetadata.inspireTheme` | INSPIRE Annex Thema | K..1 | Auswahlliste | Konditionales Feld: Es wird nur angezeigt, wenn Metadatentyp "INSPIRE-harmonisiert" oder "INSPIRE-identifiziert" ausgewählt wurde.<br>Mehrfachauswahl möglich, wenn Typ = INSPIRE identifiziert. Wenn Typ = INSPIRE harmonisiert, dann kann nur ein Thema ausgewählt werden. <br>Das Feld bedingt automatische Vorbelegungen bzw. INSPIRE spezifische Auswahllisten in weiteren Formularfeldern und bei der ISO-Erzeugung. |
| 70 | `isoMetadata.inspireFormatName` | Schema-Name des INSPIRE Themas | K..1 | Auswahlliste | Konditionales Feld, wird nur angezeigt, wenn Metadatentyp "INSPIRE-harmonisiert" ausgewählt wurde.<br>Auswahl der aus dem Annex-Thema zugehörigen Schemata. |
| 38 | `isoMetadata.inspireAnnexVersion` | Schema-Version des INSPIRE Themas | K..1 | Freitextfeld | Konditionales Feld, wird nur angezeigt, wenn Metadatentyp "INSPIRE-harmonisiert" ausgewählt wurde.<br>Eintragen der INSPIRE-Annex-Schema Version in ein Freitextfeld. Alle anderen Metadaten-Typen bekommen an dieser Stelle eine automatische Vorbelegung. |
| 37 | `isoMetadata.valid` | Überprüfung des Qualitätsberichts | K..1 | Entscheidung J/N | Konditionales Feld, wird nur angezeigt, wenn Metadatentyp "INSPIRE-harmonisiert" ausgewählt wurde. |
| 4 | `isoMetadata.privacy` | Datenschutz-Einstellungen | 1..1 | Auswahlliste | Die Auswahl aus der Liste bedingt die Vorbelegung der Nutzungsbestimmungen:<br>Wird "Nicht Datenschut relevant" ausgewählt, so wird bei den NB die codeliste "terms_of_use.yaml" angezeigt.<br>Wird ein anderer Datenschutz ausgewählt, wird bei den NB die codeliste "terms_of_use_on_privacy.yaml" angezeigt. |
| 25 | `isoMetadata.termsOfUseId` | Nutzungsbestimmungen | 1..1 | Auswahlliste | Auswahlliste ist abhängig vom ausgewählten Datenschutz:<br>Wird "Nicht Datenschut relevant" ausgewählt, so wird bei den NB die codeliste "terms_of_use.yaml" angezeigt. Vorbelegung mit "Datenlizenz Deutschland Zero 2.0".<br>Wird ein anderer Datenschutz ausgewählt, wird bei den NB die codeliste "terms_of_use_on_privacy.yaml" angezeigt. Vorbelegung mit "Dienstgebrauch". |
| 26 | `isoMetadata.termsOfUseSource` | Quellenangabe | k..1 | Freitextfeld | Konditionales Feld. Es erscheint nur, wenn die NB 2, 3 oder 4 der  "terms_of_use.yaml" ausgewählt wurde. Die NB 1 brauch keine Quellenangabe. Erfassen der anzugebenden Quelle. Diese wird bei der ISO-Erzeugung als Variable in die JSON-Notation und in den Text der Nutzungsbestimmungen übernommen. |
| 6 | `isoMetadata.highValueDataset` | High Value Datensatz | 1..1 | Entscheidung J/N | Ein "ja" bedingt das Eintragen der HVD-Kategorie in die ISO-Metadaten. Ebenso muss bei "ja" das Feld HVD-Kategorie ausgefüllt werden. |
| 8 | `isoMetadata.highValueDataCategory` | HVD Kategorien | K..1 | Auswahlliste | Auswahlliste von HVD-Kategorien, wenn HVD-Betroffenheit vorliegt. Mehrfachauswahl möglich. Keine Automatische Vorbelegung. |
| 13 | `isoMetadata.topicCategory` | Themenkategorie | 1..1 | Auswahlliste | Wenn oben ein INSPIRE Thema ausgewählt wurde, wird die Auswahlliste entsprechend der Zuordnungstabelle der GDI-DE vorausgefüllt. Wenn nicht, kann aus der Auswahlliste ein Eintrag frei ausgewählt werden. |

### Zeitliche und Räumliche Angaben

| ID | Feldname (`key`) | Anzeige-Titel (`label`) | Multiplizität | Typ | Funktionsweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 9 | `isoMetadata.created` | Erstellungsdatum | 0..1 | Datumsauswahl | Optionales Feld. Erfassen einer Datumsangabe, freihändig oder über eine Kalenderauswahl.<br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| 10 | `isoMetadata.published` | Veröffentlichungsdatum | 1..1 | Datumsauswahl | Optionales Feld. Erfassen einer Datumsangabe, freihändig oder über eine Kalenderauswahl.<br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| 14 | `isoMetadata.maintenanceFrequency` | Pflegeintervall | 1..1 | Auswahlliste | Erfassen des Pflegeintervalls über  eine Auswahlliste auf Basis der ISO-Codeliste.<br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| 11 | `isoMetadata.modified` | letzte Aktualisierung | 0..1 | Datumsauswahl | Optionales Feld. Erfassen einer Datumsangabe, freihändig oder über eine Kalenderauswahl.<br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| - | `-` | Gültigkeitszeitraum | 0..1 | Überschrift | Optionales Feld. Erfassen eines Anfang- und eines Enddatums, freihändig oder über eine Kalenderauswahl.<br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| 12 | `isoMetadata.validFrom` | gültig ab | 1..1 | Datumsauswahl | Optionales Feld. Erfassen eines Anfangsdatums, freihändig oder über eine Kalenderauswahl.<br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| 24 | `isoMetadata.validTo` | gültig bis | 1..1 | Datumsauswahl | Optionales Feld. Erfassen eines Enddatums, freihändig oder über eine Kalenderauswahl.<br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| 16 | `technicalMetadata.deliveredCrs` | geliefertes Koordinatensystem | 0..1 | Freitextfeld | Erfassen des gelieferten CRS in einem Freitextfeld. |
| 17 | `isoMetadata.crs` | abzugebendes Koordinatensystem | 1..1 | Auswahlliste | Erfassen des CRS über eine Auswahlliste in dem die Daten in der sekundären Datenhaltung vorliegen und über Dienste abgegeben werden. |
| 18 | `isoMetadata.extent` | Räumliche Ausdehnung | 1..1 | Überschrift | Erfassen der Ausdehnung des Datensatzes. Vorlagen sind für Berlin und Brandenburg über Buttons auswählbar. Freie Eingabe von Koordinaten im ausgewählten CRS möglich. <br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten.<br>Bedingt die Angabe des Regionalschlüssels bei der ISO-Erzeugung bei Auswahl der Vorlage Berlin. |
| 71 | `isoMetadata.extent.minx` | Minimaler X-Wert | 1..1 | Gleitkommazahl | Freie Eingabe von Koordinaten im ausgewählten CRS möglich. <br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| 72 | `isoMetadata.extent.maxx` | Maximaler X-Wert | 1..1 | Gleitkommazahl | Freie Eingabe von Koordinaten im ausgewählten CRS möglich. <br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| 73 | `isoMetadata.extent.miny` | Minimaler Y-Wert | 1..1 | Gleitkommazahl | Freie Eingabe von Koordinaten im ausgewählten CRS möglich. <br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| 74 | `isoMetadata.extent.maxy` | Maximaler Y-Wert | 1..1 | Gleitkommazahl | Freie Eingabe von Koordinaten im ausgewählten CRS möglich. <br>Übernahme der Angabe in alle zugehörigen Dienstmetadaten. |
| - | `-` | Räumliche Auflösung | 1..1 | Entscheidung | Erfassen, ob Vergleichsmaßstab oder Bodenauflösung verpflichtend auszufüllen ist. |
| 27 | `isoMetadata.scale` | Vergleichsmaßstab | k..1 | Ganze Zahl | Konditionales Feld, Verpflichtung und Anzeige im Formular ist abhängig von der Auswahl unter "Auflösung". |
| 28 | `isoMetadata.resolutions` | Bodenauflösung | k..1 | Gleitkommazahl | Konditionales Feld, Verpflichtung und Anzeige im Formular ist abhängig von der Auswahl unter "Auflösung". |
| 39 | `isoMetadata.spatialRepresentationTypes` | Räumliche Darstellungsart | 1..1 | Auswahlliste | Erfassen der Darstellungsart durch Auswahl aus einer ISO-basierten Auswahlliste. |

### Weitere Angaben

| ID | Feldname (`key`) | Anzeige-Titel (`label`) | Multiplizität | Typ | Funktionsweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 30 | `isoMetadata.contentDescription` | Inhaltliche Beschreibung | 0..1 | URL | Optionales Erfassen einer URL auf ein PDF-Dokument.<br>Die URL auf diese Ressource wird unter transfer-Options mit dem Code "information" und der Beschreibung "Inhaltliche Beschreibung" verlinkt. |
| 31 | `isoMetadata.technicalDescription` | Technische Beschreibung | 0..1 | URL | Optionales Erfassen einer URL auf ein PDF-Dokument.<br>Die URL auf diese Ressource wird unter transfer-Options mit dem Code "information" und der Beschreibung "Technische Beschreibung" verlinkt. |
| 32 | `isoMetadata.lineage` | Herkunft der Daten | 0..* | Inkrement | Optionales Erfassen von keiner, einer oder mehreren Datengrundlagen. |
| 33 | `isoMetadata.lineage.title` | Titel | k..1 | Freitextfeld/ Suchfeld/ Vorschlagsliste | Konditionales Feld in Abhängigkeit vom Feld Datengrundlage. Erfassen eines Datengrundlagen-Titels als Freitext oder Suchen und Übernahme eines Datenbestand-Titels aus dem bestehenden Katalog mittels Auswahl aus einer Vorschlagsliste. Die Übernahme wird nicht automatisch aktualisiert, wenn sich der eingetragene Datenbestand verändert. |
| 34 | `isoMetadata.lineage.date` | Datum der Veröffentlichung | k..1 | Datumsauswahl | Konditionales Feld in Abhängigkeit vom Feld Datengrundlage. Erfassen des Datums der Veröffentlichung einer Datengrundlage. Wird bei Auswahl eines Datenbestandes aus dem eigenen Katalog automatisch übernommen. Die Übernahme wird nicht automatisch aktualisiert, wenn sich der eingetragene Datenbestand verändert. |
| 35 | `isoMetadata.lineage.identifier` | Identifier | k..1 | URL mit Identifier | Konditionales Feld in Abhängigkeit vom Feld Datengrundlage. Erfassen des Identifiers bzw. eines eindeutigen Ressourcenaufrufs einer Datengrundlage. Wird bei Auswahl eines Datenbestandes aus dem eigenen Katalog automatisch übernommen bzw. erzeugt. Die Übernahme wird nicht automatisch aktualisiert, wenn sich der eingetragene Datenbestand verändert. |
| 36 | `clientMetadata.relatedTopics` | Verwandte Themen (MTK) | 0..1 | Freitextfeld | Keine Erfassung im Formular möglich. Anzeige nur in der Leseansicht. |
| 41 | `isoMetadata.contentDescriptions` | Weitere Informationen | 0..* | Inkrement | Optionales Erfassen von keinem, einem oder mehreren Verweisen auf weitere Quellen zu dem Datenbestand. |
| 42 | `isoMetadata.contentDescriptions.title` | Titel | 0..1 | Freitext | Erfassen eines Quellen-Titels als Freitext. |
| 43 | `isoMetadata.contentDescriptions.code` | Code | 0..1 | Auswahlliste | Erfassen der Funktion der angebebenen Quelle aus der ISO-Code-Auswahlliste. |
| 44 | `isoMetadata.contentDescriptions.url` | URL | 0..1 | URL | Erfassen einer validen URL auf eine bestehende Ressource. |

### Dienste

| ID | Feldname (`key`) | Anzeige-Titel (`label`) | Multiplizität | Typ | Funktionsweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 40 | `isoMetadata.services` | + | 0..* | Inkrement | Optionales Erfassen von keinem, einem oder mehreren Diensten des Datenbestandes. |
| 58 | `isoMetadata.services.type` | Dienst-Typ | 1..1 | Auswahlliste | Erfassen des Dienste-Typs. |
| 59 | `isoMetadata.services.title` | Titel des Dienstes | 1..1 | Freitext (max 250 Zeichen) | Erfassen des Dienste-Titels als Freitext.<br>Ab 100 Zeichen wird die Zeichenanzeige rot eingefärbt. |
| 60 | `isoMetadata.services.shortDescription` | Kurzbeschreibung des Dienstes | 1..1 | Freitext (max 500 Zeichen) | Erfassen der Dienste-Kurzbeschreibung als Freitext. |
| 45 | `isoMetadata.services.workspace` | Arbeitsbereich des Dienstes | 1..1 | Textfeld mit ^[a-z0-9_]+$ | Erfassen eines eindeutigen Bezeichners für den Arbeitsbereich des Dienstes.<br>Tupel aus Dienst-Typ und Dienst-ID muss metadatenübergreifend eindeutig sein. Das Formular verhindert durch Überprüfung eine Fehleingabe. |
| 46 | `isoMetadata.services.preview` | Vorschau des Dienstes | 1..1 | URL | Automatische Übernahme der Vorschau aus dem Datenbestand. Anpassen oder Ersetzen im Freitextfeld möglich. |

### WMS / WMTS

| ID | Feldname (`key`) | Anzeige-Titel (`label`) | Multiplizität | Typ | Funktionsweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 47 | `isoMetadata.services.legendImage` | Gesamtlegende | 0..1 | Überschrift | Erfassen einer Gesamtlegende für einen Darstellungsdienst. Breite, Höhe und Datenformat werden automatisiert abgeleitet, in der Datenbank abgelegt und bei der ISO-Erzeugung in die Metadaten übernommen. |
| 75 | `isoMetadata.services.legendImage.url` | URL | 0..1 | URL | Erfassen einer validen URL auf eine bestehende Ressource. |
| 76 | `isoMetadata.services.legendImage.format` | Format | 0..1 | Freitext | Das Format wird automatisch vom angegebenen Bild ermittelt, wenn die URL valide ist. |
| 77 | `isoMetadata.services.legendImage.width` | Breite | 0..1 | Ganze Zahlen | Die Breite wird automatisch vom angegebenen Bild ermittelt, wenn die URL valide ist. |
| 78 | `isoMetadata.services.legendImage.height` | Höhe | 0..1 | Ganze Zahlen | Die Höhe wird automatisch vom angegebenen Bild ermittelt, wenn die URL valide ist. |
| 48 | `clientMetadata.layers` | Kartenebenen | 1..* | Inkrement | Erfassen mindestens einer oder mehrerer Kartenebenen. |
| 49 | `clientMetadata.layers.title` | Titel der Kartenebene | 1..1 | Freitext (max 250 Zeichen) | Erfassen des Ebenen-Titels als Freitext. |
| 50 | `clientMetadata.layers.name` | Name der Kartenebene | 1..1 | Freitext<br>(nur ASCII<br>max 100 Zeichen) | Erfassen des Ebenen-Namens als Freitext. |
| 52 | `clientMetadata.layers.styleTitle` | Titel des Styles | k..1 | Freitext<br>(max 250 Zeichen) | Optionales Erfassen des Style-Titels als Freitext. Wenn  unter "Metadatentyp" -> "INSPIRE-harmonisiert" ausgewählt wurde, ist es ein Pflichtfeld. |
| 51 | `clientMetadata.layers.styleName` | Name des Style | 1..1 | Freitext<br>(Nur ASCII max 100 Zeichen) | Erfassen des Style-Namens als Freitext, Sonderzeichen sind untersagt. |
| 53 | `clientMetadata.layers.legendImage` | Legende | 0..1 | URL<br>oder Upload | Erfassen einer validen URL auf eine bestehende Ressource. |
| 54 | `clientMetadata.layers.shortDescription` | Kurzbeschreibung | 1..1 | Freitext (max 500 Zeichen) | Erfassen der Ebenen-Kurzbeschreibung als Freitext. |
| 55 | `clientMetadata.layers.datasource` | Ablageort der Daten | 0..1 | Freitext oder Upload | Optionales Erfassen eines Ablageortes der von der DHS übergebenden Geodaten für diese Kartenebene. |
| 68 | `clientMetadata.layers.secondaryDatasource` | sekundäre Datenhaltung | 0..1 | Freitext | Optionales Erfassen des Ablageortes in der sekundären Datenhaltung der GDI. |

### WFS

| ID | Feldname (`key`) | Anzeige-Titel (`label`) | Multiplizität | Typ | Funktionsweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 56 | `isoMetadata.services.featureTypes` | FeatureTypes | 1..* | Inkrement | Erfassen mindestens eines oder mehrerer FeatureTypes. |
| 61 | `isoMetadata.services.featureTypes.title` | Titel des FeatureTypes | 1..1 | Freitextfeld<br>(max 100 Zeichen) | Erfassen des FeatureType-Titels als Freitext. |
| 62 | `isoMetadata.services.featureTypes.name` | Name des FeatureTypes | 1..1 | Freitextfeld<br>(nur ASCII<br>max 100 Zeichen) | Erfassen des FeatureType-Namens als Freitext. |
| 69 | `isoMetadata.services.featureTypes.shortDescription` | Kurzbeschreibung des FeatureTypes | 1..1 | Freitext (max 500 Zeichen) | Erfassen der FeatureType-Kurzbeschreibung als Freitext. |
| 63 | `isoMetadata.services.featureTypes.columns` | Attribute | 1..* | Inkrement | Erfassen mindestens eines oder mehrerer Attribute. |
| 64 | `isoMetadata.services.featureTypes.columns.name` | Attribut-Name | 1..1 | Freitextfeld<br>(nur ASCII<br>max 100 Zeichen) | Erfassen eines Attribut-Namens. |
| 65 | `isoMetadata.services.featureTypes.columns.alias` | Attribut-Alias | 1..1 | Freitextfeld | Erfassen eines Attribut-Alias für das angelegt Attribut (Menschenlesbarer Titel). |
| 66 | `isoMetadata.services.featureTypes.columns.type` | Attribut-Datentyp | 0..1 | Auswahlliste | Optionales Erfassen des Attribut-Datentyps in der sekundären GDI Datenhaltung. |
| 67 | `isoMetadata.services.featureTypes.columns.filterType` | Attribut-Filter-Typ | 0..1 | Auswahlliste | Optionales Erfassen des Attribut-Filtertyps für mögliche Oberflächenfilterfunktionen.<br>Vorrübergehend deaktiviert. |

### Sonstige

| ID | Feldname (`key`) | Anzeige-Titel (`label`) | Multiplizität | Typ | Funktionsweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 3 | `clientMetadata.comments` | Kommentare | 1..1 | Freitextfeld | Erfassen von Kommentaren zur internen Kommunikation zwischen den verschiedenen Rollen. |