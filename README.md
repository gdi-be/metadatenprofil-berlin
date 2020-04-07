# Metadatenprofil-Berlin
## Metadatenprofil der Geodateninfrastruktur Berlin
## BE-Profil 2.0
### Inhaltsmodell und Anwendungsprofil für BROKER-Metadaten
### Inhaltsmodell für Metadaten gemäß ISO 19115
### Inhaltsmodell für Metadaten gemäß ISO 19119

#### DEFINITIONEN IM SINNE DIESES PROFILS

##### Anwendungsprofil
Schema zur formalen Umsetzung eines Inhaltsmodells. Das Anwendungsprofil des BE-Profils besteht weiter aus spezifischen Metadatenschemata für BROKER-Metadaten.

##### ATOM
Synonym: ATOM-Datensätze. Datensatzklasse im BROKER-Informationssystem, für welche ein eigenes Metadatenschema existiert.

##### Datenbestand
Datensatzklasse im BROKER-Informationssystem, für welche ein eigenes Metadatenschema existiert.

##### Fachverfahren
Datensatzklasse im BROKER-Informationssystem, für welche ein eigenes Metadatenschema existiert.

##### Geometriedatensätze 
Datensatzklasse im BROKER-Informationssystem, für welche ein eigenes Metadatenschema existiert.

##### Inhaltsmodell
Spezifikation zu beschreibender Informationen. Das Inhaltsmodell des BE-Profils wird durch die Angaben zu Multiplizität, Datentypen und Wertebereichen für alle Elemente und Attribute sowohl der proprietären, als auch der Norm-konformen Metadaten konkretisiert.

##### Karten
Synonym: Kartendatensätze. Datensatzklasse im BROKER-Informationssystem, für welche ein eigenes Metadatenschema existiert. 

##### Katalogdienst
Webdienst für den Zugriff auf Metadaten über standardisierte Schnittstellen. Über die GDI-BE wird ein Katalogdienst in Form des durch das OGC spezifizierten Catalogue Service Web (CSW) bereitgestellt.

##### Metadaten
Beschreibende Daten für Datenbestände, Datensätze, Dienste oder Anwendungen.

##### Metadatendokument
Formale Ausprägung eines auf einen spezifischen Datenbestand oder Dienst angewandten Metadatenschemas in XML.

##### Metadatenprofil
Gesamtheit aus Inhaltsmodell und Anwendungsprofil für Metadaten in einem spezifischen, gemeinsamen Bezugsraum, hier der Geodateninfrastruktur Berlin (GDI-BE).

##### Metadatenschema
Formale Beschreibung des Inhaltsmodells und Anwendungsprofils einer bestimmten Klasse von Metadaten. In diesem Profil stehen Metadatenschemata in der Sprache XSD (XML Schema Definition) zur Verfügung.

##### Sachdaten
Synonym: Sachdatensätze. Datensatzklasse im BROKER-Informationssystem, für welche ein eigenes Metadatenschema existiert.

