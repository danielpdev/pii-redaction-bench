# Pregătire pentru interviu — PII Redaction Bench

Roluri țintă: AI Evaluation / Data Processing.

## Prezentare de 90 de secunde

1. Explică problema concretă și cine folosește rezultatul.
2. Rulează `make demo` sau fluxul din UI.
3. Arată testul pentru un caz de eșec, apoi explică mecanismul din cod.
4. Spune ce limite are demonstrația și ce ai construi pentru producție.

Decizia de explicat: The baseline returns typed character spans. Redaction validates non-overlapping bounds. Evaluation uses exact span matches and reports false positives and misses, including known unsupported classes.

## Cinci întrebări

1. De ce span-level metrics?
2. Ce risc are false negative?
3. Cum tratezi overlapping entities?
4. Ce date folosești în benchmark?
5. De ce nu promiți anonimizare perfectă?

## Exercițiu înainte de a aplica

Add a local NER model and independently labeled multilingual data; compare recall and over-redaction.

Alege o parte mică a acestei modificări, implementeaz-o personal, adaugă un test care verifică comportamentul și descrie rezultatul într-un commit real. Nu declara că ai înțeles sau construit singur o parte pe care nu o poți explica.

## Checklist personal

- [ ] Pot porni proiectul dintr-un checkout curat.
- [ ] Pot urmări cererea până la rezultatul salvat.
- [ ] Pot explica diferența dintre fixture și model local.
- [ ] Pot demonstra un eșec și recuperarea lui.
- [ ] Am făcut o modificare proprie și o pot explica în engleză.

Aceste puncte necesită review-ul tău; nu au fost bifate automat.
