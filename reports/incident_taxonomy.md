# AI Safety Incident Taxonomy

A proposed classification framework for standardizing how frontier AI safety incidents are reported, categorized, and compared across jurisdictions. Developed as part of the Frontier AI Safety Policy Monitor project.

## Purpose

Currently, AI safety incidents are disclosed inconsistently across countries, companies, and media outlets, making it difficult to compare risks or identify emerging patterns. This taxonomy proposes a standardized structure, similar in spirit to incident classification systems used in aviation and cybersecurity, to support more systematic tracking and policy response.

## Severity Levels

| Level | Description | Example Indicator |
|-------|-------------|-------------------|
| **Critical** | Incident causes or risks significant physical, financial, or systemic harm; involves loss of human oversight or control | AI system used in critical infrastructure fails or is misused with real-world safety consequences |
| **High** | Incident causes significant harm to individuals or institutions, or reveals a serious vulnerability, but is contained | Wrongful identification by a facial recognition system leading to real-world consequences for an individual |
| **Medium** | Incident reveals a notable risk or failure but with limited direct harm; often prompts investigation or regulatory scrutiny | Regulatory probe into an AI-driven system's safety practices |
| **Low** | Incident is a near-miss, minor misuse, or isolated technical failure with minimal real-world impact | Unauthorized but low-impact use of an AI agent in a non-critical system |

## Risk Categories

1. **Safety Failure** — The AI system behaves in an unintended or harmful way during normal operation (e.g., misidentification, faulty decision-making in autonomous systems).
2. **Security / Misuse** — The AI system or its access is exploited, hijacked, or used maliciously by a third party.
3. **Bias & Discrimination** — The AI system produces outcomes that disproportionately harm or misidentify specific groups.
4. **Regulatory & Compliance** — Government or regulatory bodies take formal action (investigation, fine, restriction) against an AI developer or deployer.
5. **Geopolitical / National Security** — Incidents involving AI in the context of international relations, defense policy, or cross-border tensions.
6. **Governance & Institutional** — Incidents reflecting gaps, failures, or breakdowns in AI governance processes themselves (e.g., failed international coordination).

## Applying the Taxonomy: Sample Cases from the Dataset

| Incident (from dataset) | Country | Proposed Category | Proposed Severity |
|---|---|---|---|
| Delhi Police Facial Recognition System Misidentification | India | Bias & Discrimination | High |
| OpenAI AI Agents Hijack German Programming Wiki | Germany | Security / Misuse | Medium |
| US Regulators Probe Tesla's AI-Driven Cybercab | United States | Regulatory & Compliance | Medium |
| US and Russia Block Progress on International AI Governance | Switzerland | Governance & Institutional | High |

*Note: Categorizations above are illustrative examples applying the proposed taxonomy to real incidents collected in this project's dataset. A full classification of all 20 incidents would be the next step in validating and refining this framework.*

## Next Steps for This Framework

- Apply this taxonomy systematically across the full incident dataset.
- Test the taxonomy against incident types not yet represented in the current dataset (e.g., biosecurity, critical infrastructure).
- Engage with existing incident classification frameworks (e.g., OECD.AI, AI Incident Database) to align terminology where possible.
- Pilot minimum disclosure timelines (e.g., 72 hours for Critical/High severity) with a small group of willing AI developers and regulators.