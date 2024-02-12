# Constitution-Helper

# Introduction

Constitution-Helper is a simple program, written in python, which takes user input text and searches sentences in a text file that contain the exact or similar words from the user input text.

# Usage

## Clone the repository

```bash
git clone https://github.com/MarAraqelyan/Constitution-Helper.git
```

## Make sure you have spaCy

```bash
pip install spacy
```

## Run the program

```bash
python constitution_helper.py find "User input text"
```
Replace "User input text" with the search text.

## Examples
### Input:

python constitution_helper.py find  "red, blue, orange"

### Output:

1  The flag of the Republic of Armenia shall be tricolour, with equal horizontal stripes of red, blue and orange

Similar sentence:
  The flag of the Republic of Armenia shall be tricolour, with equal horizontal stripes of red, blue and orange


### Input:

python constitution_helper.py find  "ownership"

### Output:

1  Guaranteeing Ownership

2  All forms of ownership shall be recognised and equally protected in the Republic of Armenia

3  The subsoil and water resources shall fall under the exclusive ownership of the State

4  Right of Ownership

5  The right of ownership may be restricted only by law, for the purpose of protecting public interests or the basic rights and freedoms of others

6  No one may be deprived of ownership except through judicial procedure, in the cases prescribed by law

7  Foreign citizens and stateless persons shall not enjoy the right of ownership over land, except for the cases prescribed by law

8  The powers of a Deputy shall discontinue upon expiry of the term of powers of the National Assembly, in case of loss of citizenship of the Republic of Armenia or acquisition of citizenship of another State, entry into force of a criminal judgment on sentencing him or her to imprisonment, entry into force of a civil judgment on declaring him or her as having no active legal capacity, as missing or dead, in case of his or her death, or resignation

Similar sentence:
  Guaranteeing Ownership
