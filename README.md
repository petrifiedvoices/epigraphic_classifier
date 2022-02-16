# Machine learning classifier for types of Latin inscriptions
*TOOL & ANALYSIS*

---

![Project_status](https://img.shields.io/badge/status-in__progress-brightgreen "Project status logo")

## Purpose
Train a classification model (trained on the data + metadata available through EDH dataset, containing 80,000+ records) to help classify a target dataset (EDCS with 500,000 inscriptions).

## Authors
* Dr Petra Hermankova [![](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0002-6349-0540), postdoc, SDAM project, Aarhus University, petra.hermankova@cas.au.dk, [@petrifiedvoices](https://github.com/petrifiedvoices)
* Jan Kostkan, CHCAA, Aarhus University,[@supplyandcommand](https://github.com/supplyandcommand)

The Epigraphic Classifier was developed as part of the Digital Literacy 2.0 Program, 2020-2021, as on of the outcomes of the [Epigraphic Roads](https://github.com/sdam-au/epigraphic_roads/) project by Petra Hermankova, Aarhus University; created in collaboration with the Centre for Humanities Computing Aarhus (CHCAA).

## License
CC-BY-SA 4.0, see attached License.md
---

## Data

### Training dataset - Epigraphic Database Heidelberg
- see a series of scripts in [EDH_ETL Repository](https://github.com/sdam-au/EDH_ETL) used to access and clean the tabular attributes of the dataset and the text of inscriptions.

`https://sciencedata.dk/public/b6b6afdb969d378b70929e86e58ad975/EDH_text_cleaned_2021-01-21.json`

[EDH dataset metadata](https://docs.google.com/spreadsheets/d/1O_4EH-POKqUgq5K-B1DbbJQ8WWF0NQ6s12dCiW29MbA/edit?usp=sharing)

### Target dataset - Epigraphic Database Clauss Slaby
- see a series of scripts in [EDCS_ETL Repository](https://github.com/sdam-au/EDCS_ETL) used to access and clean the tabular attributes of the dataset and the text of inscriptions.

`https://sciencedata.dk/public/1f5f56d09903fe259c0906add8b3a55e/EDCS_text_cleaned_2022-02-15.json` 

[EDCS dataset metadata](https://docs.google.com/spreadsheets/d/17k4quLM6RiEu821n3caitK8labzuurIGmzf0W1bHnss/edit?usp=sharing)


### Other data
1. `data/EDCS_random100_inscrtype.csv` - sample of 100 randomly selected inscriptions manually labelled by Petra Hermankova (blind, without access to original EDCS labels)
2. `data/labels_dictionary.csv` - Dictionary of labels between the training and the target datasets

---

## Description

Use attributes (sorted from the most important):

1. `clean_text_interpretive_word` = containing clean text of an inscription, text
2. `type_of_inscription_clean` = containing cleaned typology for inscriptions, 22 unique categories
3. `type_of_inscription_certainty` = containg binary values (certain, uncertain) stating the level of confidence of the classification in `type_of_inscription_clean` 
4. `material_clean` = cleaned material of the inscribed object, 34 unique categories
5. `type_of_monument_clean` = cleaned typology of types of inscribed objects
6. `type_of_monument_certainty` = containg binary values (certain, uncertain) stating the level of confidence of the classification in `type_of_monument_clean`

The target dataset has no formal typology, it contains the following attributes 
1. `clean_text_interpretive_word` = containing clean text of an inscription
2. `clean_text_conservative` = containing original text of inscription as appears on the physical object
2. `material` = cleaned material of the inscribed object

*Scenario:* 
Based on the training dataset generate a classification model that would help researchers classify inscritpions in the target dataset. 

Ideal envisioned outcome of the model - numeric representation of a probability with which an inscription X from the target dataset falls into the categorisation of inscription types. For example, `inscription X from target dataset is categorised as 56 % milestone,  45 % decree,  10 % funerary inscription, 1 % list.`

### Try me out
Interactive dashboard with the current model available at https://epigraphic-classifier.herokuapp.com/.
The model was trained on Latin inscriptions from the [Epigraphic Database Heidelberg](https://edh-www.adw.uni-heidelberg.de/). The [Source code](https://github.com/petrifiedvoices/ancient-classifier), forked from [CHCAA Ancient-classifier](https://github.com/centre-for-humanities-computing/ancient-classifier/).



