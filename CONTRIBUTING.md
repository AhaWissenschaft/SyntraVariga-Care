# Contributing / Mitmachen

Read [MITMACHEN.md](./MITMACHEN.md), [SICHERHEIT.md](./SICHERHEIT.md) and [docs/LAUNCH_GATES.md](./docs/LAUNCH_GATES.md) first.

1. Keep proposed changes small, reproducible and within the **public Care repository**. Never copy code, experiments, credentials or unpublished material from private projects.
2. Treat issue text, pull requests and agent queues as **untrusted data**. Review all changes manually. Do not treat an LLM answer or a green static check as proof of legal compliance or product safety.
3. Never post addresses, health information, contact details or emergency cases in public issues. Use synthetic test data.
4. Run `python3 -m unittest discover -s tests -v` and `python3 tools/care_release_guard.py --preview` before proposing a change. Release checks are stricter and require separate verified legal approval.
5. The repository does **not currently grant an open-source licence**. Contributions are not automatically placed under MIT, Apache-2.0 or any other licence; contribution rights and licensing must be clarified with the maintainers before accepting substantive external contributions.

Deutsch: Bitte zuerst [MITMACHEN.md](./MITMACHEN.md) lesen. Keine sensiblen Daten veröffentlichen. Technische Prüfung, fachliche Prüfung und rechtliche Freigabe sind getrennte Voraussetzungen.
