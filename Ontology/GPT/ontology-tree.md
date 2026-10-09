# Proposed ontology — complete canonical tree

555 defined classes. Every indented edge means **is a subclass of**. One primary parent per nonroot; additional superclass edges and role-qualified expressions appear below. JSON is authoritative.

Sibling lists are **selective**, not declarations of exhaustiveness or disjointness. A specification and the entity satisfying it are distinct: “Food specification” classifies unary specifications; actual food portions use a qualified bearer expression.

## Canonical tree

- <a id="Entity"></a>**Entity** — Anything admitted as a subject of reference or predication. `Entity`
    - <a id="RealizedEntity"></a>**Realized entity** — An entity individuated by its concrete occurrence, embodiment, or situated realization. `RealizedEntity`
        - <a id="Object"></a>**Object** — A realized entity identified by its organization or constitution rather than by an occurrence. `Object`
            - <a id="Item"></a>**Item** — An object unified as one constituent whole rather than by membership alone. `Item`
                - <a id="NaturalObject"></a>**Natural object** — An item whose kind identity does not require intentional production or modification. `NaturalObject`
                    - <a id="AbioticObject"></a>**Abiotic object** — A natural object whose constitution does not derive from biological activity. `AbioticObject`
                - <a id="BioticObject"></a>**Biotic object** — An item constituted by an organism or by products of biological activity. `BioticObject`
                    - <a id="Organism"></a>**Organism** — A cellular living individual with an integrated biological organization. `Organism`
                        - <a id="Bacterium"></a>**Bacterium** — An organism belonging to the bacterial lineage. `Bacterium`
                        - <a id="Archaeon"></a>**Archaeon** — An organism belonging to the archaeal lineage. `Archaeon`
                        - <a id="Eukaryote"></a>**Eukaryote** — An organism belonging to the lineage characterized ancestrally by nucleated cells. `Eukaryote`
                            - <a id="Plant"></a>**Land plant** — A eukaryote belonging to the embryophyte lineage. `Plant`
                                - <a id="Moss"></a>**Moss** — A land plant belonging to the moss lineage, Bryophyta. `Moss`
                                - <a id="VascularPlant"></a>**Vascular plant** — A land plant belonging to the lineage with specialized vascular tissues. `VascularPlant`
                                    - <a id="Fern"></a>**Fern** — A vascular plant belonging to the fern lineage, including horsetails. `Fern`
                                    - <a id="SeedPlant"></a>**Seed plant** — A vascular plant belonging to the lineage characterized by seeds. `SeedPlant`
                                        - <a id="Gymnosperm"></a>**Gymnosperm** — A seed plant in the living lineages whose ovules are not enclosed in ovaries. `Gymnosperm`
                                        - <a id="FloweringPlant"></a>**Flowering plant** — A seed plant belonging to the angiosperm lineage. `FloweringPlant`
                                    - <a id="Lycophyte"></a>**Lycophyte** — A vascular plant belonging to the clubmoss, spikemoss, and quillwort lineage. `Lycophyte`
                            - <a id="Fungus"></a>**Fungus** — A eukaryote belonging to the fungal lineage. `Fungus`
                        - <a id="Animal"></a>**Animal** — A eukaryote belonging to the metazoan lineage. `Animal`
                            - <a id="Sponge"></a>**Sponge** — An animal belonging to the sponge lineage, Porifera. `Sponge`
                            - <a id="Cnidarian"></a>**Cnidarian** — An animal belonging to the lineage characterized by cnidocytes. `Cnidarian`
                            - <a id="Bilaterian"></a>**Bilaterian** — An animal belonging to the lineage with ancestrally bilateral body organization. `Bilaterian`
                                - <a id="Arthropod"></a>**Arthropod** — A bilaterian belonging to the lineage with jointed appendages and an exoskeleton. `Arthropod`
                                    - <a id="Insect"></a>**Insect** — An arthropod belonging to the lineage with ancestrally three pairs of thoracic legs. `Insect`
                                    - <a id="Arachnid"></a>**Arachnid** — An arthropod belonging to the arachnid lineage, including spiders and scorpions. `Arachnid`
                                - <a id="Mollusc"></a>**Mollusc** — A bilaterian belonging to the molluscan lineage. `Mollusc`
                                - <a id="Annelid"></a>**Annelid** — A bilaterian belonging to the annelid lineage of segmented worms. `Annelid`
                                - <a id="Nematode"></a>**Nematode** — A bilaterian belonging to the nematode lineage of roundworms. `Nematode`
                                - <a id="Echinoderm"></a>**Echinoderm** — A bilaterian belonging to the lineage with a water vascular system. `Echinoderm`
                                - <a id="Chordate"></a>**Chordate** — A bilaterian belonging to the lineage characterized ancestrally by a notochord. `Chordate`
                            - <a id="Vertebrate"></a>**Vertebrate** — A chordate belonging to the lineage characterized ancestrally by vertebral elements. `Vertebrate`
                                - <a id="JawedVertebrate"></a>**Jawed vertebrate** — A vertebrate belonging to the lineage characterized ancestrally by jaws. `JawedVertebrate`
                                    - <a id="CartilaginousFish"></a>**Cartilaginous fish** — A jawed vertebrate belonging to the shark, ray, and chimaera lineage. `CartilaginousFish`
                                    - <a id="BonyVertebrate"></a>**Bony vertebrate** — A jawed vertebrate belonging to the bony-vertebrate lineage, including tetrapods. `BonyVertebrate`
                                        - <a id="RayFinnedFish"></a>**Ray-finned fish** — A bony vertebrate belonging to the ray-finned lineage. `RayFinnedFish`
                                        - <a id="LobeFinnedVertebrate"></a>**Lobe-finned vertebrate** — A bony vertebrate belonging to the lobe-finned lineage, including tetrapods. `LobeFinnedVertebrate`
                                            - <a id="Tetrapod"></a>**Tetrapod** — A lobe-finned vertebrate belonging to the lineage with ancestrally four limbs. `Tetrapod`
                                                - <a id="Amphibian"></a>**Amphibian** — A tetrapod belonging to the amphibian lineage, including frogs, salamanders, and caecilians. `Amphibian`
                                - <a id="Amniote"></a>**Amniote** — A tetrapod belonging to the lineage with ancestrally amniotic embryonic membranes. `Amniote`
                                    - <a id="Synapsid"></a>**Synapsid** — An amniote belonging to the mammal-line lineage with an ancestral single temporal opening. `Synapsid`
                                    - <a id="Mammal"></a>**Mammal** — A synapsid belonging to the lineage characterized by mammary glands and hair. `Mammal`
                                        - <a id="Monotreme"></a>**Monotreme** — A mammal belonging to the egg-laying monotreme lineage. `Monotreme`
                                        - <a id="Marsupial"></a>**Marsupial-line mammal** — A mammal belonging to Metatheria, including living marsupials and their extinct stem relatives. `Marsupial`
                                        - <a id="PlacentalMammal"></a>**Eutherian mammal** — A mammal belonging to Eutheria, including crown placentals and their extinct stem relatives. `PlacentalMammal`
                                            - <a id="Carnivoran"></a>**Carnivoran** — A placental mammal belonging to the order Carnivora, irrespective of diet. `Carnivoran`
                                                - <a id="Canine"></a>**Canid** — A carnivoran belonging to the dog family, Canidae. `Canine`
                                                    - <a id="Dog"></a>**Domestic dog** — A canid belonging to the domestic dog lineage. `Dog`
                                                - <a id="Feline"></a>**Felid** — A carnivoran belonging to the cat family, Felidae. `Feline`
                                                    - <a id="Cat"></a>**Domestic cat** — A felid belonging to the domestic cat lineage. `Cat`
                                            - <a id="Rodent"></a>**Rodent** — A placental mammal belonging to the rodent lineage. `Rodent`
                                            - <a id="Cetartiodactyl"></a>**Cetartiodactyl** — A placental mammal in the even-toed ungulate and cetacean lineage. `Cetartiodactyl`
                                                - <a id="Cetacean"></a>**Cetacean** — A cetartiodactyl belonging to the whale, dolphin, and porpoise lineage. `Cetacean`
                                            - <a id="Perissodactyl"></a>**Odd-toed ungulate** — A placental mammal belonging to the horse, rhinoceros, and tapir lineage. `Perissodactyl`
                                            - <a id="Lagomorph"></a>**Lagomorph** — A placental mammal belonging to the rabbit, hare, and pika lineage. `Lagomorph`
                                        - <a id="Primate"></a>**Primate** — A placental mammal belonging to the primate lineage. `Primate`
                                            - <a id="Ape"></a>**Ape** — A primate belonging to the hominoid lineage, including humans. `Ape`
                                                - <a id="Hominid"></a>**Great ape** — An ape belonging to the family Hominidae, including humans. `Hominid`
                                                - <a id="Human"></a>**Human** — A great ape belonging to the species Homo sapiens. `Human`
                                            - <a id="Simian"></a>**Simian** — A primate belonging to the monkey-and-ape lineage, Simiiformes. `Simian`
                                    - <a id="Sauropsid"></a>**Sauropsid** — An amniote belonging to the reptile-line lineage, including birds. `Sauropsid`
                                        - <a id="Turtle"></a>**Turtle** — A sauropsid belonging to the turtle lineage. `Turtle`
                                        - <a id="Lepidosaur"></a>**Lepidosaur** — A sauropsid belonging to the lizard, snake, and tuatara lineage. `Lepidosaur`
                                        - <a id="Archosaur"></a>**Archosaur** — A sauropsid belonging to the crocodilian and dinosaur lineage. `Archosaur`
                                            - <a id="Crocodilian"></a>**Crocodilian** — An archosaur belonging to the crocodile, alligator, and gharial lineage. `Crocodilian`
                                            - <a id="Dinosaur"></a>**Dinosaur** — An archosaur belonging to Dinosauria, including birds. `Dinosaur`
                                                - <a id="Bird"></a>**Bird** — A dinosaur belonging to the avian lineage. `Bird`
                    - <a id="BiologicalStructure"></a>**Biological structure** — A biotic object individuated by its structural organization within or from an organism. `BiologicalStructure`
                        - <a id="Cell"></a>**Cell** — A biological structure bounded by a membrane and organized as a cellular unit. `Cell`
                        - <a id="AnatomicalStructure"></a>**Anatomical structure** — A biological structure constituting an anatomical unit of an organism. `AnatomicalStructure`
                            - <a id="BodyPart"></a>**Body part** — An anatomical structure identified as a constituent part of an organism's body. `BodyPart`
                                - <a id="BodyCovering"></a>**Body covering** — A body part forming an outer protective layer. `BodyCovering`
                                - <a id="BodyJunction"></a>**Body junction** — A body part forming the connection between bodily structures. `BodyJunction`
                                - <a id="BodyVessel"></a>**Body vessel** — A body part forming a conduit for bodily fluids. `BodyVessel`
                                - <a id="Organ"></a>**Organ** — A body part integrating tissues into a functional anatomical unit. `Organ`
                                    - <a id="Gland"></a>**Gland** — An organ specialized for producing and releasing secretions. `Gland`
                            - <a id="ReproductiveBody"></a>**Reproductive body** — An anatomical structure organized for producing or developing offspring. `ReproductiveBody`
                            - <a id="Fruit"></a>**Botanical fruit** — An anatomical structure developing from a flower's ovary, sometimes with associated tissues. `Fruit`
                    - <a id="AcellularInfectiousEntity"></a>**Acellular infectious entity** — A biotic object propagated through hosts without cellular organization of its own. `AcellularInfectiousEntity`
                        - <a id="Virus"></a>**Virus** — An acellular infectious entity whose genome replicates through host-cell machinery. `Virus`
                        - <a id="Viroid"></a>**Viroid** — An acellular infectious entity consisting of a replicating noncoding RNA without a capsid. `Viroid`
                        - <a id="Prion"></a>**Prion** — An acellular infectious entity propagated by inducing a protein conformation in host proteins. `Prion`
                - <a id="MaterialBody"></a>**Material body** — An item individuated as a bounded body of matter. `MaterialBody`
                    - <a id="ParticleBody"></a>**Particle body** — A material body treated as an individual constituent at microscopic scales. `ParticleBody`
                        - <a id="Atom"></a>**Atom** — A particle body consisting of a nucleus and its bound electrons. `Atom`
                        - <a id="AtomicNucleus"></a>**Atomic nucleus** — A particle body consisting of one or more nucleons that form an atomic core. `AtomicNucleus`
                        - <a id="SubatomicParticle"></a>**Subatomic particle** — A particle body belonging to a constituent kind below the atomic level. `SubatomicParticle`
                            - <a id="Electron"></a>**Electron** — A negatively charged lepton of the electron species. `Electron`
                            - <a id="Proton"></a>**Proton** — A positively charged nucleon of the proton species. `Proton`
                            - <a id="Neutron"></a>**Neutron** — An electrically neutral nucleon of the neutron species. `Neutron`
                        - <a id="Molecule"></a>**Molecule** — A particle body of two or more chemically bonded atoms forming one molecular unit. `Molecule`
                    - <a id="AstronomicalBody"></a>**Celestial body** — A material body individuated on astronomical scales. `AstronomicalBody`
                        - <a id="Star"></a>**Star** — A celestial body sustained during its active lifetime by nuclear fusion. `Star`
                        - <a id="Planet"></a>**Planet** — A roughly rounded celestial body orbiting a star that dominates its orbital neighborhood. `Planet`
                        - <a id="Satellite"></a>**Natural satellite** — A celestial body naturally orbiting another celestial body other than a star. `Satellite`
                        - <a id="SmallCelestialBody"></a>**Small celestial body** — A celestial body smaller than a planet and neither a star nor a natural satellite. `SmallCelestialBody`
                            - <a id="Asteroid"></a>**Asteroid** — A small celestial body primarily composed of rock or metal. `Asteroid`
                            - <a id="Comet"></a>**Comet** — A small celestial body whose volatile material can produce a coma near a star. `Comet`
                    - <a id="GeologicalBody"></a>**Geological body** — A material body individuated by geological structure or formation. `GeologicalBody`
                        - <a id="Rock"></a>**Rock** — A consolidated geological body composed of minerals or mineraloids. `Rock`
                        - <a id="Mountain"></a>**Mountain** — A geological body forming a prominent elevation of the land surface. `Mountain`
                - <a id="Artifact"></a>**Artifact** — An item whose identity involves intentional production or modification for a purpose. `Artifact`
                    - <a id="Device"></a>**Device** — An artifact organized to perform an operation through its construction. `Device`
                        - <a id="Machine"></a>**Machine** — A device using an organized mechanism to transform energy or execute operations. `Machine`
                            - <a id="Computer"></a>**Computer** — A machine that executes encoded operations on data. `Computer`
                            - <a id="Appliance"></a>**Appliance** — A machine designed for a routine household or personal task. `Appliance`
                        - <a id="TransportationDevice"></a>**Vehicle** — A device designed to carry people or goods between places. `TransportationDevice`
                            - <a id="LandVehicle"></a>**Land vehicle** — A vehicle designed for travel over land. `LandVehicle`
                            - <a id="Watercraft"></a>**Watercraft** — A vehicle designed for travel on or through water. `Watercraft`
                            - <a id="Aircraft"></a>**Aircraft** — A vehicle designed for controlled travel through the atmosphere. `Aircraft`
                            - <a id="Spacecraft"></a>**Spacecraft** — A vehicle designed for travel beyond the atmosphere. `Spacecraft`
                        - <a id="MusicalInstrument"></a>**Musical instrument** — A device designed to produce controlled sounds for music. `MusicalInstrument`
                        - <a id="Weapon"></a>**Weapon** — A device designed to inflict injury or destructive force. `Weapon`
                        - <a id="Tool"></a>**Tool** — A device designed for direct manipulation in performing a task. `Tool`
                    - <a id="EngineeringComponent"></a>**Engineered component** — An artifact designed as a constituent of an engineered assembly. `EngineeringComponent`
                        - <a id="EngineeringConnection"></a>**Engineered connector** — An engineered component designed to join other components. `EngineeringConnection`
                    - <a id="Clothing"></a>**Clothing** — An artifact designed to be worn as a bodily covering. `Clothing`
                    - <a id="Furniture"></a>**Furniture** — An artifact designed to support activities in an occupied space. `Furniture`
                    - <a id="Container"></a>**Manufactured container** — An artifact designed to enclose or hold contents. `Container`
                    - <a id="StationaryArtifact"></a>**Built structure** — An artifact designed as a structure fixed to a site. `StationaryArtifact`
                        - <a id="Building"></a>**Building** — A built structure enclosing space for occupancy or sheltered use. `Building`
                    - <a id="ArtWork"></a>**Physical artwork** — An artifact whose constitutive purpose is aesthetic or artistic presentation. `ArtWork`
                    - <a id="InformationCarrier"></a>**Manufactured information carrier** — An artifact designed to embody or store interpretable content. `InformationCarrier`
                        - <a id="PrintedBook"></a>**Printed book** — An information carrier consisting of bound pages containing a book's content. `PrintedBook`
                    - <a id="TextileArtifact"></a>**Textile article** — An artifact constituted as a made article of textile material. `TextileArtifact`
            - <a id="MaterialPortion"></a>**Material portion** — An object individuated as an amount of material rather than as a structured whole. `MaterialPortion`
                - <a id="Substance"></a>**Substance portion** — A material portion individuated by chemical composition. `Substance`
                    - <a id="PureSubstance"></a>**Pure substance portion** — A substance portion having one chemical substance as its specified composition. `PureSubstance`
                        - <a id="ElementalSubstance"></a>**Elemental substance portion** — A pure substance portion composed of one chemical element. `ElementalSubstance`
                            - <a id="Metal"></a>**Elemental metal portion** — An elemental substance portion of an element exhibiting metallic properties. `Metal`
                        - <a id="CompoundSubstance"></a>**Compound substance portion** — A pure substance portion of chemically bonded elements in fixed composition. `CompoundSubstance`
                            - <a id="Water"></a>**Water portion** — A compound substance portion whose chemical substance is H2O. `Water`
                            - <a id="Carbohydrate"></a>**Carbohydrate portion** — A compound substance portion of a sugar, saccharide polymer, or their chemical derivatives. `Carbohydrate`
                            - <a id="Protein"></a>**Protein portion** — A compound substance portion of one polypeptide-based macromolecular substance. `Protein`
                    - <a id="Mixture"></a>**Mixture portion** — A substance portion containing multiple chemical substances as constituents. `Mixture`
                        - <a id="Solution"></a>**Solution portion** — A mixture portion forming one homogeneous phase with dispersed solutes. `Solution`
                    - <a id="Mineral"></a>**Mineral substance portion** — A substance portion belonging to a naturally formed mineral species with characteristic structure and composition. `Mineral`
                - <a id="BiologicalMaterial"></a>**Biological material portion** — A material portion produced by or constituting an organism. `BiologicalMaterial`
                    - <a id="BodySubstance"></a>**Body material portion** — A biological material portion originating as or constituting bodily tissue, fluid, secretion, or excretion. `BodySubstance`
                        - <a id="Blood"></a>**Blood portion** — A body material portion of the circulating fluid carrying blood cells. `Blood`
                        - <a id="Tissue"></a>**Tissue portion** — A body material portion organized as a tissue of cells and associated matrix. `Tissue`
                            - <a id="Bone"></a>**Bone tissue portion** — A tissue portion with mineralized extracellular matrix forming skeletal bone. `Bone`
                            - <a id="FatTissue"></a>**Adipose tissue portion** — A tissue portion specialized for storage in fat-containing cells. `FatTissue`
                            - <a id="Muscle"></a>**Muscle tissue portion** — A tissue portion specialized for contraction through muscle cells. `Muscle`
                - <a id="ManufacturedMaterial"></a>**Manufactured material portion** — A material portion intentionally processed to meet a specified material use. `ManufacturedMaterial`
                    - <a id="Fabric"></a>**Fabric portion** — A manufactured material portion formed as a flexible textile sheet. `Fabric`
                    - <a id="PreparedFood"></a>**Prepared food portion** — A manufactured material portion processed for consumption as food. `PreparedFood`
                - <a id="GeologicalMaterial"></a>**Geological material portion** — A material portion individuated by geological origin or occurrence. `GeologicalMaterial`
            - <a id="Collection"></a>**Collection** — An object individuated by its members rather than by an integrated constituent structure. `Collection`
                - <a id="MaterialAggregate"></a>**Material aggregate** — A collection whose members are material objects. `MaterialAggregate`
                    - <a id="AstronomicalSystem"></a>**Astronomical system** — A material aggregate whose members form an astronomical grouping. `AstronomicalSystem`
                        - <a id="Galaxy"></a>**Galaxy** — An astronomical system of stars, gas, and other matter bound on galactic scales. `Galaxy`
                    - <a id="HumanGroup"></a>**Human group** — A material aggregate of humans identified by a shared membership criterion. `HumanGroup`
                        - <a id="AgeGroup"></a>**Age cohort** — A human group whose membership is specified by an age range or birth interval. `AgeGroup`
                        - <a id="EthnicGroup"></a>**Ethnic group** — A human group whose membership involves shared ethnic identification or heritage. `EthnicGroup`
                        - <a id="FamilyGroup"></a>**Family group** — A human group whose membership is constituted by kinship or familial recognition. `FamilyGroup`
                        - <a id="Community"></a>**Community** — A human group sustained by shared association, place, or practice. `Community`
                    - <a id="OrganismAggregate"></a>**Organism aggregate** — A material aggregate whose members are organisms. `OrganismAggregate`
                - <a id="SocialGroup"></a>**Social group** — A collection whose membership is constituted by social recognition or coordinated interaction. `SocialGroup`
                    - <a id="Organization"></a>**Organization** — A social group constituted by coordinated participation under an enduring structure. `Organization`
                        - <a id="OrganizationUnit"></a>**Organizational unit** — An organization constituted as an internal division of another organization. `OrganizationUnit`
                        - <a id="EducationalOrganization"></a>**Educational organization** — An organization constituted to provide education. `EducationalOrganization`
                            - <a id="School"></a>**School** — An educational organization constituted for organized teaching of enrolled learners. `School`
                        - <a id="PoliticalOrganization"></a>**Political organization** — An organization constituted to pursue or exercise political power. `PoliticalOrganization`
                            - <a id="Government"></a>**Government** — A political organization constituted to exercise public governing authority. `Government`
                        - <a id="ReligiousOrganization"></a>**Religious organization** — An organization constituted to sustain religious practice or affiliation. `ReligiousOrganization`
                        - <a id="Corporation"></a>**Corporation** — An organization constituted as a distinct legal corporate person. `Corporation`
                        - <a id="Club"></a>**Club** — An organization constituted by voluntary membership for shared activities. `Club`
                        - <a id="Court"></a>**Court** — An organization constituted to adjudicate disputes under recognized rules. `Court`
                        - <a id="MarketInstitution"></a>**Market organization** — An organization constituted to organize or administer exchange among participants. `MarketInstitution`
            - <a id="SocialObject"></a>**Social object** — An object whose identity is constituted by situated social recognition or practice. `SocialObject`
                - <a id="Institution"></a>**Institution** — A social object consisting of an established system of rules, positions, and practices. `Institution`
                - <a id="Office"></a>**Office** — A social object consisting of a continuing institutional position with specified duties and powers. `Office`
                - <a id="Currency"></a>**Currency system** — A social object constituting a recognized system of monetary units and issuance. `Currency`
            - <a id="FieldConfiguration"></a>**Physical field configuration** — An object individuated as the organized state of a physical field over a specified domain. `FieldConfiguration`
            - <a id="InformationToken"></a>**Information token** — An object individuated as a particular embodiment of interpretable content. `InformationToken`
                - <a id="MonetaryToken"></a>**Monetary token** — An information token embodying a monetary denomination or monetary claim. `MonetaryToken`
                - <a id="LinguisticToken"></a>**Linguistic token** — An information token embodying a particular linguistic expression. `LinguisticToken`
        - <a id="Region"></a>**Region** — A realized entity individuated by an extent rather than by what occupies it. `Region`
            - <a id="SpatialRegion"></a>**Spatial region** — A region individuated by spatial extent in a specified reference framework. `SpatialRegion`
                - <a id="GeographicArea"></a>**Geographic area** — A spatial region identified relative to a planetary surface. `GeographicArea`
                    - <a id="LandArea"></a>**Land area** — A geographic area whose specified extent lies on land. `LandArea`
                        - <a id="Continent"></a>**Continental area** — A land area corresponding to a principal continental landmass. `Continent`
                        - <a id="Island"></a>**Island area** — A land area corresponding to land surrounded by water. `Island`
                    - <a id="GeopoliticalArea"></a>**Jurisdictional area** — A geographic area delimited by a political or administrative jurisdiction. `GeopoliticalArea`
                        - <a id="State"></a>**State territory** — A jurisdictional area corresponding to a sovereign state or a federated state. `State`
                    - <a id="WaterArea"></a>**Water area** — A geographic area corresponding to a body or course of water. `WaterArea`
                        - <a id="FreshWaterArea"></a>**Freshwater area** — A water area whose water is characterized by low salinity. `FreshWaterArea`
                        - <a id="SaltWaterArea"></a>**Saltwater area** — A water area whose water is characterized by substantial salinity. `SaltWaterArea`
                        - <a id="StaticWaterArea"></a>**Standing-water area** — A water area corresponding to a principally standing body of water. `StaticWaterArea`
                        - <a id="StreamWaterArea"></a>**Flowing-water area** — A water area corresponding to a principally flowing watercourse. `StreamWaterArea`
                - <a id="Room"></a>**Room space** — A spatial region delimited as an interior compartment of a built structure. `Room`
                - <a id="Hole"></a>**Hole space** — A spatial region delimited by an opening or cavity in a surrounding object. `Hole`
            - <a id="TemporalRegion"></a>**Temporal region** — A region individuated by temporal extent in a specified reference framework. `TemporalRegion`
                - <a id="TimeInterval"></a>**Time interval** — A temporal region containing the times between specified bounds. `TimeInterval`
                - <a id="TimeInstant"></a>**Time instant** — A temporal region specified as a single temporal position. `TimeInstant`
            - <a id="SpacetimeRegion"></a>**Spacetime region** — A region individuated by combined spatial and temporal extent. `SpacetimeRegion`
        - <a id="Process"></a>**Process** — A realized entity individuated as an occurrence or course of activity or change. `Process`
            - <a id="PhysicalProcess"></a>**Physical process** — A process individuated by a change in physical configuration, composition, or energy. `PhysicalProcess`
                - <a id="Motion"></a>**Motion** — A physical process involving change of spatial position relative to a reference framework. `Motion`
                    - <a id="BodyMotion"></a>**Bodily movement** — A motion of an organism's body or body parts. `BodyMotion`
                        - <a id="walk"></a>**Walking** — A bodily movement advancing by successive supported steps. `walk`
                        - <a id="swim"></a>**Swimming** — A bodily movement advancing through fluid by propulsive action. `swim`
                        - <a id="dance"></a>**Dancing** — A bodily movement organized as rhythmic or expressive performance. `dance`
                    - <a id="Transportation"></a>**Transport** — A motion organized to convey something between locations. `Transportation`
                    - <a id="Putting"></a>**Placement** — A motion ending with an object at an intended location. `Putting`
                    - <a id="Removing"></a>**Removal** — A motion taking an object away from a specified location. `Removing`
                    - <a id="Impelling"></a>**Propulsion** — A motion produced by imparting force or momentum to an object. `Impelling`
                        - <a id="shoot"></a>**Shooting** — A propulsion that launches a projectile from a discharge mechanism. `shoot`
                - <a id="Touching"></a>**Contact onset** — A physical process establishing contact between objects. `Touching`
                    - <a id="impact"></a>**Impact** — A contact onset involving rapid transfer of momentum. `impact`
                - <a id="Radiating"></a>**Emission** — A physical process releasing energy outward from a source. `Radiating`
                    - <a id="RadiatingLight"></a>**Light emission** — An emission of electromagnetic radiation in an optical range. `RadiatingLight`
                    - <a id="RadiatingSound"></a>**Sound emission** — An emission of mechanical pressure waves through a medium. `RadiatingSound`
                        - <a id="music"></a>**Musical sound production** — A sound emission organized as musical performance. `music`
                - <a id="ConfigurationChange"></a>**Configuration change** — A physical process changing arrangement, connection, or form. `ConfigurationChange`
                    - <a id="attach"></a>**Attachment** — A configuration change joining objects through an enduring connection. `attach`
                    - <a id="detach"></a>**Detachment** — A configuration change removing a connection between objects. `detach`
                    - <a id="combine"></a>**Combination** — A configuration change bringing constituents together into a whole or mixture. `combine`
                    - <a id="separate"></a>**Separation** — A configuration change dividing or isolating constituents. `separate`
                    - <a id="substitute"></a>**Replacement** — A configuration change exchanging one constituent for another. `substitute`
                    - <a id="ShapeChange"></a>**Shape change** — A configuration change altering an object's geometric form. `ShapeChange`
                        - <a id="cut"></a>**Cutting** — A shape change dividing material along a path through applied force. `cut`
                    - <a id="Poking"></a>**Poking** — A configuration change caused by a localized directed push into or against a surface. `Poking`
                    - <a id="cover"></a>**Covering** — A configuration change placing a layer or object over another. `cover`
                    - <a id="uncover"></a>**Uncovering** — A configuration change exposing something by removing a covering. `uncover`
                - <a id="SurfaceChange"></a>**Surface change** — A physical process altering a surface's condition or constitution. `SurfaceChange`
                    - <a id="Coloring"></a>**Coloring** — A surface change altering its color through treatment or applied material. `Coloring`
                - <a id="QuantityChange"></a>**Quantity change** — A physical process changing the magnitude of a specified physical quantity. `QuantityChange`
                    - <a id="Increasing"></a>**Increase** — A quantity change raising a specified magnitude. `Increasing`
                        - <a id="Heating"></a>**Heating** — An increase of temperature through energy transfer or conversion. `Heating`
                    - <a id="Decreasing"></a>**Decrease** — A quantity change lowering a specified magnitude. `Decreasing`
                        - <a id="Cooling"></a>**Cooling** — A decrease of temperature through energy transfer or conversion. `Cooling`
                - <a id="StateChange"></a>**Phase change** — A physical process changing the phase of a material. `StateChange`
                    - <a id="Boiling"></a>**Boiling** — A phase change from liquid to gas through vapor formation within the liquid. `Boiling`
                    - <a id="Condensing"></a>**Condensation** — A phase change from gas to liquid. `Condensing`
                    - <a id="Freezing"></a>**Freezing** — A phase change from liquid to solid. `Freezing`
                    - <a id="Melting"></a>**Melting** — A phase change from solid to liquid. `Melting`
                - <a id="ChemicalProcess"></a>**Chemical reaction** — A physical process changing chemical species through rearrangement of chemical bonds or electrons. `ChemicalProcess`
                    - <a id="ChemicalSynthesis"></a>**Chemical synthesis** — A chemical reaction producing a target substance from precursor substances. `ChemicalSynthesis`
                    - <a id="ChemicalDecomposition"></a>**Chemical decomposition** — A chemical reaction breaking a chemical species into simpler species. `ChemicalDecomposition`
                    - <a id="combust"></a>**Combustion** — A chemical reaction involving rapid oxidation with release of energy. `combust`
                - <a id="wett"></a>**Wetting** — A physical process establishing liquid contact over a material surface. `wett`
                - <a id="dry"></a>**Drying** — A physical process removing liquid or moisture from a material. `dry`
                - <a id="Absorbing"></a>**Energy absorption** — A physical process taking up energy from incident radiation or a propagating disturbance. `Absorbing`
                    - <a id="AbsorbingLight"></a>**Light absorption** — An energy absorption taking up energy from optical electromagnetic radiation. `AbsorbingLight`
                    - <a id="AbsorbingSound"></a>**Sound absorption** — An energy absorption taking up energy from propagating mechanical pressure waves. `AbsorbingSound`
            - <a id="Creation"></a>**Creation** — A process bringing an entity into existence within the specified context. `Creation`
                - <a id="Making"></a>**Making** — A creation accomplished through intentional production. `Making`
                    - <a id="Constructing"></a>**Construction** — A making that assembles components into a structure. `Constructing`
                    - <a id="Cooking"></a>**Cooking** — A making that prepares food through controlled physical or chemical treatment. `Cooking`
                    - <a id="Manufacture"></a>**Manufacturing** — A making organized to produce artifacts or processed materials. `Manufacture`
                    - <a id="ContentDevelopment"></a>**Content creation** — A making that produces or revises representational content. `ContentDevelopment`
                        - <a id="write"></a>**Writing** — A content creation producing linguistic content in an inscribed or encoded form. `write`
            - <a id="Damaging"></a>**Damage** — A process reducing an entity's integrity or functional capacity. `Damaging`
                - <a id="Destruction"></a>**Destruction** — A damage ending the entity's identity or operative organization. `Destruction`
                    - <a id="kill"></a>**Killing** — A destruction that causes an organism's death. `kill`
                - <a id="Injuring"></a>**Injury** — A damage to a living organism's body. `Injuring`
                    - <a id="poison"></a>**Poisoning** — An injury caused by a substance's toxic action. `poison`
            - <a id="BiologicalProcess"></a>**Biological process** — A process constituted by the activity or life history of biological entities. `BiologicalProcess`
                - <a id="PhysiologicProcess"></a>**Physiological process** — A biological process contributing to the normal functioning of an organism. `PhysiologicProcess`
                    - <a id="OrganOrTissueProcess"></a>**Organ or tissue activity** — A physiological process individuated at the level of an organ or tissue. `OrganOrTissueProcess`
                    - <a id="breath"></a>**Breathing** — A physiological process moving respiratory medium into and out of respiratory structures. `breath`
                    - <a id="Digesting"></a>**Digestion** — A physiological process breaking ingested material into absorbable constituents. `Digesting`
                - <a id="OrganismProcess"></a>**Organism-level process** — A biological process individuated by an organism's life history or integrated activity. `OrganismProcess`
                    - <a id="Birth"></a>**Birth** — An organism-level process in which offspring emerge or are delivered from a parent. `Birth`
                    - <a id="Death"></a>**Death** — An organism-level process ending the organism's life. `Death`
                    - <a id="Growth"></a>**Biological growth** — An organism-level process increasing bodily size or biological mass. `Growth`
                    - <a id="Replication"></a>**Reproduction** — An organism-level process generating new organisms of a lineage. `Replication`
                        - <a id="AsexualReplication"></a>**Asexual reproduction** — A reproduction without fusion of gametes. `AsexualReplication`
                        - <a id="SexualReplication"></a>**Sexual reproduction** — A reproduction involving fusion of gametes. `SexualReplication`
                    - <a id="BiologicalDevelopment"></a>**Biological development** — An organism-level process changing biological organization or developmental stage. `BiologicalDevelopment`
                - <a id="Ingesting"></a>**Ingestion** — A biological process taking material into an organism for consumption. `Ingesting`
                    - <a id="eat"></a>**Eating** — An ingestion of food through an oral opening. `eat`
                    - <a id="drink"></a>**Drinking** — An ingestion of liquid through an oral opening. `drink`
                - <a id="PathologicProcess"></a>**Pathological process** — A biological process constituting a disorder of biological functioning. `PathologicProcess`
            - <a id="MentalProcess"></a>**Mental process** — A process constituted by perception, cognition, emotion, or other mental activity. `MentalProcess`
                - <a id="Perception"></a>**Perception** — A mental process acquiring sensory awareness of something. `Perception`
                    - <a id="hear"></a>**Hearing** — A perception through the auditory system. `hear`
                    - <a id="see"></a>**Seeing** — A perception through the visual system. `see`
                    - <a id="smell"></a>**Smelling** — A perception through the olfactory system. `smell`
                    - <a id="taste"></a>**Tasting** — A perception through the gustatory system. `taste`
                    - <a id="TactilePerception"></a>**Touch perception** — A perception through bodily contact or mechanical stimulation of skin. `TactilePerception`
                - <a id="Remembering"></a>**Remembering** — A mental process retrieving or sustaining previously acquired experience or information. `Remembering`
                - <a id="CognitiveProcess"></a>**Cognitive process** — A mental process operating on interpretations, representations, or judgments. `CognitiveProcess`
                    - <a id="calculate"></a>**Calculation** — A cognitive process determining a result through specified operations. `calculate`
                    - <a id="classify"></a>**Classifying** — A cognitive process assigning something to a category. `classify`
                    - <a id="compare"></a>**Comparison** — A cognitive process determining similarities or differences. `compare`
                    - <a id="learn"></a>**Learning** — A cognitive process acquiring or revising knowledge or skill. `learn`
                    - <a id="plan"></a>**Planning** — A cognitive process constructing a course of intended action. `plan`
                    - <a id="predict"></a>**Prediction** — A cognitive process forming a judgment about an unobserved outcome. `predict`
                    - <a id="reason"></a>**Reasoning** — A cognitive process drawing conclusions from premises or considerations. `reason`
                    - <a id="select"></a>**Selection** — A cognitive process choosing among alternatives. `select`
                    - <a id="read"></a>**Reading** — A cognitive process interpreting inscribed or encoded linguistic content. `read`
            - <a id="IntentionalProcess"></a>**Intentional activity** — A process constituted by an agent's purposive action. `IntentionalProcess`
                - <a id="Guiding"></a>**Guidance** — An intentional activity directing another's action toward an outcome. `Guiding`
                    - <a id="Managing"></a>**Management** — A guidance coordinating resources, participants, or operations. `Managing`
                    - <a id="Steering"></a>**Steering** — A guidance controlling the direction of a moving system. `Steering`
                    - <a id="EducationalProcess"></a>**Education** — A guidance organized to support another's learning. `EducationalProcess`
                - <a id="Maintaining"></a>**Maintenance** — An intentional activity preserving a specified condition or capacity. `Maintaining`
                    - <a id="Keeping"></a>**Retention** — A maintenance preserving possession, custody, or presence. `Keeping`
                        - <a id="confine"></a>**Confinement** — A retention restricting an entity's movement beyond a boundary. `confine`
                - <a id="Repairing"></a>**Repair** — An intentional activity restoring damaged organization or capacity. `Repairing`
                - <a id="TherapeuticalProcess"></a>**Treatment** — An intentional activity intended to alleviate or correct a health condition. `TherapeuticalProcess`
                    - <a id="Surgery"></a>**Surgery** — A treatment involving operative intervention in bodily tissue. `Surgery`
                - <a id="Searching"></a>**Search** — An intentional activity attempting to find a specified entity or information. `Searching`
                    - <a id="Investigating"></a>**Investigation** — A search organized to establish an answer through evidence. `Investigating`
                        - <a id="DiagnosticProcess"></a>**Diagnosis** — An investigation intended to identify a condition or its cause. `DiagnosticProcess`
                    - <a id="pursue"></a>**Pursuit** — A search involving following or tracking a target. `pursue`
                - <a id="Maneuver"></a>**Maneuver** — An intentional activity executing a coordinated change of position for an objective. `Maneuver`
                - <a id="RecreationOrExercise"></a>**Recreation or exercise** — An intentional activity undertaken for enjoyment, practice, or bodily conditioning. `RecreationOrExercise`
                    - <a id="Gaming"></a>**Game playing** — A recreation or exercise conducted under the rules of a game. `Gaming`
                        - <a id="Sport"></a>**Sport participation** — A game playing involving organized competition in physical skill or exertion. `Sport`
            - <a id="SocialInteraction"></a>**Social interaction** — A process constituted by reciprocal or socially directed action among participants. `SocialInteraction`
                - <a id="Communication"></a>**Communication** — A social interaction conveying interpretable content to a recipient. `Communication`
                    - <a id="LinguisticCommunication"></a>**Linguistic communication** — A communication using expressions of a language. `LinguisticCommunication`
                        - <a id="Directing"></a>**Directive communication** — A linguistic communication intended to elicit an action or response. `Directing`
                            - <a id="order"></a>**Ordering** — A directive communication presented as authoritative instruction. `order`
                            - <a id="question"></a>**Questioning** — A directive communication seeking an answer. `question`
                            - <a id="request"></a>**Requesting** — A directive communication asking for action without claiming authority to compel it. `request`
                        - <a id="committ"></a>**Committing** — A linguistic communication undertaking a commitment. `committ`
                        - <a id="declare"></a>**Declaring** — A linguistic communication purporting to establish a status through recognized authority. `declare`
                        - <a id="express"></a>**Expressing** — A linguistic communication conveying an attitude, feeling, or intention. `express`
                        - <a id="state"></a>**Asserting** — A linguistic communication presenting a proposition as true. `state`
                    - <a id="Disseminating"></a>**Dissemination** — A communication distributing content to an audience. `Disseminating`
                        - <a id="advertise"></a>**Advertising** — A dissemination intended to promote interest in an offering or activity. `advertise`
                    - <a id="Publication"></a>**Publication** — A communication making content available to a public audience. `Publication`
                - <a id="Meeting"></a>**Meeting** — A social interaction involving participants assembled for a shared occasion. `Meeting`
                - <a id="Cooperation"></a>**Cooperation** — A social interaction coordinating participants toward a shared outcome. `Cooperation`
                - <a id="pretend"></a>**Pretending** — A social interaction enacting a situation understood as imagined. `pretend`
                - <a id="Contest"></a>**Contest** — A social interaction organized around incompatible participant objectives or competing outcomes. `Contest`
                    - <a id="ViolentContest"></a>**Violent contest** — A contest conducted through physical force against participants. `ViolentContest`
                        - <a id="Battle"></a>**Battle** — A violent contest constituting an episode of organized armed conflict. `Battle`
                        - <a id="War"></a>**War** — A violent contest constituting sustained organized armed conflict. `War`
                - <a id="LegalAction"></a>**Legal proceeding** — A social interaction conducted through recognized legal procedures. `LegalAction`
                - <a id="ChangeOfPossession"></a>**Possession transfer** — A social interaction changing custody, control, possession, or ownership entitlement. `ChangeOfPossession`
                    - <a id="Getting"></a>**Acquisition** — A possession transfer considered as receipt by a participant. `Getting`
                        - <a id="borrow"></a>**Borrowing** — An acquisition with an undertaking to return the received item or its equivalent. `borrow`
                        - <a id="UnilateralGetting"></a>**Unilateral taking** — An acquisition without a reciprocal provision by the acquiring participant. `UnilateralGetting`
                    - <a id="Giving"></a>**Giving** — A possession transfer considered as provision by a participant. `Giving`
                        - <a id="lend"></a>**Lending** — A giving with an expectation of return of the item or its equivalent. `lend`
                        - <a id="UnilateralGiving"></a>**Unilateral giving** — A giving without a reciprocal transfer from the recipient. `UnilateralGiving`
                    - <a id="OwnershipTransfer"></a>**Ownership transfer** — A possession transfer changing a legally or socially recognized ownership entitlement. `OwnershipTransfer`
                - <a id="Transaction"></a>**Transaction** — A social interaction implementing an agreed exchange or change of entitlement. `Transaction`
                    - <a id="FinancialTransaction"></a>**Financial transaction** — A transaction involving monetary value, payment, or financial claims. `FinancialTransaction`
                        - <a id="buy"></a>**Buying** — A financial transaction considered as acquisition in exchange for payment. `buy`
                        - <a id="sell"></a>**Selling** — A financial transaction considered as provision in exchange for payment. `sell`
                        - <a id="bet"></a>**Betting** — A financial transaction staking value on an uncertain outcome. `bet`
                - <a id="OrganizationalProcess"></a>**Organizational process** — A social interaction constituted by an organization's procedures or coordinated activity. `OrganizationalProcess`
                    - <a id="JoiningAnOrganization"></a>**Organizational admission** — An organizational process establishing someone's membership or participation. `JoiningAnOrganization`
                        - <a id="hire"></a>**Hiring** — An organizational admission establishing an employment engagement. `hire`
                        - <a id="matriculate"></a>**Matriculation** — An organizational admission establishing a student's enrollment. `matriculate`
                    - <a id="LeavingAnOrganization"></a>**Organizational departure** — An organizational process ending someone's membership or participation. `LeavingAnOrganization`
                        - <a id="graduate"></a>**Graduation** — An organizational departure marking completion of a course of study. `graduate`
                        - <a id="terminate_Employment"></a>**Employment termination** — An organizational departure ending an employment engagement. `terminate_Employment`
                    - <a id="MilitaryProcess"></a>**Military process** — An organizational process constituted by military operations or administration. `MilitaryProcess`
                    - <a id="RegulatoryProcess"></a>**Regulation** — An organizational process establishing, applying, or enforcing governing requirements. `RegulatoryProcess`
                - <a id="PoliticalProcess"></a>**Political process** — A social interaction concerning collective governing power or public decisions. `PoliticalProcess`
                - <a id="ReligiousProcess"></a>**Religious practice occurrence** — A social interaction enacting religious beliefs, observances, or rites. `ReligiousProcess`
            - <a id="encode"></a>**Encoding** — A process transforming content into a representation under a coding scheme. `encode`
            - <a id="decode"></a>**Decoding** — A process recovering content from a representation under a coding scheme. `decode`
            - <a id="ObservationProcess"></a>**Observation activity** — A process acquiring information through attention, detection, or instrumentation. `ObservationProcess`
                - <a id="MeasurementProcess"></a>**Measurement activity** — An observation activity assigning a quantity value through a specified procedure. `MeasurementProcess`
            - <a id="Event"></a>**Event** — A process individuated as a bounded occurrence in a specified context. `Event`
            - <a id="SignalOccurrence"></a>**Signal occurrence** — A process whose concrete variation conveys information under an interpretation. `SignalOccurrence`
        - <a id="StateInstance"></a>**State instance** — A realized entity consisting in an entity or system's condition over a specified context. `StateInstance`
            - <a id="MentalState"></a>**Mental state** — A state instance constituted by a subject's mental condition. `MentalState`
                - <a id="BeliefState"></a>**Belief state** — A mental state in which a subject accepts a proposition as true. `BeliefState`
                    - <a id="KnowledgeState"></a>**Knowledge state** — A belief state counted as knowledge under specified epistemic criteria. `KnowledgeState`
                - <a id="PreferenceState"></a>**Preference state** — A mental state ranking alternatives as more or less desirable. `PreferenceState`
            - <a id="RelationalState"></a>**Relational state** — A state instance constituted by a connection among two or more participants. `RelationalState`
                - <a id="Relationship"></a>**Social relationship instance** — A relational state sustained by social interaction or recognition. `Relationship`
                - <a id="Agreement"></a>**Agreement instance** — A relational state constituted by participants' shared acceptance or commitment. `Agreement`
                - <a id="ObligationInstance"></a>**Obligation instance** — A relational state binding a bearer to a required action under a normative context. `ObligationInstance`
            - <a id="Status"></a>**Status instance** — A state instance consisting in socially recognized standing in a context. `Status`
        - <a id="DependentFeature"></a>**Dependent feature** — A realized entity individuated through the particular bearer whose feature it is. `DependentFeature`
            - <a id="Quality"></a>**Quality instance** — A dependent feature specifying a bearer's actual condition on a descriptive dimension. `Quality`
                - <a id="QuantitativeQuality"></a>**Quantitative quality instance** — A quality instance admitting magnitude on a specified scale. `QuantitativeQuality`
            - <a id="Disposition"></a>**Disposition instance** — A dependent feature consisting in a bearer's tendency to respond under specified conditions. `Disposition`
                - <a id="Capability"></a>**Capability instance** — A disposition instance enabling a bearer to perform a specified activity. `Capability`
            - <a id="RoleInstance"></a>**Role instance** — A dependent feature constituted by a bearer's assigned or contextual function. `RoleInstance`
            - <a id="PurposeInstance"></a>**Purpose instance** — A dependent feature constituted by an intended outcome assigned to a bearer. `PurposeInstance`
        - <a id="SocialEntity"></a>**Socially constituted entity** — A realized entity whose identity depends on social recognition, interaction, or practice. `SocialEntity`
            - <a id="InstitutionalEntity"></a>**Institutionally constituted entity** — A socially constituted entity whose identity depends on institutional rules or authority. `InstitutionalEntity`
    - <a id="AbstractEntity"></a>**Abstract entity** — An entity individuated without reference to a particular concrete realization. `AbstractEntity`
        - <a id="AbstractStructure"></a>**Abstract structure** — An abstract entity individuated by constituent elements and their organization. `AbstractStructure`
            - <a id="ComputationalEntity"></a>**Computational structure** — An abstract structure specified by computational operations, states, or resources. `ComputationalEntity`
                - <a id="Algorithm"></a>**Algorithm** — A computational structure specifying an effective procedure for a class of tasks. `Algorithm`
                - <a id="Automaton"></a>**Abstract automaton** — A computational structure specified by states and rules of transition. `Automaton`
                - <a id="ComplexityClass"></a>**Complexity class** — A computational structure grouping problems by specified resource bounds and a computational model. `ComplexityClass`
                - <a id="Software"></a>**Software content** — A computational structure encoded as instructions or associated data for execution or interpretation. `Software`
            - <a id="Language"></a>**Language system** — An abstract structure of signs and conventions for constructing interpretable expressions. `Language`
                - <a id="HumanLanguage"></a>**Human language** — A language system used or designed for human linguistic communication. `HumanLanguage`
                    - <a id="NaturalLanguage"></a>**Natural language** — A human language developed through communal use rather than deliberate full design. `NaturalLanguage`
                    - <a id="ConstructedLanguage"></a>**Constructed human language** — A human language deliberately designed as a linguistic system. `ConstructedLanguage`
                - <a id="ArtificialLanguage"></a>**Artificial language** — A language system deliberately specified rather than arising through natural communal use. `ArtificialLanguage`
                    - <a id="ComputerLanguage"></a>**Computer language** — An artificial language specified for representing instructions or data for computer processing. `ComputerLanguage`
                - <a id="AnimalLanguage"></a>**Animal communication system** — A language system constituted by nonhuman animals' structured signaling conventions. `AnimalLanguage`
            - <a id="FormalLanguage"></a>**Formal language** — An abstract structure consisting of strings admitted by a specified formal syntax. `FormalLanguage`
            - <a id="Notation"></a>**Notation system** — An abstract structure of symbols and conventions for representing a domain. `Notation`
        - <a id="MathematicalEntity"></a>**Mathematical entity** — An abstract entity individuated by mathematical specification. `MathematicalEntity`
            - <a id="Number"></a>**Number** — A mathematical object specifying numerical magnitude, order, or a numerical extension thereof. `Number`
                - <a id="NaturalNumber"></a>**Natural number** — A number in the nonnegative integer sequence beginning with zero. `NaturalNumber`
                - <a id="Integer"></a>**Integer** — A number in the whole-number sequence and its negatives. `Integer`
                - <a id="RationalNumber"></a>**Rational number** — A number expressible as a ratio of integers with nonzero denominator. `RationalNumber`
                - <a id="RealNumber"></a>**Real number** — A number in the complete ordered field extending the rational numbers. `RealNumber`
                - <a id="ComplexNumber"></a>**Complex number** — A number expressible as a real part plus an imaginary part times a square root of minus one. `ComplexNumber`
            - <a id="Set"></a>**Set** — A mathematical object individuated extensionally by its members under a specified set theory. `Set`
            - <a id="Sequence"></a>**Sequence** — A mathematical object assigning an element to each position in an ordered index domain. `Sequence`
            - <a id="Function"></a>**Function** — A mathematical object assigning exactly one output to each input in its domain. `Function`
                - <a id="ComputableFunction"></a>**Computable function** — A function whose outputs can be obtained by an effective computational procedure. `ComputableFunction`
                    - <a id="RecursiveFunction"></a>**Recursive function** — A computable function definable by the specified recursion formalism. `RecursiveFunction`
            - <a id="AlgebraicEntity"></a>**Algebraic structure** — A mathematical structure specified by operations and their governing laws. `AlgebraicEntity`
                - <a id="AlgebraicGroup"></a>**Algebraic group** — An algebraic structure with one associative operation, an identity, and inverses. `AlgebraicGroup`
            - <a id="GeometricEntity"></a>**Geometric object** — A mathematical object specified through spatial form or geometric incidence. `GeometricEntity`
                - <a id="Curve"></a>**Curve** — A geometric object parameterized along one dimension, subject to a specified regularity. `Curve`
                    - <a id="Circle"></a>**Circle** — A planar curve whose points are at one fixed distance from a center. `Circle`
                    - <a id="Ellipse"></a>**Ellipse** — A planar curve whose distances to two foci have a constant sum. `Ellipse`
                    - <a id="Parabola"></a>**Parabola** — A planar curve whose points are equidistant from a focus and a directrix. `Parabola`
                    - <a id="Hyperbola"></a>**Hyperbola** — A planar curve whose distances to two foci have a constant absolute difference. `Hyperbola`
            - <a id="TopologicalEntity"></a>**Topological structure** — A mathematical structure specified by neighborhoods, open sets, or continuity relations. `TopologicalEntity`
            - <a id="AnalyticEntity"></a>**Analytic structure** — A mathematical structure specified through limiting or differential relations. `AnalyticEntity`
            - <a id="ProbabilityEntity"></a>**Probability structure** — A mathematical structure specifying probabilistic outcomes and their measures. `ProbabilityEntity`
            - <a id="Graph"></a>**Graph** — A mathematical structure of vertices and edges connecting specified vertex occurrences. `Graph`
        - <a id="InformationContent"></a>**Information content** — An abstract entity individuated by what can be conveyed, recorded, interpreted, or asserted. `InformationContent`
            - <a id="Data"></a>**Data content** — An information content represented as values or observations for interpretation or processing. `Data`
                - <a id="Record"></a>**Record content** — A data content preserving information about an entity, occurrence, or assertion. `Record`
                    - <a id="Observation"></a>**Observation result** — A record content reporting what was detected or perceived. `Observation`
                        - <a id="Measurement"></a>**Measurement result** — An observation result assigning a measured value with its measurement context. `Measurement`
                - <a id="Dataset"></a>**Dataset content** — A data content comprising records or values organized as one body for use. `Dataset`
            - <a id="Proposition"></a>**Proposition** — An information content capable of truth or falsity in an interpretation. `Proposition`
                - <a id="Fact"></a>**True proposition** — A proposition true in the specified interpretation. `Fact`
                - <a id="Theorem"></a>**Theorem** — A proposition established by proof in a specified formal system. `Theorem`
                - <a id="Belief"></a>**Belief content** — A proposition accepted as true by a subject in a specified context. `Belief`
                - <a id="Knowledge"></a>**Knowledge content** — A proposition known by a subject under specified epistemic criteria. `Knowledge`
                - <a id="Goal"></a>**Goal content** — A proposition specifying a state of affairs an agent aims to realize. `Goal`
            - <a id="RepresentationalEntity"></a>**Representational content** — An information content organized to represent, encode, or express something. `RepresentationalEntity`
                - <a id="Description"></a>**Description** — A representational content characterizing an entity or situation. `Description`
                    - <a id="Definition"></a>**Definition** — A description stipulating or delimiting the meaning or application of an expression or category. `Definition`
                    - <a id="Summary"></a>**Summary** — A description condensing the principal content of a larger representation. `Summary`
                    - <a id="FictionalDescription"></a>**Fictional entity description** — A description specifying an entity within an imagined narrative or world. `FictionalDescription`
                - <a id="Model"></a>**Model content** — A representational content representing selected features or relationships of a target. `Model`
                    - <a id="MathematicalModel"></a>**Mathematical model** — A model content expressed through mathematical structures and constraints. `MathematicalModel`
                        - <a id="PhysicalSystemModel"></a>**Physical-system model** — A mathematical model representing a physical system. `PhysicalSystemModel`
                - <a id="Classification"></a>**Classification scheme** — A representational content specifying categories and criteria for assigning entities to them. `Classification`
                - <a id="Schema"></a>**Schema** — A representational content specifying permitted structures and constraints for representations. `Schema`
                    - <a id="OntologyRepresentation"></a>**Ontology specification** — A schema specifying entity categories, relations, and their intended semantics. `OntologyRepresentation`
                - <a id="Proof"></a>**Proof** — A representational content establishing a conclusion through valid steps in a specified system. `Proof`
                - <a id="FormalExpression"></a>**Formal expression** — A representational content constructed according to a formal syntax. `FormalExpression`
                    - <a id="LogicalEntity"></a>**Logical expression** — A formal expression interpreted in a specified logical system. `LogicalEntity`
                    - <a id="SymbolicString"></a>**Symbol string** — A formal expression consisting of an ordered sequence of symbols. `SymbolicString`
                        - <a id="Character"></a>**Character string** — A symbol string of one character in a specified encoding or alphabet. `Character`
                - <a id="LinguisticExpression"></a>**Linguistic expression** — A representational content constructed from meaningful units of a language. `LinguisticExpression`
                    - <a id="Morpheme"></a>**Morpheme** — A linguistic expression that is a minimal meaning-bearing grammatical unit. `Morpheme`
                    - <a id="Word"></a>**Word** — A linguistic expression treated as a lexical unit by a language's conventions. `Word`
                        - <a id="Noun"></a>**Noun** — A word in a grammatical category conventionally serving as a nominal head. `Noun`
                        - <a id="Verb"></a>**Verb** — A word in a grammatical category conventionally serving as a predicate head. `Verb`
                        - <a id="Adjective"></a>**Adjective** — A word in a grammatical category conventionally modifying a nominal expression. `Adjective`
                        - <a id="Adverb"></a>**Adverb** — A word in a grammatical category conventionally modifying a predicate or other modifier. `Adverb`
                        - <a id="Particle"></a>**Grammatical particle** — A word whose grammatical function is not assigned to the principal lexical categories. `Particle`
                    - <a id="Phrase"></a>**Phrase** — A linguistic expression organized around a grammatical head without requiring a full clause. `Phrase`
                        - <a id="NounPhrase"></a>**Noun phrase** — A phrase whose grammatical head or distribution is nominal. `NounPhrase`
                        - <a id="VerbPhrase"></a>**Verb phrase** — A phrase whose grammatical head is verbal. `VerbPhrase`
                        - <a id="PrepositionalPhrase"></a>**Prepositional phrase** — A phrase headed by a preposition or corresponding adposition. `PrepositionalPhrase`
                    - <a id="Sentence"></a>**Sentence** — A linguistic expression conventionally functioning as a complete sentential unit. `Sentence`
                - <a id="Text"></a>**Text content** — A representational content organized as an extended linguistic composition. `Text`
                    - <a id="Article"></a>**Article content** — A text content composed as a relatively self-contained contribution to a publication. `Article`
                    - <a id="Certificate"></a>**Certificate content** — A text content attesting a fact or status under an issuer's authority. `Certificate`
                - <a id="Message"></a>**Message content** — A representational content composed for conveyance to a recipient. `Message`
                - <a id="Document"></a>**Document content** — A representational content organized as an identifiable documentary unit. `Document`
                    - <a id="Book"></a>**Book content** — A document content composed as a substantial self-contained work for book publication. `Book`
                - <a id="Image"></a>**Image content** — A representational content encoding a spatial visual presentation. `Image`
                    - <a id="Icon"></a>**Icon content** — An image content representing a referent through resemblance or convention. `Icon`
                - <a id="Audio"></a>**Audio content** — A representational content encoding a sound presentation. `Audio`
                - <a id="Video"></a>**Video content** — A representational content encoding a temporal sequence of visual presentations. `Video`
                    - <a id="MotionPicture"></a>**Motion-picture content** — A video content composed as a cinematic work. `MotionPicture`
                - <a id="Series"></a>**Publication series** — A representational content grouping publications under a continuing identity or plan. `Series`
                    - <a id="Periodical"></a>**Periodical series** — A publication series intended to issue successive parts at recurring intervals. `Periodical`
                - <a id="Address"></a>**Address content** — A representational content identifying a destination within an addressing system. `Address`
                - <a id="SignalContent"></a>**Signal content** — A representational content conveyed through a signal occurrence. `SignalContent`
            - <a id="NormativeContent"></a>**Normative content** — An information content specifying permissions, requirements, or standards of conduct. `NormativeContent`
                - <a id="Norm"></a>**Norm specification** — A normative content prescribing or evaluating conduct in a context. `Norm`
                    - <a id="Law"></a>**Legal rule** — A norm specification recognized as governing under a legal system. `Law`
                    - <a id="Policy"></a>**Policy specification** — A norm specification adopted to guide decisions or conduct within a domain. `Policy`
                    - <a id="Convention"></a>**Convention specification** — A norm specification sustained by shared acceptance or customary coordination. `Convention`
                - <a id="Obligation"></a>**Obligation specification** — A normative content specifying an action required of a bearer in a context. `Obligation`
                - <a id="Contract"></a>**Contract content** — A normative content specifying mutually accepted terms that establish obligations or rights. `Contract`
                - <a id="License"></a>**License content** — A normative content granting permission under specified terms and authority. `License`
                - <a id="Patent"></a>**Patent grant content** — A normative content specifying an exclusive legal right concerning an invention. `Patent`
                - <a id="InferenceRule"></a>**Inference rule specification** — A normative content specifying permitted inferential transitions in a formal system. `InferenceRule`
            - <a id="Practice"></a>**Practice pattern** — An information content specifying a recurrent socially recognized way of acting. `Practice`
                - <a id="Game"></a>**Game rule system** — A practice pattern specifying permitted moves, objectives, and conditions of play. `Game`
                    - <a id="SportRules"></a>**Sport rule system** — A game rule system specifying competition in physical skill or exertion. `SportRules`
            - <a id="TheorySpecification"></a>**Theory specification** — An information content specifying a body of claims and their inferential commitments. `TheorySpecification`
        - <a id="QuantityValue"></a>**Quantity value** — An abstract entity specifying magnitude through a number and a scale or unit. `QuantityValue`
        - <a id="QualityValue"></a>**Quality value** — An abstract entity specifying a position or category in a descriptive value domain. `QualityValue`
        - <a id="PredicateSpecification"></a>**Predicate specification** — An abstract entity specifying a condition on one or more arguments in an interpretation. `PredicateSpecification`
            - <a id="Property"></a>**Property specification** — A predicate specification applying a condition to one argument. `Property`
                - <a id="DescriptiveProperty"></a>**Descriptive property specification** — A property specification characterizing an entity without assigning a role or prescribing conduct. `DescriptiveProperty`
                    - <a id="QualityProperty"></a>**Quality property specification** — A descriptive property specification assigning a category or value on a qualitative dimension. `QualityProperty`
                    - <a id="Quantity"></a>**Quantity property specification** — A descriptive property specification assigning a magnitude on a specified scale. `Quantity`
                    - <a id="ModalProperty"></a>**Modal property specification** — A descriptive property specification concerning necessity, possibility, or contingency under a modality. `ModalProperty`
                    - <a id="LogicalProperty"></a>**Logical property specification** — A descriptive property specification determined by logical form or consequence. `LogicalProperty`
                    - <a id="MathematicalProperty"></a>**Mathematical property specification** — A descriptive property specification determined by a mathematical condition. `MathematicalProperty`
                    - <a id="DispositionProperty"></a>**Disposition property specification** — A descriptive property specification characterizing conditional tendencies of a bearer. `DispositionProperty`
                        - <a id="CapabilityProperty"></a>**Capability property specification** — A disposition property specification characterizing the ability to perform an activity. `CapabilityProperty`
                    - <a id="SentientRole"></a>**Sentience specification** — A descriptive property specification characterizing an entity as a subject of experience. `SentientRole`
                    - <a id="CognitiveRole"></a>**Cognition specification** — A descriptive property specification characterizing an entity as a bearer of cognitive activity. `CognitiveRole`
                - <a id="Role"></a>**Role specification** — A property specification characterizing an entity by its contextual function or standing. `Role`
                    - <a id="AgentRole"></a>**Agent role specification** — A role specification characterizing participation as an intentional actor. `AgentRole`
                    - <a id="Person"></a>**Personhood specification** — A role specification characterizing recognized personal standing under a stated biological, social, or legal criterion. `Person`
                    - <a id="LocationRole"></a>**Location role specification** — A role specification characterizing an entity as where another is situated. `LocationRole`
                    - <a id="InstrumentRole"></a>**Instrument role specification** — A role specification characterizing an entity as a means in an activity. `InstrumentRole`
                    - <a id="ContentBearerRole"></a>**Content bearer specification** — A role specification characterizing an entity as embodying interpretable content. `ContentBearerRole`
                    - <a id="ProductRole"></a>**Product specification** — A role specification characterizing an entity as an output of production in a context. `ProductRole`
                    - <a id="Food"></a>**Food specification** — A role specification characterizing material as intended or suitable for consumption by an organism. `Food`
                        - <a id="Beverage"></a>**Beverage specification** — A food specification characterizing a liquid intended for drinking. `Beverage`
                        - <a id="Vegetable"></a>**Vegetable food specification** — A food specification characterizing edible plant material conventionally treated as vegetable food. `Vegetable`
                        - <a id="FruitFood"></a>**Fruit food specification** — A food specification characterizing botanical fruits as food. `FruitFood`
                        - <a id="AnimalDerivedFood"></a>**Animal-derived food specification** — A food specification characterizing material derived from animals, including tissues, eggs, or secretions. `AnimalDerivedFood`
                            - <a id="Meat"></a>**Meat specification** — A food specification characterizing animal tissue as food. `Meat`
                    - <a id="BiologicallyActiveSubstance"></a>**Bioactive material specification** — A role specification characterizing material by its effect on biological activity. `BiologicallyActiveSubstance`
                        - <a id="Hormone"></a>**Hormone specification** — A bioactive material specification characterizing a signaling substance regulating target cells through a biological signaling system. `Hormone`
                        - <a id="Nutrient"></a>**Nutrient specification** — A bioactive material specification characterizing a substance required or utilized for growth, maintenance, or metabolism. `Nutrient`
                            - <a id="Vitamin"></a>**Vitamin specification** — A nutrient specification characterizing an organic micronutrient required in small amounts by a specified organism. `Vitamin`
                        - <a id="Enzyme"></a>**Enzyme specification** — A bioactive material specification characterizing a biological catalyst. `Enzyme`
                    - <a id="Symbol"></a>**Symbol specification** — A role specification characterizing a sign as representing something under an interpretation. `Symbol`
                        - <a id="Name"></a>**Name specification** — A symbol specification characterizing a sign as designating an entity. `Name`
                        - <a id="Label"></a>**Label specification** — A symbol specification characterizing a sign as identifying or annotating something in a representation. `Label`
                - <a id="Purpose"></a>**Purpose specification** — A property specification assigning an intended outcome or use to an entity. `Purpose`
                - <a id="Preference"></a>**Preference specification** — A property specification characterizing an ordering of alternatives for a subject in a context. `Preference`
            - <a id="Relation"></a>**Relation specification** — A predicate specification applying a condition to two or more arguments. `Relation`
                - <a id="ClassificationRelation"></a>**Classification relation specification** — A relation specification connecting an entity to a class it instantiates or a class to its superclass. `ClassificationRelation`
                - <a id="PartWholeRelation"></a>**Part-whole relation specification** — A relation specification connecting a constituent to the whole it constitutes. `PartWholeRelation`
                - <a id="SpatialRelation"></a>**Spatial relation specification** — A relation specification connecting entities through spatial position, extent, or orientation. `SpatialRelation`
                - <a id="TemporalRelation"></a>**Temporal relation specification** — A relation specification connecting entities through temporal position, duration, or sequence. `TemporalRelation`
                - <a id="CausalRelation"></a>**Causal relation specification** — A relation specification connecting a contributing cause to an effect in a context. `CausalRelation`
                - <a id="ExplanatoryRelation"></a>**Explanatory relation specification** — A relation specification connecting an explanans to what it accounts for. `ExplanatoryRelation`
                - <a id="ParticipationRelation"></a>**Participation relation specification** — A relation specification connecting a participant to an occurrence and its participation context. `ParticipationRelation`
                - <a id="SocialRelation"></a>**Social relation specification** — A relation specification connecting participants through social interaction or recognition. `SocialRelation`
                    - <a id="InstitutionalRelation"></a>**Institutional relation specification** — A social relation specification established by institutional rules or authority. `InstitutionalRelation`
                - <a id="PerceptualRelation"></a>**Perceptual relation specification** — A relation specification connecting a perceiver to an object of perception. `PerceptualRelation`
                - <a id="EpistemicRelation"></a>**Epistemic relation specification** — A relation specification connecting a subject, content, or evidence through epistemic standing. `EpistemicRelation`
                - <a id="LogicalRelation"></a>**Logical relation specification** — A relation specification determined by logical consequence or logical form. `LogicalRelation`
                    - <a id="IdentityRelation"></a>**Identity relation specification** — A logical relation specification satisfied exactly when its two arguments are the same entity. `IdentityRelation`
                - <a id="MathematicalRelation"></a>**Mathematical relation specification** — A relation specification connecting mathematical objects under a mathematical condition. `MathematicalRelation`
                    - <a id="SetTheoreticRelation"></a>**Set-theoretic relation specification** — A mathematical relation specification connecting sets or their elements through membership or set structure. `SetTheoreticRelation`
                    - <a id="EquivalenceRelation"></a>**Equivalence relation specification** — A mathematical relation specification reflexive, symmetric, and transitive on its stated domain. `EquivalenceRelation`
                - <a id="TransformationRelation"></a>**Transformation relation specification** — A relation specification connecting an input or prior entity to a result of transformation. `TransformationRelation`
                - <a id="RepresentationalRelation"></a>**Representational relation specification** — A relation specification connecting a representation to its content, referent, or encoding convention. `RepresentationalRelation`
                - <a id="ProvenanceRelation"></a>**Provenance relation specification** — A relation specification connecting an entity to a source, derivation, or production context. `ProvenanceRelation`
            - <a id="EntityKind"></a>**Entity kind specification** — A predicate specification delimiting a class of entities through identity-relevant criteria. `EntityKind`
                - <a id="TaxonSpecification"></a>**Taxon specification** — An entity kind specification identifying membership in a biological taxon. `TaxonSpecification`
        - <a id="MeasurementUnit"></a>**Measurement unit** — An abstract entity specifying a reference magnitude for expressing quantity values. `MeasurementUnit`

