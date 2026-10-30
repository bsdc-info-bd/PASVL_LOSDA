# Translations

The framework was founded in Bangladesh and is meant for the world. The authoritative text is
English; translations exist so that people can understand their rights without reading legal
English.

## 1. The rule

> **The English text prevails.** A translation is for convenience only, unless the Steward has
> expressly designated it authoritative for a jurisdiction and published that designation here.

See PASVL §28.4.

## 2. Available translations

| Language | Code | Files | Status | Reviewer |
|---|---|---|---|---|
| English | `en` | the root documents | **Authoritative** | License Council |
| Bengali (বাংলা) | `bn` | [summary set](bn/) | Complete for summaries; full licence pending | *seeking reviewer* |

## 3. What gets translated, in priority order

1. **The plain-language summary** — the single most useful document for a reader.
2. **The LOSDA summary** — what permission is, and how to ask for it.
3. **The FAQ** — the questions people actually ask.
4. **The code of conduct** — so that participation is safe in the participant's language.
5. **The licence itself** — a large undertaking; requires legal review.
6. **The templates** — so that applicants can apply in their own language.

## 4. Rules for translators

1. **Never change the meaning.** If a sentence is ambiguous in English, translate the ambiguity
   and add a translator's note; do not resolve it.
2. **Keep defined terms.** Either keep the English defined term in parentheses, or use one
   consistent translated term and list it in the glossary.
3. **Do not translate identifiers.** `LOSDA-BSDC-2026-000001`, `PASVL-1.0`, and
   `LicenseRef-PASVL-1.0` stay exactly as they are.
4. **Preserve the warnings.** The "not legal advice" and "not open source" statements must appear
   in every translation.
5. **Mark the status.** Every translated file begins with the banner below.
6. **Two reviewers.** A translation is merged only after review by a second native speaker, one of
   whom should be able to read the English legal text.

## 5. Required banner

```markdown
> **অনুবাদ · Translation.** This is a translation for convenience only.
> The English text prevails in case of conflict. See `translations/README.md`.
```

## 6. Contributing a language

1. Open an RFC or a pull request adding `translations/<code>/`.
2. Start with the plain-language summary.
3. Add a `README.md` in that directory describing the status and the reviewers.
4. Add the language to the table above.
5. Update `translations/bn/`-style banners and the root README language badge if appropriate.

## 7. Machine translation

Machine-translated text may be used as a **first draft**, but must be fully reviewed by a human
before publication, and the reviewer must be named. Publishing unreviewed machine translation of
a legal document is worse than publishing nothing.

## 8. Disagreements between translations

If two translations conflict, the English text resolves it. If the English text is itself
ambiguous, raise an RFC so that the ambiguity is fixed at the source.
