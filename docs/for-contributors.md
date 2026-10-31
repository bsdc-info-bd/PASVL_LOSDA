# For Contributors

You want to fix a bug or add a feature to a PASVL work. Good. Here is what you need to know
before you open a pull request.

---

## 1. You can fork and contribute — that is expressly allowed

Article 3.3 and Article 3.6 grant the right to fork and to prepare Contributions. No one needs
permission to send a pull request, and no one needs permission to publish a fork for the purpose
of contributing or studying.

## 2. What you are agreeing to

By contributing, you agree to **Article 12** of the license:

- You keep copyright in your Contribution.
- You grant the Author and BSD C a perpetual, worldwide, royalty-free, irrevocable license to
  use, modify, distribute, sublicense, and relicense your Contribution — including for
  commercial licensing under a LOSDA.
- This is what allows the Author to enforce the license and to sell deployment permission. Without
  it, the framework cannot work.

If you are not comfortable with that, do not contribute. You are still free to fork and study.

## 3. Sign your commits

Every commit must be signed off under the Developer Certificate of Origin 1.1:

```bash
git commit -s -m "fix: correct off-by-one in queue length"
```

This adds a trailer:

```
Signed-off-by: Your Name <you@example.com>
```

A pull request without sign-off will be returned.

## 4. Check your employer's rights

If you contribute code written in the course of your employment, your employer may own it. Get
written permission first, or have your employer sign
[`../templates/CONTRIBUTOR-AUTHORIZATION.md`](../templates/CONTRIBUTOR-AUTHORIZATION.md),
Section 5.

## 5. Do not import incompatible code

Before you add a dependency or copy code from elsewhere:

| Source license | Can you put it in a PASVL work? |
|---|---|
| MIT, BSD, ISC, Apache-2.0 | ✅ Yes, with notices |
| MPL-2.0 | ✅ File-level, with notices |
| LGPL | ⚠️ Dynamic linking only, with care |
| GPL, AGPL | ❌ No |
| Unknown or unlicensed | ❌ Never |

See [`../legal/compatibility.md`](../legal/compatibility.md).

## 6. What a good contribution looks like

1. **One purpose per pull request.**
2. **A test that fails before and passes after.**
3. **A description that explains *why*, not just *what*.**
4. **No unrelated formatting changes.**
5. **No license header removal.**
6. **No new dependency without a license check.**
7. **No telemetry, tracking, or network calls** unless discussed and documented.
8. **No generated code** unless the generator is included.

## 7. What gets rejected

- Malicious or obfuscated code.
- Code under an incompatible license.
- Code that removes attribution or notices.
- Code that adds tracking without disclosure.
- Code that breaks the deployment Gate (see below).
- Plagiarized code.
- Bulk reformatting that obscures the change.

## 8. The deployment gate

Some PASVL works include a **deployment gate** — a check that verifies a LOSDA is present before
the software runs in production. You may:

- inspect it;
- test it;
- report bugs in it;
- propose improvements.

You may **not** disable, bypass, or defeat it (PASVL §13.7), except for security research under
Article 8. If a gate causes you a legitimate problem (for example, it misidentifies your
testing environment), report it — the author is required to provide a documented means to
resolve it.

## 9. Documentation contributions

Documentation is as valuable as code. Apply the same rules: sign-off, license header, no
incompatible content. Translations are welcome — see [`../translations/`](../translations/).

## 10. Code of conduct

Participation is governed by [`../CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md). Report concerns to
the address in that document.

## 11. Getting credit

Contributors are listed in `CONTRIBUTORS.md`. Substantial contributions may be acknowledged in
the release notes. The Author must credit contributions "where reasonably practicable"
(§12.7); a missing credit is not a breach, but it is a good reason to ask.

## 12. After your pull request merges

- Your contribution is licensed to the public under PASVL-1.0.
- You do **not** receive deployment rights by contributing. If you want to deploy, apply for a
  LOSDA like everyone else.
- You retain the right to use your own contribution in your own work, subject to the inbound
  license you granted.

## 13. Security issues

Do not open a public issue. Use [`../templates/SECURITY-REPORT.md`](../templates/SECURITY-REPORT.md)
and follow [`../SECURITY.md`](../SECURITY.md).