##### Spatiale Karte
Innerhalb der GDI-BE verwendete Bezeichnung für eine Datenbanktabellen mit räumlicher Information, welche über das Format [sld](https://en.wikipedia.org/wiki/Styled_Layer_Descriptor) durch die Mapserver-Komponente des BROKER-Informationssystems visualisiert wird.

##### Webdienst
Synonyme: Webservice, Dienst. Eindeutig identifizierbare und standardisierte Schnittstelle zum Abruf von Geodaten oder Metadaten über das http-Protokoll. In der GDI-BE kommen derzeit die durch das OGC spezifizierten Webdienste WMS, WFS und CSW zum Einsatz.


#### IM PROFIL VERWENDETE ABKÜRZUNGEN UND AKRONYME

##### BE – Berlin

##### DB - Datenbank

##### DE – Deutschland

##### EN – English

##### CRS – Coordinate Reference System

##### CSW – Catalogue Service Web

##### EPSG – European Petroleum Survey Group Geodesy

##### GIS – Geographisches Informationssystem

##### GDI – Geodateninfrastruktur

##### HTTP – Hypertext Transfer Protocol

##### INSPIRE - Infrastructure for Spatial Information in the European Community

##### ISO – International Organization for Standardization

##### METEOR – Metadaten- und Themeneditor

##### OGC – Open Geospatial Consortium

##### SLD – Styled Layer Descriptor

##### UML – Unified Modeling Language

##### URL - Uniform Resource Locator

##### UUID – Universally Unique Identifier

##### WFS – Web Feature Service

##### WMS – Web Map Service

##### XML – Extensible Markup Language

##### XSD – XML Schema Definition

#### ERLÄUTERUNGEN ZUM BERLINER METADATENPROFIL
##### ZWECK UND INHALT DES BERLINER METADATENPROFILS
Die Dokumente zum Berliner Metadatenprofil (BE-Profil) richten sich an alle Personen und Institutionen, die geographische Informationen in Form von raumbezogenen Daten (Geodaten) im Geoportal Berlin/FIS-Broker veröffentlichen möchten. Diese Daten sind mit Metadaten zu beschreiben. Sofern eine Datenbereitstellung auch über standardisierte Webdienste vorgesehen ist, sind diese Dienste ebenfalls mit Metadaten zu beschreiben. Metadaten bestehen in der Geodateninfrastruktur Berlin (GDI-BE) zu einem Teil aus Informationssystem-spezifischen, proprietären Metadaten und zu einem weiteren Teil aus Metadaten, welche konform zu über das Land Berlin hinaus gültigen Normen und Verabredungen erzeugt werden. 
Das BE-Profil bietet eine Dokumentation aller zu beschreibenden Metadateninhalte (Inhaltsmodell) sowohl für proprietäre als auch für Norm-konforme Metadaten. Für den proprietären Teil der Berliner Metadaten dient das BE-Profil darüber hinaus als Anwendungsprofil, nach welchem strukturierte Metadatendokumente erzeugt werden können.
Im Tagesgeschäft der GDI-BE werden Metadaten mit Hilfe spezifischer Anwendungskomponenten erzeugt, welche die Konformität zum BE-Profil sicherstellen. Die Nutzung dieser Komponenten steht den Geodatenbereitstellenden Stellen zur Verfügung. Davon unabhängig ist es anhand des BE-Profils auch möglich, Metadaten ohne die Nutzung dieser Komponenten zu erzeugen. Das Einpflegen von Metadaten in das Informationssystem der GDI-BE bleibt aber auch in diesem Fall den zur Administration berechtigten Angehörigen der GDI-BE vorbehalten. Für die selbständige Erzeugung von Metadaten ohne die Komponenten der GDI-BE wird ein Verständnis von Extensible Markup Language (XML) sowie den Zusammenhängen zwischen Metadaten und Geodaten vorausgesetzt. 

##### NORM-KONFORME METADATEN IN DER GDI-BE („ISO-METADATEN“)
Die Standardisierung der Beschreibung von Geographischer Information durch Metadaten ist über die Normen ISO 19115 und ISO 19119 umgesetzt. ISO 19115 definiert den Rahmen für die inhaltliche Modellierung der Beschreibung von Datenbeständen, Serien und Anwendungen. Für Webdienste kommt analog ISO 19119 zur Geltung. Sollen Geodaten über Webdienste bereitgestellt werden, ist den in der Geodateninfrastruktur Deutschland (GDI-DE) vereinbarten Verfahrensregeln zur Umsetzung des Prinzips der Daten-Dienste-Kopplung zu folgen, welches den Zusammenhang zwischen den Normen ISO 19115 und ISO 19119 und deren technischer Implementierung nach ISO 19139 gewährleistet [GDI-DE Konventionen MD]. 
ISO 19115 und ISO 19119 enthalten eine Vielzahl an Metadatenelementen und Attributen, die entweder als verpflichtend, bedingt verpflichtend oder optional zu beschreiben, definiert sind. Im Rahmen der Mitarbeit des Landes Berlin in der GDI-DE sowie in internen Abstimmungsprozessen sind zu beschreibende Teilmengen der Gesamtheit dieser Metadatenelemente und -Attribute erarbeitet worden. Diese Teilmengen ergeben das Berlin-spezifische Inhaltsmodell, welches den Norm-konformen Teil des BE-Profils abbildet. Ist für Geodaten eine Betroffenheit gemäß der europäischen INSPIRE-Richtlinie festgestellt worden, sind weitere und unter Umständen abweichende Inhalte aus den beiden ISO-Normen zu beschreiben, welche ebenfalls in diesem Metadatenprofil dokumentiert sind. Grundsätzlich folgt dabei die GDI-BE den bundesweit abgestimmten Konventionen zu Metadaten, welche dem Dokument „GDI-DE Architektur – Konventionen zu Metadaten“ ([GDI-DE Konventionen]) zu entnehmen sind.
Die inhaltliche Modellierung der Norm-konformen Metadaten ist in dem Verzeichnis [tables](tables) dieses Profils (-[>Arbeitsblatt ISO Metadata …ISO 19115, 19119](tables/oeffentlich/iso.html)) dokumentiert. Für die Erzeugung von Norm-konformen Metadaten im XML-Format ist dem Implementierungsschema ISO/TS19139:2007 zu folgen. 

*Hinweis:  
Einzelne Inhalte der ISO-konformen Metadaten werden direkt aus proprietären BROKER-Metadateninhalten (s.u.) abgeleitet. Die betroffenen Elemente und Attribute sind dem Tabellenteil dieses Profils zu entnehmen (Spalte G  „Relation zu“ in den Arbeitsblättern der einzelnen BROKER-Datensatzklassen). 
Die Metadatenerfassungskomponente METEOR bietet die Möglichkeit zur teilautomatisierten Erzeugung von Norm- und INSPIRE-konformen Metadaten, sofern bereits proprietäre BROKER-Metadaten beschrieben worden sind.*

##### PROPRIETÄRE METADATEN IN DER GDI-BE („BROKER-METADATEN“)
Geodatenbereitstellende Komponente der Geodateninfrastruktur Berlin ist das Metadatengestützte Informationssystem BROKER. Eine Veröffentlichung von Geodaten im Geoportal Berlin/FIS-Broker ist ohne die Beschreibung von Metadaten nicht möglich.
Neben den oben beschriebenen, nach ISO-Vorgaben international genormten Metadaten, gibt es innerhalb der GDI-BE auch proprietäre Metadaten, welche für Verarbeitungsprozesse und Kategorisierungen gemäß der Systemlogik des BROKER-Informationssystems benötigt werden. Diese proprietären Metadaten werden im Folgenden als BROKER-Metadaten bezeichnet. In diesem Profil ist die Metadatenbeschreibung für sechs verschiedene Klassen von Datensätzen dokumentiert, welche sich hinsichtlich ihrer Funktion innerhalb der BROKER-Infrastruktur und in ihrer Präsentation im Geoportal Berlin unterscheiden. Für jede Datensatzklasse steht in diesem Profil ein eigenes Metadatenschema zur Verfügung. 
Der Zusammenhang zwischen den mit proprietären BROKER-Metadaten zu beschreibenden Datensatzklassen und den mit Norm-konformen Metadaten zu beschreibenden Ressourcen im Sinne der GDI-DE- und INSPIRE-Architektur ist in der folgenden Tabelle vereinfacht dargestellt. Für BROKER-Metadaten bietet das BE-Profil neben einem Inhaltsmodell auch ein vollständiges Anwendungsprofil.

BROKER-Metadatenschema | Entsprechung in ISO-Norm
------------ | -------------
[Datenbestand](tables/oeffentlich/datenbestand.html) | 19115 (hierarchyLevel@codeListValue: dataset)
[Karte](tables/oeffentlich/karte.html) | 19119 (hierarchyLevel@codeListValue: service, serviceType: view)
[Sachdatensatz](tables/oeffentlich/sachdatensatz.html) | 19119 (hierarchyLevel@codeListValue: service, serviceType: download)
[Geometriedatensatz](tables/oeffentlich/geometriedatensatz.html) | 19119 (hierarchyLevel@codeListValue: service, serviceType: download)
[ATOM](tables/oeffentlich/atom.html) | 19119 (hierarchyLevel@codeListValue: service, serviceType: download)
[Fachverfahren](tables/oeffentlich/fachverfahren.html) | 19119 (hierarchyLevel@codeListValue: service, serviceType: application)

*Hinweis:  
Aus den BROKER-Metadaten können bestimmte Inhalte der ISO-Norm-konformen Metadaten mit Hilfe der Metadaten-Erfassungskomponente METEOR automatisiert abgeleitet werden.*

##### ANWENDUNG DES BE-PROFILS
Ein vollständiges Metadatendokument nach den Vorgaben dieses Metadatenprofils beinhaltet immer sowohl BROKER- als auch ISO-konforme Metadaten. Das Format eines Metadatendokuments ist XML. Wie ein solches XML-Dokument zu strukturieren ist, ist für die BROKER-Metadaten in den Tabellen dieses Profils dokumentiert. Zudem steht für jede hier dokumentierte Datensatzklasse eine XML-Schemadatei (XSD) zur Verfügung, gegen welche ein BROKER-Metadaten beschreibendes XML-Dokument validiert werden kann. Codelisten, welche zulässige Inhalte für spezifische Metadatenattribute und –Elemente definieren, liegen ebenfalls in diesem Profil vor.
Die ISO-konformen Metadaten werden durch das BROKER-Metadatenelement IsoMetadata umschlossen. Für die Validierung von Metadaten auf ISO- und INSPIRE-Konformität kann die Testsuite der GDI-DE genutzt werden. Eine Validierung der ISO-Metadaten ist für ISO 19115 gegen das Schema http://schemas.opengis.net/iso/19139/20060504/gmd/gmd.xsd und für ISO 19119 gegen das Schema http://schemas.opengis.net/iso/19139/20060504/srv/srv.xsd möglich.
Metadaten werden analog zur Geodatenbereitstellung im Geoportal Berlin veröffentlicht und sind zudem über Katalogdienste abrufbar.

*Hinweis:  
In den Komponenten des BROKER-Informationssystems wurden Validierungsprüfungen implementiert, welche die Konformität zum BE-Profil sicherstellen. Sofern die Erfassungskomponente METEOR zur Erzeugung von Metadaten genutzt wird, kann auf weitere Validierungen verzichtet werden.*

##### REFERENZEN
*	[GDI-DE Konventionen MD] GDI-DE Architektur – Konventionen zu Metadaten“ (Architektur der Geodateninfrastruktur Deutschland: Konventionen zu Metadaten der GDI.DE (Konventionendokument), V1.2, 01.08.2017)
*	 [INS TG Metadata 1.3] INSPIRE Metadata Implementing Rules: Technical Guidelines based on EN ISO 19115 and EN ISO 19119, V1.3, 2013-10-29 (last revision)
*	[INS VO MD] VERORDNUNG (EG) Nr. 1205/2008 DER KOMMISSION vom 3. Dezember 2008 zur Durchführung der Richtlinie 2007/2/EG des Europäischen Parlaments und des Rates hinsichtlich Metadaten
*	[ISO 19115 DE-ÜB] Koordinierungsstelle GDI-DE: Deutsche Übersetzung der Metadatenfelder des ISO 19115 Geographic Information Metadata (Standardversion ISO 19115:2003E/Cor.1:2006E)
*	[ISO 19119:2005] ISO 19119 - Geographic Information - Services
*	 [OGC CSW 2.0.2 APISO] OpenGIS® Catalogue Services Specification 2.0.2 - ISO Metadata Application Profile: Corrigendum, 07-045r1, 2018-03-07