## Additional valid superclass edges

These are semantic subclass links, not use, location, part-whole, or provenance relations.

| Class | Additional superclass |
|---|---|
| [Atomic nucleus](#AtomicNucleus) | [Subatomic particle](#SubatomicParticle) |
| [Animal](#Animal) | [Eukaryote](#Eukaryote) |
| [Vertebrate](#Vertebrate) | [Chordate](#Chordate) |
| [Amniote](#Amniote) | [Tetrapod](#Tetrapod) |
| [Mammal](#Mammal) | [Synapsid](#Synapsid) |
| [Primate](#Primate) | [Eutherian mammal](#PlacentalMammal) |
| [Ape](#Ape) | [Simian](#Simian) |
| [Human](#Human) | [Great ape](#Hominid) |
| [Organization](#Organization) | [Social object](#SocialObject) |
| [Government](#Government) | [Institutionally constituted entity](#InstitutionalEntity) |
| [Corporation](#Corporation) | [Institutionally constituted entity](#InstitutionalEntity) |
| [Court](#Court) | [Institutionally constituted entity](#InstitutionalEntity) |
| [Institution](#Institution) | [Institutionally constituted entity](#InstitutionalEntity) |
| [Office](#Office) | [Institutionally constituted entity](#InstitutionalEntity) |
| [Currency system](#Currency) | [Institutionally constituted entity](#InstitutionalEntity) |
| [Bodily movement](#BodyMotion) | [Biological process](#BiologicalProcess) |
| [Writing](#write) | [Intentional activity](#IntentionalProcess) |
| [Death](#Death) | [Event](#Event) |
| [Injury](#Injuring) | [Biological process](#BiologicalProcess) |
| [Killing](#kill) | [Biological process](#BiologicalProcess) |
| [Social relationship instance](#Relationship) | [Socially constituted entity](#SocialEntity) |
| [Agreement instance](#Agreement) | [Socially constituted entity](#SocialEntity) |
| [Status instance](#Status) | [Socially constituted entity](#SocialEntity) |
| [Natural number](#NaturalNumber) | [Integer](#Integer) |
| [Integer](#Integer) | [Rational number](#RationalNumber) |
| [Rational number](#RationalNumber) | [Real number](#RealNumber) |
| [Real number](#RealNumber) | [Complex number](#ComplexNumber) |
| [Circle](#Circle) | [Ellipse](#Ellipse) |
| [Quantity value](#QuantityValue) | [Quality value](#QualityValue) |
| [Constructed human language](#ConstructedLanguage) | [Artificial language](#ArtificialLanguage) |
| [Formal language](#FormalLanguage) | [Set](#Set) |
| [Entity kind specification](#EntityKind) | [Property specification](#Property) |

## Cross-cutting class expressions

These remain defined and searchable without dictating the primary kind hierarchy. `satisfies_specification` means the bearer satisfies some instance of the named specification class in the relevant context; the bearer is not itself a specification. Operational facets need the stated domain criterion.

| ID and label | Definition | Expression | Canonical entry |
|---|---|---|---|
| `facet:Agent` **Agent** | An entity acting intentionally in a specified activity or possessing the relevant agency capacity. | `{"op":"intersection","base_class":"Entity","restrictions":[{"op":"satisfies_specification","specification_class":"AgentRole","context_required":true}]}` | [Entity](#Entity) |
| `facet:SentientAgent` **Sentient agent** | An agent capable of experience or perception as a subject. | `{"op":"intersection","base_class":"Entity","restrictions":[{"op":"satisfies_specification","specification_class":"AgentRole","context_required":true},{"op":"satisfies_specification","specification_class":"SentientRole","context_required":true}]}` | [Entity](#Entity) |
| `facet:CognitiveAgent` **Cognitive agent** | An agent capable of cognition under a stated criterion. | `{"op":"intersection","base_class":"Entity","restrictions":[{"op":"satisfies_specification","specification_class":"AgentRole","context_required":true},{"op":"satisfies_specification","specification_class":"CognitiveRole","context_required":true}]}` | [Entity](#Entity) |
| `facet:AquaticMammal` **Aquatic mammal** | A mammal adapted to a principally aquatic way of life. | `{"op":"intersection","base_class":"Mammal","restrictions":[{"op":"contextual_facet","condition":"habitat=aquatic","formalization_status":"requires a domain-specific operational criterion"}]}` | [Mammal](#Mammal) |
| `facet:HoofedMammal` **Hoofed mammal** | A mammal with hooves, irrespective of evolutionary lineage. | `{"op":"intersection","base_class":"Mammal","restrictions":[{"op":"contextual_facet","condition":"anatomy=hoofed","formalization_status":"requires a domain-specific operational criterion"}]}` | [Mammal](#Mammal) |
| `facet:MicroOrganism` **Microorganism** | An organism requiring magnification for ordinary structural observation. | `{"op":"intersection","base_class":"Organism","restrictions":[{"op":"contextual_facet","condition":"scale=microscopic","formalization_status":"requires a domain-specific operational criterion"}]}` | [Organism](#Organism) |
| `facet:ToxicOrganism` **Toxic organism** | An organism producing or containing material harmful to a specified recipient under specified exposure. | `{"op":"intersection","base_class":"Organism","restrictions":[{"op":"contextual_facet","condition":"toxicity=recipient_and_exposure_dependent","formalization_status":"requires a domain-specific operational criterion"}]}` | [Organism](#Organism) |
| `facet:Invertebrate` **Invertebrate** | An animal outside the vertebrate lineage. | `{"op":"intersection","base_class":"Animal","restrictions":[{"op":"not_instance_of","class":"Vertebrate"}]}` | [Animal](#Animal) |
| `facet:Fish` **Fish in the ordinary sense** | An aquatic vertebrate with a fish body organization, excluding tetrapods in ordinary usage. | `{"op":"intersection","base_class":"Vertebrate","restrictions":[{"op":"contextual_facet","condition":"body_plan=ordinary_fish","formalization_status":"requires a domain-specific operational criterion"}]}` | [Vertebrate](#Vertebrate) |
| `facet:Reptile` **Reptile in the traditional sense** | A sauropsid outside the avian lineage. | `{"op":"intersection","base_class":"Sauropsid","restrictions":[{"op":"not_instance_of","class":"Bird"}]}` | [Sauropsid](#Sauropsid) |
| `facet:Monkey` **Monkey in the ordinary sense** | A simian primate outside the ape lineage. | `{"op":"intersection","base_class":"Simian","restrictions":[{"op":"not_instance_of","class":"Ape"}]}` | [Simian](#Simian) |
| `facet:Alga` **Alga** | A photosynthetic eukaryote conventionally called an alga, outside land plants. | `{"op":"intersection","base_class":"Eukaryote","restrictions":[{"op":"contextual_facet","condition":"form=algal","formalization_status":"requires a domain-specific operational criterion"}]}` | [Eukaryote](#Eukaryote) |
| `facet:NonFloweringPlant` **Nonflowering land plant** | A land plant outside the angiosperm lineage. | `{"op":"intersection","base_class":"Plant","restrictions":[{"op":"not_instance_of","class":"FloweringPlant"}]}` | [Land plant](#Plant) |
| `facet:ColdBloodedVertebrate` **Ectothermic vertebrate** | A vertebrate relying principally on external sources for bodily heat. | `{"op":"intersection","base_class":"Vertebrate","restrictions":[{"op":"contextual_facet","condition":"thermoregulation=ectothermic","formalization_status":"requires a domain-specific operational criterion"}]}` | [Vertebrate](#Vertebrate) |
| `facet:Warm-BloodedVertebrate` **Endothermic vertebrate** | A vertebrate generating substantial internal heat for thermoregulation. | `{"op":"intersection","base_class":"Vertebrate","restrictions":[{"op":"contextual_facet","condition":"thermoregulation=endothermic","formalization_status":"requires a domain-specific operational criterion"}]}` | [Vertebrate](#Vertebrate) |
| `facet:CarnivoreDiet` **Dietary carnivore** | An organism whose diet principally consists of animal material. | `{"op":"intersection","base_class":"Organism","restrictions":[{"op":"contextual_facet","condition":"diet=carnivorous","formalization_status":"requires a domain-specific operational criterion"}]}` | [Organism](#Organism) |
| `facet:DualObjectProcess` **Two-patient process** | A process having at least two distinct patients. | `{"op":"intersection","base_class":"Process","restrictions":[{"op":"contextual_facet","condition":"distinct_patient_count>=2","formalization_status":"requires a domain-specific operational criterion"}]}` | [Process](#Process) |
| `facet:InternalChange` **Intrinsic change** | A process altering a participant's constitution or intrinsic condition. | `{"op":"intersection","base_class":"Process","restrictions":[{"op":"contextual_facet","condition":"change_axis=intrinsic","formalization_status":"requires a domain-specific operational criterion"}]}` | [Process](#Process) |
| `facet:Transfer` **Externally caused translocation** | A motion in which the moving patient differs from the acting agent. | `{"op":"intersection","base_class":"Motion","restrictions":[{"op":"contextual_facet","condition":"agent_distinct_from_patient=true","formalization_status":"requires a domain-specific operational criterion"}]}` | [Motion](#Motion) |
| `facet:SelfConnectedObject` **Self-connected object** | An object whose relevant constituent parts form a connected whole. | `{"op":"intersection","base_class":"Object","restrictions":[{"op":"contextual_facet","condition":"connected=true_in_stated_topology","formalization_status":"requires a domain-specific operational criterion"}]}` | [Object](#Object) |
| `facet:CorpuscularObject` **Constituent-differentiated object** | A connected object having constituent properties not shared by the whole. | `{"op":"intersection","base_class":"Item","restrictions":[{"op":"contextual_facet","condition":"connected=true;constituent_properties_differ=true","formalization_status":"requires a domain-specific operational criterion"}]}` | [Item](#Item) |
| `facet:ContentBearingObject` **Content-bearing object** | An object embodying interpretable content. | `{"op":"intersection","base_class":"Object","restrictions":[{"op":"satisfies_specification","specification_class":"ContentBearerRole","context_required":true}]}` | [Object](#Object) |
| `facet:Product` **Manufactured product** | An artifact produced through manufacturing. | `{"op":"intersection","base_class":"Artifact","restrictions":[{"op":"satisfies_specification","specification_class":"ProductRole","context_required":true}]}` | [Artifact](#Artifact) |
| `facet:FoodBearer` **Food material** | A material portion intended or suitable for consumption by a specified organism. | `{"op":"intersection","base_class":"MaterialPortion","restrictions":[{"op":"satisfies_specification","specification_class":"Food","context_required":true}]}` | [Material portion](#MaterialPortion) |
| `facet:BeverageBearer` **Beverage portion** | A material portion intended for drinking. | `{"op":"intersection","base_class":"MaterialPortion","restrictions":[{"op":"satisfies_specification","specification_class":"Beverage","context_required":true}]}` | [Material portion](#MaterialPortion) |
| `facet:MeatBearer` **Meat portion** | A portion of animal tissue treated as food. | `{"op":"intersection","base_class":"BiologicalMaterial","restrictions":[{"op":"satisfies_specification","specification_class":"Meat","context_required":true}]}` | [Biological material portion](#BiologicalMaterial) |
| `facet:VegetableBearer` **Vegetable food portion** | A portion of plant material conventionally treated as vegetable food. | `{"op":"intersection","base_class":"BiologicalMaterial","restrictions":[{"op":"satisfies_specification","specification_class":"Vegetable","context_required":true}]}` | [Biological material portion](#BiologicalMaterial) |
| `facet:FruitFoodBearer` **Fruit food portion** | A portion of botanical fruit treated as food. | `{"op":"intersection","base_class":"BiologicalMaterial","restrictions":[{"op":"satisfies_specification","specification_class":"FruitFood","context_required":true}]}` | [Biological material portion](#BiologicalMaterial) |
| `facet:BioactiveMaterial` **Bioactive material** | A material portion affecting biological activity in a stated context. | `{"op":"intersection","base_class":"MaterialPortion","restrictions":[{"op":"satisfies_specification","specification_class":"BiologicallyActiveSubstance","context_required":true}]}` | [Material portion](#MaterialPortion) |
| `facet:HormoneBearer` **Hormonal material** | A material portion functioning as a biological regulatory signal. | `{"op":"intersection","base_class":"MaterialPortion","restrictions":[{"op":"satisfies_specification","specification_class":"Hormone","context_required":true}]}` | [Material portion](#MaterialPortion) |
| `facet:NutrientBearer` **Nutrient material** | A material portion utilized or required for nutrition by a specified organism. | `{"op":"intersection","base_class":"MaterialPortion","restrictions":[{"op":"satisfies_specification","specification_class":"Nutrient","context_required":true}]}` | [Material portion](#MaterialPortion) |
| `facet:VitaminBearer` **Vitamin material** | A material portion functioning as an organic micronutrient for a specified organism. | `{"op":"intersection","base_class":"MaterialPortion","restrictions":[{"op":"satisfies_specification","specification_class":"Vitamin","context_required":true}]}` | [Material portion](#MaterialPortion) |
| `facet:EnzymeBearer` **Enzymatic material** | A biological material portion functioning as a catalyst. | `{"op":"intersection","base_class":"BiologicalMaterial","restrictions":[{"op":"satisfies_specification","specification_class":"Enzyme","context_required":true}]}` | [Biological material portion](#BiologicalMaterial) |
| `facet:AgentCollection` **Agent collection** | A collection whose members qualify as agents in the relevant context. | `{"op":"intersection","base_class":"Collection","restrictions":[{"op":"all_members_satisfy_specification","specification_class":"AgentRole","context_required":true}]}` | [Collection](#Collection) |
| `facet:PersonBearer` **Person** | An entity meeting a specified criterion for personhood. | `{"op":"intersection","base_class":"Entity","restrictions":[{"op":"satisfies_specification","specification_class":"Person","context_required":true}]}` | [Entity](#Entity) |
| `facet:IntentionalPsychologicalProcess` **Intentional mental activity** | A mental process constituted by intentional activity. | `{"op":"intersection","base_class":"MentalProcess","restrictions":[{"op":"instance_of","class":"IntentionalProcess"}]}` | [Mental process](#MentalProcess) |
| `facet:OrganicObject` **Biological object in the legacy sense** | An organism, its anatomical part, or an item naturally produced by biological activity. | `{"op":"intersection","base_class":"BioticObject","restrictions":[{"op":"contextual_facet","condition":"origin_or_constitution=biological","formalization_status":"requires a domain-specific operational criterion"}]}` | [Biotic object](#BioticObject) |
| `facet:InstitutionalBearer` **Institutional entity** | A socially constituted entity identified under institutional rules or authority. | `{"op":"class_reference","class":"InstitutionalEntity"}` | [Institutionally constituted entity](#InstitutionalEntity) |
| `facet:LocationBearer` **Location** | A region serving as where an entity is situated in a reference context. | `{"op":"intersection","base_class":"Region","restrictions":[{"op":"satisfies_specification","specification_class":"LocationRole","context_required":true}]}` | [Region](#Region) |
| `facet:SymbolBearer` **Symbol bearer** | An entity representing something under an interpretation. | `{"op":"intersection","base_class":"Entity","restrictions":[{"op":"satisfies_specification","specification_class":"Symbol","context_required":true}]}` | [Entity](#Entity) |
| `facet:NameBearer` **Name bearer** | An entity used as a designating sign. | `{"op":"intersection","base_class":"Entity","restrictions":[{"op":"satisfies_specification","specification_class":"Name","context_required":true}]}` | [Entity](#Entity) |
| `facet:LabelBearer` **Label bearer** | An entity used as an identifying or annotating sign. | `{"op":"intersection","base_class":"Entity","restrictions":[{"op":"satisfies_specification","specification_class":"Label","context_required":true}]}` | [Entity](#Entity) |
| `facet:SlimeMold` **Slime mold** | A eukaryote exhibiting a life cycle conventionally described as slime-mold organization. | `{"op":"intersection","base_class":"Eukaryote","restrictions":[{"op":"contextual_facet","condition":"life_cycle=slime_mold","formalization_status":"requires a domain-specific operational criterion"}]}` | [Eukaryote](#Eukaryote) |
| `facet:AnimalFoodBearer` **Animal-derived food portion** | A material portion derived from an animal and treated as food. | `{"op":"intersection","base_class":"BiologicalMaterial","restrictions":[{"op":"satisfies_specification","specification_class":"AnimalDerivedFood","context_required":true}]}` | [Biological material portion](#BiologicalMaterial) |
| `facet:ImpureWater` **Impure water portion** | A material portion consisting principally of water with other substances. | `{"op":"intersection","base_class":"Mixture","restrictions":[{"op":"contextual_facet","condition":"principal_component=H2O","formalization_status":"requires a domain-specific operational criterion"}]}` | [Mixture portion](#Mixture) |
| `facet:PrintedProduction` **Printed-content production** | A manufacturing process producing a printed information carrier. | `{"op":"intersection","base_class":"Manufacture","restrictions":[{"op":"contextual_facet","condition":"result=printed_information_carrier","formalization_status":"requires a domain-specific operational criterion"}]}` | [Manufacturing](#Manufacture) |

## Typed predicate examples

These are predicate instances classified by the specification classes above. They are not extra class-tree nodes. Context arguments count toward arity.

| Predicate | Typed arguments | Meaning |
|---|---|---|
| `predicate:instance_of` | individual: Entity, class_specification: EntityKind | An individual satisfies the membership criterion of a class specification. |
| `predicate:subclass_of` | subclass_specification: EntityKind, superclass_specification: EntityKind | Every instance admitted by the first class specification is admitted by the second. |
| `predicate:part_of` | part: RealizedEntity, whole: RealizedEntity, context: Entity | The first realized entity constitutes part of the second in the stated context. |
| `predicate:member_of` | element: Entity, set: Set | The first entity is an element of the second under the selected set theory. |
| `predicate:collection_member_of` | member: Entity, collection: Collection, context: Entity | The first entity is admitted as a member of the realized collection in the stated context. |
| `predicate:located_in` | located_entity: RealizedEntity, region: SpatialRegion, reference_context: Entity | The located entity occupies a location within the region in the stated reference context. |
| `predicate:occurs_during` | process: Process, interval: TemporalRegion, reference_context: Entity | The process occurs within the temporal extent in the stated reference context. |
| `predicate:participates_in` | participant: Entity, process: Process, context: Entity | The participant takes part in the process in the stated context. |
| `predicate:realizes_content` | carrier: RealizedEntity, content: InformationContent, interpretation: Entity | The carrier embodies the specified content under the interpretation. |
| `predicate:satisfies_role` | bearer: Entity, role_specification: Role, context: Entity | The bearer fulfills the role specification in the stated context. |
| `predicate:has_quality` | bearer: RealizedEntity, quality_instance: Quality, context: Entity | The quality instance characterizes the bearer in the stated context. |
| `predicate:has_quality_value` | quality_instance: Quality, value: QualityValue, scale_context: Entity | The quality instance is represented by the value on the stated descriptive scale. |
| `predicate:has_quantity_value` | quality_instance: QuantitativeQuality, value: QuantityValue, scale_context: Entity | The quantitative quality instance is represented by the magnitude on the stated scale. |
| `predicate:quantity_greater_than` | first: QuantityValue, second: QuantityValue, comparison_scale: Entity | The first magnitude exceeds the second after conversion to the stated compatible scale. |
| `predicate:causally_contributes_to` | cause: RealizedEntity, effect: RealizedEntity, context: Entity | The cause contributes to the effect under a specified causal account. |
| `predicate:derived_from` | result: Entity, source: Entity, derivation_context: Entity | The result derives from the source through the stated history or operation. |
| `predicate:same_as` | first: Entity, second: Entity | Both arguments denote the same entity. |
| `predicate:has_arity` | predicate: PredicateSpecification, argument_count: NaturalNumber | The predicate specification has the stated number of arguments. |
| `predicate:describes_fictional_entity` | description: FictionalDescription, world_description: InformationContent | The description individuates a fictional referent within the specified described world. |
| `predicate:is_red` | bearer: RealizedEntity | The bearer is red under a fixed color interpretation. |

## Split policies

All child groups are selective. The following notes expose the axis and any expected overlap.

| Parent | Axis | Disjointness | Note |
|---|---|---|---|
| [Entity](#Entity) | identity dependence | not_asserted | Concrete realization and abstract identity are useful routes, not a theorem settling all ontology. |
| [Realized entity](#RealizedEntity) | basis of individuation | not_asserted | Organization, extent, occurrence, condition, bearer dependence, and social constitution can cross-cut. |
| [Abstract entity](#AbstractEntity) | basis of abstract identity | overlapping | Structure, content, values, predicates, and units are not intrinsically disjoint. |
| [Object](#Object) | constitution and unity | overlapping | Items, material portions, collections, social objects, fields, and tokens are not a closed partition. |
| [Item](#Item) | constitutive organization and origin | overlapping | Origin and design remain useful but overlapping kinds; a cultured organism may be biotic and an artifact. |
| [Natural object](#NaturalObject) | biological contribution to constitution | not_asserted | Only the abiotic branch is projected here; natural biotic items use Biotic object with a natural-origin facet. |
| [Biotic object](#BioticObject) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Material body](#MaterialBody) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Particle body](#ParticleBody) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Subatomic particle](#SubatomicParticle) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Celestial body](#AstronomicalBody) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Small celestial body](#SmallCelestialBody) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Geological body](#GeologicalBody) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Organism](#Organism) | selected evolutionary lineages | overlapping_ancestry | Animal is displayed directly for accessibility, with Eukaryote retained as alternate superclass. |
| [Eukaryote](#Eukaryote) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Land plant](#Plant) | selected evolutionary lineages | overlapping_ancestry | Moss and vascular plants do not exhaust land plants; liverworts and hornworts remain admissible. |
| [Vascular plant](#VascularPlant) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Seed plant](#SeedPlant) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Animal](#Animal) | compressed evolutionary lineages | overlapping_ancestry | Vertebrate is projected near Animal; full intermediate clades remain in alternate parents and source lineage. |
| [Bilaterian](#Bilaterian) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Arthropod](#Arthropod) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Vertebrate](#Vertebrate) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Jawed vertebrate](#JawedVertebrate) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Bony vertebrate](#BonyVertebrate) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Lobe-finned vertebrate](#LobeFinnedVertebrate) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Tetrapod](#Tetrapod) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Amniote](#Amniote) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Mammal](#Mammal) | selected evolutionary lineages | overlapping_ancestry | Primate is displayed directly; eutherian ancestry remains in alternate parents. |
| [Eutherian mammal](#PlacentalMammal) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Carnivoran](#Carnivoran) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Canid](#Canine) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Felid](#Feline) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Primate](#Primate) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Ape](#Ape) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Cetartiodactyl](#Cetartiodactyl) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Sauropsid](#Sauropsid) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Archosaur](#Archosaur) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Dinosaur](#Dinosaur) | selected evolutionary lineages | overlapping_ancestry | Compressed evolutionary subclasses; hidden source lineage preserves omitted ranks. No assertion that selected children exhaust the taxon. |
| [Biological structure](#BiologicalStructure) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Anatomical structure](#AnatomicalStructure) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Body part](#BodyPart) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Organ](#Organ) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Acellular infectious entity](#AcellularInfectiousEntity) | propagated biological organization | not_asserted | Convenience organism-independent infectious classes; not a single phylogenetic clade. |
| [Artifact](#Artifact) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Device](#Device) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Machine](#Machine) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Vehicle](#TransportationDevice) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Engineered component](#EngineeringComponent) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Built structure](#StationaryArtifact) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Manufactured information carrier](#InformationCarrier) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Material portion](#MaterialPortion) | material individuation | overlapping | Composition, biological constitution, and manufacturing history cross-cut; do not infer siblings disjoint. |
| [Substance portion](#Substance) | composition uniformity | overlapping | Mineral kinds may occupy compositions in either pure or mixed preparations. |
| [Pure substance portion](#PureSubstance) | chemical constitution | not_asserted | Elemental and compound categories are not asserted as a foundation-independent exhaustive partition. |
| [Elemental substance portion](#ElementalSubstance) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Compound substance portion](#CompoundSubstance) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Mixture portion](#Mixture) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Biological material portion](#BiologicalMaterial) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Body material portion](#BodySubstance) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Tissue portion](#Tissue) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Manufactured material portion](#ManufacturedMaterial) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Collection](#Collection) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Material aggregate](#MaterialAggregate) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Astronomical system](#AstronomicalSystem) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Human group](#HumanGroup) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Organization](#Organization) | constitutive charter or function | overlapping | A religious school, corporate university, or government court can satisfy several kinds. |
| [Educational organization](#EducationalOrganization) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Political organization](#PoliticalOrganization) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Social object](#SocialObject) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Region](#Region) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Spatial region](#SpatialRegion) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Temporal region](#TemporalRegion) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Geographic area](#GeographicArea) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Land area](#LandArea) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Jurisdictional area](#GeopoliticalArea) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Water area](#WaterArea) | salinity and water movement | overlapping | Two declared axes: salinity (fresh/salt) and flow (standing/flowing); one area can qualify along both. |
| [Process](#Process) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Physical process](#PhysicalProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Motion](#Motion) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Bodily movement](#BodyMotion) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Propulsion](#Impelling) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Contact onset](#Touching) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Emission](#Radiating) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Sound emission](#RadiatingSound) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Configuration change](#ConfigurationChange) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Shape change](#ShapeChange) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Surface change](#SurfaceChange) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Quantity change](#QuantityChange) | direction of change on a fixed scale | disjoint_in_same_context | Increase and decrease differ only after fixing quantity, interval, and comparison convention. |
| [Increase](#Increasing) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Decrease](#Decreasing) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Phase change](#StateChange) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Chemical reaction](#ChemicalProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Creation](#Creation) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Making](#Making) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Content creation](#ContentDevelopment) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Damage](#Damaging) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Destruction](#Destruction) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Biological process](#BiologicalProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Physiological process](#PhysiologicProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Organism-level process](#OrganismProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Reproduction](#Replication) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Ingestion](#Ingesting) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Injury](#Injuring) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Mental process](#MentalProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Perception](#Perception) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Cognitive process](#CognitiveProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Intentional activity](#IntentionalProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Guidance](#Guiding) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Maintenance](#Maintaining) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Retention](#Keeping) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Treatment](#TherapeuticalProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Search](#Searching) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Investigation](#Investigating) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Recreation or exercise](#RecreationOrExercise) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Game playing](#Gaming) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Social interaction](#SocialInteraction) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Communication](#Communication) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Linguistic communication](#LinguisticCommunication) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Dissemination](#Disseminating) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Directive communication](#Directing) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Contest](#Contest) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Violent contest](#ViolentContest) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Possession transfer](#ChangeOfPossession) | participant perspective | overlapping | Acquisition and giving are role-bound occurrence classes; the same event can instantiate both. |
| [Acquisition](#Getting) | reciprocity and temporary custody | overlapping | Borrowing is temporary custody; unilateral taking is a reciprocity condition, so these are cross-cutting. |
| [Giving](#Giving) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Transaction](#Transaction) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Financial transaction](#FinancialTransaction) | participant perspective and transaction purpose | overlapping | Buying and selling are perspectives; betting is a transaction purpose. |
| [Organizational process](#OrganizationalProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Organizational admission](#JoiningAnOrganization) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Organizational departure](#LeavingAnOrganization) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Observation activity](#ObservationProcess) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [State instance](#StateInstance) | constitutive condition | overlapping | Mental, relational, and socially recognized conditions are not a closed partition. |
| [Mental state](#MentalState) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Belief state](#BeliefState) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Relational state](#RelationalState) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Dependent feature](#DependentFeature) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Quality instance](#Quality) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Disposition instance](#Disposition) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Abstract structure](#AbstractStructure) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Mathematical entity](#MathematicalEntity) | specified mathematical structure | overlapping | Functions, sets, graphs, and spaces may share mathematical encodings without asserting identity of those encodings. |
| [Number](#Number) | numeric domains | overlapping | Nested domains are retained as alternate parents, not a disjoint partition. |
| [Function](#Function) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Computable function](#ComputableFunction) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Algebraic structure](#AlgebraicEntity) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Geometric object](#GeometricEntity) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Curve](#Curve) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Computational structure](#ComputationalEntity) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Information content](#InformationContent) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Data content](#Data) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Record content](#Record) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Observation result](#Observation) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Proposition](#Proposition) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Representational content](#RepresentationalEntity) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Description](#Description) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Model content](#Model) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Mathematical model](#MathematicalModel) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Schema](#Schema) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Formal expression](#FormalExpression) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Symbol string](#SymbolicString) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Linguistic expression](#LinguisticExpression) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Word](#Word) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Phrase](#Phrase) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Text content](#Text) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Document content](#Document) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Image content](#Image) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Video content](#Video) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Publication series](#Series) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Language system](#Language) | use community and design | overlapping | Human languages can be artificial; formal-language extensions are classified separately as structures. |
| [Human language](#HumanLanguage) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Artificial language](#ArtificialLanguage) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Normative content](#NormativeContent) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Norm specification](#Norm) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Practice pattern](#Practice) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Game rule system](#Game) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Predicate specification](#PredicateSpecification) | arity and classification purpose | overlapping | Entity kinds are unary predicates; arity classes are disjoint but kind specifications overlap Property specifications. |
| [Property specification](#Property) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Descriptive property specification](#DescriptiveProperty) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Disposition property specification](#DispositionProperty) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Role specification](#Role) | contextual bearer function | overlapping | Food, product, agency, designation, and instrumental use are qualifications, not bearer kinds. |
| [Food specification](#Food) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Bioactive material specification](#BiologicallyActiveSubstance) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Nutrient specification](#Nutrient) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Relation specification](#Relation) | relation subject matter | overlapping | Identity and equivalence are nested within logical and mathematical families, not peer partition axes. |
| [Social relation specification](#SocialRelation) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Logical relation specification](#LogicalRelation) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Mathematical relation specification](#MathematicalRelation) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Symbol specification](#Symbol) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Socially constituted entity](#SocialEntity) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Information token](#InformationToken) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Social group](#SocialGroup) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Entity kind specification](#EntityKind) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Animal-derived food specification](#AnimalDerivedFood) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |
| [Energy absorption](#Absorbing) | defined distinguishing criteria of the named child kinds | not_asserted | Named subclasses provide coverage without asserting a closed partition. |

## Editorial and ambiguity notes

- **[Realized entity](#RealizedEntity)**: Situated social and dependent entities are included. No universal present, atomistic substance metaphysics, or exclusively material embodiment is assumed.
- **[Abstract entity](#AbstractEntity)**: Abstract does not mean unreal, eternal, or causally inert by stipulation. These are content, structure, and predicate identity criteria; nominalist and realist interpretations remain open.
- **[Object](#Object)**: Organization-based individuation permits either three-dimensional or spacetime models. Canonical Object and Process descriptions are not declared disjoint.
- **[Biotic object](#BioticObject)**: Canonical ancestry is compressed; alternate superclass links and biological source lineage retain the intervening categories.
- **[Molecule](#Molecule)**: Neutral molecules are central examples; charged molecular units are included here. Atoms and molecules are individuals; substance portions are amounts of material.
- **[Animal](#Animal)**: Canonical ancestry is compressed; alternate superclass links and biological source lineage retain the intervening categories.
- **[Vertebrate](#Vertebrate)**: Canonical ancestry is compressed; alternate superclass links and biological source lineage retain the intervening categories.
- **[Amniote](#Amniote)**: Canonical ancestry is compressed; alternate superclass links and biological source lineage retain the intervening categories.
- **[Mammal](#Mammal)**: Canonical ancestry is compressed; alternate superclass links and biological source lineage retain the intervening categories.
- **[Primate](#Primate)**: Canonical ancestry is compressed; alternate superclass links and biological source lineage retain the intervening categories.
- **[Ape](#Ape)**: Canonical ancestry is compressed; alternate superclass links and biological source lineage retain the intervening categories.
- **[Human](#Human)**: Canonical ancestry is compressed; alternate superclass links and biological source lineage retain the intervening categories.
- **[Protein portion](#Protein)**: This node denotes a portion of one protein substance. A protein molecule is a Molecule; a mixed protein preparation is a Mixture with a composition facet. RNA catalysts are permitted by Enzyme specification.
- **[Region](#Region)**: A reference-dependent concrete extent is distinguished from its coordinate description or mathematical region model. Holes and rooms here are spaces; surrounding walls and structures are objects.
- **[True proposition](#Fact)**: Truth is interpretation-indexed. A worldly state of affairs is a State instance, not the proposition describing it.
- **[Character string](#Character)**: A character as an abstract alphabet element is represented by this one-character string class; a glyph occurrence is an Information token; a narrative character is a Fictional entity description.
- **[Formal language](#FormalLanguage)**: The language here is the extension of admitted strings; a grammar specifying it is representational content. No claim that every natural language is identical to a formal-language extension.
- **[Quantity property specification](#Quantity)**: A class of unary quantity specifications. Actual bearer-specific magnitudes are Quantitative quality instances; numbers with units or scales are Quantity values.
- **[Personhood specification](#Person)**: This is a class of unary personhood specifications, not a subclass of Human. A bearer may be a human, an organization, or another entity under explicitly recorded criteria. Biological humans retain a direct route through Human.

Full source identifiers, retrieved biological lineages, aliases, formalization constraints, and coverage scope are retained in [ontology-proposal.json](ontology-proposal.json).
