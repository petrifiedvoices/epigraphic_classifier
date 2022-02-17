# Machine learning classifier for types of Latin inscriptions
*TOOL & ANALYSIS*

---

![Project_status](https://img.shields.io/badge/status-in__progress-brightgreen "Project status logo")

## Purpose
There are more several thousand Latin inscriptions, yet they reside in several lrage databases that do not share the same classification system, hindering any potential quantitative study by the inoperability of their taxonomies. The aim of the project is to train a classification model on a well curated dataset with consistent taxonomic model (EDH dataset, containing 80,000+ records and their metadata) to help classify inscriptions in the target dataset (in our case EDCS database with 500,000 inscriptions). We evaluate the model using manually labelled data. Additonally, we search for patterns between the two taxonomies, that could contribute to the current academic debate on the use of Linked Open Data in epigraphy and the practicalities of aligning diverse datasets. 

## Authors
* Dr Petra Hermankova [![](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0002-6349-0540), postdoc, SDAM project, Aarhus University, petra.hermankova@cas.au.dk, [@petrifiedvoices](https://github.com/petrifiedvoices)
* Jan Kostkan, CHCAA, Aarhus University,[@supplyandcommand](https://github.com/supplyandcommand)

The Epigraphic Classifier was developed as part of the Digital Literacy 2.0 Program, 2020-2021, as on of the outcomes of the [Epigraphic Roads](https://github.com/sdam-au/epigraphic_roads/) project by Petra Hermankova, Aarhus University; created in collaboration with the Centre for Humanities Computing Aarhus (CHCAA).

## License
CC-BY-SA 4.0, see attached [License](./License.md)

---

## Data

### Training dataset - Epigraphic Database Heidelberg
For details see a series of scripts in [EDH_ETL Repository](https://github.com/sdam-au/EDH_ETL) used to access and clean the tabular attributes of the dataset and the text of inscriptions. For more details on the contents see the [EDH dataset metadata](https://docs.google.com/spreadsheets/d/1O_4EH-POKqUgq5K-B1DbbJQ8WWF0NQ6s12dCiW29MbA/edit?usp=sharing)

`https://sciencedata.dk/public/b6b6afdb969d378b70929e86e58ad975/EDH_text_cleaned_2021-01-21.json`


### Target dataset - Epigraphic Database Clauss Slaby
FOr details see a series of scripts in [EDCS_ETL Repository](https://github.com/sdam-au/EDCS_ETL) used to access and clean the tabular attributes of the dataset and the text of inscriptions. For more details on the contents see the [EDCS dataset metadata](https://docs.google.com/spreadsheets/d/17k4quLM6RiEu821n3caitK8labzuurIGmzf0W1bHnss/edit?usp=sharing).

`https://sciencedata.dk/public/1f5f56d09903fe259c0906add8b3a55e/EDCS_text_cleaned_2022-02-15.json` 


### Other data
1. `data/EDCS_random100_inscrtype.csv` - sample of 100 randomly selected inscriptions manually labelled by Petra Hermankova (blind, without access to original EDCS labels, only to ID, Material and the original and cleaned text of the inscription)
1. `data/EDCS_to_EDH_types_inscr_dictionary.csv` - dictionary containing approximate translation of labels between the training and the target datasets
1. `data/EDCS_types_inscr.csv` - all labels used in the target dataset for the type of inscription
1. `data/EDH_types_inscr.csv` - all labels used in the training dataset for the type of inscription

---

## Description

To train the model, we use the following attributes:

1. `clean_text_interpretive_word` = containing clean text of an inscription, text
1. `clean_text_conservative` = containing original text of inscription as appears on the physical object
1. `type_of_inscription_clean` = containing cleaned typology for inscriptions, 22 unique categories
1. `type_of_inscription_certainty` = containg binary values (certain, uncertain) stating the level of confidence of the classification in `type_of_inscription_clean` 
1. `material_clean` = cleaned material of the inscribed object, 34 unique categories
1. `type_of_monument_clean` = cleaned typology of types of inscribed objects
1. `type_of_monument_certainty` = containg binary values (certain, uncertain) stating the level of confidence of the classification in `type_of_monument_clean`

The target dataset contains the following attributes 
1. `clean_text_interpretive_word` = containing clean text of an inscription
1. `clean_text_conservative` = containing original text of inscription as appears on the physical object
1. `material` = cleaned material of the inscribed object

Ideal envisioned outcome of the model - numeric representation of a probability with which an inscription X from the target dataset falls into the categorisation of inscription types. For example, `inscription X from target dataset is categorised as 56 % milestone,  45 % decree,  10 % funerary inscription, 1 % list.`

For evaluation of the model we a) use the manually labelled data, and b) we contrast model-produced labels with the labels present in the EDCS (that however, follow a different taxonomy and allow for combination of labels, instead of assigning just one and thus are not immediately translatable to the taxonomy used in EDH, but can provide additional information).


### Try the model out
Interactive dashboard with the current model available at https://epigraphic-classifier.herokuapp.com/.
The model was trained on Latin inscriptions from the [Epigraphic Database Heidelberg](https://edh-www.adw.uni-heidelberg.de/). The [Source code](https://github.com/petrifiedvoices/ancient-classifier), forked from [CHCAA Ancient-classifier](https://github.com/centre-for-humanities-computing/ancient-classifier/).



