# Public Tech Footprint

A repeatable, confidence-tagged method for mapping an organization’s public technology posture from open sources.

## Purpose

Before interviews or deeper engagement, it is useful to understand what an organization exposes publicly: hosting, mail, digital banking or core platforms, cloud presence, certificates, and whether they operate their own ASN.

This project captures a structured process for doing that research cleanly and documenting the results with explicit confidence levels.

## What It Covers

- Certificate Transparency inventory and service inference
- Live DNS resolution and reachability classification
- ASN verification (owned vs. cloud/vendor)
- Mail and email security signals (MX, SPF, DMARC)
- Key vendor and platform identification (e.g., Jack Henry, Proofpoint, Cloudflare, AWS)
- Network map (owned-edge / cloud / CT-only)
- Advanced inference signals
- Job-stack alignment notes when used for role preparation

## Process Outline

1. Identify primary domain and high-signal hostnames
2. Pull Certificate Transparency data and infer services
3. Resolve DNS and classify reachability
4. Verify ASN ownership on primary domain and company-looking IPs
5. Map mail, CDN, digital banking, and support surfaces
6. Tag every finding with confidence (Observed / Inferred / Not found / Not attempted)
7. Produce a concise summary (Markdown or PDF) plus supporting CSV

## Confidence Tags

| Tag | Meaning |
|-----|---------|
| Observed | Directly confirmed via DNS, CT, public records, or live resolution |
| Inferred | Reasonable conclusion from available signals |
| Not found | Explicitly checked and absent |
| Not attempted | Not investigated in this pass |

## Output Structure

Each completed footprint typically includes:

- Summary Markdown or PDF
- CT inventory CSV
- Reachability table
- Network map
- Advanced inference signals section

## Status

Methodology and template ready. Example outputs can be added as sanitized case studies.

## Related

Developed and refined while preparing for senior infrastructure and IT management roles.
