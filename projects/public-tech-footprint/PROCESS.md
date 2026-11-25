# Public Tech Footprint – Process Checklist

## 1. Scope
- [ ] Primary domain identified
- [ ] Company legal / brand name confirmed
- [ ] Target role or context noted (if used for job prep)

## 2. Certificate Transparency
- [ ] CT search performed (crt.sh or equivalent)
- [ ] High-signal hostnames extracted
- [ ] Service inference applied (banking platform, mail, CDN, support, etc.)
- [ ] CSV inventory created

## 3. DNS & Reachability
- [ ] Live resolution on primary and high-signal hosts
- [ ] Reachability classified (External / Internal-only / Unknown)
- [ ] Reachability table produced

## 4. ASN Verification
- [ ] Primary domain ASN checked
- [ ] Any company-looking resolved IPs checked
- [ ] Result recorded (owned ASN or none)

## 5. Core Surfaces
- [ ] Mail (MX, SPF, DMARC)
- [ ] Web hosting / CDN
- [ ] Digital banking or core platform (if applicable)
- [ ] Support / remote access tools
- [ ] Investor or other major portals

## 6. Network Map
- [ ] Owned-edge / Cloud / CT-only / Vendor categories completed

## 7. Advanced Signals
- [ ] Passive DNS / historical notes
- [ ] Certificate issuer patterns
- [ ] PeeringDB / colo (if relevant)
- [ ] Other signals tagged with confidence

## 8. Documentation
- [ ] Summary written with confidence tags
- [ ] Supporting files (CSV, etc.) included
- [ ] Sources listed

## Notes
- Never assume “no ASN” — verify.
- Prefer Observed over Inferred.
- Keep outputs professional and suitable for sharing when sanitized.
